import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
from PySide6.QtGui import QKeySequence, QShortcut
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile, Qt

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # QUiLoader を使用して UI ファイルをロード
        loader = QUiLoader()
        ui_file = QFile("test_ui.ui")  # UIファイルの名前が正しいことを確認
        if not ui_file.open(QFile.ReadOnly):
            print(f"Cannot open UI file: {ui_file.errorString()}")
            sys.exit(-1)
        self.ui = loader.load(ui_file, self)
        ui_file.close()

        if not self.ui:
            print("Failed to load UI file.")
            sys.exit(-1)

        # UIを中央ウィジェットとして設定
        self.setCentralWidget(self.ui)

        # 初期サイズをUIのサイズに合わせる
        self.resize(self.ui.size())
        self.setMinimumSize(self.ui.minimumSize())
        self.setMaximumSize(self.ui.maximumSize())

        # UI内のボタンにアクセス
        self.setup_buttons()

        # ショートカット設定
        self.shortcut = QShortcut(QKeySequence("Ctrl+P"), self)
        self.shortcut.activated.connect(self.print_window_geometry)

        # デバッグログ
        print("Debug: Shortcut Ctrl+P has been set up.")

    def setup_buttons(self):
        """UI内のボタン設定"""
        # UI内の pushButton を取得してクリックイベントを接続
        self.button = self.ui.findChild(QPushButton, "pushButton")
        if self.button:
            self.button.clicked.connect(self.on_button_clicked)
            print("Debug: Button found and connected.")
        else:
            print("Debug: Button not found in the UI file.")

    def on_button_clicked(self):
        """ボタンクリック時の処理"""
        print("Debug: Button clicked!")

    def keyPressEvent(self, event):
        """キー入力を監視してデバッグログを出力"""
        if event.modifiers() == Qt.ControlModifier and event.key() == Qt.Key_P:
            self.print_window_geometry()  # Ctrl+Pが押された場合の処理
            print("Debug: Ctrl+P detected.")
        else:
            print(f"Debug: Key pressed - Text: {event.text()}, KeyCode: {event.key()}")
        super().keyPressEvent(event)

    def get_window_geometry(self):
        """ウィンドウの現在の位置とサイズを取得する関数"""
        position = self.geometry().topLeft()  # ウィンドウの位置 (QPoint)
        size = self.geometry().size()         # ウィンドウのサイズ (QSize)
        print("Debug: get_window_geometry called.")  # デバッグログ
        return position, size

    def print_window_geometry(self):
        """現在のウィンドウ位置とサイズを出力"""
        print("Debug: print_window_geometry activated.")  # デバッグログ
        position, size = self.get_window_geometry()
        print(f"Window Position: x={position.x()}, y={position.y()}")
        print(f"Window Size: width={size.width()}, height={size.height()}")

if __name__ == "__main__":
    print("Debug: QApplication instance is about to be created.")  # デバッグログ
    app = QApplication(sys.argv)
    print("Debug: QApplication instance created.")  # デバッグログ

    window = MyWindow()
    print("Debug: MyWindow instance created.")  # デバッグログ
    window.show()  # UI を表示
    print("Debug: Window is now visible.")  # デバッグログ

    sys.exit(app.exec())
