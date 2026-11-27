# -*- coding: utf-8 -*-

def add_es(L, K):
    L("es-mx",
      h2k="Atajos, Cmd+I primero",
      keys=K(
          "Cmd+I instala un solo APK cuando la instancia ya está corriendo. El menú dice Command-I. Arrastrar hace la misma instalación.",
          "F12 o Command-K cambia entre escritura y teclas de juego.",
          "F10 es el dedo cuando un diálogo lo pide.",
          "Command-Shift-G muestra u oculta los botones en pantalla.",
          "Shift-Escape suelta un dedo virtual que se quedó pegado.",
          "Escape sale de pantalla completa. Afuera es Atrás de Android mientras la imagen tiene el foco.",
      ),
      more="En esta página:",
      labels=("la instalación", "los atajos", "la comparación", "la descarga"),
      hfaq="Preguntas",
      **{
        "mumu-player-alternative-mac": (
          "Lo que no se pasa de MuMu",
          [
            "Una instancia de MuMu se queda en MuMu. SiliconPlay no se lleva los juegos, el mapa de teclas ni la sesión. La Play Store del tablet de SiliconPlay es la tienda de la imagen Play, no una cuenta copiada de otro programa.",
            "El DMG no trae el emulador. En el primer arranque aceptas la licencia del Android SDK. La app baja las command-line tools, el emulador Apple silicon, platform-tools (ahí está adb) y la imagen Play arm64. El tablet queda horizontal, 1920×1080, 320 dpi, sin rotación automática, nombre Android 16 Tablet. Si ya tienes un SDK con emulator, adb y sdkmanager, puedes señalar esa carpeta.",
            "MuMu puede seguir siendo mejor si quieres sus presets de juego. SiliconPlay puede crear otra instancia, y eso no es la misma biblioteca de presets. Los caminos de gráficos son distintos: MuMu traduce el OpenGL ES de los juegos a Metal. SiliconPlay dibuja Vulkan con Metal, shaders en safe math para que el follaje salga bien. No publiqué una comparación entre las dos frases.",
          ],
          "Cómo lo probaría junto a MuMu",
          "La misma escena, la misma Mac, el mismo nivel de gráficos en el juego. Si se traba, baja primero los gráficos del juego. La única medición que publiqué salió de una MacBook Pro con M3 Max: hasta 60 fps en un juego 3D pesado, render hasta 2560×1440, 7–43 ms de la tecla al juego. Eso no compara con MuMu, y no medí lo mismo en M1, M2, M4, M5 o M6. Root está apagado y es opcional. La imagen Play rechaza adb root. Root es un segundo tablet en la imagen Google APIs, sin Play Store. No es un interruptor de velocidad.",
          [
            ("¿SiliconPlay se queda con mi cuenta de MuMu?", "No. Vuelves a entrar en la imagen Play. La contraseña se queda en Android. La app de Mac no la ve."),
            ("¿Funciona en Mac Intel?", "No. No es compatible con Macs Intel. El soporte es Apple silicon, M1 a M6, incluidos Pro, Max y Ultra. Lo probé en macOS Tahoe y macOS 27 Golden Gate."),
            ("¿SiliconPlay es gratis?", "Sí. SiliconPlay es gratis. Apoyar el proyecto es opcional."),
          ],
        ),
        "bluestacks-alternative-mac": (
          "Lo que sí puedo decir de BlueStacks Air",
          [
            "BlueStacks Air, según sus propios requisitos de septiembre de 2026, corre Android 13 en Apple silicon y apunta a juegos. Tiene años de presets, varias instancias y un equipo grande de soporte. SiliconPlay corre Android 16 en los núcleos ARM de la Mac, con el Hypervisor de Apple, y dibuja Vulkan con Metal.",
            "Trabajo solo. Si necesitas el estante de presets y un soporte, BlueStacks puede seguir siendo la mejor opción. Prefiero decirlo a fingir lo contrario. NoxPlayer, LDPlayer y MEmu no corren en estas Mac. UTM no tiene aceleración 3D y no sirve para estos juegos. El emulador de Android Studio es la herramienta oficial cuando quieres el IDE, y pesa por el IDE.",
            "El primer arranque de SiliconPlay no carga la imagen de BlueStacks. Acepta la licencia del Android SDK y trae command-line tools, el emulador Apple silicon, platform-tools y la imagen Play arm64. El tablet es 1920×1080, 320 dpi, horizontal, sin rotación automática.",
          ],
          "La misma escena, no dos anuncios",
          "Juega el mismo tramo en la misma Mac y baja primero los gráficos del juego si un lado se traba. El root opcional de SiliconPlay empieza apagado y es un segundo tablet en la imagen Google APIs, porque la imagen Play rechaza adb root. Ese tablet con root no tiene Play Store. La app es gratis. Probada en macOS Tahoe y macOS 27 Golden Gate, Apple silicon de M1 a M6. No es compatible con Macs Intel.",
          [
            ("¿Es Android 16 o Android 13?", "SiliconPlay levanta un tablet Android 16. BlueStacks Air cita Android 13 en sus propios requisitos. Son dos imágenes, no dos nombres de lo mismo."),
            ("¿Necesito root para jugar?", "No. Root está apagado. Para jugar, quédate en el tablet Play. Root es un segundo tablet sin Play Store."),
            ("¿Qué Macs?", "Apple silicon, M1 a M6, incluidos Pro, Max y Ultra. No es compatible con Macs Intel. Probado en macOS Tahoe y macOS 27 Golden Gate."),
          ],
        ),
        "android-emulator-mac-m1-m2-m3-m4": (
          "Una app de M1 a M6",
          [
            "M1, M2, M3, M4, M5 y M6 no son descargas distintas. SiliconPlay es una app de Mac. Pro, Max y Ultra son los mismos chips con más núcleos, no otro producto. El primer arranque hace el mismo trabajo en cada chip: licencia del Android SDK, luego command-line tools, el emulador Apple silicon, platform-tools y la imagen Play arm64 en una carpeta que tú eliges.",
            "El tablet se llama Android 16 Tablet, horizontal, 1920×1080 a 320 dpi, rotación automática apagada. El número 2560×1440 no es el tamaño de ese tablet. Sale de la única medición publicada, en una MacBook Pro con M3 Max: hasta 60 fps en un juego 3D pesado, render hasta 2560×1440, 7–43 ms de la tecla al juego. No publiqué la misma medición para M1, M2, M4, M5 o M6. Los chips más nuevos tienen más margen. Esto no es una tabla de benchmarks.",
            "Si falta un JDK, macOS muestra el stub /usr/bin/java. El mensaje indica brew install openjdk@17. El chip no cambia esa frase. Un paquete sin biblioteca ARM64 no corre en ningún chip de la lista. Esta versión no instala APK divididos ni archivos XAPK.",
          ],
          "Lo que el nombre del chip no dice",
          "Si un juego se traba, baja primero sus gráficos. No concluyas, por el nombre M1 o M4, que la Mac es la incorrecta. Lo probé en macOS Tahoe y macOS 27 Golden Gate. Otra versión: pruébala y mándame el chip y la versión. No es compatible con Macs Intel. Vulkan lo dibuja Metal, shaders en safe math para el follaje. Es el mismo camino en cada chip, no un modo por chip.",
          [
            ("¿Hay una versión M1 y otra M4?", "No. Una app, de M1 a M6, incluidos Pro, Max y Ultra."),
            ("¿Los 60 fps valen para mi M1?", "No. El número es una medición en una MacBook Pro con M3 Max. El resultado depende del juego, de la Mac y de los ajustes."),
            ("¿Qué macOS?", "Probado en macOS Tahoe y macOS 27 Golden Gate. No es compatible con Macs Intel."),
          ],
        ),
        "free-android-emulator-mac-m1-m5-comparison": (
          "En qué conviene fijarse",
          [
            "Esta página no es un ranking ni una lista de tarifas. Yo hago SiliconPlay, el sesgo está dicho. Lo que cobre otro programa, o cómo lo licencie, está en el sitio de quien lo hace. Aquí está para qué sirve cada herramienta, y qué no confirmé.",
            "SiliconPlay es gratis, para juegos y para un solo APK, sin dejar el IDE abierto. BlueStacks Air apunta a juegos, varias instancias y controles listos. MuMu Player Pro apunta a juegos con teclado, mouse y control. Android Studio es el entorno de desarrollo: el emulador viene con el IDE y no tiene mapa de teclas de juego. UTM es una máquina virtual general sin aceleración 3D. LDPlayer describe Windows. MEmu cita Windows. El soporte de NoxPlayer escribe que el chip Apple M1 no está soportado. Waydroid corre en Linux.",
            "Debajo de SiliconPlay está el emulador oficial de Android, nativo en los núcleos ARM, Android 16, Vulkan vía Metal, shaders en safe math. El primer arranque trae la imagen Play arm64, 1920×1080, 320 dpi, horizontal. Root es un segundo tablet sin tienda. La única medición de rendimiento publicada es la de la MacBook Pro con M3 Max, y no compara a nadie más.",
          ],
          "Una prueba justa",
          "La misma escena, la misma Mac, el mismo nivel de gráficos. Luego decides. Yo no mido por ti qué programa va adelante en tu juego. Si un paso sale distinto en tu Mac, quiero el chip, la versión de macOS y el nombre del juego. No es compatible con Macs Intel. El soporte es Apple silicon, M1 a M6. Probado en macOS Tahoe y macOS 27 Golden Gate.",
          [
            ("¿SiliconPlay es gratis?", "Sí. Apoyar el proyecto es opcional. Lo que cobren los demás no está en esta página."),
            ("¿Qué herramienta para desarrollar?", "Android Studio si quieres el IDE. SiliconPlay si quieres probar un APK sin dejar el IDE abierto."),
            ("¿LDPlayer corre en Mac?", "LDPlayer describe Windows. MEmu cita Windows. NoxPlayer escribe que el chip Apple M1 no está soportado."),
          ],
        ),
      },
    )

    L("es-es",
      h2k="Atajos, Cmd+I primero",
      keys=K(
          "Cmd+I instala un solo APK cuando la instancia ya está en marcha. El menú muestra Command-I. Arrastrar hace la misma instalación.",
          "F12 o Command-K cambia entre escritura y teclas de juego.",
          "F10 es el dedo cuando un diálogo lo necesita.",
          "Command-Shift-G muestra u oculta los botones en pantalla.",
          "Shift-Escape suelta un dedo virtual que se ha quedado pulsado.",
          "Escape sale de pantalla completa. Fuera de ella es Atrás de Android mientras la imagen tiene el foco.",
      ),
      more="En esta web:",
      labels=("la puesta en marcha", "los atajos", "la comparación", "la descarga"),
      hfaq="Preguntas",
      **{
        "mumu-player-alternative-mac": (
          "Lo que no viaja desde MuMu",
          [
            "Una instancia de MuMu se queda en MuMu. SiliconPlay no importa los juegos, la disposición de teclas ni la sesión. La Play Store de la tableta de SiliconPlay es la tienda de la imagen Play, no una cuenta copiada de otro programa.",
            "El DMG no incluye el emulador. En el primer arranque aceptas la licencia del Android SDK. La app descarga las command-line tools, el emulador para Apple silicon, platform-tools (ahí está adb) y la imagen Play arm64. La tableta queda en horizontal, 1920×1080, 320 ppp, sin rotación automática, con el nombre Android 16 Tablet. Si ya tienes un SDK con emulator, adb y sdkmanager, puedes indicar esa carpeta.",
            "MuMu puede seguir encajando mejor si quieres sus preajustes de juego. SiliconPlay puede crear otra instancia, y eso no es su biblioteca de preajustes. Los caminos gráficos no coinciden: MuMu traduce el OpenGL ES de los juegos a Metal. SiliconPlay dibuja Vulkan con Metal, sombreadores en safe math para que el follaje cuadre. No he publicado una comparación entre las dos frases.",
          ],
          "Cómo lo pondría al lado de MuMu",
          "La misma escena, el mismo Mac, el mismo nivel gráfico dentro del juego. Si va a tirones, baja primero los gráficos del juego. La única medición que he publicado salió de un MacBook Pro con M3 Max: hasta 60 fps en un juego 3D exigente, render hasta 2560×1440, 7–43 ms de la tecla al juego. Eso no compara con MuMu, y no he medido lo mismo en M1, M2, M4, M5 o M6. Root está apagado y es opcional. La imagen Play rechaza adb root. Root es una segunda tableta en la imagen Google APIs, sin Play Store. No es un interruptor de velocidad.",
          [
            ("¿SiliconPlay se queda con mi cuenta de MuMu?", "No. Vuelves a entrar en la imagen Play. La contraseña se queda en Android. La app del Mac no la ve."),
            ("¿Funciona en un Mac Intel?", "No. No es compatible con Macs Intel. El soporte es Apple silicon, del M1 al M6, incluidos Pro, Max y Ultra. Lo he probado en macOS Tahoe y macOS 27 Golden Gate."),
            ("¿SiliconPlay es gratis?", "Sí. SiliconPlay es gratis. Apoyar el proyecto es voluntario."),
          ],
        ),
        "bluestacks-alternative-mac": (
          "Lo que puedo afirmar de BlueStacks Air",
          [
            "BlueStacks Air, según sus propios requisitos de septiembre de 2026, ejecuta Android 13 en Apple silicon y está orientado a juegos. Tiene años de preajustes, varias instancias y un equipo grande de soporte. SiliconPlay ejecuta Android 16 en los núcleos ARM del Mac, mediante el Hypervisor de Apple, y dibuja Vulkan con Metal.",
            "Trabajo solo. Si necesitas el estante de preajustes y un servicio de soporte, BlueStacks puede seguir siendo la opción más adecuada. Prefiero decirlo antes que fingir lo contrario. NoxPlayer, LDPlayer y MEmu no se ejecutan en estos Mac. UTM no tiene aceleración 3D y no vale para estos juegos. El emulador de Android Studio es la herramienta oficial cuando quieres el IDE, y pesa por el IDE.",
            "El primer arranque de SiliconPlay no carga la imagen de BlueStacks. Acepta la licencia del Android SDK y obtiene command-line tools, el emulador para Apple silicon, platform-tools y la imagen Play arm64. La tableta es de 1920×1080, 320 ppp, apaisada, sin rotación automática.",
          ],
          "La misma escena, no dos eslóganes",
          "Juega el mismo tramo en el mismo Mac y baja primero los gráficos del juego si un lado va a tirones. El root opcional de SiliconPlay empieza apagado y es una segunda tableta en la imagen Google APIs, porque la imagen Play rechaza adb root. Esa tableta con root no incluye Play Store. La app es gratis. Probada en macOS Tahoe y macOS 27 Golden Gate, Apple silicon del M1 al M6. No es compatible con Macs Intel.",
          [
            ("¿Es Android 16 o Android 13?", "SiliconPlay arranca una tableta Android 16. BlueStacks Air cita Android 13 en sus propios requisitos. Son dos imágenes, no dos nombres para lo mismo."),
            ("¿Hace falta root para jugar?", "No. Root está apagado. Para jugar, quédate en la tableta Play. Root es una segunda tableta sin Play Store."),
            ("¿Qué Macs?", "Apple silicon, del M1 al M6, incluidos Pro, Max y Ultra. No es compatible con Macs Intel. Probado en macOS Tahoe y macOS 27 Golden Gate."),
          ],
        ),
        "android-emulator-mac-m1-m2-m3-m4": (
          "Una app del M1 al M6",
          [
            "M1, M2, M3, M4, M5 y M6 no son descargas separadas. SiliconPlay es una app para Mac. Pro, Max y Ultra son los mismos chips con más núcleos, no otro producto. El primer arranque hace el mismo trabajo en cada chip: licencia del Android SDK, luego command-line tools, el emulador para Apple silicon, platform-tools y la imagen Play arm64 en una carpeta que eliges.",
            "La tableta se llama Android 16 Tablet, en horizontal, 1920×1080 a 320 ppp, rotación automática desactivada. La cifra 2560×1440 no es el tamaño de esa tableta. Sale de la única medición publicada, en un MacBook Pro con M3 Max: hasta 60 fps en un juego 3D exigente, render hasta 2560×1440, 7–43 ms de la tecla al juego. No he publicado la misma medición para M1, M2, M4, M5 o M6. Los chips más nuevos tienen más margen. Esto no es una tabla de benchmarks.",
            "Si falta un JDK, macOS muestra el stub /usr/bin/java. El mensaje indica brew install openjdk@17. El chip no cambia esa frase. Un paquete sin biblioteca ARM64 no se ejecuta en ningún chip de la lista. Esta versión no instala APK divididos ni archivos XAPK.",
          ],
          "Lo que el nombre del chip no permite afirmar",
          "Si un juego va a tirones, baja primero sus gráficos. No concluyas, por el nombre M1 o M4, que el Mac no sirve. Lo he probado en macOS Tahoe y macOS 27 Golden Gate. Otra versión: pruébala y envíame el chip y la versión. No es compatible con Macs Intel. Vulkan lo dibuja Metal, sombreadores en safe math para el follaje. Es el mismo camino en cada chip, no un modo por chip.",
          [
            ("¿Hay una versión M1 y otra M4?", "No. Una app, del M1 al M6, incluidos Pro, Max y Ultra."),
            ("¿Los 60 fps valen para mi M1?", "No. La cifra es una medición en un MacBook Pro con M3 Max. El resultado depende del juego, del Mac y de los ajustes."),
            ("¿Qué versión de macOS?", "Probado en macOS Tahoe y macOS 27 Golden Gate. No es compatible con Macs Intel."),
          ],
        ),
        "free-android-emulator-mac-m1-m5-comparison": (
          "En qué fijarse al elegir",
          [
            "Esta página no es una clasificación ni una lista de tarifas. Yo hago SiliconPlay, el sesgo está declarado. Lo que cobre otro programa, o cómo lo licencie, está en la web de quien lo hace. Aquí está para qué sirve cada herramienta, y qué no he confirmado.",
            "SiliconPlay es gratis, para juegos y para un solo APK, sin dejar el IDE abierto. BlueStacks Air se orienta a juegos, varias instancias y controles preparados. MuMu Player Pro se orienta a juegos con teclado, ratón y mando. Android Studio es el entorno de desarrollo: el emulador llega con el IDE y no tiene disposición de teclas de juego. UTM es una máquina virtual general sin aceleración 3D. LDPlayer describe Windows. MEmu cita Windows. El soporte de NoxPlayer escribe que el chip Apple M1 no está soportado. Waydroid se ejecuta en Linux.",
            "Debajo de SiliconPlay está el emulador oficial de Android, nativo en los núcleos ARM, Android 16, Vulkan mediante Metal, sombreadores en safe math. El primer arranque obtiene la imagen Play arm64, 1920×1080, 320 ppp, apaisada. Root es una segunda tableta sin tienda. La única medición de rendimiento publicada es la del MacBook Pro con M3 Max, y no compara a nadie más.",
          ],
          "Una prueba justa",
          "La misma escena, el mismo Mac, el mismo nivel gráfico. Luego decides. Yo no mido por ti qué programa va por delante en tu juego. Si un paso sale distinto en tu Mac, quiero el chip, la versión de macOS y el nombre del juego. No es compatible con Macs Intel. El soporte es Apple silicon, del M1 al M6. Probado en macOS Tahoe y macOS 27 Golden Gate.",
          [
            ("¿SiliconPlay es gratis?", "Sí. Apoyar el proyecto es voluntario. Lo que cobren los demás no está en esta página."),
            ("¿Qué herramienta para desarrollar?", "Android Studio si quieres el IDE. SiliconPlay si quieres probar un APK sin dejar el IDE abierto."),
            ("¿LDPlayer funciona en el Mac?", "LDPlayer describe Windows. MEmu cita Windows. NoxPlayer escribe que el chip Apple M1 no está soportado."),
          ],
        ),
      },
    )
