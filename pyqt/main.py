
import sys
from PyQt5.QtWidgets import (
    QApplication, 
    QMainWindow, 
    QDesktopWidget, 
    QVBoxLayout, 
    QWidget,
    QSizePolicy
)
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl, Qt
from run_server import (
    start_django_server,
    start_reactjs_server,
    start_redis_server,
    start_celery_processes,
    stop_django_server,
    stop_reactjs_server,
    stop_redis_server,
    stop_celery_processes,

)
import requests
import os
import ctypes
from pathlib import Path
from decouple import Config, RepositoryEnv
from pathlib import Path


env_path = Path(__file__).resolve().parent.parent / ".env"
config = Config(repository=RepositoryEnv(env_path))


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        start_reactjs_server()
        start_django_server()
        start_redis_server()
        start_celery_processes()

        self.setWindowTitle("Alena")
        self.resize(1000, 600)
        self.center()
                
        central_widget = QWidget()
        layout = QVBoxLayout()
        view = QWebEngineView()
        view.setUrl(QUrl("http://localhost:5173/"))
        view.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        
        layout.addWidget(view)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
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
        stop_celery_processes()
        stop_redis_server()
        event.accept()
        

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())



if __name__ == "__main__":
    main()