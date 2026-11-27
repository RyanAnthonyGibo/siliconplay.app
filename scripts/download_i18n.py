# -*- coding: utf-8 -*-
"""Download-page copy for the 20 localized landing pages."""

def pack(lang, og, title, desc, h1, start, done, lead, link, h2setup, steps, h2need, needs, h2keys, keys, tail, compare, blog, crumb, os_line, og_alt, icon_alt, legal, rtl=False):
    return {
        "lang": lang, "og_locale": og, "rtl": rtl, "title": title, "desc": desc, "h1": h1,
        "start": start, "done": done, "lead": lead, "link": link, "h2setup": h2setup,
        "steps": steps, "h2need": h2need, "needs": needs, "h2keys": h2keys, "keys": keys,
        "tail": tail, "compare": compare, "blog": blog, "crumb": crumb, "os": os_line,
        "og_alt": og_alt, "icon_alt": icon_alt, "legal": legal,
    }

# Shared factual steps are translated per language. Cmd+I is always the first shortcut.
EXTRA = {}

def add(prefix, **kwargs):
    EXTRA[prefix] = pack(**kwargs)

add("de", lang="de", og="de_DE",
    title="SiliconPlay für den Mac laden (M1–M6)",
    desc="SiliconPlay 1.1.3 laden: kostenloser Android-Emulator für Apple-Silicon-Macs von M1 bis M6. Getestet auf macOS Tahoe und macOS 27 Golden Gate. Nicht kompatibel mit Intel Macs.",
    h1="SiliconPlay für den Mac laden",
    start="Der Download wird vorbereitet…",
    done="Der Download sollte gleich starten. Wenn nicht, nimm den Link.",
    lead="SiliconPlay ist ein kostenloser Android-Emulator für Macs mit Apple silicon, von M1 bis M6. Die Datei ist SiliconPlay.dmg, Version 1.1.3. Das DMG ist die Mac-App. Android selbst lädt beim ersten Öffnen.",
    link="SiliconPlay für den Mac laden",
    h2setup="Wenn die Datei da ist",
    steps=[
        "Öffne das DMG und ziehe SiliconPlay in den Ordner Programme.",
        "Öffne SiliconPlay. Der erste Start akzeptiert die Android-SDK-Lizenz und lädt den Apple-silicon-Emulator, platform-tools und das Play-arm64-Abbild, außer du hast schon ein SDK mit emulator, adb und sdkmanager.",
        "Wenn das Android-16-Tablet da ist (1920×1080, 320 dpi, quer), melde dich bei Google Play an oder installiere eine APK.",
    ],
    h2need="Was du brauchst",
    needs=[
        "Einen Mac mit Apple silicon, M1 bis M6, auch Pro, Max und Ultra.",
        "Getestet auf macOS Tahoe und macOS 27 Golden Gate. Eine andere Version: ausprobieren und mir schreiben, was passiert ist.",
        "Nicht kompatibel mit Intel Macs.",
    ],
    h2keys="Kurzbefehle, Cmd+I zuerst",
    keys=[
        "Cmd+I installiert eine einzelne APK, sobald Android läuft. Im Menü steht Command-I. Ziehen macht dasselbe.",
        "F12 oder Command-K schaltet Tippen und Spieltasten um.",
        "F10 ist der Finger, wenn ein Dialog einen braucht.",
        "Command-Shift-G zeigt oder versteckt die Tasten auf dem Bildschirm.",
        "Shift-Escape lässt einen hängengebliebenen virtuellen Finger los.",
        "Escape verlässt den Vollbildmodus. Außerhalb ist es Android-Zurück, solange das Bild den Fokus hat.",
    ],
    tail="Stoppt das Einrichten wegen eines fehlenden JDK, zeigt macOS den Stub /usr/bin/java. Die Meldung nennt brew install openjdk@17. Installieren und den Paketschritt erneut ausführen. Die längere Einrichtung steht im Blog, die Einordnung der Programme auf",
    compare="dem Vergleich", blog="Blog", crumb="Download",
    os_line="macOS Tahoe und macOS 27 Golden Gate (getestet), Apple Silicon M1–M6",
    og_alt="SiliconPlay-Symbol und der Text kostenloser Android-Emulator für den Mac",
    icon_alt="SiliconPlay-Symbol",
    legal="SiliconPlay ist nicht mit Apple Inc. oder Google LLC verbunden. Android ist eine Marke von Google LLC. Mac, macOS und Metal sind Marken von Apple Inc.")

add("fr", lang="fr", og="fr_FR",
    title="Télécharger SiliconPlay pour Mac (M1–M6)",
    desc="Télécharger SiliconPlay 1.1.3, émulateur Android gratuit pour Mac Apple silicon de M1 à M6. Testé sur macOS Tahoe et macOS 27 Golden Gate. Pas compatible avec les Mac Intel.",
    h1="Télécharger SiliconPlay pour Mac",
    start="Préparation du téléchargement…",
    done="Le téléchargement devrait commencer. Sinon, utilisez le lien.",
    lead="SiliconPlay est un émulateur Android gratuit pour les Mac Apple silicon, de M1 à M6. Le fichier est SiliconPlay.dmg, version 1.1.3. Le DMG est l’app Mac. Android se télécharge au premier lancement.",
    link="Télécharger SiliconPlay pour Mac",
    h2setup="Une fois le fichier là",
    steps=[
        "Ouvrez le DMG et glissez SiliconPlay dans Applications.",
        "Ouvrez SiliconPlay. Le premier lancement accepte la licence Android SDK et télécharge l’émulateur Apple silicon, platform-tools et l’image Play arm64, sauf si vous avez déjà un SDK avec emulator, adb et sdkmanager.",
        "Quand la tablette Android 16 est là (1920×1080, 320 dpi, paysage), connectez-vous à Google Play ou installez un APK.",
    ],
    h2need="Ce qu’il vous faut",
    needs=[
        "Un Mac Apple silicon, M1 à M6, y compris Pro, Max et Ultra.",
        "Testé sur macOS Tahoe et macOS 27 Golden Gate. Une autre version : essayez et dites-moi ce qui se passe.",
        "Pas compatible avec les Mac Intel.",
    ],
    h2keys="Raccourcis, Cmd+I d’abord",
    keys=[
        "Cmd+I installe un seul APK une fois Android lancé. Le menu affiche Command-I. Le glisser-déposer fait la même chose.",
        "F12 ou Command-K bascule entre la saisie et les touches de jeu.",
        "F10, c’est le doigt quand une boîte de dialogue en veut un.",
        "Command-Shift-G affiche ou cache les boutons à l’écran.",
        "Shift-Escape relâche un doigt virtuel resté enfoncé.",
        "Escape quitte le plein écran. En dehors, c’est Retour Android tant que l’image a le focus.",
    ],
    tail="Si l’installation s’arrête sur un JDK manquant, macOS montre le stub /usr/bin/java. Le message indique brew install openjdk@17. Installez-le et relancez l’étape des paquets. La mise en route longue est sur le blog, et la place de chaque outil sur",
    compare="la comparaison", blog="Blog", crumb="Téléchargement",
    os_line="macOS Tahoe et macOS 27 Golden Gate (testé), Apple Silicon M1–M6",
    og_alt="Icône SiliconPlay et le texte émulateur Android gratuit pour Mac",
    icon_alt="Icône SiliconPlay",
    legal="SiliconPlay n’est pas affilié à Apple Inc. ni à Google LLC. Android est une marque de Google LLC. Mac, macOS et Metal sont des marques d’Apple Inc.")

add("pt-br", lang="pt-BR", og="pt_BR",
    title="Baixar o SiliconPlay para Mac (M1–M6)",
    desc="Baixe o SiliconPlay 1.1.3, emulador de Android grátis para Macs com Apple silicon, do M1 ao M6. Testado no macOS Tahoe e no macOS 27 Golden Gate. Não é compatível com Macs Intel.",
    h1="Baixar o SiliconPlay para Mac",
    start="Preparando o download…",
    done="O download deve começar em instantes. Se não começar, use o link.",
    lead="O SiliconPlay é um emulador de Android grátis para Macs com Apple silicon, do M1 ao M6. O arquivo é SiliconPlay.dmg, versão 1.1.3. O DMG é o app do Mac. O Android em si baixa na primeira abertura.",
    link="Baixar o SiliconPlay para Mac",
    h2setup="Quando o arquivo chegar",
    steps=[
        "Abra o DMG e arraste o SiliconPlay para Aplicativos.",
        "Abra o SiliconPlay. A primeira execução aceita a licença do Android SDK e baixa o emulador Apple silicon, o platform-tools e a imagem Play arm64, a menos que você já tenha um SDK com emulator, adb e sdkmanager.",
        "Quando o tablet Android 16 aparecer (1920×1080, 320 dpi, paisagem), entre no Google Play ou instale um APK.",
    ],
    h2need="O que você precisa",
    needs=[
        "Um Mac com Apple silicon, M1 a M6, inclusive Pro, Max e Ultra.",
        "Testado no macOS Tahoe e no macOS 27 Golden Gate. Em outra versão, experimente e me conte o que aconteceu.",
        "Não é compatível com Macs Intel.",
    ],
    h2keys="Atalhos, Cmd+I primeiro",
    keys=[
        "Cmd+I instala um único APK quando o Android está rodando. O menu mostra Command-I. Arrastar faz a mesma instalação.",
        "F12 ou Command-K alterna entre digitação e teclas de jogo.",
        "F10 é o dedo quando um diálogo precisa de um toque.",
        "Command-Shift-G mostra ou esconde os botões na tela.",
        "Shift-Escape solta um dedo virtual que ficou preso.",
        "Escape sai da tela cheia. Fora dela, é o Voltar do Android enquanto a imagem está em foco.",
    ],
    tail="Se a instalação parar por falta de JDK, o macOS está mostrando o stub /usr/bin/java. A mensagem aponta brew install openjdk@17. Instale e rode o passo dos pacotes de novo. O passo a passo longo está no blog, e o lugar de cada ferramenta em",
    compare="a comparação", blog="Blog", crumb="Download",
    os_line="macOS Tahoe e macOS 27 Golden Gate (testado), Apple Silicon M1–M6",
    og_alt="Ícone do SiliconPlay e o texto emulador de Android grátis para Mac",
    icon_alt="Ícone do SiliconPlay",
    legal="O SiliconPlay não é afiliado à Apple Inc. nem à Google LLC. Android é marca da Google LLC. Mac, macOS e Metal são marcas da Apple Inc.")

add("es-mx", lang="es-MX", og="es_MX",
    title="Descargar SiliconPlay para Mac (M1–M6), México",
    desc="Descarga SiliconPlay 1.1.3, emulador de Android gratis para Macs con Apple silicon, del M1 al M6. Probado en macOS Tahoe y macOS 27 Golden Gate. No es compatible con Macs Intel.",
    h1="Descargar SiliconPlay para Mac",
    start="Preparando la descarga…",
    done="La descarga debe empezar en un momento. Si no, usa el enlace.",
    lead="SiliconPlay es un emulador de Android gratis para Macs con Apple silicon, del M1 al M6. El archivo es SiliconPlay.dmg, versión 1.1.3. El DMG es la app de Mac. Android se descarga la primera vez que la abres.",
    link="Descargar SiliconPlay para Mac",
    h2setup="Cuando llegue el archivo",
    steps=[
        "Abre el DMG y arrastra SiliconPlay a Aplicaciones.",
        "Abre SiliconPlay. El primer arranque acepta la licencia del Android SDK y descarga el emulador Apple silicon, platform-tools y la imagen Play arm64, salvo que ya tengas un SDK con emulator, adb y sdkmanager.",
        "Cuando aparezca la tableta Android 16 (1920×1080, 320 dpi, horizontal), entra a Google Play o instala un APK.",
    ],
    h2need="Qué necesitas",
    needs=[
        "Una Mac con Apple silicon, M1 a M6, incluidos Pro, Max y Ultra.",
        "Probado en macOS Tahoe y macOS 27 Golden Gate. En otra versión, pruébalo y cuéntame qué pasó.",
        "No es compatible con Macs Intel.",
    ],
    h2keys="Atajos, Cmd+I primero",
    keys=[
        "Cmd+I instala un solo APK cuando Android ya está corriendo. El menú dice Command-I. Arrastrar hace la misma instalación.",
        "F12 o Command-K cambia entre escritura y teclas de juego.",
        "F10 es el dedo cuando un diálogo lo pide.",
        "Command-Shift-G muestra u oculta los botones en pantalla.",
        "Shift-Escape suelta un dedo virtual que se quedó pegado.",
        "Escape sale de pantalla completa. Afuera es Atrás de Android mientras la imagen tiene el foco.",
    ],
    tail="Si la instalación se detiene por un JDK faltante, macOS está mostrando el stub /usr/bin/java. El mensaje indica brew install openjdk@17. Instálalo y vuelve a correr el paso de paquetes. La guía larga está en el blog, y el lugar de cada herramienta en",
    compare="la comparación", blog="Blog", crumb="Descarga",
    os_line="macOS Tahoe y macOS 27 Golden Gate (probado), Apple Silicon M1–M6",
    og_alt="Icono de SiliconPlay y el texto emulador de Android gratis para Mac",
    icon_alt="Icono de SiliconPlay",
    legal="SiliconPlay no está afiliado a Apple Inc. ni a Google LLC. Android es una marca de Google LLC. Mac, macOS y Metal son marcas de Apple Inc.")

add("es-es", lang="es-ES", og="es_ES",
    title="Descargar SiliconPlay para Mac (M1–M6), España",
    desc="Descarga SiliconPlay 1.1.3, emulador de Android gratis para Macs con chip de Apple, del M1 al M6. Probado en macOS Tahoe y macOS 27 Golden Gate. No es compatible con Macs Intel.",
    h1="Descargar SiliconPlay para el Mac",
    start="Preparando la descarga…",
    done="La descarga debería empezar enseguida. Si no, usa el enlace.",
    lead="SiliconPlay es un emulador de Android gratis para Macs con chip de Apple, del M1 al M6. El archivo es SiliconPlay.dmg, versión 1.1.3. El DMG es la app del Mac. Android se descarga la primera vez que la abres.",
    link="Descargar SiliconPlay para Mac",
    h2setup="Cuando tengas el archivo",
    steps=[
        "Abre el DMG y arrastra SiliconPlay a la carpeta Aplicaciones.",
        "Abre SiliconPlay. El primer arranque acepta la licencia del Android SDK y descarga el emulador para Apple silicon, platform-tools y la imagen Play arm64, salvo que ya tengas un SDK con emulator, adb y sdkmanager.",
        "Cuando aparezca la tableta Android 16 (1920×1080, 320 ppp, apaisada), entra en Google Play o instala un APK.",
    ],
    h2need="Qué hace falta",
    needs=[
        "Un Mac con chip de Apple, del M1 al M6, incluidos Pro, Max y Ultra.",
        "Probado en macOS Tahoe y macOS 27 Golden Gate. En otra versión, pruébalo y dime qué ha pasado.",
        "No es compatible con Macs Intel.",
    ],
    h2keys="Atajos, Cmd+I primero",
    keys=[
        "Cmd+I instala un solo APK cuando Android ya está en marcha. El menú muestra Command-I. Arrastrar hace la misma instalación.",
        "F12 o Command-K cambia entre escritura y teclas de juego.",
        "F10 es el dedo cuando un diálogo lo necesita.",
        "Command-Shift-G muestra u oculta los botones en pantalla.",
        "Shift-Escape suelta un dedo virtual que se ha quedado pulsado.",
        "Escape sale de pantalla completa. Fuera de ella es Atrás de Android mientras la imagen tiene el foco.",
    ],
    tail="Si la instalación se para por falta de JDK, macOS está mostrando el stub /usr/bin/java. El mensaje indica brew install openjdk@17. Instálalo y repite el paso de los paquetes. La guía larga está en el blog, y el sitio de cada herramienta en",
    compare="la comparación", blog="Blog", crumb="Descarga",
    os_line="macOS Tahoe y macOS 27 Golden Gate (probado), Apple Silicon M1–M6",
    og_alt="Icono de SiliconPlay y el texto emulador de Android gratis para Mac",
    icon_alt="Icono de SiliconPlay",
    legal="SiliconPlay no está afiliado a Apple Inc. ni a Google LLC. Android es una marca de Google LLC. Mac, macOS y Metal son marcas de Apple Inc.")

from download_i18n_b import register as _register_rest
_register_rest(add)
