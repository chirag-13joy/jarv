"""
Test for Hindi language support in Jarvis AI.
"""

import sys
import os

# Add the parent directory to the path to allow imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from modules.nlp import NLPProcessor
from modules.personality import PersonalityEngine


def test_hindi_language_support():
    """Test Hindi language processing and responses."""
    print("Testing Hindi language support...")
    
    # Initialize components
    nlp = NLPProcessor()
    personality = PersonalityEngine()
    
    # Test Hindi input detection
    hindi_inputs = [
        "नमस्ते जार्विस",
        "आप कैसे हैं?",
        "मुझे एक कार्य निर्धारित करें",
        "मुझे बताएं कि कृत्रिम बुद्धिमत्ता क्या है"
    ]
    
    print("\nTesting Hindi language detection:")
    print("-" * 35)
    
    for input_text in hindi_inputs:
        language = nlp.detect_language(input_text)
        print(f"Input: {input_text}")
        print(f"Detected language: {language}")
        assert language == 'hindi', f"Expected 'hindi', got '{language}'"
        print("✓ Language detection passed\n")
    
    # Test English language detection (should still work)
    english_inputs = [
        "Hello Jarvis",
        "How are you?",
        "Set a reminder",
        "Tell me about artificial intelligence"
    ]
    
    print("\nTesting English language detection:")
    print("-" * 35)
    
    for input_text in english_inputs:
        language = nlp.detect_language(input_text)
        print(f"Input: {input_text}")
        print(f"Detected language: {language}")
        assert language == 'english', f"Expected 'english', got '{language}'"
        print("✓ Language detection passed\n")
    
    # Test Hindi NLP processing
    print("\nTesting Hindi NLP processing:")
    print("-" * 30)
    
    for input_text in hindi_inputs[:2]:  # Test first two inputs
        print(f"Input: {input_text}")
        result = nlp.process(input_text)
        print(f"Intent: {result['intent']}")
        print(f"Sentiment: {result['sentiment']}")
        print(f"Language: {result['language']}")
        assert result['language'] == 'hindi', f"Expected language 'hindi', got '{result['language']}'"
        print("✓ Hindi NLP processing passed\n")
    
    # Test Hindi responses
    print("\nTesting Hindi responses:")
    print("-" * 22)
    
    # Create a mock NLP result for Hindi greeting
    nlp_result = {
        'original_text': 'नमस्ते जार्विस',
        'language': 'hindi',
        'intent': 'greeting',
        'entities': {},
        'sentiment': 'neutral'
    }
    
    response = personality.get_contextual_response(nlp_result)
    print(f"Input: {nlp_result['original_text']}")
    print(f"Response: {response}")
    assert 'नमस्ते' in response or 'जार्विस' in response, "Response should be in Hindi"
    print("✓ Hindi response generation passed\n")
    
    print("All Hindi language support tests passed!")


def main():
    """Run all Hindi language support tests."""
    print("Running Hindi language support tests...")
    
    try:
        test_hindi_language_support()
        print("\nAll Hindi language support tests completed successfully!")
    except Exception as e:
        print(f"Error during testing: {str(e)}")
        raise


if __name__ == "__main__":
    main()