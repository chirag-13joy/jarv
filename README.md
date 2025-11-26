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

3.  **Run Voice Assistant**:
    ```bash
    python voice_assistant.py
    ```

4.  **Run Web Interface** (Optional):
    ```bash
    python web_server.py
    ```
    Then open your browser to `http://localhost:5000`

## Web Interface

The web interface provides:
- **Speak Button**: Trigger voice listening
- **Mute Button**: Toggle voice output on/off
- **Example Commands**: Click any example to test it!
- **Modern UI**: Beautiful glassmorphism design

### Features
- ✅ Real-time status monitoring
- ✅ Interactive example commands (click to test)
- ✅ Backend API integration
- ✅ Responsive design

## Deployment & Sharing

### Run Locally
```bash
python web_server.py
```
Then open: `http://localhost:5000`

### Share with Friends (Same Network)
1. Find your IP address:
   ```powershell
   ipconfig
   ```
   Look for "IPv4 Address" (e.g., 192.168.1.100)

2. Run the server:
   ```bash
   python web_server.py
   ```

3. Share this URL with friends on the same WiFi:
   ```
   http://YOUR_IP:5000
   ```
   Example: `http://192.168.1.100:5000`

### Deploy Online (Free Options)
- **Render**: https://render.com (Free tier available)
- **Railway**: https://railway.app (Free tier available)
- **PythonAnywhere**: https://www.pythonanywhere.com (Free tier)

## Current Implementation Status

- [x] Core framework and module structure
- [x] Natural Language Processing module
- [x] Personality engine
- [x] Voice recognition module
- [x] Speech synthesis module
- [x] Hindi language support
- [x] System integration
- [x] Comprehensive testing