# -*- coding: utf-8 -*-
"""pt-BR, es-MX, es-ES, it, nl, pl, ru, uk, tr, and the rest."""


def more(L):
    def K(*lines):
        return list(lines)

    L("pt-br",
      h2k="Atalhos, Cmd+I primeiro",
      keys=K(
          "Cmd+I instala um único APK quando a instância está rodando. O menu mostra Command-I. Arrastar faz a mesma instalação.",
          "F12 ou Command-K alterna digitação e teclas de jogo.",
          "F10 é o dedo quando um diálogo precisa de um toque.",
          "Command-Shift-G mostra ou esconde os botões na tela.",
          "Shift-Escape solta um dedo virtual que ficou preso.",
          "Escape sai da tela cheia. Fora dela é o Voltar do Android enquanto a imagem está em foco.",
      ),
      more="Nesta língua:",
      labels=("a configuração", "os atalhos", "a comparação", "o download"),
      hfaq="Perguntas",
      **{
        "mumu-player-alternative-mac": (
          "O que não vem do MuMu",
          [
            "Uma instância do MuMu fica no MuMu. O SiliconPlay não traz os jogos, o mapa de teclas nem a sessão. A Play Store no tablet do SiliconPlay é a loja da imagem Play, não uma conta copiada de outro programa.",
            "O DMG não contém o emulador. Na primeira execução você aceita a licença do Android SDK. O app baixa as command-line tools, o emulador Apple silicon, platform-tools (é onde está o adb) e a imagem Play arm64. O tablet fica deitado, 1920×1080, 320 dpi, sem rotação automática, nome Android 16 Tablet. Se já houver um SDK com emulator, adb e sdkmanager, você pode apontar essa pasta.",
            "O MuMu pode continuar melhor se você quer os presets de jogo prontos. O SiliconPlay cria outra instância, mas isso não é a biblioteca de presets deles. Os caminhos de gráfico são diferentes: o MuMu traduz o OpenGL ES dos jogos para Metal. O SiliconPlay desenha Vulkan com Metal, shaders em safe math para a folhagem sair certa. Não publiquei uma comparação entre as duas frases.",
          ],
          "Como eu compararia os dois",
          "A mesma cena, o mesmo Mac, o mesmo nível de gráfico no jogo. Se travar, baixe primeiro o gráfico do jogo. A única medição que publiquei veio de um MacBook Pro com M3 Max: até 60 fps num jogo 3D pesado, render até 2560×1440, 7–43 ms da tecla ao jogo. Isso não é comparação com o MuMu, e não medi o mesmo em M1, M2, M4, M5 ou M6. Root fica desligado e é opcional. A imagem Play recusa adb root. Root é um segundo tablet na imagem Google APIs, sem Play Store. Não é um botão de velocidade.",
          [
            ("O SiliconPlay leva a minha conta do MuMu?", "Não. Você entra de novo na imagem Play. A senha fica no Android. O app do Mac não a vê."),
            ("Funciona em Mac Intel?", "Não. Não é compatível com Macs Intel. O suporte é Apple silicon, M1 a M6, inclusive Pro, Max e Ultra. Testei no macOS Tahoe e no macOS 27 Golden Gate."),
            ("O SiliconPlay é grátis?", "Sim. O SiliconPlay é grátis. Apoiar o projeto é opcional."),
          ],
        ),
        "bluestacks-alternative-mac": (
          "O que dá para dizer do BlueStacks Air",
          [
            "O BlueStacks Air, pelos requisitos deles de setembro de 2026, roda Android 13 em Apple silicon e mira jogos. Tem anos de presets, várias instâncias e uma equipe grande de suporte. O SiliconPlay roda Android 16 nos núcleos ARM do Mac, pelo Hypervisor da Apple, e desenha Vulkan com Metal.",
            "Eu trabalho sozinho. Se você precisa da estante de presets e de um suporte, o BlueStacks pode continuar a escolha melhor. Prefiro dizer isso a fingir o contrário. NoxPlayer, LDPlayer e MEmu não rodam nesses Macs. O UTM não tem aceleração 3D e não serve para esses jogos. O emulador do Android Studio é a ferramenta oficial quando você quer o IDE, e ele é pesado por causa do IDE.",
            "A primeira execução do SiliconPlay não carrega a imagem do BlueStacks. Ela aceita a licença do Android SDK e busca command-line tools, o emulador Apple silicon, platform-tools e a imagem Play arm64. O tablet é 1920×1080, 320 dpi, deitado, sem rotação automática.",
          ],
          "A mesma cena, não dois anúncios",
          "Jogue o mesmo trecho no mesmo Mac e baixe primeiro o gráfico do jogo se um lado travar. O root opcional do SiliconPlay começa desligado e é um segundo tablet na imagem Google APIs, porque a imagem Play recusa adb root. Esse tablet com root não tem Play Store. O app é grátis. Testado no macOS Tahoe e no macOS 27 Golden Gate, Apple silicon de M1 a M6. Não é compatível com Macs Intel.",
          [
            ("É Android 16 ou Android 13?", "O SiliconPlay sobe um tablet Android 16. O BlueStacks Air cita Android 13 nos próprios requisitos. São duas imagens, não dois nomes para a mesma coisa."),
            ("Preciso de root para jogar?", "Não. O root fica desligado. Para jogar, fique no tablet Play. Root é um segundo tablet sem Play Store."),
            ("Quais Macs?", "Apple silicon, M1 a M6, inclusive Pro, Max e Ultra. Não é compatível com Macs Intel. Testado no macOS Tahoe e no macOS 27 Golden Gate."),
          ],
        ),
        "android-emulator-mac-m1-m2-m3-m4": (
          "Um app do M1 ao M6",
          [
            "M1, M2, M3, M4, M5 e M6 não são downloads separados. O SiliconPlay é um app de Mac. Pro, Max e Ultra são os mesmos chips com mais núcleos, não outro produto. A primeira execução faz o mesmo trabalho em cada chip: licença do Android SDK, depois command-line tools, o emulador Apple silicon, platform-tools e a imagem Play arm64 numa pasta que você escolhe.",
            "O tablet se chama Android 16 Tablet, deitado, 1920×1080 a 320 dpi, rotação automática desligada. O número 2560×1440 não é o tamanho desse tablet. Ele vem da única medição publicada, num MacBook Pro com M3 Max: até 60 fps num jogo 3D pesado, render até 2560×1440, 7–43 ms da tecla ao jogo. Não publiquei a mesma medição para M1, M2, M4, M5 ou M6. Chips mais novos têm mais folga. Isso não é uma tabela de benchmark.",
            "Se faltar JDK, o macOS mostra o stub /usr/bin/java. A mensagem aponta brew install openjdk@17. O chip não muda essa frase. Um pacote sem biblioteca ARM64 não roda em chip nenhum da lista. Esta versão não instala APK dividido nem arquivo XAPK.",
          ],
          "O que o nome do chip não diz",
          "Se um jogo travar, baixe primeiro o gráfico dele. Não conclua, pelo nome M1 ou M4, que o Mac é o errado. Testei no macOS Tahoe e no macOS 27 Golden Gate. Outra versão: experimente e me mande o chip e a versão. Não é compatível com Macs Intel. Vulkan é desenhado pelo Metal, shaders em safe math para a folhagem. É o mesmo caminho em cada chip, não um modo por chip.",
          [
            ("Existe uma versão M1 e outra M4?", "Não. Um app, do M1 ao M6, inclusive Pro, Max e Ultra."),
            ("Os 60 fps valem para o meu M1?", "Não. O número é uma medição num MacBook Pro com M3 Max. O resultado depende do jogo, do Mac e dos ajustes."),
            ("Qual macOS?", "Testado no macOS Tahoe e no macOS 27 Golden Gate. Não é compatível com Macs Intel."),
          ],
        ),
        "free-android-emulator-mac-m1-m5-comparison": (
          "No que vale a pena escolher",
          [
            "Esta página não é ranking nem tabela de valores. Eu faço o SiliconPlay, o viés está dito. Quanto outro programa cobra, ou como licencia, está no site de quem o faz. Aqui está para que serve cada ferramenta, e o que eu não confirmei.",
            "O SiliconPlay é grátis, para jogos e para um APK só, sem deixar o IDE aberto. O BlueStacks Air mira jogos, várias instâncias e controles prontos. O MuMu Player Pro mira jogos com teclado, mouse e controle. O Android Studio é o ambiente de desenvolvimento: o emulador vem com o IDE e não tem mapa de teclas de jogo. O UTM é uma máquina virtual geral sem aceleração 3D. O LDPlayer descreve Windows. O MEmu cita Windows. O suporte do NoxPlayer escreve que o chip Apple M1 não é suportado. O Waydroid roda no Linux.",
            "Por baixo do SiliconPlay está o emulador oficial de Android, nativo nos núcleos ARM, Android 16, Vulkan via Metal, shaders em safe math. A primeira execução busca a imagem Play arm64, 1920×1080, 320 dpi, deitada. Root é um segundo tablet sem loja. A única medição de desempenho publicada é a do MacBook Pro com M3 Max, e ela não compara mais ninguém.",
          ],
          "Um teste justo",
          "A mesma cena, o mesmo Mac, o mesmo nível de gráfico. Aí você decide. Eu não meço no seu lugar qual programa ganha no seu jogo. Se um passo for diferente no seu Mac, quero o chip, a versão do macOS e o nome do jogo. Não é compatível com Macs Intel. O suporte é Apple silicon, M1 a M6. Testado no macOS Tahoe e no macOS 27 Golden Gate.",
          [
            ("O SiliconPlay é grátis?", "Sim. Apoiar o projeto é opcional. O que os outros cobram não está nesta página."),
            ("Qual ferramenta para desenvolver?", "Android Studio se você quer o IDE. SiliconPlay se você quer testar um APK sem deixar o IDE aberto."),
            ("O LDPlayer roda no Mac?", "O LDPlayer descreve Windows. O MEmu cita Windows. O NoxPlayer escreve que o chip Apple M1 não é suportado."),
          ],
        ),
      },
    )

    from guide_notes_es import add_es
    add_es(L, K)
    from guide_notes_eu import add_eu
    add_eu(L, K)
    from guide_notes_asia import add_asia
    add_asia(L, K)
