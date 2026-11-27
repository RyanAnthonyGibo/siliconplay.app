# -*- coding: utf-8 -*-
"""Extra sections for the four thin translated guides.

Each language has its own sentences. The four slugs do not share a paragraph.
"""

SLUGS = (
    "mumu-player-alternative-mac",
    "bluestacks-alternative-mac",
    "android-emulator-mac-m1-m2-m3-m4",
    "free-android-emulator-mac-m1-m5-comparison",
)


def _page(prefix, h2, paragraphs, h2k, keys, closer_h, closer, more, labels, hfaq, faqs):
    root = f"/{prefix}"
    lis = "\n".join(f"<li>{item}</li>" for item in keys)
    body = "\n".join(f"<p>{p}</p>" for p in paragraphs)
    qa = "\n".join(f"<h3>{q}</h3><p>{a}</p>" for q, a in faqs)
    a, b, c, d = labels
    return f"""<!-- seo-expand-2026-11-27 -->
<h2>{h2}</h2>
{body}
<h2>{h2k}</h2>
<ul>
{lis}
</ul>
<h2>{closer_h}</h2>
<p>{closer}</p>
<p>{more} <a href="{root}/blog/android-emulator-mac-m1-m4-setup/">{a}</a>, <a href="{root}/blog/android-emulator-mac-shortcuts/">{b}</a>, <a href="{root}/compare/">{c}</a>, <a href="{root}/download/">{d}</a>.</p>
<h2>{hfaq}</h2>
{qa}
"""


def _keys(lines):
    if not lines[0].startswith("Cmd+I"):
        raise ValueError(lines[0])
    return lines


# Per language: shared shortcut lines (Cmd+I first), link labels, FAQ heading,
# and four slug records: (h2, [p, p, p], closer_h, closer, [(q,a)*3])
# Built below as NOTES[prefix][slug] = html.

def build():
    out = {}
    for prefix, pack in LANGS.items():
        out[prefix] = {}
        keys = _keys(pack["keys"])
        for slug in SLUGS:
            h2, paras, ch, closer, faqs = pack[slug]
            out[prefix][slug] = _page(
                prefix, h2, paras, pack["h2k"], keys, ch, closer,
                pack["more"], pack["labels"], pack["hfaq"], faqs,
            )
    return out


# The practical facts are the same product. The wording and the question
# each page answers are not. Intel Macs is the only Intel phrasing used.
LANGS = {}

def L(prefix, **kwargs):
    LANGS[prefix] = kwargs

# German
L("de",
  h2k="Kurzbefehle, Cmd+I zuerst",
  keys=_keys([
      "Cmd+I installiert eine einzelne APK, sobald die Instanz läuft. Im Menü steht Command-I. Ziehen macht dasselbe.",
      "F12 oder Command-K schaltet Tippen und Spieltasten um.",
      "F10 ist wieder der Finger, wenn ein Dialog einen braucht.",
      "Command-Shift-G zeigt oder versteckt die Tasten auf dem Bildschirm.",
      "Shift-Escape lässt einen hängengebliebenen virtuellen Finger los.",
      "Escape verlässt den Vollbildmodus. Außerhalb ist es Android-Zurück, solange das Bild den Fokus hat.",
  ]),
  more="Weiter auf dieser Seite:",
  labels=("Einrichtung", "Kurzbefehle", "Vergleich", "Download"),
  hfaq="Fragen",
  **{
    "mumu-player-alternative-mac": (
      "Was von MuMu nicht mitkommt",
      [
        "Eine MuMu-Instanz bleibt in MuMu. SiliconPlay übernimmt weder die Spiele noch die Tastenbelegung noch die Anmeldung. Der Play Store auf dem SiliconPlay-Tablet ist der Store im Play-Abbild, nicht ein Konto, das ich aus einem anderen Programm kopiere.",
        "Das DMG enthält den Emulator nicht. Beim ersten Start akzeptierst du die Android-SDK-Lizenz. Danach lädt die App die command-line tools, den Apple-silicon-Emulator, platform-tools (dort liegt adb) und das Play-arm64-Abbild. Das Tablet ist quer, 1920×1080, 320 dpi, ohne Auto-Rotation, Name Android 16 Tablet. Liegt schon ein SDK mit emulator, adb und sdkmanager auf dem Mac, kannst du diesen Ordner wählen.",
        "MuMu kann die bessere Wahl bleiben, wenn du die fertigen Spiel-Presets willst. SiliconPlay hat Create New Instance, das ist aber nicht dieselbe Preset-Bibliothek. Die Grafikwege sind verschieden: MuMu übersetzt OpenGL ES der Spiele nach Metal. SiliconPlay zeichnet Vulkan mit Metal, Shader in safe math, damit Laub stimmt. Ich habe keinen veröffentlichten Vergleich der beiden Sätze.",
      ],
      "Wie ich es neben MuMu prüfen würde",
      "Dieselbe Szene, derselbe Mac, dieselbe Grafikstufe im Spiel. Ruckelt eine Seite, zuerst die Grafik im Spiel senken. Die einzige Messung, die ich veröffentlicht habe, stammt von einem MacBook Pro mit M3 Max: bis zu 60 fps in einem anspruchsvollen 3D-Spiel, Render bis 2560×1440, 7–43 ms von der Taste ins Spiel. Das ist kein MuMu-Vergleich, und ich habe dieselben Zahlen nicht für M1, M2, M4, M5 oder M6 gemessen. Root ist aus und optional. Das Play-Abbild verweigert adb root. Root ist ein zweites Tablet auf dem Google-APIs-Abbild, ohne Play Store. Es ist kein Geschwindigkeitsschalter.",
      [
        ("Übernimmt SiliconPlay meinen MuMu-Account?", "Nein. Du meldest dich im Play-Abbild neu an. Das Passwort bleibt in Android. Die Mac-App sieht es nicht."),
        ("Läuft es auf Intel Macs?", "Nein. Nicht kompatibel mit Intel Macs. Unterstützt sind Apple silicon, M1 bis M6, einschließlich Pro, Max und Ultra. Getestet habe ich auf macOS Tahoe und macOS 27 Golden Gate."),
        ("Ist SiliconPlay kostenlos?", "Ja. SiliconPlay ist kostenlos. Unterstützung für das Projekt ist freiwillig."),
      ],
    ),
    "bluestacks-alternative-mac": (
      "Was ich über BlueStacks Air sagen kann",
      [
        "BlueStacks Air läuft, nach den eigenen Angaben vom September 2026, mit Android 13 auf Apple silicon und zielt auf Spiele. Es hat Jahre an Spiel-Presets, mehrere Instanzen und ein großes Support-Team. SiliconPlay läuft mit Android 16 auf den ARM-Kernen des Mac, über Apples Hypervisor, und zeichnet Vulkan mit Metal.",
        "Ich bin eine Person. Wenn du die Preset-Sammlung und einen Support-Schalter brauchst, kann BlueStacks die passendere Wahl bleiben. Das sage ich lieber, als so zu tun, als hätte eine jüngere App dasselbe Regal. NoxPlayer, LDPlayer und MEmu laufen auf diesen Macs nicht. UTM hat keine 3D-Beschleunigung und taugt nicht für diese Spiele. Der Emulator in Android Studio ist das offizielle Werkzeug, wenn du die IDE willst, und er ist schwer, weil die IDE mitkommt.",
        "Der erste Start von SiliconPlay lädt nicht das BlueStacks-Image. Er akzeptiert die Android-SDK-Lizenz und holt command-line tools, den Apple-silicon-Emulator, platform-tools und das Play-arm64-Abbild. Das Tablet ist 1920×1080, 320 dpi, quer, ohne Auto-Rotation. Ein vorhandenes SDK mit emulator, adb und sdkmanager kannst du direkt angeben.",
      ],
      "Dieselbe Szene, nicht zwei Werbesätze",
      "Spiel dieselbe Stelle auf demselben Mac und senke zuerst die Grafik im Spiel, wenn eine Seite ruckelt. Optionaler Root ist in SiliconPlay aus und ein zweites Tablet auf dem Google-APIs-Abbild, weil das Play-Abbild adb root verweigert. Das rooted Tablet hat keinen Play Store. Spiele-Emulatoren bieten diese Trennung meist nicht an, weil sie keine adb-root-Werkbank sein wollen. Die App ist kostenlos. Getestet habe ich auf macOS Tahoe und macOS 27 Golden Gate, auf Apple silicon von M1 bis M6. Nicht kompatibel mit Intel Macs.",
      [
        ("Ist das Android 16 oder Android 13?", "SiliconPlay startet ein Android-16-Tablet. BlueStacks Air nennt in den eigenen Anforderungen Android 13. Das sind zwei verschiedene Abbilder, nicht zwei Namen für dasselbe."),
        ("Brauche ich Root, um zu spielen?", "Nein. Root ist aus. Für Spiele bleibt das Play-Tablet. Root ist ein zweites Tablet ohne Play Store."),
        ("Welche Macs?", "Apple silicon, M1 bis M6, auch Pro, Max und Ultra. Nicht kompatibel mit Intel Macs. Getestet auf macOS Tahoe und macOS 27 Golden Gate."),
      ],
    ),
    "android-emulator-mac-m1-m2-m3-m4": (
      "Ein Programm für M1 bis M6",
      [
        "M1, M2, M3, M4, M5 und M6 sind keine getrennten Downloads. SiliconPlay ist eine Mac-App. Pro, Max und Ultra sind dieselben Chips mit mehr Kernen, kein anderes Produkt. Der erste Start macht auf jedem Chip dieselbe Arbeit: Android-SDK-Lizenz, dann command-line tools, der Apple-silicon-Emulator, platform-tools und das Play-arm64-Abbild in einen Ordner, den du wählst.",
        "Das Tablet heißt Android 16 Tablet, liegt quer, 1920×1080 bei 320 dpi, Auto-Rotation aus. Die Zahl 2560×1440 ist nicht die Größe dieses Tablets. Sie stammt aus der einen veröffentlichten Messung auf einem MacBook Pro mit M3 Max: bis zu 60 fps in einem anspruchsvollen 3D-Spiel, Render bis 2560×1440, 7–43 ms von der Taste ins Spiel. Dieselbe Messung habe ich nicht für M1, M2, M4, M5 oder M6 veröffentlicht. Neuere Chips haben mehr Reserve. Das ist kein Benchmark-Tabelle.",
        "Fehlt ein JDK, zeigt macOS den Stub /usr/bin/java. Die Meldung nennt brew install openjdk@17. Der Chip ändert diesen Satz nicht. Ein Paket ohne ARM64-Bibliothek läuft auf keinem Chip in der Liste. Geteilte APKs und XAPK installiert diese Version nicht.",
      ],
      "Was du nicht aus den Chip-Namen schließen solltest",
      "Wenn ein Spiel ruckelt, senke zuerst seine Grafik. Entscheide nicht aus dem Namen M1 oder M4, dass der Mac ungeeignet ist. Getestet habe ich auf macOS Tahoe und macOS 27 Golden Gate. Andere macOS-Versionen: ausprobieren und mir Chip und Version schreiben. Nicht kompatibel mit Intel Macs. Vulkan wird von Metal gezeichnet, Shader in safe math, damit Laub stimmt. Das ist derselbe Pfad auf jedem Chip, kein eigener Modus pro Chip.",
      [
        ("Gibt es eine eigene M1- und eine eigene M4-Version?", "Nein. Eine App, M1 bis M6, einschließlich Pro, Max und Ultra."),
        ("Gelten die 60 fps für meinen M1?", "Nein. Die Zahl ist eine Messung auf einem MacBook Pro mit M3 Max. Ergebnisse hängen von Spiel, Mac und Einstellungen ab."),
        ("Welche macOS-Version?", "Getestet auf macOS Tahoe und macOS 27 Golden Gate. Nicht kompatibel mit Intel Macs."),
      ],
    ),
    "free-android-emulator-mac-m1-m5-comparison": (
      "Wonach du wählen solltest",
      [
        "Diese Seite ist keine Rangliste und keine Preisliste. Ich baue SiliconPlay, die Neigung liegt offen. Was ein anderes Programm kostet oder wie es lizenziert, steht auf der Seite des Herstellers. Hier steht, wofür jedes Werkzeug gedacht ist und was ich nicht bestätigt habe.",
        "SiliconPlay ist kostenlos, für Spiele und für eine einzelne APK, ohne die IDE offen zu lassen. BlueStacks Air ist auf Spiele, mehrere Instanzen und fertige Steuerungen ausgerichtet. MuMu Player Pro ist auf Spiele mit Tastatur, Maus und Gamepad ausgerichtet. Android Studio ist die Entwicklungsumgebung, der Emulator kommt mit der IDE und hat keine Spiel-Tastenbelegung. UTM ist eine allgemeine virtuelle Maschine ohne 3D-Beschleunigung. LDPlayer beschreibt Windows. MEmu nennt Windows. Der NoxPlayer-Support schreibt, der Apple-M1-Chip werde nicht unterstützt. Waydroid läuft unter Linux.",
        "Unter SiliconPlay liegt der offizielle Android-Emulator, nativ auf den ARM-Kernen, Android 16, Vulkan über Metal, Shader in safe math. Der erste Start holt das Play-arm64-Abbild, 1920×1080, 320 dpi, quer. Root ist ein zweites Tablet ohne Store. Die einzige veröffentlichte Leistungsmessung ist die vom MacBook Pro mit M3 Max, und sie vergleicht niemanden sonst.",
      ],
      "Ein fairer Test",
      "Dieselbe Szene, derselbe Mac, dieselbe Grafikstufe. Dann entscheiden. Ich messe nicht für dich, welches Programm in deinem Spiel vorn liegt. Wenn ein Schritt auf deinem Mac anders ist, will ich Chip, macOS-Version und den Namen des Spiels. Nicht kompatibel mit Intel Macs. Unterstützt sind Apple silicon, M1 bis M6. Getestet auf macOS Tahoe und macOS 27 Golden Gate.",
      [
        ("Ist SiliconPlay kostenlos?", "Ja. Unterstützung ist freiwillig. Was andere Hersteller verlangen, steht nicht auf dieser Seite."),
        ("Welches Programm ist für Entwicklung?", "Android Studio, wenn du die IDE willst. SiliconPlay, wenn du eine APK prüfen willst, ohne die IDE offen zu lassen."),
        ("Läuft LDPlayer auf dem Mac?", "LDPlayer beschreibt Windows. MEmu nennt Windows. NoxPlayer schreibt, der Apple-M1-Chip werde nicht unterstützt."),
      ],
    ),
  },
)

from guide_notes_rest import register as _register_rest
_register_rest(L)
NOTES = build()
