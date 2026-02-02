import sys
import os
import groq
from PyQt6.QtWidgets import QApplication
from app.window import AppWindow

def main():
    API_KEY = os.getenv("GROQ_API_KEY")
    if not API_KEY:
        raise ValueError("GROQ_API_KEY not found")

    client = groq.Client(api_key=API_KEY)

    app = QApplication(sys.argv)
    app.setStyle("Fusion")

    base_dir = os.path.dirname(os.path.dirname(__file__))
    css_path = os.path.join(base_dir, "assets", "dark_theme.css")
    with open(css_path, "r", encoding="utf-8") as f:
        app.setStyleSheet(f.read())

    window = AppWindow(client)
    window.show()

    sys.exit(app.exec())