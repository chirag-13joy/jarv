# Jarvis Voice Assistant

A fully functional voice assistant inspired by Jarvis, powered by Google Gemini and Python.

## Features
- **Voice Interaction**: Speaks and listens using `SpeechRecognition` and `pyttsx3`.
- **AI Brain**: Uses **Google Gemini** for intelligent conversation, personality, and general knowledge.
- **Commands**:
    - Play music on YouTube (`pywhatkit`)
    - Tell time
    - Search Wikipedia
    - Tell jokes
- **Language Support**: English and Hindi (via Gemini's multilingual capabilities).

## Setup

1.  **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```
    *Note: If PyAudio fails to install, try:*
    ```bash
    pip install pipwin
    pipwin install pyaudio
    ```

2.  **Optional: Set Gemini API Key** (for smart chat):
    - Get a key from [Google AI Studio](https://aistudio.google.com/).
    - Set it in your terminal:
      ```powershell
      $env:GEMINI_API_KEY="your_api_key_here"
      ```

3.  **Run**:
    ```bash
    python voice_assistant.py
    ```

## Current Implementation Status

- [x] Core framework and module structure
- [x] Natural Language Processing module
- [x] Personality engine
- [x] Voice recognition module
- [x] Speech synthesis module
- [x] Hindi language support
- [x] System integration
- [x] Comprehensive testing