# -*- coding: utf-8 -*-
"""Localized download copy and the extra guide sections for thin translations."""

DOWNLOAD_JS = r"""
(function () {
  var DMG = "https://github.com/RyanAnthonyGibo/siliconplay.app/releases/download/v1.1.2/SiliconPlay.dmg";
  var RUM = "cloudflareinsights.com";
  var left = false;
  var rumStarted = false;
  var rumDone = false;
  var t0 = Date.now();

  function leave() {
    if (left) return;
    left = true;
    var frame = document.getElementById("sp-dl-frame");
    if (!frame) {
      frame = document.createElement("iframe");
      frame.id = "sp-dl-frame";
      frame.hidden = true;
      frame.title = "SiliconPlay download";
      frame.setAttribute("aria-hidden", "true");
      document.body.appendChild(frame);
    }
    frame.src = DMG;
    var status = document.querySelector(".status");
    if (status && window.SP_DL_DONE) status.textContent = window.SP_DL_DONE;
  }

  function maybeLeave() {
    if (left) return;
    var elapsed = Date.now() - t0;
    if (rumDone) leave();
    else if (!rumStarted && elapsed > 4500) leave();
    else if (elapsed > 8000) leave();
  }

  var timer = setInterval(function () {
    maybeLeave();
    if (left) clearInterval(timer);
  }, 200);

  var origOpen = XMLHttpRequest.prototype.open;
  var origSend = XMLHttpRequest.prototype.send;
  XMLHttpRequest.prototype.open = function (method, url) {
    try { this.__spUrl = String(url || ""); } catch (e) { this.__spUrl = ""; }
    return origOpen.apply(this, arguments);
  };
  XMLHttpRequest.prototype.send = function () {
    var xhr = this;
    try {
      if (xhr.__spUrl && xhr.__spUrl.indexOf(RUM) !== -1) {
        rumStarted = true;
        xhr.addEventListener("loadend", function () {
          rumDone = true;
          maybeLeave();
        });
      }
    } catch (e) {}
    return origSend.apply(this, arguments);
  };

  if (typeof navigator.sendBeacon === "function") {
    var origBeacon = navigator.sendBeacon.bind(navigator);
    navigator.sendBeacon = function (url, data) {
      var result = false;
      try { result = origBeacon(url, data); } catch (e) { result = false; }
      try {
        if (!rumStarted && String(url || "").indexOf(RUM) !== -1) {
          rumStarted = true;
          rumDone = true;
          setTimeout(maybeLeave, 50);
        }
      } catch (e) {}
      return result;
    };
  }

  var link = document.getElementById("dl");
  if (link) {
    link.addEventListener("click", function (e) {
      if (left) return;
      e.preventDefault();
      if (rumDone || !window.XMLHttpRequest) leave();
    });
  }
})();
"""


def _dl(lang, og, title, desc, h1, start, done, lead, link, h2setup, steps, h2need, needs, h2keys, keys, tail, compare, blog, crumb, os_line, og_alt, icon_alt, legal, rtl=False):
    return {
        "lang": lang,
        "og_locale": og,
        "rtl": rtl,
        "title": title,
        "desc": desc,
        "h1": h1,
        "start": start,
        "done": done,
        "lead": lead,
        "link": link,
        "h2setup": h2setup,
        "steps": steps,
        "h2need": h2need,
        "needs": needs,
        "h2keys": h2keys,
        "keys": keys,
        "tail": tail,
        "compare": compare,
        "blog": blog,
        "crumb": crumb,
        "os": os_line,
        "og_alt": og_alt,
        "icon_alt": icon_alt,
        "legal": legal,
    }


_OS_EN = "macOS Tahoe and macOS 27 Golden Gate (tested), Apple Silicon M1–M6"
_KEYS_EN = [
    "Cmd+I installs one APK once Android is running. The menu shows Command-I. Drag and drop does the same install.",
    "F12 or Command-K switches Typing and game keys.",
    "F10 is direct touch when a dialog wants a finger.",
    "Command-Shift-G shows or hides the on-screen buttons.",
    "Shift-Escape releases a stuck virtual finger.",
    "Escape leaves fullscreen. Outside fullscreen it is Android Back while the display is focused.",
]

DOWNLOAD = {
    "": _dl(
        "en-US", "en_US",
        "Download SiliconPlay for Mac (M1–M6)",
        "Download SiliconPlay 1.1.2, a free Android emulator for Apple Silicon Macs from M1 through M6. Tested on macOS Tahoe and macOS 27 Golden Gate. Not compatible with Intel Macs.",
        "Download SiliconPlay for Mac",
        "Preparing the download…",
        "The download should start in a moment. If it does not, use the link.",
        "SiliconPlay is a free Android emulator for Macs with Apple silicon, from M1 through M6. The file is SiliconPlay.dmg, version 1.1.2. The DMG is the Mac app. Android itself downloads the first time you open it.",
        "Download SiliconPlay for Mac",
        "After the file arrives",
        [
            "Open the DMG and drag SiliconPlay to Applications.",
            "Open SiliconPlay. The first run accepts the Android SDK license and downloads the Apple silicon emulator, platform-tools, and the Play arm64 image, unless you already have an SDK with emulator, adb, and sdkmanager.",
            "When the Android 16 tablet is up (1920×1080, 320 dpi, landscape), sign in to Google Play or install one APK.",
        ],
        "What you need",
        [
            "A Mac with Apple silicon, M1 through M6, including Pro, Max, and Ultra.",
            "Tested on macOS Tahoe and macOS 27 Golden Gate. If you are on another version, try it and tell me what happened.",
            "Not compatible with Intel Macs.",
        ],
        "Shortcuts, Cmd+I first",
        _KEYS_EN,
        "If setup stops on a missing JDK, macOS is showing the stub at /usr/bin/java. The message points at brew install openjdk@17. Install that and run the package step again. A longer setup is on the blog, and the product lineup is on",
        "the comparison",
        "Blog",
        "Download",
        _OS_EN,
        "SiliconPlay app icon and the words Free Android emulator for Apple Silicon Macs",
        "SiliconPlay icon",
        "SiliconPlay is not affiliated with Apple Inc. or Google LLC. Android is a trademark of Google LLC. Mac, macOS and Metal are trademarks of Apple Inc.",
    ),
}


from download_i18n import EXTRA
DOWNLOAD.update(EXTRA)


def snippet(prefix: str, slug: str) -> str:
    from guide_notes import NOTES
    return NOTES[prefix][slug]
