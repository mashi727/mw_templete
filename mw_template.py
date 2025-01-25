import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QPoint, QSize

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Window Position and Size Example")
        self.resize(800, 600)  # 初期サイズを設定

    def get_window_geometry(self):
        """ウィンドウの現在の位置とサイズを取得する関数"""
        position = self.pos()  # ウィンドウの位置 (QPoint)
        size = self.size()     # ウィンドウのサイズ (QSize)
        print(f"Window Position: x={position.x()}, y={position.y()}")
        print(f"Window Size: width={size.width()}, height={size.height()}")
        return position, size

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()  # ウィンドウを表示

    # ウィンドウの位置とサイズを取得 (例: ウィンドウが表示された直後)
    window.get_window_geometry()

    sys.exit(app.exec())
