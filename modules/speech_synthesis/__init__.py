"""
Speech synthesis module for Jarvis AI.
Handles text-to-speech conversion using various engines.
"""

import os
import subprocess
from typing import Optional
from utils.logger import logger


class DirectSpeechSynthesizer:
    """Direct speech synthesizer using espeak."""
    
    def __init__(self):
        """Initialize the direct speech synthesizer."""
        self.initialized = self._check_espeak_availability()
        
    def _check_espeak_availability(self):
        """Check if espeak is available."""
        try:
            result = subprocess.run(['espeak', '--version'], 
                                  capture_output=True, text=True, timeout=5)
            return result.returncode == 0
        except Exception as e:
            logger.warning(f"espeak availability check failed: {e}")
            return False
    
    def speak(self, text: str) -> bool:
        """Convert text to speech using espeak."""
        if not self.initialized:
            logger.warning("Speech synthesis engine not available. Text response only.")
            return False
            
        try:
            logger.info(f"Speaking: {text}")
            # Use espeak directly
            result = subprocess.run(['espeak', text], 
                                  capture_output=True, text=True, timeout=30)
            if result.returncode == 0:
                return True
            else:
                logger.error(f"espeak failed with return code {result.returncode}: {result.stderr}")
                return False
        except Exception as e:
            logger.error(f"Error during speech synthesis: {str(e)}")
            return False
    
    def set_voice_properties(self, rate: int = None, volume: float = None, voice_id: str = None):
        """Set voice properties (stub for compatibility)."""
        logger.info("DirectSpeechSynthesizer: set_voice_properties called (not implemented)")


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
                # Try to initialize pyttsx3, but catch voice selection errors
                try:
                    self.synthesizer = pyttsx3.init()
                    # Set default properties
                    self.synthesizer.setProperty('rate', 200)  # Speed of speech
                    self.synthesizer.setProperty('volume', 0.9)  # Volume level
                    self.initialized = True
                    logger.info("pyttsx3 engine initialized successfully")
                except Exception as init_error:
                    # If pyttsx3 fails, fall back to direct espeak
                    if "SetVoiceByName" in str(init_error):
                        logger.warning("pyttsx3 voice selection failed, falling back to direct espeak")
                        self.synthesizer = DirectSpeechSynthesizer()
                        self.initialized = self.synthesizer.initialized
                        if self.initialized:
                            logger.info("Direct espeak engine initialized successfully")
                        else:
                            logger.error("Direct espeak engine failed to initialize")
                    else:
                        # Re-raise if it's a different error
                        raise init_error
            elif self.engine == "direct_espeak":
                # Use our direct espeak implementation
                self.synthesizer = DirectSpeechSynthesizer()
                self.initialized = self.synthesizer.initialized
                if self.initialized:
                    logger.info("Direct espeak engine initialized successfully")
                else:
                    logger.error("Direct espeak engine failed to initialize")
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
            # Try to fall back to direct espeak
            self.synthesizer = DirectSpeechSynthesizer()
            self.initialized = self.synthesizer.initialized
            if self.initialized:
                logger.info("Falling back to direct espeak engine")
            else:
                self.synthesizer = None
        except Exception as e:
            logger.error(f"Error initializing speech synthesis engine: {str(e)}")
            # Try to fall back to direct espeak
            self.synthesizer = DirectSpeechSynthesizer()
            self.initialized = self.synthesizer.initialized
            if self.initialized:
                logger.info("Falling back to direct espeak engine after error")
            else:
                self.synthesizer = None
            
    def speak(self, text: str) -> bool:
        """Convert text to speech and play it."""
        if not self.synthesizer:
            logger.warning("Speech synthesis engine not available. Text response only.")
            return False
            
        try:
            logger.info(f"Speaking: {text}")
            if hasattr(self.synthesizer, 'say'):
                # pyttsx3 interface
                self.synthesizer.say(text)
                self.synthesizer.runAndWait()
                return True
            elif hasattr(self.synthesizer, 'speak'):
                # DirectSpeechSynthesizer interface
                return self.synthesizer.speak(text)
            else:
                logger.error("Unknown synthesizer interface")
                return False
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
            if hasattr(self.synthesizer, 'setProperty'):
                # pyttsx3 interface
                if rate is not None:
                    self.synthesizer.setProperty('rate', rate)
                if volume is not None:
                    self.synthesizer.setProperty('volume', volume)
                if voice_id is not None:
                    self.synthesizer.setProperty('voice', voice_id)
            elif hasattr(self.synthesizer, 'set_voice_properties'):
                # DirectSpeechSynthesizer interface
                self.synthesizer.set_voice_properties(rate, volume, voice_id)
            else:
                logger.warning("Unknown synthesizer interface for setting properties")
        except Exception as e:
            logger.error(f"Error setting voice properties: {str(e)}")


# Global speech synthesizer instance
speech_synthesizer = SpeechSynthesizer()