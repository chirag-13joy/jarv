"""
Core module for Jarvis AI system.
Handles initialization and coordination of all subsystems.
"""

import os
import sys
from typing import Dict, Any

# Add the parent directory to the path to allow imports
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Import modules
from modules.nlp import nlp_processor
from modules.personality import personality_engine
from modules.voice_recognition import voice_recognizer
from modules.speech_synthesis import speech_synthesizer


class JarvisCore:
    """Main coordinator for the Jarvis AI system."""
    
    def __init__(self, config: Dict[str, Any] = None):
        """Initialize the Jarvis AI system."""
        self.config = config or {}
        self.modules = {}
        self.is_running = False
        self.nlp_processor = nlp_processor
        self.personality_engine = personality_engine
        self.voice_recognizer = voice_recognizer
        self.speech_synthesizer = speech_synthesizer
        
    def initialize_modules(self):
        """Initialize all system modules."""
        # Initialize NLP module
        self.modules['nlp'] = self.nlp_processor
        print("NLP module initialized.")
        
        # Initialize Personality module
        self.modules['personality'] = self.personality_engine
        print("Personality engine initialized.")
        
        # Initialize Voice Recognition module
        self.modules['voice_recognition'] = self.voice_recognizer
        voice_status = "available" if getattr(self.voice_recognizer, 'initialized', False) else "not available (missing dependencies)"
        print(f"Voice recognition module initialized ({voice_status}).")
        
        # Initialize Speech Synthesis module
        self.modules['speech_synthesis'] = self.speech_synthesizer
        speech_status = "available" if getattr(self.speech_synthesizer, 'initialized', False) else "not available (missing dependencies)"
        print(f"Speech synthesis module initialized ({speech_status}).")
        
    def start(self):
        """Start the Jarvis AI system."""
        self.is_running = True
        print("Jarvis AI system initialized and running.")
        
    def stop(self):
        """Stop the Jarvis AI system."""
        self.is_running = False
        print("Jarvis AI system stopped.")
        
    def process_input(self, input_data: str) -> str:
        """Process input through the NLP pipeline and generate personalized response."""
        # Process the input through NLP
        nlp_result = self.nlp_processor.process(input_data)
        
        # Learn from the interaction
        self.personality_engine.learn_from_interaction(input_data, nlp_result)
        
        # Generate a contextual response based on personality
        response = self.personality_engine.get_contextual_response(nlp_result)
        
        # Add to conversation history
        self.personality_engine.add_to_conversation_history(input_data, response)
        
        return response
        
    def listen_and_respond(self):
        """Listen for voice input and respond with voice output."""
        # Check if voice recognition is available
        if not getattr(self.voice_recognizer, 'initialized', False):
            print("Voice recognition not available. Please install required dependencies.")
            return False
            
        # Listen for input
        user_input = self.voice_recognizer.listen()
        if user_input:
            # Process the input
            response = self.process_input(user_input)
            # Speak the response
            self.speech_synthesizer.speak(response)
            return True
        return False


def main():
    """Main entry point for the Jarvis AI system."""
    jarvis = JarvisCore()
    jarvis.start()
    return jarvis


if __name__ == "__main__":
    main()