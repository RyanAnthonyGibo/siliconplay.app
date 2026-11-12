#!/usr/bin/env python3
"""Check the static tree the way GitHub Pages will serve it.

A directory URL without a trailing slash is a 301. A trailing slash is 200
when index.html exists. A real file is 200. An extensionless path is 200 when
the .html file exists (/privacy -> privacy.html). Every sitemap <loc>,
canonical, and hreflang href must be a direct 200.
"""
from __future__ import annotations

import hashlib
import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlparse

ROOT = Path(__file__).resolve().parents[1]
HOST = "https://siliconplay.app"
SKIP_PARTS = {"download", "painel-f25ce03a71c3"}
LANGS = [
    "en-US", "pt-BR", "es-MX", "es-ES", "fr", "de", "it", "nl", "pl", "ru",
    "uk", "tr", "ar", "hi", "id", "th", "vi", "ja", "ko", "zh-Hans", "zh-Hant",
]
GENERIC = {"en", "es", "pt", "zh"}
PROTECTED = {
    "download/index.html": "0213a24079008de006b47dcd83ee1cb7639d188dd3a11e5e1734772525e99c90",
    "painel-f25ce03a71c3/index.html": "ee9fc4c9816571eba9df46268c85c320173884b6020b2e09547765d5b5d2fcf6",
}
EN_HREFLANG = {"en-US", "en", "x-default"}
ADSENSE_SCRIPT = '<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-8721719872183277" crossorigin="anonymous"></script>'
ADSENSE_META = '<meta name="google-adsense-account" content="ca-pub-8721719872183277">'
# English-only guides. Translations of these slugs are not published.
EN_ONLY_POSTS = [
    "first-run-android-16-on-mac",
    "install-apk-with-command-i",
    "typing-game-keys-and-direct-touch",
    "root-versus-play-store-image",
    "vulkan-metal-and-safe-math-shaders",
    "which-macs-run-siliconplay",
    "wasd-gamepad-and-on-screen-buttons",
    "pro-mode-sdk-folder-and-app-files",
    "google-play-sign-in-on-the-tablet",
    "when-keys-go-to-the-wrong-place",
    "apks-that-do-not-install-or-open",
    "test-a-build-without-android-studio",
    "fixing-common-siliconplay-problems",
    "adb-on-siliconplay",
    "choose-play-store-or-an-apk",
    "google-play-services-on-siliconplay",
    "what-the-android-16-tablet-includes",
    "settings-by-mac-chip-m1-to-m6",
    "game-performance-on-apple-silicon",
    "keymap-layouts-for-different-games",
    "moving-from-another-emulator-on-mac",
    "siliconplay-next-to-android-studio",
    "disk-space-sdk-folder-and-uninstall",
    "report-a-siliconplay-bug",
]
LONG_POSTS = EN_ONLY_POSTS + [
    "android-emulator-mac-m1-m2-m3-m4",
    "bluestacks-alternative-mac",
    "mumu-player-alternative-mac",
]
POSTS = [
    "android-emulator-mac-keyboard-mapping",
    "android-emulator-mac-shortcuts",
    "rooted-android-emulator-mac",
    "android-emulator-mac-m1-m2-m3-m4",
    "bluestacks-alternative-mac",
    "mumu-player-alternative-mac",
    "android-emulator-mac-m1-m4-setup",
    "free-android-emulator-mac-m1-m5-comparison",
]
PREFIXES = [
    "", "pt-br", "es-mx", "es-es", "fr", "de", "it", "nl", "pl", "ru", "uk",
    "tr", "ar", "hi", "id", "th", "vi", "ja", "ko", "zh-hans", "zh-hant",
]

errors: list[str] = []


def fail(msg: str) -> None:
    errors.append(msg)


def classify(url: str) -> str:
    parsed = urlparse(url)
    if parsed.scheme not in {"http", "https"} or parsed.netloc != "siliconplay.app":
        return "external"
    path = unquote(parsed.path)
    if path != "/" and "//" in path:
        return "404"
    if path == "/":
        return "200" if (ROOT / "index.html").is_file() else "404"
    rel = path.lstrip("/")
    if path.endswith("/"):
        return "200" if (ROOT / rel / "index.html").is_file() else "404"
    if (ROOT / rel).is_file():
        return "200"
    if (ROOT / rel / "index.html").is_file():
        return "301"
    if (ROOT / f"{rel}.html").is_file():
        return "200"
    return "404"


def html_files():
    for path in ROOT.rglob("*.html"):
        if any(part in SKIP_PARTS for part in path.parts):
            continue
        yield path


def public_text_files():
    for path in ROOT.rglob("*"):
        if not path.is_file():
            continue
        if any(part in SKIP_PARTS for part in path.parts):
            continue
        if path.name == "licenses.html":
            continue
        if path.suffix.lower() not in {".html", ".xml", ".js", ".json", ".css", ".txt", ".md"}:
            continue
        if path.resolve() == Path(__file__).resolve():
            continue
        yield path


def is_translated(path: Path) -> bool:
    rel = path.relative_to(ROOT)
    return bool(rel.parts) and rel.parts[0] in {p for p in PREFIXES if p}


def public_url(path: Path) -> str:
    rel = path.relative_to(ROOT).as_posix()
    if rel == "index.html":
        return f"{HOST}/"
    if rel.endswith("/index.html"):
        return f"{HOST}/" + rel[: -len("index.html")]
    return f"{HOST}/{rel}"


def indexable_english_urls() -> set[str]:
    urls = set()
    for path in ROOT.rglob("*.html"):
        if is_translated(path):
            continue
        if any(part in SKIP_PARTS for part in path.parts):
            continue
        text = path.read_text(encoding="utf-8")
        if 'name="robots"' in text and "noindex" in text:
            continue
        urls.add(public_url(path))
    return urls


def check_urls() -> None:
    seen = []
    sitemap = (ROOT / "sitemap.xml").read_text(encoding="utf-8")
    locs = re.findall(r"<loc>([^<]+)</loc>", sitemap)
    expected = indexable_english_urls()
    if set(locs) != expected:
        missing = sorted(expected - set(locs))[:8]
        extra = sorted(set(locs) - expected)[:8]
        fail(f"sitemap urls {len(locs)} != english indexable {len(expected)} missing {missing} extra {extra}")
    if any("/pt-br/" in loc or "/de/" in loc or "/ja/" in loc for loc in locs):
        fail("sitemap still lists a translation")
    if sitemap.count("<lastmod>") != len(locs):
        fail("a sitemap url is missing lastmod")
    if "/download/" in sitemap or "painel-f25ce03a71c3" in sitemap:
        fail("sitemap includes a protected path")
    for loc in locs:
        seen.append(("sitemap", loc))
        hrefs = []
    # hreflang inside each url block: English self-references only.
    # Translations are noindex, so they are not alternates.
    for block in re.findall(r"<url>(.*?)</url>", sitemap, re.S):
        loc = re.search(r"<loc>([^<]+)</loc>", block).group(1)
        alts = re.findall(r'hreflang="([^"]+)" href="([^"]+)"', block)
        if loc.endswith("/privacy.html") or loc.endswith("/licenses.html"):
            if alts:
                fail(f"privacy/licenses should not carry hreflang: {loc}")
            continue
        codes = {code for code, _ in alts}
        if codes != EN_HREFLANG:
            fail(f"sitemap hreflang set for {loc} is {sorted(codes)}")
        for code, href in alts:
            if href != loc:
                fail(f"sitemap hreflang {code} for {loc} points at {href}")
            seen.append((f"sitemap:{code}", href))

    for path in html_files():
        text = path.read_text(encoding="utf-8")
        rel = path.relative_to(ROOT).as_posix()
        canon = re.search(r'<link rel="canonical" href="([^"]+)"', text)
        if canon:
            seen.append((f"canonical:{rel}", canon.group(1)))
        for code, href in re.findall(r'<link rel="alternate" hreflang="([^"]+)" href="([^"]+)"', text):
            seen.append((f"hreflang:{rel}:{code}", href))
        if is_translated(path):
            if "hreflang=" in text:
                fail(f"{rel} is noindex but still has hreflang")
            if "noindex" not in text:
                fail(f"{rel} translation is missing noindex")
        elif 'hreflang="x-default"' in text:
            codes = set(re.findall(r'hreflang="([^"]+)"', text))
            if codes != EN_HREFLANG:
                fail(f"{rel} hreflang set is {sorted(codes)}")
        for match in re.finditer(r"https://siliconplay\.app[^\s\"'<>]*", text):
            url = match.group(0).rstrip(".,)")
            if re.search(r"/blog/[a-z0-9-]+$", url):
                fail(f"{rel} blog url missing trailing slash: {url}")
        for href in re.findall(r'(?:href|value)="([^"]+)"', text):
            if re.search(r"(?:^|/)blog/[a-z0-9-]+$", href) and "feed" not in href:
                fail(f"{rel} relative blog url missing trailing slash: {href}")

    bad = [(src, url, classify(url)) for src, url in seen if classify(url) != "200"]
    if bad:
        for src, url, status in bad[:25]:
            fail(f"{status} {url} ({src})")
        if len(bad) > 25:
            fail(f"... {len(bad) - 25} more urls are not direct 200s")
    print(f"checked {len(seen)} urls")


def check_jsonld(path: Path, required: set[str]) -> None:
    text = path.read_text(encoding="utf-8")
    blocks = re.findall(r'<script type="application/ld\+json">\s*(.*?)\s*</script>', text, re.S)
    if not blocks:
        fail(f"{path.relative_to(ROOT)} has no JSON-LD")
        return
    types = set()
    for block in blocks:
        try:
            data = json.loads(block)
        except json.JSONDecodeError as exc:
            fail(f"{path.relative_to(ROOT)} JSON-LD: {exc}")
            return
        ctx = json.dumps(data)
        if "schema.org" not in ctx:
            fail(f"{path.relative_to(ROOT)} JSON-LD is missing schema.org")
        nodes = data.get("@graph", [data])
        for node in nodes:
            kind = node.get("@type")
            if isinstance(kind, list):
                types.update(kind)
            elif kind:
                types.add(kind)
    if not required <= types:
        fail(f"{path.relative_to(ROOT)} JSON-LD types {sorted(types)} missing {sorted(required - types)}")


def check_structured() -> None:
    homes = [ROOT / "index.html"] + [ROOT / p / "index.html" for p in PREFIXES if p]
    for home in homes:
        check_jsonld(home, {"SoftwareApplication", "Organization", "WebSite", "FAQPage"})
        text = home.read_text(encoding="utf-8")
        faq = re.search(r'<section id="faq">(.*?)</section>', text, re.S)
        visible = len(re.findall(r"<h3>", faq.group(1))) if faq else 0
        data = json.loads(re.search(r'<script type="application/ld\+json">\s*(.*?)\s*</script>', text, re.S).group(1))
        questions = next(n for n in data["@graph"] if n["@type"] == "FAQPage")["mainEntity"]
        if len(questions) != visible or visible == 0:
            fail(f"{home.relative_to(ROOT)} FAQ JSON-LD {len(questions)} != visible {visible}")
        app = next(n for n in data["@graph"] if n["@type"] == "SoftwareApplication")
        if app.get("softwareVersion") != "1.0.0":
            fail(f"{home.relative_to(ROOT)} softwareVersion")
        if "screenshot" in app or "aggregateRating" in app:
            fail(f"{home.relative_to(ROOT)} has screenshot or rating")
        if app["offers"].get("price") != "0":
            fail(f"{home.relative_to(ROOT)} offer price")
    compares = [ROOT / "compare/index.html"] + [ROOT / p / "compare/index.html" for p in PREFIXES if p]
    if len(compares) != 21 or not all(p.is_file() for p in compares):
        fail("expected 21 compare pages")
    for page in compares:
        check_jsonld(page, {"WebPage", "BreadcrumbList", "ItemList"})
    for prefix in PREFIXES:
        for slug in POSTS:
            path = ROOT / prefix / "blog" / slug / "index.html" if prefix else ROOT / "blog" / slug / "index.html"
            check_jsonld(path, {"BlogPosting", "BreadcrumbList"})
    for slug in EN_ONLY_POSTS:
        path = ROOT / "blog" / slug / "index.html"
        if not path.is_file():
            fail(f"missing english guide {slug}")
            continue
        check_jsonld(path, {"BlogPosting", "BreadcrumbList"})


def check_content() -> None:
    for path in public_text_files():
        text = path.read_text(encoding="utf-8", errors="ignore")
        scrubbed = re.sub(r"Intel Macs?", "", text)
        if re.search(r"x86", text, re.I) or re.search(r"intel", scrubbed, re.I):
            fail(f"forbidden wording in {path.relative_to(ROOT)}")
        if "Ragnarok" in text:
            fail(f"Ragnarok in {path.relative_to(ROOT)}")
    homes = [ROOT / "index.html"] + [ROOT / p / "index.html" for p in PREFIXES if p]
    for home in homes:
        text = home.read_text(encoding="utf-8")
        h1s = [re.sub(r"<[^>]+>", "", h) for h in re.findall(r"<h1[^>]*>(.*?)</h1>", text, re.S)]
        if not h1s or any("SiliconPlay" not in h for h in h1s):
            fail(f"{home.relative_to(ROOT)} h1 missing brand: {h1s[:1]}")
        if any(re.sub(r"\s+", "", h) == "SiliconPlay" for h in h1s):
            fail(f"{home.relative_to(ROOT)} still has a bare SiliconPlay h1")
        if "fonts.googleapis" in text:
            fail(f"{home.relative_to(ROOT)} still loads fonts")
        if "compare/" not in text:
            fail(f"{home.relative_to(ROOT)} does not link to compare")
    ko = (ROOT / "ko/index.html").read_text(encoding="utf-8")
    title = re.search(r"<title>(.*?)</title>", ko).group(1)
    desc = re.search(r'<meta name="description" content="([^"]*)"', ko).group(1)
    if "앱플레이어" not in title or "앱플레이어" not in desc or "앱플레이어" not in ko.split("</h1>", 1)[0]:
        fail("ko home is missing 앱플레이어 in title, description, or h1")
    for token, path in (("晶片", "zh-hant/index.html"), ("giả lập Android", "vi/index.html")):
        text = (ROOT / path).read_text(encoding="utf-8")
        h1 = re.search(r"<h1[^>]*>(.*?)</h1>", text, re.S).group(1)
        if token not in h1:
            fail(f"{path} h1 missing {token}")
    for path in ("th/index.html", "hi/index.html"):
        h1 = re.search(r"<h1[^>]*>(.*?)</h1>", (ROOT / path).read_text(encoding="utf-8"), re.S).group(1)
        if "Android emulator Mac" not in h1:
            fail(f"{path} h1 missing Android emulator Mac")
    icon = ROOT / "assets/icon-tile-128.webp"
    if not icon.is_file() or icon.stat().st_size > 15 * 1024:
        fail(f"display icon missing or over 15 KB ({icon.stat().st_size if icon.is_file() else 'missing'})")
    if "icon-tile.png" in (ROOT / "index.html").read_text(encoding="utf-8"):
        fail("home still references the large icon tile")
    css = (ROOT / "style.css").read_text(encoding="utf-8")
    if "fonts.googleapis" in css or "JetBrains" in css or re.search(r"\bInter\b", css):
        fail("style.css still names a web font")
    for path in html_files():
        text = path.read_text(encoding="utf-8")
        rel = path.relative_to(ROOT).as_posix()
        if "fonts.googleapis" in text:
            fail(f"render-blocking font in {rel}")
    for path in ROOT.rglob("*.html"):
        text = path.read_text(encoding="utf-8")
        rel = path.relative_to(ROOT).as_posix()
        if ADSENSE_SCRIPT not in text or ADSENSE_META not in text:
            fail(f"AdSense head tag missing in {rel}")
        if 'href="/about/"' not in text or 'href="/contact/"' not in text or 'href="/privacy.html"' not in text:
            fail(f"About, Contact, or Privacy link missing in {rel}")
    for rel, digest in PROTECTED.items():
        got = hashlib.sha256((ROOT / rel).read_bytes()).hexdigest()
        if got != digest:
            fail(f"{rel} hash changed")
    for slug in LONG_POSTS:
        path = ROOT / "blog" / slug / "index.html"
        article = re.search(r"<article>(.*)</article>", path.read_text(encoding="utf-8"), re.S)
        chunk = article.group(1) if article else ""
        plain = re.sub(r"<[^>]+>", " ", chunk)
        count = len(re.findall(r"[A-Za-z0-9']+", plain))
        if count < 1000:
            fail(f"{slug} is {count} words, need 1000+")
    about = (ROOT / "about" / "index.html").read_text(encoding="utf-8")
    contact = (ROOT / "contact" / "index.html").read_text(encoding="utf-8")
    if "28.148.946 RYAN ANTHONY GIBO - ME" not in about or "Brazil" not in about:
        fail("about page is missing the company or Brazil")
    if "siliconplay.app@gmail.com" not in contact:
        fail("contact page is missing an email address")
    retired = "katz" + "doll"
    for path in ROOT.rglob("*"):
        if not path.is_file():
            continue
        if path.suffix.lower() not in {".html", ".js", ".txt", ".xml", ".css", ".json", ".py"}:
            continue
        if retired in path.read_text(encoding="utf-8", errors="ignore").lower():
            fail(f"retired contact email still in {path.relative_to(ROOT)}")
    if "28.148.946 RYAN ANTHONY GIBO - ME" not in contact or "Brazil" not in contact:
        fail("contact page is missing the company or Brazil")
    robots = (ROOT / "robots.txt").read_text(encoding="utf-8")
    if "Disallow: /painel-f25ce03a71c3/" not in robots:
        fail("robots.txt should disallow the stats dashboard")
    if "Sitemap: https://siliconplay.app/sitemap.xml" not in robots:
        fail("robots.txt is missing the sitemap line")
    for path in html_files():
        text = path.read_text(encoding="utf-8")
        rel = path.relative_to(ROOT).as_posix()
        head, _, body = text.partition("</head>")
        if re.search(r'<a href="[^"]*feed\.xml"', body):
            fail(f"{rel} links to feed.xml as a page")
        if "/blog/" in f"/{rel}" and 'type="application/rss+xml"' not in head:
            fail(f"{rel} is missing the RSS autodiscovery link")
    key = "c7e4a91b2d08f6e35a0c4b7d9e1f83a6"
    key_file = ROOT / f"{key}.txt"
    if not key_file.is_file() or key_file.read_text(encoding="utf-8").strip() != key:
        fail("IndexNow key file missing")
    if not (ROOT / "llms.txt").is_file():
        fail("llms.txt missing")
    if 'property="og:url" content="https://siliconplay.app/privacy.html"' not in (ROOT / "privacy.html").read_text(encoding="utf-8"):
        fail("privacy og:url")
    if 'og:locale" content="en_US"' not in (ROOT / "index.html").read_text(encoding="utf-8"):
        fail("home og:locale")


def main() -> int:
    check_urls()
    check_structured()
    check_content()
    if errors:
        print(f"{len(errors)} problems")
        for item in errors:
            print(" -", item)
        return 1
    print("ok")
    return 0


if __name__ == "__main__":
    sys.exit(main())
