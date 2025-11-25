"""
Voice recognition module for Jarvis AI.
Handles speech-to-text conversion using various engines.
"""

import os
import io
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
        self.microphone_available = False
        self._initialize_engine()
        
    def _initialize_engine(self):
        """Initialize the selected voice recognition engine."""
        try:
            if self.engine == "speech_recognition":
                import speech_recognition as sr
                self.recognizer = sr.Recognizer()
                # Try to initialize microphone, but catch errors gracefully
                try:
                    self.microphone = sr.Microphone()
                    # Adjust for ambient noise
                    with self.microphone as source:
                        self.recognizer.adjust_for_ambient_noise(source)
                    self.initialized = True
                    self.microphone_available = True
                    logger.info("SpeechRecognition engine initialized successfully with microphone")
                except Exception as mic_error:
                    logger.warning(f"Microphone initialization failed: {str(mic_error)}")
                    logger.info("Voice recognition will work with file input only")
                    self.microphone = None
                    self.microphone_available = False
                    # Still mark as initialized since the recognizer works without microphone
                    # for file-based recognition
                    self.initialized = True
                    logger.info("SpeechRecognition engine initialized successfully (no microphone)")
            elif self.engine == "vosk":
                # Vosk implementation would go here
                logger.info("Vosk engine selected (not implemented yet)")
            else:
                logger.warning(f"Unknown engine '{self.engine}', falling back to SpeechRecognition")
                import speech_recognition as sr
                self.recognizer = sr.Recognizer()
                try:
                    self.microphone = sr.Microphone()
                    self.initialized = True
                    self.microphone_available = True
                except:
                    self.microphone = None
                    self.microphone_available = False
                    self.initialized = True
        except ImportError:
            logger.error("Required voice recognition libraries not installed")
            logger.info("Please install speechrecognition: pip install SpeechRecognition")
            self.recognizer = None
            self.microphone = None
            self.initialized = False
            self.microphone_available = False
        except Exception as e:
            logger.error(f"Error initializing voice recognition engine: {str(e)}")
            self.recognizer = None
            self.microphone = None
            self.initialized = False
            self.microphone_available = False
            
    def listen(self, timeout: Optional[float] = None) -> Optional[str]:
        """Listen for audio input and convert to text."""
        if not self.recognizer:
            logger.warning("Voice recognition engine not available. Voice input not supported.")
            return None
            
        # If microphone is not available, provide alternative input method
        if not self.microphone:
            logger.info("Microphone not available. Please provide audio input through alternative means.")
            return self._listen_from_file_or_text()
            
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
            
    def _listen_from_file_or_text(self) -> Optional[str]:
        """Alternative input method when microphone is not available."""
        logger.info("Using alternative input method...")
        try:
            # In a real implementation, this could read from a file or other input source
            # For now, we'll just log that this is available
            logger.info("Alternative input methods available: file input, text input")
            return None
        except Exception as e:
            logger.error(f"Error in alternative input method: {str(e)}")
            return None
            
    def listen_for_wake_word(self, wake_word: str = "jarvis") -> bool:
        """Listen specifically for the wake word."""
        if not self.initialized:
            logger.warning("Voice recognition not available. Cannot listen for wake word.")
            return False
            
        # If microphone is not available, wake word detection is not possible
        if not self.microphone_available:
            logger.warning("Microphone not available. Wake word detection not possible.")
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
            
    def recognize_from_file(self, file_path: str) -> Optional[str]:
        """Recognize speech from an audio file."""
        if not self.recognizer or not self.initialized:
            logger.warning("Voice recognition engine not available.")
            return None
            
        try:
            import speech_recognition as sr
            with sr.AudioFile(file_path) as source:
                audio = self.recognizer.record(source)
            text = self.recognizer.recognize_google(audio)
            logger.info(f"Recognized text from file: {text}")
            return text
        except Exception as e:
            logger.error(f"Error recognizing speech from file: {str(e)}")
            return None
            
    def is_microphone_available(self) -> bool:
        """Check if microphone is available."""
        return self.microphone_available


# Global voice recognizer instance
voice_recognizer = VoiceRecognizer()