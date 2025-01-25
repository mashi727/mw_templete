import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import Qt, QPoint, QSize
from test_ui import Ui_MainWindow  # uic で生成された Python ファイルをインポート

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # uic で生成された UI クラスをロード
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # デバッグログ
        print("Debug: MyWindow instance created.")

    def keyPressEvent(self, event):
        """キーボード入力を処理する"""
        if event.modifiers() == Qt.MetaModifier and event.key() == Qt.Key_P:
            # Command+P が押された場合
            self.print_window_geometry()
        else:
            # 他のキーはデフォルトの動作に戻す
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
    app = QApplication(sys.argv)
    window = MyWindow()
    print("Debug: MyWindow instance created.")  # デバッグログ
    window.show()  # UI を表示
    print("Debug: Window is now visible.")  # デバッグログ
    sys.exit(app.exec())
