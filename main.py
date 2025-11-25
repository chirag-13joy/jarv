#!/usr/bin/env python3
"""
Main entry point for the Jarvis AI system.
Initializes and coordinates all modules.
"""

import sys
import os

# Add the current directory to the path to allow imports
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from core import JarvisCore
from utils.logger import logger


def main():
    """Main entry point for the Jarvis AI system."""
    logger.info("Starting Jarvis AI system...")
    
    try:
        # Initialize the core system
        jarvis = JarvisCore()
        jarvis.initialize_modules()
        jarvis.start()
        
        # Welcome message
        welcome_msg = "Jarvis AI system is now operational. You can type your messages."
        
        # Check if voice features are available
        voice_available = jarvis.voice_recognizer.initialized if hasattr(jarvis.voice_recognizer, 'initialized') else False
        speech_available = jarvis.speech_synthesizer.initialized if hasattr(jarvis.speech_synthesizer, 'initialized') else False
        
        if voice_available and speech_available:
            welcome_msg += " You can also use voice input by selecting (V)oice mode."
        elif speech_available:
            welcome_msg += " Text responses will be spoken aloud."
        else:
            welcome_msg += " Voice features require additional system dependencies."
            
        print(welcome_msg)
        jarvis.speech_synthesizer.speak(welcome_msg)
        
        # Main interaction loop
        while jarvis.is_running:
            try:
                # Option for voice input
                if voice_available:
                    mode = input("\nSelect input mode - (T)ext or (V)oice, or (Q)uit: ").strip().lower()
                else:
                    mode = 't'  # Default to text mode if voice not available
                    print("\nText mode selected (voice features not available)")
                
                if mode == 'q':
                    break
                elif mode == 'v' and voice_available:
                    # Voice mode
                    print("Listening... (say 'jarvis' followed by your command)")
                    if jarvis.voice_recognizer.listen_for_wake_word("jarvis"):
                        jarvis.listen_and_respond()
                    else:
                        print("Wake word not detected or voice input failed.")
                else:
                    # Text mode (default)
                    user_input = input("You: ")
                    if user_input.lower() in ['exit', 'quit', 'stop']:
                        break
                    response = jarvis.process_input(user_input)
                    print(f"Jarvis: {response}")
                    jarvis.speech_synthesizer.speak(response)
                    
            except KeyboardInterrupt:
                break
            except EOFError:
                break
                
        jarvis.stop()
        logger.info("Jarvis AI system stopped.")
        
    except Exception as e:
        logger.error(f"Error running Jarvis AI system: {str(e)}")
        return 1
        
    return 0


if __name__ == "__main__":
    sys.exit(main())