"""
Tests for the Voice modules of Jarvis AI.
"""

import sys
import os

# Add the parent directory to the path to allow imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from modules.voice_recognition import VoiceRecognizer
from modules.speech_synthesis import SpeechSynthesizer


def test_voice_recognizer():
    """Test voice recognizer functionality."""
    # Create a voice recognizer
    recognizer = VoiceRecognizer()
    
    # Check that it was initialized (even if not fully functional without hardware)
    print("Voice recognizer initialized successfully!")
    print(f"Engine: {recognizer.engine}")
    
    print("Voice recognition test completed!")


def test_speech_synthesizer():
    """Test speech synthesizer functionality."""
    # Create a speech synthesizer
    synthesizer = SpeechSynthesizer()
    
    # Check that it was initialized
    print("Speech synthesizer initialized successfully!")
    print(f"Engine: {synthesizer.engine}")
    
    # Test setting voice properties
    synthesizer.set_voice_properties(rate=150, volume=0.8)
    print("Voice properties set successfully!")
    
    print("Speech synthesis test completed!")


def main():
    """Run all voice module tests."""
    print("Running voice module tests...")
    
    try:
        test_voice_recognizer()
        test_speech_synthesizer()
        print("\nAll voice module tests completed successfully!")
    except Exception as e:
        print(f"Error during testing: {str(e)}")


if __name__ == "__main__":
    main()