#!/usr/bin/env python3
"""
Hindi Language Support Demo for the Jarvis AI system.
"""

import sys
import os

# Add the parent directory to the path to allow imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from modules.nlp import NLPProcessor
from modules.personality import PersonalityEngine


def hindi_demo():
    """Demonstrate the Hindi language capabilities."""
    print("Jarvis AI Hindi Language Support Demo")
    print("=" * 38)
    
    nlp = NLPProcessor()
    personality = PersonalityEngine()
    
    # Sample inputs in Hindi
    hindi_inputs = [
        "नमस्ते जार्विस, आप कैसे हैं?",
        "आप मुझे कृत्रिम बुद्धिमत्ता के बारे में बता सकते हैं?",
        "क्या आप मेरे लिए एक कार्य निर्धारित कर सकते हैं?",
        "मुझे बताएं कि आज का मौसम कैसा है",
        "यह बहुत अच्छा है!",
        "यह बहुत बुरा है!"
    ]
    
    print("\nHindi NLP Processing Demo:")
    print("-" * 26)
    
    for input_text in hindi_inputs:
        print(f"\nInput: {input_text}")
        result = nlp.process(input_text)
        print(f"Language: {result['language']}")
        print(f"Intent: {result['intent']}")
        print(f"Entities: {result['entities']}")
        print(f"Sentiment: {result['sentiment']}")
    
    print("\n\nHindi Personality Engine Demo:")
    print("-" * 31)
    
    # Test contextual responses in Hindi
    for input_text in hindi_inputs[:4]:  # First 4 for brevity
        print(f"\nInput: {input_text}")
        nlp_result = nlp.process(input_text)
        response = personality.get_contextual_response(nlp_result)
        print(f"Response: {response}")
        personality.add_to_conversation_history(input_text, response)
    
    print("\n\nLanguage Detection Comparison:")
    print("-" * 32)
    
    # Compare language detection
    mixed_inputs = [
        "Hello जार्विस",
        "नमस्ते Jarvis",
        "How are you? कैसे हैं आप?",
        "मैं ठीक हूँ, thank you"
    ]
    
    for input_text in mixed_inputs:
        language = nlp.detect_language(input_text)
        print(f"Input: {input_text}")
        print(f"Detected language: {language}")
        print()


if __name__ == "__main__":
    hindi_demo()