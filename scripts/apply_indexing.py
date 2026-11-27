#!/usr/bin/env python3
"""Unlock indexing for every public SiliconPlay page and rebuild sitemap hreflang.

The stats dashboard stays noindex. Feed URLs stay out of the sitemap.
Localized /download/ pages were instant redirects to /download/; they become
real landing pages so they are not redirects and not noindex.
"""
from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path

import locale_guide_notes as notes

ROOT = Path(__file__).resolve().parents[1]
HOST = "https://siliconplay.app"
PREFIXES = [
    "", "pt-br", "es-mx", "es-es", "fr", "de", "it", "nl", "pl", "ru", "uk",
    "tr", "ar", "hi", "id", "th", "vi", "ja", "ko", "zh-hans", "zh-hant",
]
PREFIX_SET = {p for p in PREFIXES if p}
CODE = {
    "": "en-US",
    "pt-br": "pt-BR",
    "es-mx": "es-MX",
    "es-es": "es-ES",
    "zh-hans": "zh-Hans",
    "zh-hant": "zh-Hant",
}
ARIA = {
    "": "Languages",
    "pt-br": "Idiomas",
    "es-mx": "Idiomas",
    "es-es": "Idiomas",
    "fr": "Langues",
    "de": "Sprachen",
    "it": "Lingue",
    "nl": "Talen",
    "pl": "Języki",
    "ru": "Языки",
    "uk": "Мови",
    "tr": "Diller",
    "ar": "اللغات",
    "hi": "भाषाएँ",
    "id": "Bahasa",
    "th": "ภาษา",
    "vi": "Ngôn ngữ",
    "ja": "言語",
    "ko": "언어",
    "zh-hans": "语言",
    "zh-hant": "語言",
}
NAMES = {
    "": "English",
    "pt-br": "Português",
    "es-mx": "Español (MX)",
    "es-es": "Español (ES)",
    "fr": "Français",
    "de": "Deutsch",
    "it": "Italiano",
    "nl": "Nederlands",
    "pl": "Polski",
    "ru": "Русский",
    "uk": "Українська",
    "tr": "Türkçe",
    "ar": "العربية",
    "hi": "हिन्दी",
    "id": "Indonesia",
    "th": "ไทย",
    "vi": "Tiếng Việt",
    "ja": "日本語",
    "ko": "한국어",
    "zh-hans": "简体中文",
    "zh-hant": "繁體中文",
}
THIN = {
    "mumu-player-alternative-mac",
    "bluestacks-alternative-mac",
    "android-emulator-mac-m1-m2-m3-m4",
    "free-android-emulator-mac-m1-m5-comparison",
}
NO_HREFLANG_KEYS = {"privacy.html", "licenses.html"}
DMG = "https://github.com/RyanAnthonyGibo/siliconplay.app/releases/download/v1.1.2/SiliconPlay.dmg"
BEACON = "74ebf9abc28f487282469b38ed706bb4"
ADSENSE_META = '<meta name="google-adsense-account" content="ca-pub-8721719872183277">'
ADSENSE_SCRIPT = '<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-8721719872183277" crossorigin="anonymous"></script>'
PRICE_SWAPS = [
    (": comparativo e preços", ""),
    (": vergelijking en prijzen", ": vergelijking"),
    (": confronto e prezzi", ": confronto"),
    (": comparativa y precios", ": comparativa"),
    (": तुलना और कीमतें", ": तुलना"),
    (": порівняння і ціни", ": порівняння"),
    (": perbandingan dan harga", ": perbandingan"),
    (" : comparatif et prix", " : comparatif"),
    (": Vergleich und Preise", ": Vergleich"),
    (": сравнение и цены", ": сравнение"),
    (": مقارنة وأسعار", ": مقارنة"),
    ("：对比与价格", "：对比"),
    (": 비교와 가격", ": 비교"),
    (": เปรียบเทียบและราคา", ": เปรียบเทียบ"),
    ("：比較與價格", "：比較"),
    (": porównanie i ceny", ": porównanie"),
    (": so sánh và giá", ": so sánh"),
    (": karşılaştırma ve fiyatlar", ": karşılaştırma"),
    (", con precios de las páginas oficiales.", "."),
    (", com preços das páginas oficiais.", "."),
    (", met prijzen van de officiële pagina’s.", "."),
    (", con i prezzi delle pagine ufficiali.", "."),
    (", आधिकारिक पेजों से ली गई कीमतों के साथ.", "."),
    (", dengan harga dari situs resmi.", "."),
    (", avec les prix des pages officielles.", "."),
    (", mit Preisen von den offiziellen Seiten.", "."),
    ("، مع الأسعار من المواقع الرسمية.", "."),
    ("，价格来自官网。", "。"),
    ("을 공식 사이트 가격과 함께 나란히 비교합니다.", "을 나란히 비교합니다."),
    (" พร้อมราคาจากเว็บไซต์ทางการ", ""),
    ("，價格來自官方網站。", "。"),
    (", với giá lấy từ trang chính thức.", "."),
    (", resmi sayfalardaki fiyatlarla.", "."),
]


def code_for(prefix: str) -> str:
    return CODE.get(prefix, prefix)


def split_page(path: Path) -> tuple[str, str]:
    rel = path.relative_to(ROOT)
    parts = rel.parts
    if parts[0] in PREFIX_SET:
        prefix = parts[0]
        rest = parts[1:]
    else:
        prefix = ""
        rest = parts
    if rest[-1] == "index.html":
        key = "/".join(rest[:-1])
    else:
        key = "/".join(rest)
    return prefix, key


def public_url(prefix: str, key: str) -> str:
    if key.endswith(".html"):
        path = f"/{prefix}/{key}" if prefix else f"/{key}"
    elif not key:
        path = f"/{prefix}/" if prefix else "/"
    else:
        path = f"/{prefix}/{key}/" if prefix else f"/{key}/"
    while "//" in path:
        path = path.replace("//", "/")
    return HOST + path


def html_pages():
    for path in ROOT.rglob("*.html"):
        if "painel-f25ce03a71c3" in path.parts:
            continue
        yield path


def label_from(home: Path, href: str, fallback: str) -> str:
    text = home.read_text(encoding="utf-8")
    match = re.search(rf'href="{re.escape(href)}">([^<]+)</a>', text)
    return match.group(1) if match else fallback


def download_page(prefix: str) -> str:
    pack = notes.DOWNLOAD[prefix]
    url = public_url(prefix, "download")
    home = public_url(prefix, "")
    home_path = Path(prefix) / "index.html" if prefix else ROOT / "index.html"
    if prefix:
        home_file = ROOT / prefix / "index.html"
    else:
        home_file = ROOT / "index.html"
    about = label_from(home_file, "/about/", "About")
    contact = label_from(home_file, "/contact/", "Contact")
    privacy = label_from(home_file, "/privacy.html", "Privacy")
    terms = label_from(home_file, "/terms/", "Terms")
    licenses = label_from(home_file, "/licenses.html", "Licenses")
    lang = pack["lang"]
    direction = ' dir="rtl"' if pack.get("rtl") else ""
    steps = "\n".join(f"      <li>{item}</li>" for item in pack["steps"])
    needs = "\n".join(f"      <li>{item}</li>" for item in pack["needs"])
    keys = "\n".join(f"      <li>{item}</li>" for item in pack["keys"])
    graph = {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "SoftwareApplication",
                "name": "SiliconPlay",
                "operatingSystem": pack["os"],
                "applicationCategory": "DeveloperApplication",
                "softwareVersion": "1.1.2",
                "inLanguage": lang,
                "url": url,
                "downloadUrl": DMG,
                "description": pack["desc"],
                "offers": {"@type": "Offer", "price": "0", "priceCurrency": "USD"},
                "publisher": {"@id": f"{HOST}/#organization"},
            },
            {
                "@type": "BreadcrumbList",
                "itemListElement": [
                    {"@type": "ListItem", "position": 1, "name": "SiliconPlay", "item": home},
                    {"@type": "ListItem", "position": 2, "name": pack["crumb"], "item": url},
                ],
            },
        ],
    }
    payload = json.dumps(graph, ensure_ascii=False, indent=2)
    done_js = json.dumps(pack["done"], ensure_ascii=False)
    html = f"""<!doctype html>
<html lang="{lang}"{direction}>
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{pack["title"]}</title>
<meta name="description" content="{pack["desc"]}">
<meta name="color-scheme" content="light dark">
<link rel="canonical" href="{url}">
<meta property="og:site_name" content="SiliconPlay">
<meta property="og:locale" content="{pack["og_locale"]}">
<meta property="og:title" content="{pack["title"]}">
<meta property="og:description" content="{pack["desc"]}">
<meta property="og:url" content="{url}">
<meta property="og:type" content="website">
<meta property="og:image" content="{HOST}/assets/og.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="{pack["og_alt"]}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{pack["title"]}">
<meta name="twitter:description" content="{pack["desc"]}">
<meta name="twitter:image" content="{HOST}/assets/og.png">
<meta name="twitter:image:alt" content="{pack["og_alt"]}">
<script type="application/ld+json">
{payload}
</script>
<link rel="icon" href="/assets/favicon-32.png" sizes="32x32" type="image/png">
<link rel="icon" href="/assets/favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="/style.css">
{ADSENSE_META}
{ADSENSE_SCRIPT}
</head>
<body class="docpage">
<div class="wall" aria-hidden="true"></div>
<main class="doc article">
  <p class="doc-nav"><a href="{home}"><img src="/assets/favicon-32.png" width="16" height="16" alt="{pack["icon_alt"]}"> SiliconPlay</a> · <a href="{public_url(prefix, "blog")}">{pack["blog"]}</a> · <a href="/about/">{about}</a> · <a href="/contact/">{contact}</a> · <a href="/privacy.html">{privacy}</a> · <a href="/terms/">{terms}</a></p>
  <article>
    <h1>{pack["h1"]}</h1>
    <p class="status">{pack["start"]}</p>
    <p>{pack["lead"]}</p>
    <p><a class="cta" id="dl" href="{DMG}">{pack["link"]}</a></p>
    <h2>{pack["h2setup"]}</h2>
    <ol>
{steps}
    </ol>
    <h2>{pack["h2need"]}</h2>
    <ul>
{needs}
    </ul>
    <h2>{pack["h2keys"]}</h2>
    <ul>
{keys}
    </ul>
    <p>{pack["tail"]} <a href="{public_url(prefix, "compare")}">{pack["compare"]}</a>.</p>
  </article>
  <footer>
    <p>{pack["legal"]}</p>
    <p><a href="/about/">{about}</a> · <a href="/privacy.html">{privacy}</a> · <a href="/terms/">{terms}</a> · <a href="/licenses.html">{licenses}</a> · <a href="/contact/">{contact}</a> · © 2026 SiliconPlay</p>
  </footer>
</main>
<script>
window.SP_DL_DONE = {done_js};
@@DOWNLOAD_JS@@
</script>
<!-- Cloudflare Web Analytics --><script type="module" src="https://static.cloudflareinsights.com/beacon.min.js" data-cf-beacon='{{"token": "{BEACON}"}}'></script><!-- End Cloudflare Web Analytics -->
</body>
</html>
"""
    return html.replace("@@DOWNLOAD_JS@@", notes.DOWNLOAD_JS)


def hreflang_block(prefix: str, key: str, present: set[str]) -> str:
    if key in NO_HREFLANG_KEYS:
        return ""
    lines = []
    if "" in present:
        en = public_url("", key)
        lines.append(f'<link rel="alternate" hreflang="en-US" href="{en}">')
        lines.append(f'<link rel="alternate" hreflang="x-default" href="{en}">')
        lines.append(f'<link rel="alternate" hreflang="en" href="{en}">')
    for item in PREFIXES:
        if item and item in present:
            lines.append(
                f'<link rel="alternate" hreflang="{code_for(item)}" href="{public_url(item, key)}">'
            )
    return "\n" + "\n".join(lines)


def lang_nav(prefix: str, key: str, present: set[str]) -> str:
    if key in NO_HREFLANG_KEYS or len(present) < 2:
        return ""
    parts = [f'<nav class="langlinks" aria-label="{ARIA[prefix]}">']
    ordered = [p for p in PREFIXES if p in present]
    for item in ordered:
        href = public_url(item, key).replace(HOST, "") or "/"
        current = ' aria-current="page"' if item == prefix else ""
        parts.append(
            f'<a href="{href}" hreflang="{code_for(item)}" lang="{code_for(item)}"{current}>{NAMES[item]}</a>'
        )
    parts.append("</nav>")
    return "".join(parts)


def strip_hreflang(text: str) -> str:
    return re.sub(r'\n?<link rel="alternate" hreflang="[^"]+" href="[^"]+">', "", text)


def insert_hreflang(text: str, block: str) -> str:
    text = strip_hreflang(text)
    match = re.search(r'<link rel="canonical" href="[^"]+">', text)
    if not match or not block:
        return text
    return text[: match.end()] + block + text[match.end() :]


def visible_faq(html: str) -> list[tuple[str, str]]:
    match = re.search(
        r"<h2>[^<]*(?:FAQ|Fragen|Preguntas|Perguntas|Questions|Domande|Veelgestelde|Pytania|Вопросы|Питання|Sorular|أسئلة|الأسئلة|सवाल|Pertanyaan|คำถาม|Câu hỏi|質問|よくある|질문|问题|問題|常见问题|常見問題)[^<]*</h2>(.*?)(?:<h2>|</article>)",
        html,
        re.S,
    )
    if not match:
        return []
    chunk = match.group(1)
    pairs = []
    for q, a in re.findall(r"<h3>(.*?)</h3>\s*<p>(.*?)</p>", chunk, re.S):
        question = re.sub(r"<[^>]+>", "", q).strip()
        answer = re.sub(r"<[^>]+>", "", a).strip()
        answer = re.sub(r"\s+", " ", answer)
        if question and answer:
            pairs.append((question, answer))
    return pairs


def add_faq_jsonld(text: str, url: str, lang: str) -> str:
    if "FAQPage" in text:
        return text
    pairs = visible_faq(text)
    if not pairs:
        return text
    data = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "url": url,
        "inLanguage": lang,
        "mainEntity": [
            {
                "@type": "Question",
                "name": q,
                "acceptedAnswer": {"@type": "Answer", "text": a},
            }
            for q, a in pairs
        ],
    }
    blob = json.dumps(data, ensure_ascii=False, indent=2)
    snippet = f'<script type="application/ld+json">\n{blob}\n</script>\n'
    return text.replace("</head>", snippet + "</head>", 1)


def bump_dates(text: str) -> str:
    text = re.sub(
        r'("dateModified": )"\d{4}-\d{2}-\d{2}"',
        r'\1"2026-11-27"',
        text,
        count=1,
    )
    text = re.sub(
        r'(article:modified_time" content=")\d{4}-\d{2}-\d{2}"',
        r'\g<1>2026-11-27"',
        text,
        count=1,
    )
    return text


def lastmod_for(text: str, changed: bool) -> str:
    if changed:
        return "2026-11-27"
    for pattern in (
        r'article:modified_time" content="(\d{4}-\d{2}-\d{2})"',
        r'"dateModified": "(\d{4}-\d{2}-\d{2})"',
    ):
        match = re.search(pattern, text)
        if match:
            return match.group(1)
    return "2026-11-12"


def main() -> None:
    for prefix in PREFIXES:
        dest = ROOT / prefix / "download" / "index.html" if prefix else ROOT / "download" / "index.html"
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(download_page(prefix), encoding="utf-8")

    clusters: dict[str, set[str]] = {}
    pages: list[tuple[Path, str, str]] = []
    changed_paths: set[Path] = set()
    for path in html_pages():
        prefix, key = split_page(path)
        clusters.setdefault(key, set()).add(prefix)
        pages.append((path, prefix, key))

    for path, prefix, key in pages:
        text = path.read_text(encoding="utf-8")
        changed = key == "download"
        text = re.sub(r'[ \t]*<meta name="robots" content="noindex, follow">\n?', "", text)
        if prefix:
            text = text.replace('href="/download/"', f'href="/{prefix}/download/"')
            text = text.replace(
                '"downloadUrl": "https://siliconplay.app/download/"',
                f'"downloadUrl": "https://siliconplay.app/{prefix}/download/"',
            )
        for old, new in PRICE_SWAPS:
            if old in text:
                text = text.replace(old, new)
                changed = True
        if prefix and key.startswith("blog/") and key.count("/") == 1:
            slug = key.split("/", 1)[1]
            if slug in THIN and "seo-expand-2026-11-27" not in text:
                extra = notes.snippet(prefix, slug)
                if "</article>" not in text:
                    raise SystemExit(f"no article in {path}")
                text = text.replace("</article>", extra + "\n  </article>", 1)
                text = bump_dates(text)
                changed = True
        text = insert_hreflang(text, hreflang_block(prefix, key, clusters[key]))
        nav = lang_nav(prefix, key, clusters[key])
        if nav and 'class="langlinks"' not in text:
            if "</footer>" in text:
                text = text.replace("</footer>", nav + "\n</footer>", 1)
            text = re.sub(
                r'(<nav class="phone-site-nav"[^>]*>.*?</nav>)',
                lambda m, nav=nav: m.group(1) + nav,
                text,
                count=1,
                flags=re.S,
            )
        lang = "en-US" if not prefix else code_for(prefix)
        if path.name != "index.html" or key not in {"", "compare", "whats-new"}:
            text = add_faq_jsonld(text, public_url(prefix, key), lang)
        elif "FAQPage" not in text:
            text = add_faq_jsonld(text, public_url(prefix, key), lang)
        text = text.replace('href="index.html"', 'href="/"')
        path.write_text(text, encoding="utf-8")
        if changed:
            changed_paths.add(path)

    # Titles that are byte-identical across locales confuse canonical selection.
    titled: dict[str, list[Path]] = {}
    for path, prefix, key in pages:
        if key in NO_HREFLANG_KEYS:
            continue
        text = path.read_text(encoding="utf-8")
        match = re.search(r"<title>(.*?)</title>", text)
        if match:
            titled.setdefault(match.group(1), []).append(path)
    marks = {
        "es-es": "España",
        "es-mx": "México",
        "pt-br": "Brasil",
        "zh-hans": "简体",
        "zh-hant": "繁體",
        "ru": "Россия",
        "uk": "Україна",
        "fr": "France",
        "id": "Indonesia",
        "pl": "Polska",
        "nl": "Nederland",
        "de": "Deutschland",
        "it": "Italia",
        "ja": "日本",
        "ko": "한국",
        "ar": "العربية",
        "hi": "हिन्दी",
        "th": "ไทย",
        "vi": "Việt",
        "tr": "Türkiye",
    }
    for title, paths in titled.items():
        if len(paths) < 2:
            continue
        for path in paths:
            prefix, _key = split_page(path)
            mark = marks.get(prefix)
            if not mark or f"({mark})" in title:
                continue
            if " | " in title:
                left, right = title.rsplit(" | ", 1)
                updated = f"{left} ({mark}) | {right}"
            else:
                updated = f"{title} ({mark})"
            text = path.read_text(encoding="utf-8")
            text = text.replace(f"<title>{title}</title>", f"<title>{updated}</title>", 1)
            text = text.replace(
                f'<meta property="og:title" content="{title}">',
                f'<meta property="og:title" content="{updated}">',
                1,
            )
            text = text.replace(
                f'<meta name="twitter:title" content="{title}">',
                f'<meta name="twitter:title" content="{updated}">',
                1,
            )
            path.write_text(text, encoding="utf-8")

    urls = []
    for path, prefix, key in pages:
        text = path.read_text(encoding="utf-8")
        if "noindex" in text:
            raise SystemExit(f"unexpected noindex in {path}")
        loc = public_url(prefix, key)
        changed = path in changed_paths or "seo-expand-2026-11-27" in text or key == "download"
        # hreflang was added everywhere; content lastmod stays on the article date
        # except pages whose body changed.
        stamp = lastmod_for(text, changed)
        present = clusters[key]
        alts = []
        if key not in NO_HREFLANG_KEYS:
            if "" in present:
                en = public_url("", key)
                alts.append(("en-US", en))
                alts.append(("en", en))
                alts.append(("x-default", en))
            for item in PREFIXES:
                if item and item in present:
                    alts.append((code_for(item), public_url(item, key)))
        urls.append((loc, stamp, alts))
    urls.sort(key=lambda item: item[0])
    lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">',
    ]
    for loc, stamp, alts in urls:
        lines.append("  <url>")
        lines.append(f"    <loc>{loc}</loc>")
        lines.append(f"    <lastmod>{stamp}</lastmod>")
        for code, href in alts:
            lines.append(f'    <xhtml:link rel="alternate" hreflang="{code}" href="{href}"/>')
        lines.append("  </url>")
    lines.append("</urlset>")
    (ROOT / "sitemap.xml").write_text("\n".join(lines) + "\n", encoding="utf-8")
    digest = hashlib.sha256((ROOT / "download" / "index.html").read_bytes()).hexdigest()
    print(f"pages {len(urls)} sitemap bytes {(ROOT / 'sitemap.xml').stat().st_size}")
    print(f"download sha256 {digest}")


if __name__ == "__main__":
    main()
