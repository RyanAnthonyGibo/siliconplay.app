# -*- coding: utf-8 -*-

def add_asia(L, K):
    def one(prefix, h2k, keys, more, labels, hfaq, pages):
        L(prefix, h2k=h2k, keys=K(*keys), more=more, labels=labels, hfaq=hfaq, **pages)

    one("ja", "ショートカット。最初は Cmd+I", [
        "Cmd+I はインスタンスが動いているときに APK を 1 つ入れます。メニューでは Command-I です。ドラッグも同じインストールです。",
        "F12 または Command-K で、文字入力とゲームキーを切り替えます。",
        "F10 は、ダイアログが指を求めるときの直接タッチです。",
        "Command-Shift-G は画面上のボタンを表示または非表示にします。",
        "Shift-Escape は押しっぱなしの仮想指を離します。",
        "Escape はフルスクリーンを終了します。外では、画面にフォーカスがあるあいだ Android の戻るです。",
    ], "このサイトでは:", ("セットアップ", "ショートカット", "比較", "ダウンロード"), "質問", {
        "mumu-player-alternative-mac": ("MuMu から持ってこれないもの", [
            "MuMu のインスタンスは MuMu に残ります。SiliconPlay はゲームもキー配置もログイン状態も引き継ぎません。SiliconPlay のタブレットにある Play ストアは Play イメージのストアであり、別のソフトからコピーしたアカウントではありません。",
            "DMG にエミュレーターは入っていません。初回起動で Android SDK のライセンスに同意します。そのあと command-line tools、Apple silicon 向けエミュレーター、platform-tools（adb はここ）、Play arm64 イメージを取得します。タブレットは横、1920×1080、320 dpi、自動回転なし、名前は Android 16 Tablet です。emulator、adb、sdkmanager のある SDK がすでにあるなら、そのフォルダを指定できます。",
            "ゲーム用プリセットが要るなら、MuMu の方が合うことがあります。SiliconPlay は別インスタンスを作れますが、それはプリセットの庫ではありません。描き方も違います。MuMu はゲームの OpenGL ES を Metal に変換します。SiliconPlay は Vulkan を Metal で描き、葉が正しく出るようシェーダーを safe math でコンパイルします。この二つの文を比べた測定は出していません。",
        ], "MuMu の横で確かめるなら",
           "同じ場面、同じ Mac、ゲーム内の同じ画質です。カクつくなら、先にゲーム側の画質を下げます。公表している測定は MacBook Pro（M3 Max）の一つだけです。負荷の高い 3D で最大 60 fps、描画は最大 2560×1440、キーからゲームまで 7–43 ms。これは MuMu との比較ではなく、M1、M2、M4、M5、M6 では同じ数字を出していません。root はオフで、任意です。Play イメージは adb root を拒みます。root は Google APIs イメージ上の二つ目のタブレットで、Play ストアはありません。速度のスイッチではありません。",
           [("MuMu のアカウントは引き継がれますか？", "いいえ。Play イメージで入り直します。パスワードは Android の中に残り、Mac アプリは見ません。"),
            ("Intel Mac で動きますか？", "動きません。Intel Macs には対応していません。対応は Apple silicon の M1 から M6、Pro、Max、Ultra を含みます。macOS Tahoe と macOS 27 Golden Gate で確認しています。"),
            ("SiliconPlay は無料ですか？", "はい。無料です。プロジェクトへの支援は任意です。")]),
        "bluestacks-alternative-mac": ("BlueStacks Air について言えること", [
            "BlueStacks Air は、2026年9月の自身の要件では、Apple silicon 上で Android 13 を動かし、ゲーム向けです。長年のプリセット、複数インスタンス、大きなサポート体制があります。SiliconPlay は Mac の ARM コアで、Apple の Hypervisor を通して Android 16 を動かし、Vulkan を Metal で描きます。",
            "作っているのは一人です。プリセットの棚とサポート窓口が要るなら、BlueStacks の方が合うことがあります。ないものをあると言うより、そう書きます。NoxPlayer、LDPlayer、MEmu はこれらの Mac では動きません。UTM には 3D アクセラレーションがなく、これらのゲームには向きません。Android Studio のエミュレーターは IDE が欲しいときの公式の道具で、IDE のせいで重いです。",
            "SiliconPlay の初回は BlueStacks のイメージを読みません。Android SDK のライセンスに同意し、command-line tools、Apple silicon 向けエミュレーター、platform-tools、Play arm64 イメージを取ります。タブレットは 1920×1080、320 dpi、横、自動回転なしです。",
        ], "同じ場面で見る",
           "同じ箇所を同じ Mac で遊び、片方がカクつくなら先にゲームの画質を下げます。SiliconPlay の root は最初オフで、Play イメージが adb root を拒むため、Google APIs イメージ上の二つ目のタブレットです。そのタブレットに Play ストアはありません。アプリは無料です。macOS Tahoe と macOS 27 Golden Gate、M1 から M6 の Apple silicon で確認しています。Intel Macs には対応していません。",
           [("Android 16 ですか、13 ですか？", "SiliconPlay は Android 16 のタブレットを起動します。BlueStacks Air は自身の要件で Android 13 と書いています。同じものの二つの名前ではありません。"),
            ("遊ぶのに root は要りますか？", "要りません。root はオフです。遊ぶなら Play のタブレットのままです。root はストアのない二つ目のタブレットです。"),
            ("どの Mac ですか？", "Apple silicon の M1 から M6。Pro、Max、Ultra を含みます。Intel Macs には対応していません。macOS Tahoe と macOS 27 Golden Gate で確認しています。")]),
        "android-emulator-mac-m1-m2-m3-m4": ("M1 から M6 まで一つのアプリ", [
            "M1、M2、M3、M4、M5、M6 は別々のダウンロードではありません。SiliconPlay は一つの Mac アプリです。Pro、Max、Ultra はコアが多い同じチップで、別製品ではありません。初回はどのチップでも同じ作業です。Android SDK のライセンスのあと、command-line tools、Apple silicon 向けエミュレーター、platform-tools、Play arm64 イメージを、選んだフォルダへ入れます。",
            "タブレットの名前は Android 16 Tablet、横、1920×1080、320 dpi、自動回転オフです。2560×1440 はこのタブレットのサイズではありません。公表している唯一の測定、M3 Max の MacBook Pro の数字です。負荷の高い 3D で最大 60 fps、描画は最大 2560×1440、キーからゲームまで 7–43 ms。M1、M2、M4、M5、M6 では同じ測定を出していません。",
            "JDK がないと、macOS は /usr/bin/java のスタブを見せます。メッセージは brew install openjdk@17 を指します。チップはこの文を変えません。ARM64 のライブラリがないパッケージは、一覧のどのチップでも動きません。この版は分割 APK と XAPK を入れません。",
        ], "チップの名前から読まないこと",
           "ゲームがカクつくなら、先にそのゲームの画質を下げます。M1 や M4 という名前から、Mac が不向きだと決めないでください。macOS Tahoe と macOS 27 Golden Gate で確認しています。別の版なら試し、チップとバージョンを教えてください。Intel Macs には対応していません。Vulkan は Metal が描き、葉のためにシェーダーは safe math です。チップごとのモードではありません。",
           [("M1 版と M4 版は別ですか？", "別ではありません。一つのアプリで、M1 から M6、Pro、Max、Ultra を含みます。"),
            ("60 fps は自分の M1 にも当てはまりますか？", "当てはまりません。数字は M3 Max の MacBook Pro での測定です。結果はゲーム、Mac、設定で変わります。"),
            ("どの macOS ですか？", "macOS Tahoe と macOS 27 Golden Gate で確認しています。Intel Macs には対応していません。")]),
        "free-android-emulator-mac-m1-m5-comparison": ("何で選ぶか", [
            "このページは順位表でも料金表でもありません。SiliconPlay は私が作っているので、偏りは先に書きます。他のソフトが何を求めるか、どう許諾するかは、作り手のサイトにあります。ここにあるのは、各ツールが何のためのもので、私が確認していないことは何かです。",
            "SiliconPlay は無料で、ゲームと APK 1 枚のため、IDE を開いたままにしません。BlueStacks Air はゲーム、複数インスタンス、用意された操作向けです。MuMu Player Pro はキーボード、マウス、ゲームパッドでのゲーム向けです。Android Studio は開発環境で、エミュレーターは IDE と一緒に来て、ゲーム用のキー配置はありません。UTM は 3D アクセラレーションのない汎用の仮想マシンです。LDPlayer は Windows 向けと書いています。MEmu の要件は Windows です。NoxPlayer のサポートは Apple M1 チップに非対応と書いています。Waydroid は Linux です。",
            "SiliconPlay の下は公式の Android エミュレーターで、ARM コア上でネイティブ、Android 16、Vulkan は Metal、シェーダーは safe math です。初回は Play arm64 イメージを取り、1920×1080、320 dpi、横です。root はストアのない二つ目のタブレットです。公表している性能の測定は M3 Max の MacBook Pro のものだけで、他の誰かと比べていません。",
        ], "公平な試し方",
           "同じ場面、同じ Mac、同じ画質です。そのあと自分で決めます。あなたのゲームでどちらが前かは、私は測りません。手順が Mac で違ったら、チップ、macOS の版、ゲーム名が欲しいです。Intel Macs には対応していません。対応は Apple silicon の M1 から M6。macOS Tahoe と macOS 27 Golden Gate で確認しています。",
           [("SiliconPlay は無料ですか？", "はい。支援は任意です。他の作り手が求めるものはこのページには書きません。"),
            ("開発にはどれですか？", "IDE が要るなら Android Studio。IDE を開いたままにせず APK を試すなら SiliconPlay。"),
            ("LDPlayer は Mac で動きますか？", "LDPlayer は Windows 向けと書いています。MEmu の要件は Windows です。NoxPlayer は Apple M1 チップに非対応と書いています。")]),
    })

    one("ko", "단축키, Cmd+I가 먼저", [
        "Cmd+I는 인스턴스가 실행 중일 때 APK 하나를 설치합니다. 메뉴에는 Command-I로 나옵니다. 끌어다 놓기도 같은 설치입니다.",
        "F12 또는 Command-K는 입력과 게임 키를 바꿉니다.",
        "F10은 대화상자가 손가락을 원할 때의 직접 터치입니다.",
        "Command-Shift-G는 화면 위 버튼을 보이거나 숨깁니다.",
        "Shift-Escape는 눌린 채로 남은 가상 손가락을 뗍니다.",
        "Escape는 전체 화면을 끝냅니다. 밖에서는 화면이 포커스인 동안 Android 뒤로입니다.",
    ], "이 사이트에서:", ("설치", "단축키", "비교", "다운로드"), "질문", {
        "mumu-player-alternative-mac": ("MuMu에서 넘어오지 않는 것", [
            "MuMu 인스턴스는 MuMu에 남습니다. SiliconPlay는 게임, 키 배치, 로그인 상태를 가져오지 않습니다. SiliconPlay 태블릿의 Play 스토어는 Play 이미지의 스토어이지, 다른 프로그램에서 복사한 계정이 아닙니다.",
            "DMG에는 에뮬레이터가 없습니다. 첫 실행에서 Android SDK 라이선스에 동의합니다. 그다음 command-line tools, Apple silicon 에뮬레이터, platform-tools(adb가 여기 있습니다), Play arm64 이미지를 받습니다. 태블릿은 가로, 1920×1080, 320 dpi, 자동 회전 없음, 이름은 Android 16 Tablet입니다. emulator, adb, sdkmanager가 있는 SDK가 있으면 그 폴더를 가리키면 됩니다.",
            "게임 프리셋이 필요하면 MuMu가 더 맞을 수 있습니다. SiliconPlay는 다른 인스턴스를 만들 수 있지만, 그건 프리셋 서가가 아닙니다. 그리는 길도 다릅니다. MuMu는 게임의 OpenGL ES를 Metal로 바꿉니다. SiliconPlay는 Vulkan을 Metal로 그리고, 잎이 맞게 나오도록 셰이더를 safe math로 컴파일합니다. 이 두 문장을 견준 측정은 내지 않았습니다.",
        ], "MuMu 옆에 두고 보는 법",
           "같은 장면, 같은 Mac, 게임 안의 같은 그래픽입니다. 끊기면 먼저 게임 그래픽을 낮추세요. 공개한 측정은 M3 Max MacBook Pro 하나뿐입니다. 무거운 3D에서 최대 60 fps, 렌더는 최대 2560×1440, 키에서 게임까지 7–43 ms. 이것은 MuMu와의 비교가 아니고, M1, M2, M4, M5, M6에서는 같은 숫자를 재지 않았습니다. root는 꺼져 있고 선택입니다. Play 이미지는 adb root를 거부합니다. root는 Play 스토어가 없는 Google APIs 이미지의 두 번째 태블릿입니다. 속도 스위치가 아닙니다.",
           [("MuMu 계정을 가져오나요?", "아닙니다. Play 이미지에서 다시 로그인합니다. 비밀번호는 Android 안에 남고 Mac 앱은 보지 못합니다."),
            ("Intel Mac에서 되나요?", "되지 않습니다. Intel Macs와는 호환되지 않습니다. 지원은 Apple silicon M1부터 M6, Pro, Max, Ultra 포함입니다. macOS Tahoe와 macOS 27 Golden Gate에서 확인했습니다."),
            ("SiliconPlay는 무료인가요?", "예. 무료입니다. 프로젝트 지원은 선택입니다.")]),
        "bluestacks-alternative-mac": ("BlueStacks Air에 대해 말할 수 있는 것", [
            "BlueStacks Air는 2026년 9월 자체 요구사항 기준으로 Apple silicon에서 Android 13을 돌리고 게임에 맞춰져 있습니다. 오랜 프리셋, 여러 인스턴스, 큰 지원 조직이 있습니다. SiliconPlay는 Mac의 ARM 코어에서 Apple Hypervisor로 Android 16을 돌리고 Vulkan을 Metal로 그립니다.",
            "만드는 사람은 한 명입니다. 프리셋 선반과 지원 창구가 필요하면 BlueStacks가 더 맞을 수 있습니다. 없는 것을 있는 척하기보다 그렇게 씁니다. NoxPlayer, LDPlayer, MEmu는 이 Mac들에서 돌지 않습니다. UTM에는 3D 가속이 없어 이 게임들에는 맞지 않습니다. Android Studio 에뮬레이터는 IDE가 필요할 때의 공식 도구이고, IDE 때문에 무겁습니다.",
            "SiliconPlay의 첫 실행은 BlueStacks 이미지를 읽지 않습니다. Android SDK 라이선스에 동의한 뒤 command-line tools, Apple silicon 에뮬레이터, platform-tools, Play arm64 이미지를 받습니다. 태블릿은 1920×1080, 320 dpi, 가로, 자동 회전 없음입니다.",
        ], "같은 장면으로 보기",
           "같은 구간을 같은 Mac에서 하고, 한쪽이 끊기면 먼저 게임 그래픽을 낮추세요. SiliconPlay의 root는 꺼진 채로 시작하고, Play 이미지가 adb root를 거부해서 Google APIs 이미지의 두 번째 태블릿입니다. 그 태블릿에는 Play 스토어가 없습니다. 앱은 무료입니다. macOS Tahoe와 macOS 27 Golden Gate, M1부터 M6 Apple silicon에서 확인했습니다. Intel Macs와는 호환되지 않습니다.",
           [("Android 16인가요, 13인가요?", "SiliconPlay는 Android 16 태블릿을 켭니다. BlueStacks Air는 자체 요구사항에 Android 13이라고 적습니다. 같은 것의 두 이름이 아닙니다."),
            ("하려면 root가 필요한가요?", "필요 없습니다. root는 꺼져 있습니다. 하려면 Play 태블릿에 두세요. root는 스토어 없는 두 번째 태블릿입니다."),
            ("어떤 Mac인가요?", "Apple silicon M1부터 M6, Pro, Max, Ultra 포함. Intel Macs와는 호환되지 않습니다. macOS Tahoe와 macOS 27 Golden Gate에서 확인했습니다.")]),
        "android-emulator-mac-m1-m2-m3-m4": ("M1부터 M6까지 앱 하나", [
            "M1, M2, M3, M4, M5, M6는 따로 받는 파일이 아닙니다. SiliconPlay는 Mac 앱 하나입니다. Pro, Max, Ultra는 코어가 더 많은 같은 칩이지 다른 제품이 아닙니다. 첫 실행은 어느 칩에서나 같습니다. Android SDK 라이선스 다음 command-line tools, Apple silicon 에뮬레이터, platform-tools, Play arm64 이미지를 고른 폴더에 넣습니다.",
            "태블릿 이름은 Android 16 Tablet, 가로, 1920×1080, 320 dpi, 자동 회전 끔입니다. 2560×1440은 이 태블릿의 크기가 아닙니다. 공개한 유일한 측정, M3 Max MacBook Pro의 숫자입니다. 무거운 3D에서 최대 60 fps, 렌더는 최대 2560×1440, 키에서 게임까지 7–43 ms. M1, M2, M4, M5, M6에서는 같은 측정을 내지 않았습니다.",
            "JDK가 없으면 macOS가 /usr/bin/java 스텁을 보여 줍니다. 메시지는 brew install openjdk@17을 가리킵니다. 칩이 이 문장을 바꾸지 않습니다. ARM64 라이브러리가 없는 패키지는 목록의 어떤 칩에서도 돌지 않습니다. 이 버전은 분할 APK와 XAPK를 설치하지 않습니다.",
        ], "칩 이름에서 읽지 말 것",
           "게임이 끊기면 먼저 그 게임의 그래픽을 낮추세요. M1이나 M4라는 이름만으로 Mac이 맞지 않다고 정하지 마세요. macOS Tahoe와 macOS 27 Golden Gate에서 확인했습니다. 다른 버전이면 해보고 칩과 버전을 알려 주세요. Intel Macs와는 호환되지 않습니다. Vulkan은 Metal이 그리고, 잎을 위해 셰이더는 safe math입니다. 칩마다 다른 모드가 아닙니다.",
           [("M1 버전과 M4 버전이 따로 있나요?", "따로 없습니다. 앱 하나, M1부터 M6, Pro, Max, Ultra 포함입니다."),
            ("60 fps가 제 M1에도 해당하나요?", "해당하지 않습니다. 숫자는 M3 Max MacBook Pro 측정입니다. 결과는 게임, Mac, 설정에 따라 달라집니다."),
            ("어떤 macOS인가요?", "macOS Tahoe와 macOS 27 Golden Gate에서 확인했습니다. Intel Macs와는 호환되지 않습니다.")]),
        "free-android-emulator-mac-m1-m5-comparison": ("무엇으로 고르나", [
            "이 페이지는 순위표도 요금표도 아닙니다. SiliconPlay는 제가 만들므로 기울기는 먼저 밝힙니다. 다른 프로그램이 무엇을 요구하는지는 만든 쪽 사이트에 있습니다. 여기에는 각 도구가 무엇을 위한 것인지, 제가 확인하지 않은 것이 무엇인지가 있습니다.",
            "SiliconPlay는 무료이고, 게임과 APK 한 장을 위해 IDE를 열어 두지 않습니다. BlueStacks Air는 게임, 여러 인스턴스, 준비된 조작을 위한 것입니다. MuMu Player Pro는 키보드, 마우스, 게임패드로 하는 게임을 위한 것입니다. Android Studio는 개발 환경이고, 에뮬레이터는 IDE와 함께 오며 게임 키 배치는 없습니다. UTM은 3D 가속이 없는 일반 가상 머신입니다. LDPlayer는 Windows용이라고 적습니다. MEmu 요구사항은 Windows입니다. NoxPlayer 지원은 Apple M1 칩을 지원하지 않는다고 적습니다. Waydroid는 Linux입니다.",
            "SiliconPlay 아래는 공식 Android 에뮬레이터이고, ARM 코어에서 네이티브, Android 16, Vulkan은 Metal, 셰이더는 safe math입니다. 첫 실행은 Play arm64 이미지를 받고, 1920×1080, 320 dpi, 가로입니다. root는 스토어 없는 두 번째 태블릿입니다. 공개한 성능 측정은 M3 Max MacBook Pro 것뿐이고, 다른 누구와도 견주지 않습니다.",
        ], "공정하게 해 보는 법",
           "같은 장면, 같은 Mac, 같은 그래픽입니다. 그다음 직접 정합니다. 당신 게임에서 어느 쪽이 앞인지는 제가 재지 않습니다. 단계가 Mac에서 다르면 칩, macOS 버전, 게임 이름이 필요합니다. Intel Macs와는 호환되지 않습니다. 지원은 Apple silicon M1부터 M6. macOS Tahoe와 macOS 27 Golden Gate에서 확인했습니다.",
           [("SiliconPlay는 무료인가요?", "예. 지원은 선택입니다. 다른 쪽이 요구하는 것은 이 페이지에 적지 않습니다."),
            ("개발에는 어느 쪽인가요?", "IDE가 필요하면 Android Studio. IDE를 열어 두지 않고 APK를 보려면 SiliconPlay."),
            ("LDPlayer가 Mac에서 되나요?", "LDPlayer는 Windows용이라고 적습니다. MEmu 요구사항은 Windows입니다. NoxPlayer는 Apple M1 칩을 지원하지 않는다고 적습니다.")]),
    })

    # The remaining locales share the same facts, written in that language.
    from guide_notes_asia2 import add_rest
    add_rest(one)
