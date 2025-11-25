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
        welcome_msg = "Jarvis AI system is now operational. You can type your messages or say 'jarvis' followed by your command."
        print(welcome_msg)
        jarvis.speech_synthesizer.speak(welcome_msg)
        
        # Main interaction loop
        while jarvis.is_running:
            try:
                # Option for voice input
                mode = input("\nSelect input mode - (T)ext or (V)oice, or (Q)uit: ").strip().lower()
                
                if mode == 'q':
                    break
                elif mode == 'v':
                    # Voice mode
                    print("Listening... (say 'jarvis' followed by your command)")
                    jarvis.voice_recognizer.listen_for_wake_word("jarvis")
                    jarvis.listen_and_respond()
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