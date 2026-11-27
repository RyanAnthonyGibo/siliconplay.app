# -*- coding: utf-8 -*-
"""Remaining languages for the thin-guide expansions."""


def register(L):
    def K(*lines):
        return list(lines)

    L("fr",
      h2k="Raccourcis, Cmd+I d’abord",
      keys=K(
          "Cmd+I installe un seul APK une fois l’instance lancée. Le menu affiche Command-I. Glisser fait la même chose.",
          "F12 ou Command-K bascule entre la saisie et les touches de jeu.",
          "F10, c’est le doigt quand une boîte en veut un.",
          "Command-Shift-G affiche ou cache les boutons à l’écran.",
          "Shift-Escape relâche un doigt virtuel resté enfoncé.",
          "Escape quitte le plein écran. En dehors, c’est Retour Android tant que l’image a le focus.",
      ),
      more="Sur ce site, en français :",
      labels=("l’installation", "les raccourcis", "la comparaison", "le téléchargement"),
      hfaq="Questions",
      **{
        "mumu-player-alternative-mac": (
          "Ce qui ne suit pas depuis MuMu",
          [
            "Une instance MuMu reste dans MuMu. SiliconPlay ne reprend ni les jeux, ni la disposition des touches, ni la session. Le Play Store du tablet SiliconPlay est celui de l’image Play, pas un compte copié depuis un autre programme.",
            "Le DMG ne contient pas l’émulateur. Au premier lancement vous acceptez la licence Android SDK. L’app télécharge ensuite les command-line tools, l’émulateur Apple silicon, platform-tools (adb est dedans) et l’image Play arm64. La tablette est en paysage, 1920×1080, 320 dpi, sans rotation auto, nommée Android 16 Tablet. Si un SDK contient déjà emulator, adb et sdkmanager, vous pouvez pointer ce dossier.",
            "MuMu peut rester le meilleur choix si vous voulez ses préréglages de jeux. SiliconPlay peut créer une autre instance, ce n’est pas la même bibliothèque de profils. Les chemins graphiques diffèrent : MuMu traduit l’OpenGL ES des jeux vers Metal. SiliconPlay dessine Vulkan avec Metal, shaders en safe math pour que le feuillage tienne. Je n’ai pas publié de comparatif des deux phrases.",
          ],
          "Comment je le mettrais à côté de MuMu",
          "La même scène, le même Mac, le même réglage graphique dans le jeu. Si ça saccade, baissez d’abord les graphismes du jeu. La seule mesure que j’ai publiée vient d’un MacBook Pro M3 Max : jusqu’à 60 ips dans un jeu 3D lourd, rendu jusqu’à 2560×1440, 7–43 ms de la touche au jeu. Ce n’est pas une comparaison avec MuMu, et je n’ai pas publié les mêmes chiffres pour M1, M2, M4, M5 ou M6. Le root est éteint et optionnel. L’image Play refuse adb root. Le root est une seconde tablette sur l’image Google APIs, sans Play Store. Ce n’est pas un interrupteur de vitesse.",
          [
            ("SiliconPlay reprend-il mon compte MuMu ?", "Non. Vous vous reconnectez dans l’image Play. Le mot de passe reste dans Android. L’app Mac ne le voit pas."),
            ("Ça marche sur un Mac Intel ?", "Non. Pas compatible avec les Mac Intel. Pris en charge : Apple silicon, M1 à M6, y compris Pro, Max et Ultra. J’ai testé macOS Tahoe et macOS 27 Golden Gate."),
            ("SiliconPlay est-il gratuit ?", "Oui. SiliconPlay est gratuit. Soutenir le projet est facultatif."),
          ],
        ),
        "bluestacks-alternative-mac": (
          "Ce que je peux dire de BlueStacks Air",
          [
            "BlueStacks Air, d’après ses propres prérequis de septembre 2026, fait tourner Android 13 sur Apple silicon et vise les jeux. Il a des années de préréglages, plusieurs instances et une grande équipe d’assistance. SiliconPlay fait tourner Android 16 sur les cœurs ARM du Mac, via l’hyperviseur d’Apple, et dessine Vulkan avec Metal.",
            "Je travaille seul. Si vous avez besoin de la bibliothèque de profils et d’un support, BlueStacks peut rester le meilleur choix. Je préfère le dire plutôt que de faire semblant. NoxPlayer, LDPlayer et MEmu ne tournent pas sur ces Mac. UTM n’a pas d’accélération 3D et ne sert pas à ces jeux. L’émulateur d’Android Studio est l’outil officiel quand vous voulez l’IDE, et il est lourd à cause de l’IDE.",
            "Le premier lancement de SiliconPlay ne charge pas l’image BlueStacks. Il accepte la licence Android SDK et récupère les command-line tools, l’émulateur Apple silicon, platform-tools et l’image Play arm64. La tablette fait 1920×1080, 320 dpi, en paysage, sans rotation auto.",
          ],
          "La même scène, pas deux slogans",
          "Jouez le même passage sur le même Mac et baissez d’abord les graphismes du jeu si un côté saccade. Le root optionnel de SiliconPlay est éteint, et c’est une seconde tablette sur l’image Google APIs, parce que l’image Play refuse adb root. Cette tablette root n’a pas le Play Store. L’app est gratuite. Testée sur macOS Tahoe et macOS 27 Golden Gate, Apple silicon de M1 à M6. Pas compatible avec les Mac Intel.",
          [
            ("C’est Android 16 ou Android 13 ?", "SiliconPlay démarre une tablette Android 16. BlueStacks Air indique Android 13 dans ses propres prérequis. Ce sont deux images, pas deux noms pour la même chose."),
            ("Faut-il le root pour jouer ?", "Non. Le root est éteint. Pour jouer, restez sur la tablette Play. Le root est une seconde tablette sans Play Store."),
            ("Quels Mac ?", "Apple silicon, M1 à M6, y compris Pro, Max et Ultra. Pas compatible avec les Mac Intel. Testé sur macOS Tahoe et macOS 27 Golden Gate."),
          ],
        ),
        "android-emulator-mac-m1-m2-m3-m4": (
          "Une app de M1 à M6",
          [
            "M1, M2, M3, M4, M5 et M6 ne sont pas des téléchargements séparés. SiliconPlay est une app Mac. Pro, Max et Ultra sont les mêmes puces avec plus de cœurs, pas un autre produit. Le premier lancement fait le même travail sur chaque puce : licence Android SDK, puis command-line tools, l’émulateur Apple silicon, platform-tools et l’image Play arm64 dans un dossier que vous choisissez.",
            "La tablette s’appelle Android 16 Tablet, en paysage, 1920×1080 à 320 dpi, rotation auto coupée. Le chiffre 2560×1440 n’est pas la taille de cette tablette. Il vient de la seule mesure publiée, sur un MacBook Pro M3 Max : jusqu’à 60 ips dans un jeu 3D lourd, rendu jusqu’à 2560×1440, 7–43 ms de la touche au jeu. Je n’ai pas publié la même mesure pour M1, M2, M4, M5 ou M6. Les puces plus récentes ont plus de marge. Ce n’est pas un tableau de benchmarks.",
            "S’il manque un JDK, macOS montre le stub /usr/bin/java. Le message indique brew install openjdk@17. La puce ne change pas cette phrase. Un paquet sans bibliothèque ARM64 ne tourne sur aucune puce de la liste. Cette version n’installe pas les APK scindés ni les archives XAPK.",
          ],
          "Ce qu’il ne faut pas déduire du nom de la puce",
          "Si un jeu saccade, baissez d’abord ses graphismes. Ne concluez pas, à partir du nom M1 ou M4, que le Mac est le mauvais. J’ai testé macOS Tahoe et macOS 27 Golden Gate. Une autre version : essayez, et envoyez-moi la puce et la version. Pas compatible avec les Mac Intel. Vulkan est dessiné par Metal, shaders en safe math pour le feuillage. C’est le même chemin sur chaque puce, pas un mode par puce.",
          [
            ("Y a-t-il une version M1 et une version M4 ?", "Non. Une app, de M1 à M6, y compris Pro, Max et Ultra."),
            ("Les 60 ips valent-ils pour mon M1 ?", "Non. Le chiffre est une mesure sur un MacBook Pro M3 Max. Le résultat dépend du jeu, du Mac et des réglages."),
            ("Quelle version de macOS ?", "Testé sur macOS Tahoe et macOS 27 Golden Gate. Pas compatible avec les Mac Intel."),
          ],
        ),
        "free-android-emulator-mac-m1-m5-comparison": (
          "Sur quoi choisir",
          [
            "Cette page n’est ni un classement ni une liste de tarifs. Je construis SiliconPlay, le biais est dit. Ce que coûte un autre programme, ou comment il est licencié, est sur le site de son éditeur. Ici : à quoi sert chaque outil, et ce que je n’ai pas confirmé.",
            "SiliconPlay est gratuit, pour les jeux et pour un seul APK, sans laisser l’IDE ouvert. BlueStacks Air vise les jeux, plusieurs instances et des commandes prêtes. MuMu Player Pro vise les jeux avec clavier, souris et manette. Android Studio est l’environnement de développement : l’émulateur vient avec l’IDE et n’a pas de disposition de touches pour le jeu. UTM est une machine virtuelle générale sans accélération 3D. LDPlayer décrit Windows. MEmu cite Windows. Le support NoxPlayer écrit que la puce Apple M1 n’est pas prise en charge. Waydroid tourne sous Linux.",
            "Sous SiliconPlay, c’est l’émulateur Android officiel, natif sur les cœurs ARM, Android 16, Vulkan via Metal, shaders en safe math. Le premier lancement récupère l’image Play arm64, 1920×1080, 320 dpi, paysage. Le root est une seconde tablette sans store. La seule mesure de performance publiée est celle du MacBook Pro M3 Max, et elle ne compare personne d’autre.",
          ],
          "Un essai honnête",
          "La même scène, le même Mac, le même niveau graphique. Ensuite vous décidez. Je ne mesure pas à votre place quel programme mène dans votre jeu. Si une étape diffère sur votre Mac, je veux la puce, la version de macOS et le nom du jeu. Pas compatible avec les Mac Intel. Pris en charge : Apple silicon, M1 à M6. Testé sur macOS Tahoe et macOS 27 Golden Gate.",
          [
            ("SiliconPlay est-il gratuit ?", "Oui. Soutenir le projet est facultatif. Ce que demandent les autres éditeurs n’est pas sur cette page."),
            ("Quel outil pour développer ?", "Android Studio si vous voulez l’IDE. SiliconPlay si vous voulez essayer un APK sans laisser l’IDE ouvert."),
            ("LDPlayer tourne-t-il sur Mac ?", "LDPlayer décrit Windows. MEmu cite Windows. NoxPlayer écrit que la puce Apple M1 n’est pas prise en charge."),
          ],
        ),
      },
    )
    from guide_notes_more import more
    more(L)
