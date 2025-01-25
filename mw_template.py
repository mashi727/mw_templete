from PySide6.QtCore import QEvent
from PySide6.QtWidgets import QApplication, QMainWindow

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        loader = QUiLoader()
        ui_file = QFile("test_ui.ui")
        if not ui_file.open(QFile.ReadOnly):
            print(f"Cannot open UI file: {ui_file.errorString()}")
            sys.exit(-1)
        self.ui = loader.load(ui_file, self)
        ui_file.close()

        if not self.ui:
            print("Failed to load UI file.")
            sys.exit(-1)

        # ショートカット設定
        self.shortcut = QShortcut(QKeySequence("Ctrl+p"), self)
        self.shortcut.activated.connect(self.print_window_geometry)

        # デバッグログ
        print("Debug: Shortcut Ctrl+P has been set up.")

        # QApplication レベルでイベントフィルタをインストール
        app.installEventFilter(self)

    def eventFilter(self, source, event):
        """全体のキーイベントをキャプチャ"""
        if event.type() == QEvent.KeyPress:
            print(f"Debug: Key pressed globally: {event.text()}")
        return super().eventFilter(source, event)

    def print_window_geometry(self):
        """現在のウィンドウ位置とサイズを出力"""
        print("Debug: print_window_geometry activated.")  # デバッグログ
        position = self.geometry().topLeft()
        size = self.geometry().size()
        print(f"Window Position: x={position.x()}, y={position.y()}")
        print(f"Window Size: width={size.width()}, height={size.height()}")
