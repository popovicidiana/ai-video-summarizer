# 🎥 AI Video Summarizer

A simple desktop application built with **Python** and **PyQt6** that allows you to:

- Download **YouTube video transcripts**
- Summarize those transcripts
- View everything in a clean GUI
- Save in PDF format

This personal project is currently in **early development** and will be extended with more features, tests, and UI improvements.

---

## ✨ Features

- Paste a **YouTube video URL or ID**
- Fetch the video transcript using `youtube-transcript-api`
- Summarize the transcript into **bullet points**
- Simple and clean **PyQt6 desktop interface**
- Modular project structure (ready for testing and scaling)

---
##  🚀 Getting Started
```
git clone https://github.com/popovicidiana/ai-video-summarizer.git
cd ai-video-summarizer
```
# Windows
```
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```
# macOS/Linux
```
source venv/bin/activate
pip install -r requirements.txt
```
This project uses Groq for transcript summarization. Set your Groq API key:
```
setx GROQ_API_KEY "your_api_key_here"
```
# Run the app:
```
python run.py
```
