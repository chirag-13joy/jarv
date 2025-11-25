# Jarvis AI Assistant

An AI assistant inspired by Jarvis from Iron Man, designed to be a realistic, conversational AI system.

## Features

- Natural Language Processing for intent classification and entity extraction
- Personality engine for contextual responses
- Voice recognition and synthesis capabilities
- Hindi and English language support
- Modular architecture for extensibility
- Privacy-focused design with local processing

## Project Structure

```
jarvis_ai/
├── core/                 # Core system initialization and coordination
├── modules/              # Individual system modules
│   ├── nlp/              # Natural Language Processing
│   ├── voice_recognition/ # Voice input processing
│   ├── speech_synthesis/  # Text-to-speech output
│   ├── personality/       # Personality and context engine
│   ├── command_executor/  # Command execution system
│   ├── memory/           # Memory and persistence
│   └── error_handler/    # Error handling and fallbacks
├── utils/                # Utility functions
├── tests/                # Test suite
├── main.py              # Main entry point
└── requirements.txt     # Python dependencies
```

## Getting Started

1. Clone the repository
2. Create a virtual environment:
   ```bash
   python3 -m venv jarvis_env
   source jarvis_env/bin/activate  # On Windows: jarvis_env\Scripts\activate
   ```
3. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Install system dependencies for voice features (Ubuntu/Debian):
   ```bash
   sudo apt install portaudio19-dev python3-pyaudio espeak
   ```
   For other systems:
   - Windows: PyAudio and eSpeak will be installed via pip
   - macOS: `brew install portaudio espeak`

5. Run the system:
   ```bash
   python main.py
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

## Testing

Run all tests:
```bash
python tests/test_nlp.py
python tests/test_personality.py
python tests/test_voice.py
python tests/test_conversations.py
python tests/test_integration.py
python tests/test_hindi.py
```

Or run all tests at once:
```bash
python -m pytest tests/
```

## Language Support

The system currently supports both English and Hindi languages:
- Automatic language detection
- Intent classification in both languages
- Contextual responses in both languages
- Sentiment analysis for both languages

## Demos

Run the English demo:
```bash
python demo.py
```

Run the Hindi demo:
```bash
python demo_hindi.py
```

## Voice Features

To use the voice recognition and synthesis features, you'll need to install additional system dependencies:

### Ubuntu/Debian:
```bash
sudo apt install portaudio19-dev python3-pyaudio espeak
```

### Windows:
Voice features should work out of the box with the installed Python packages.

### macOS:
```bash
brew install portaudio espeak
```

## Contributing

This project is still in development. Contributions are welcome!

## License

This project is licensed under the MIT License.