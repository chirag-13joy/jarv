"""
Speech synthesis module for Jarvis AI.
Handles text-to-speech conversion using various engines.
"""

import os
from typing import Optional
from utils.logger import logger


class SpeechSynthesizer:
    """Handles speech synthesis for the Jarvis AI system."""
    
    def __init__(self, engine: str = "pyttsx3"):
        """Initialize the speech synthesizer."""
        self.engine = engine
        self.synthesizer = None
        self.initialized = False
        self._initialize_engine()
        
    def _initialize_engine(self):
        """Initialize the selected speech synthesis engine."""
        try:
            if self.engine == "pyttsx3":
                import pyttsx3
                self.synthesizer = pyttsx3.init()
                # Set default properties
                self.synthesizer.setProperty('rate', 200)  # Speed of speech
                self.synthesizer.setProperty('volume', 0.9)  # Volume level
                self.initialized = True
                logger.info("pyttsx3 engine initialized successfully")
            elif self.engine == "gtts":
                # gTTS implementation would go here
                logger.info("gTTS engine selected (not implemented yet)")
            else:
                logger.warning(f"Unknown engine '{self.engine}', falling back to pyttsx3")
                import pyttsx3
                self.synthesizer = pyttsx3.init()
                self.initialized = True
        except ImportError:
            logger.error("Required speech synthesis libraries not installed")
            logger.info("Please install pyttsx3: pip install pyttsx3")
            self.synthesizer = None
            self.initialized = False
        except Exception as e:
            logger.error(f"Error initializing speech synthesis engine: {str(e)}")
            self.synthesizer = None
            self.initialized = False
            
    def speak(self, text: str) -> bool:
        """Convert text to speech and play it."""
        if not self.synthesizer:
            logger.warning("Speech synthesis engine not available. Text response only.")
            return False
            
        try:
            logger.info(f"Speaking: {text}")
            self.synthesizer.say(text)
            self.synthesizer.runAndWait()
            return True
        except Exception as e:
            logger.error(f"Error during speech synthesis: {str(e)}")
            # Try to reinitialize the engine
            self._initialize_engine()
            return False
            
    def set_voice_properties(self, rate: Optional[int] = None, volume: Optional[float] = None, voice_id: Optional[str] = None):
        """Set voice properties."""
        if not self.synthesizer:
            logger.warning("Cannot set voice properties: speech synthesis engine not available")
            return
            
        try:
            if rate is not None:
                self.synthesizer.setProperty('rate', rate)
            if volume is not None:
                self.synthesizer.setProperty('volume', volume)
            if voice_id is not None:
                self.synthesizer.setProperty('voice', voice_id)
        except Exception as e:
            logger.error(f"Error setting voice properties: {str(e)}")


# Global speech synthesizer instance
speech_synthesizer = SpeechSynthesizer()