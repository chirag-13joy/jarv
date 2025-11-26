import speech_recognition as sr
import pyttsx3
import pywhatkit
import wikipedia
import pyjokes
import datetime
import os
import google.generativeai as genai
from gtts import gTTS
import playsound

"""
Jarvis Voice Assistant
----------------------
Current Implementation Status:
- [x] Core framework and module structure
- [x] Natural Language Processing module (via Google Gemini)
- [x] Personality engine (via Google Gemini system instructions)
- [x] Voice recognition module (via SpeechRecognition)
- [x] Speech synthesis module (via pyttsx3)
- [x] Hindi language support (via Gemini multilingual capabilities)
- [x] System integration
- [x] Comprehensive testing
"""

# Initialize the recognizer and text-to-speech engine
listener = sr.Recognizer()
engine = pyttsx3.init()

# Configure Voice (Optional: Select a specific voice if available)
voices = engine.getProperty('voices')
if len(voices) > 1:
    engine.setProperty('voice', voices[1].id)

# Configure Gemini
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")
if GEMINI_API_KEY:
    genai.configure(api_key=GEMINI_API_KEY)
    model = genai.GenerativeModel('gemini-pro')
else:
    model = None

import sounddevice as sd
import soundfile as sf
import numpy as np
import tempfile

# Global Language Setting
CURRENT_LANGUAGE = 'en-IN'
VOICE_ENABLED = True

def is_hindi(text):
    """Checks if the text contains Hindi characters."""
    return any('\u0900' <= char <= '\u097f' for char in text)

def talk(text):
    """Speaks the given text. Uses gTTS for Hindi, pyttsx3 for English."""
    print(f"Jarvis: {text}")
    
    if not VOICE_ENABLED:
        return

    if is_hindi(text):
        try:
            tts = gTTS(text=text, lang='hi')
            filename = "temp_voice.mp3"
            if os.path.exists(filename):
                os.remove(filename)
            tts.save(filename)
            playsound.playsound(filename)
            os.remove(filename)
        except Exception as e:
            print(f"Hindi TTS Error: {e}")
            engine.say(text)
            engine.runAndWait()
    else:
        engine.say(text)
        engine.runAndWait()

def record_audio(duration=5, samplerate=44100):
    """Records audio using sounddevice."""
    print(f"Listening ({CURRENT_LANGUAGE})...")
    
    # Check for custom device index
    device_index = os.environ.get('AUDIO_DEVICE_INDEX')
    if device_index:
        device_index = int(device_index)
    else:
        device_index = None # Use default

    try:
        myrecording = sd.rec(int(duration * samplerate), samplerate=samplerate, channels=1, dtype='int16', device=device_index)
        sd.wait()  # Wait until recording is finished
        return myrecording, samplerate
    except Exception as e:
        print(f"Microphone Error: {e}")
        return None, None

def take_command():
    """Listens for a command and returns it as text."""
    global CURRENT_LANGUAGE
    command = ""
    
    # Record audio to a temporary file
    audio_data, samplerate = record_audio(duration=5) # Listen for 5 seconds
    if audio_data is None:
        return ""

    with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as temp_wav:
        sf.write(temp_wav.name, audio_data, samplerate)
        temp_wav_path = temp_wav.name

    try:
        with sr.AudioFile(temp_wav_path) as source:
            # No need to adjust for ambient noise with AudioFile usually, but can help
            audio = listener.record(source)
            
            try:
                command = listener.recognize_google(audio, language=CURRENT_LANGUAGE)
                print(f"You said: {command}")
            except sr.UnknownValueError:
                # Fallback language
                fallback_lang = 'hi-IN' if CURRENT_LANGUAGE == 'en-IN' else 'en-IN'
                print(f"Trying fallback language ({fallback_lang})...")
                try:
                    command = listener.recognize_google(audio, language=fallback_lang)
                    print(f"You said ({fallback_lang}): {command}")
                except sr.UnknownValueError:
                    pass
            
            command = command.lower()
            if 'jarvis' in command:
                command = command.replace('jarvis', '').strip()

    except Exception as e:
        print(f"Recognition Error: {e}")
    finally:
        if os.path.exists(temp_wav_path):
            os.remove(temp_wav_path)
    
    return command

def ask_gemini(query):
    """Queries Google Gemini for a response."""
    if not model:
        return "I'm sorry, I don't have my AI brain connected."
    try:
        # Instruct Gemini to be concise and use Hindi if asked
        prompt = f"You are Jarvis, a helpful AI assistant. Answer the following query concisely. If the user speaks Hindi or asks in Hindi, reply in Hindi. Query: {query}"
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return "I encountered an error."

def run_jarvis():
    """Main execution loop."""
    global CURRENT_LANGUAGE, VOICE_ENABLED
    command = take_command()
    if not command:
        return

    if 'play' in command:
        song = command.replace('play', '').strip()
        talk(f"Playing {song}")
        pywhatkit.playonyt(song)
    
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk(f"The current time is {time}")
    
    elif 'who is' in command or 'what is' in command:
        try:
            search_query = command.replace('who is', '').replace('what is', '').strip()
            info = wikipedia.summary(search_query, sentences=1)
            talk(info)
        except Exception:
            if model:
                response = ask_gemini(command)
                talk(response)
            else:
                talk("I couldn't find that.")

    elif 'joke' in command:
        talk(pyjokes.get_joke())
        
    elif 'speak hindi' in command or 'switch to hindi' in command or 'hindi mode' in command:
        CURRENT_LANGUAGE = 'hi-IN'
        talk("नमस्ते सर, अब मैं हिंदी सुनूंगा।") # Namaste sir, now I will listen in Hindi.
        
    elif 'speak english' in command or 'switch to english' in command or 'english mode' in command:
        CURRENT_LANGUAGE = 'en-IN'
        talk("Okay sir, switching to English mode.")

    elif 'turn off voice' in command or 'voice off' in command or 'silent mode' in command:
        VOICE_ENABLED = False
        print("Jarvis: Voice disabled.") # Don't speak this
        
    elif 'turn on voice' in command or 'voice on' in command:
        VOICE_ENABLED = True
        talk("Voice enabled, sir.")
    
    elif 'stop' in command or 'exit' in command:
        talk("Goodbye, sir.")
        exit()
        
    else:
        if model:
            response = ask_gemini(command)
            talk(response)
        else:
            talk("I didn't quite catch that, sir.")

import time

if __name__ == "__main__":
    talk("Jarvis is online.")
    while True:
        try:
            run_jarvis()
        except Exception as e:
            print(f"Critical Error: {e}")
            time.sleep(1)
        except KeyboardInterrupt:
            print("Exiting...")
            break
