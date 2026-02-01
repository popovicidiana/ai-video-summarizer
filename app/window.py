import os
from PyQt6.QtWidgets import (
    QWidget, QLineEdit, QPushButton, QLabel,
    QStatusBar, QTextEdit, QVBoxLayout, QHBoxLayout
)
from PyQt6.QtGui import QIcon

from app.utils import extract_video_id
from app.youtube import fetch_transcript
from app.summarizer import summarize_transcript


class AppWindow(QWidget):
    def __init__(self, client):
        super().__init__()
        self.client = client

        self.setWindowTitle("Diana's YouTube Transcript Downloader")
        self.setWindowIcon(QIcon(os.path.join("assets", "transcription.png")))
        self.resize(800, 600)
        self.setStyleSheet("font-size: 14px;")

        self.layout = {}
        self.layout["main"] = QVBoxLayout()
        self.setLayout(self.layout["main"])

        self.init_ui()

    def init_container(self):
        self.button = {}
        self.line_edit = {}
        self.label = {}

    def init_ui(self):
        self.init_container()
        self.add_video_input_section()
        self._add_output_section()
        self._add_button_section()

        self.status_bar = QStatusBar()
        self.layout["main"].addWidget(self.status_bar)

    def add_video_input_section(self):
        self.layout["video_input"] = QHBoxLayout()
        self.layout["main"].addLayout(self.layout["video_input"])

        self.label["video_id"] = QLabel("Video ID:")
        self.layout["video_input"].addWidget(self.label["video_id"])

        self.line_edit["video_id"] = QLineEdit()
        self.line_edit["video_id"].setFixedWidth(500)
        self.line_edit["video_id"].setPlaceholderText("Enter video ID or URL")
        self.layout["video_input"].addWidget(self.line_edit["video_id"])

        self.layout["video_input"].addStretch()

    def _add_output_section(self):
        self.label["output"] = QLabel("Transcript:")
        self.layout["main"].addWidget(self.label["output"])

        self.text_edit = QTextEdit()
        self.layout["main"].addWidget(self.text_edit)

    def _add_button_section(self):
        self.layout["transcript_download"] = QHBoxLayout()
        self.layout["main"].addLayout(self.layout["transcript_download"])

        self.button["download_transcript"] = QPushButton("&Download Transcript")
        self.button["download_transcript"].clicked.connect(self.download_transcript)
        self.layout["transcript_download"].addWidget(
            self.button["download_transcript"]
        )

        self.button["summarize_transcript"] = QPushButton("&Summarize Transcript")
        self.button["summarize_transcript"].clicked.connect(
            self.summarize_transcript
        )
        self.layout["transcript_download"].addWidget(
            self.button["summarize_transcript"]
        )

        self.layout["transcript_download"].addStretch()

    def download_transcript(self):
        video_id = self.line_edit["video_id"].text()

        if not video_id:
            self.status_bar.showMessage("Please enter a video ID or URL")
            return

        self.status_bar.clearMessage()

        try:
            clean_id = extract_video_id(video_id)
            transcript_text = fetch_transcript(clean_id)
            self.text_edit.setPlainText(transcript_text)

        except Exception as e:
            self.text_edit.setPlainText(f"Error: {e}")

    def summarize_transcript(self):
        transcript_text = self.text_edit.toPlainText()

        if not transcript_text:
            self.status_bar.showMessage("Transcript is empty")
            return

        self.status_bar.clearMessage()

        html = summarize_transcript(self.client, transcript_text)
        self.text_edit.setHtml(html)