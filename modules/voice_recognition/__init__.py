"""
Voice recognition module for Jarvis AI.
Handles speech-to-text conversion using various engines.
"""

import os
from typing import Optional, Dict, Any
from utils.logger import logger


class VoiceRecognizer:
    """Handles voice recognition for the Jarvis AI system."""
    
    def __init__(self, engine: str = "speech_recognition"):
        """Initialize the voice recognizer."""
        self.engine = engine
        self.recognizer = None
        self.microphone = None
        self.initialized = False
        self._initialize_engine()
        
    def _initialize_engine(self):
        """Initialize the selected voice recognition engine."""
        try:
            if self.engine == "speech_recognition":
                import speech_recognition as sr
                self.recognizer = sr.Recognizer()
                self.microphone = sr.Microphone()
                # Adjust for ambient noise
                with self.microphone as source:
                    self.recognizer.adjust_for_ambient_noise(source)
                self.initialized = True
                logger.info("SpeechRecognition engine initialized successfully")
            elif self.engine == "vosk":
                # Vosk implementation would go here
                logger.info("Vosk engine selected (not implemented yet)")
            else:
                logger.warning(f"Unknown engine '{self.engine}', falling back to SpeechRecognition")
                import speech_recognition as sr
                self.recognizer = sr.Recognizer()
                self.microphone = sr.Microphone()
                self.initialized = True
        except ImportError:
            logger.error("Required voice recognition libraries not installed")
            logger.info("Please install speechrecognition: pip install SpeechRecognition")
            self.recognizer = None
            self.microphone = None
            self.initialized = False
        except Exception as e:
            logger.error(f"Error initializing voice recognition engine: {str(e)}")
            self.recognizer = None
            self.microphone = None
            self.initialized = False
            
    def listen(self, timeout: Optional[float] = None) -> Optional[str]:
        """Listen for audio input and convert to text."""
        if not self.recognizer or not self.microphone:
            logger.warning("Voice recognition engine not available. Voice input not supported.")
            return None
            
        try:
            logger.info("Listening for audio input...")
            with self.microphone as source:
                # Listen for audio with timeout
                audio = self.recognizer.listen(source, timeout=timeout)
                
            logger.info("Processing audio...")
            # Convert audio to text
            text = self.recognizer.recognize_google(audio)
            logger.info(f"Recognized text: {text}")
            return text
            
        except Exception as e:
            logger.error(f"Error during voice recognition: {str(e)}")
            # Try to reinitialize the engine
            self._initialize_engine()
            return None
            
    def listen_for_wake_word(self, wake_word: str = "jarvis") -> bool:
        """Listen specifically for the wake word."""
        if not self.initialized:
            logger.warning("Voice recognition not available. Cannot listen for wake word.")
            return False
            
        try:
            text = self.listen(timeout=2)
            if text and wake_word.lower() in text.lower():
                logger.info(f"Wake word '{wake_word}' detected")
                return True
            return False
        except Exception as e:
            logger.error(f"Error listening for wake word: {str(e)}")
            return False


# Global voice recognizer instance
voice_recognizer = VoiceRecognizer()