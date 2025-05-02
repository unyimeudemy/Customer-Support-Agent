
import sys
from PyQt5.QtWidgets import (
    QApplication, 
    QMainWindow, 
    QDesktopWidget, 
    QVBoxLayout, 
    QWidget
)
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl, Qt
from run_server import (
    start_django_server,
    start_reactjs_server,
    stop_django_server,
    stop_reactjs_server
)
import requests

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        start_reactjs_server()
        start_django_server()

        self.setWindowTitle("Alena")
        self.resize(1000, 600)
        self.center()
                
        central_widget = QWidget()
        layout = QVBoxLayout()
        view = QWebEngineView()
        view.setUrl(QUrl("http://localhost:5173/"))
        
        layout.addWidget(view)
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def center(self):
        frameGm = self.frameGeometry()
        screen = QDesktopWidget().availableGeometry().center()
        frameGm.moveCenter(screen)
        self.move(frameGm.topLeft())
    
    def closeEvent(self, event):
        stop_reactjs_server()
        stop_django_server()
        event.accept()
        

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())



if __name__ == "__main__":
    main()