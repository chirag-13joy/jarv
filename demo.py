#!/usr/bin/env python3
"""
Demo script for the Jarvis AI system.
Shows the capabilities of the NLP and Personality modules.
"""

import sys
import os

# Add the parent directory to the path to allow imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from modules.nlp import NLPProcessor
from modules.personality import PersonalityEngine


def demo():
    """Demonstrate the NLP and Personality capabilities."""
    print("Jarvis AI Demo")
    print("=" * 30)
    
    nlp = NLPProcessor()
    personality = PersonalityEngine("demo_user")
    
    # Sample inputs to test
    sample_inputs = [
        "Hello Jarvis, how are you today?",
        "What is the weather like tomorrow?",
        "Set a reminder for 3:30 PM",
        "Open the garage door",
        "Tell me about artificial intelligence",
        "This is amazing and wonderful!",
        "This is terrible and awful!",
        "The sky is blue."
    ]
    
    print("\nNLP Processing Demo:")
    print("-" * 20)
    
    for input_text in sample_inputs:
        print(f"\nInput: {input_text}")
        result = nlp.process(input_text)
        print(f"Intent: {result['intent']}")
        print(f"Entities: {result['entities']}")
        print(f"Sentiment: {result['sentiment']}")
    
    print("\n\nPersonality Engine Demo:")
    print("-" * 25)
    
    # Test contextual responses
    for input_text in sample_inputs[:4]:  # Just first 4 for brevity
        print(f"\nInput: {input_text}")
        nlp_result = nlp.process(input_text)
        response = personality.get_contextual_response(nlp_result)
        print(f"Response: {response}")
        personality.add_to_conversation_history(input_text, response)
    
    print("\n\nUser Profile:")
    print("-" * 15)
    print(f"Total interactions: {personality.user_profile['interaction_history']['total_interactions']}")
    print(f"Learned context: {personality.user_profile['learned_context']}")


if __name__ == "__main__":
    demo()