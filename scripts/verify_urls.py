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
    "download/index.html": "b55b8c873ff665e21acb238c571c2a5418ba16b92e38e5c12d30c0719af78106",
    "painel-f25ce03a71c3/index.html": "3d352f5bd7f82c58df515c5c31cc68c84a9d742363d7e13c9a85263a655db24a",
}
POSTS = [
    "android-emulator-mac-keyboard-mapping",
    "android-emulator-mac-shortcuts",
    "rooted-android-emulator-mac",
    "android-emulator-mac-m1-m2-m3-m4",
    "bluestacks-alternative-mac",
    "mumu-player-alternative-mac",
    "android-emulator-mac-m1-m4-setup",
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


def check_urls() -> None:
    seen = []
    sitemap = (ROOT / "sitemap.xml").read_text(encoding="utf-8")
    locs = re.findall(r"<loc>([^<]+)</loc>", sitemap)
    if len(locs) != 212:
        fail(f"sitemap has {len(locs)} urls, expected 212")
    if sitemap.count("<lastmod>") != len(locs):
        fail("a sitemap url is missing lastmod")
    if "/download/" in sitemap or "painel-f25ce03a71c3" in sitemap:
        fail("sitemap includes a protected path")
    for loc in locs:
        seen.append(("sitemap", loc))
        hrefs = []
    # hreflang inside each url block
    for block in re.findall(r"<url>(.*?)</url>", sitemap, re.S):
        loc = re.search(r"<loc>([^<]+)</loc>", block).group(1)
        alts = re.findall(r'hreflang="([^"]+)" href="([^"]+)"', block)
        if loc.endswith("/privacy.html") or loc.endswith("/licenses.html"):
            if alts:
                fail(f"privacy/licenses should not carry hreflang: {loc}")
            continue
        codes = {code for code, _ in alts}
        need = set(LANGS) | GENERIC | {"x-default"}
        if codes != need:
            fail(f"sitemap hreflang set for {loc} is {sorted(codes)}")
        for code, href in alts:
            seen.append((f"sitemap:{code}", href))

    for path in html_files():
        text = path.read_text(encoding="utf-8")
        rel = path.relative_to(ROOT).as_posix()
        canon = re.search(r'<link rel="canonical" href="([^"]+)"', text)
        if canon:
            seen.append((f"canonical:{rel}", canon.group(1)))
        for code, href in re.findall(r'<link rel="alternate" hreflang="([^"]+)" href="([^"]+)"', text):
            seen.append((f"hreflang:{rel}:{code}", href))
        if 'hreflang="x-default"' in text:
            codes = set(re.findall(r'hreflang="([^"]+)"', text))
            need = set(LANGS) | GENERIC | {"x-default"}
            if not need <= codes:
                fail(f"{rel} missing hreflang {sorted(need - codes)}")
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


def check_content() -> None:
    for path in public_text_files():
        text = path.read_text(encoding="utf-8", errors="ignore")
        if re.search(r"x86|intel", text, re.I):
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
        if "fonts.googleapis" in text or "pagead2.googlesyndication.com" in text:
            fail(f"{home.relative_to(ROOT)} still loads fonts or AdSense")
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
        blocking = 'script async src="https://pagead2.googlesyndication.com' in text
        lazy = "pointerdown" in text and "pagead2.googlesyndication.com" in text
        is_home = rel == "index.html" or rel in {f"{prefix}/index.html" for prefix in PREFIXES if prefix}
        if blocking:
            fail(f"blocking AdSense in {rel}")
        if is_home and "pagead2.googlesyndication.com" in text:
            fail(f"AdSense on home {rel}")
        if "pagead2.googlesyndication.com" in text and not lazy and not is_home:
            fail(f"AdSense is not lazy in {rel}")
    for rel, digest in PROTECTED.items():
        got = hashlib.sha256((ROOT / rel).read_bytes()).hexdigest()
        if got != digest:
            fail(f"{rel} hash changed")
    for path in ROOT.rglob("*"):
        if not path.is_file():
            continue
        if "download" not in path.parts:
            continue
        # download pages must not gain AdSense
        if "pagead2" in path.read_text(encoding="utf-8", errors="ignore"):
            fail(f"AdSense appeared in {path.relative_to(ROOT)}")
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
