"""
Tests for the Personality Engine module of Jarvis AI.
"""

import sys
import os
import shutil

# Add the parent directory to the path to allow imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from modules.personality import PersonalityEngine
from modules.nlp import NLPProcessor


def test_personality_engine():
    """Test personality engine functionality."""
    # Create a test personality engine
    personality = PersonalityEngine("test_user")
    
    # Test personality traits
    assert personality.personality_traits["formality"] == "professional"
    assert personality.personality_traits["humor"] == "subtle"
    assert personality.personality_traits["empathy"] == "moderate"
    
    print("Personality traits test passed!")


def test_contextual_response():
    """Test contextual response generation."""
    # Create a test personality engine
    personality = PersonalityEngine("test_user")
    
    # Create a mock NLP result
    nlp_result = {
        "original_text": "Hello Jarvis",
        "intent": "greeting",
        "entities": {},
        "sentiment": "neutral"
    }
    
    # Get contextual response
    response = personality.get_contextual_response(nlp_result)
    
    # Check that we got a response
    assert isinstance(response, str)
    assert len(response) > 0
    
    print("Contextual response test passed!")


def test_learning_from_interaction():
    """Test learning from interaction."""
    # Create a test personality engine
    personality = PersonalityEngine("test_user")
    
    # Create a mock NLP result with entities
    nlp_result = {
        "original_text": "Set a reminder for 3:30 PM",
        "intent": "command",
        "entities": {
            "time": ["3:30 PM"],
            "number": ["3", "30"]
        },
        "sentiment": "neutral"
    }
    
    # Learn from the interaction
    personality.learn_from_interaction("Set a reminder for 3:30 PM", nlp_result)
    
    # Check that entities were learned
    assert "time" in personality.user_profile["learned_context"]
    assert "3:30 PM" in personality.user_profile["learned_context"]["time"]
    
    print("Learning from interaction test passed!")


def test_conversation_history():
    """Test conversation history management."""
    # Create a test personality engine
    personality = PersonalityEngine("test_user")
    
    # Add some interactions to history
    personality.add_to_conversation_history("Hello", "Greetings!")
    personality.add_to_conversation_history("How are you?", "I am functioning optimally.")
    
    # Check that history was recorded
    assert len(personality.conversation_history) == 2
    
    # Add more interactions to test the 50-item limit
    for i in range(50):
        personality.add_to_conversation_history(f"Message {i}", f"Response {i}")
    
    # Check that history is limited to 50 items
    assert len(personality.conversation_history) == 50
    
    print("Conversation history test passed!")


def cleanup_test_files():
    """Clean up test files."""
    # Remove test user profile if it exists
    test_profile = "user_profiles/test_user.json"
    if os.path.exists(test_profile):
        os.remove(test_profile)
        
    # Remove user_profiles directory if it's empty
    if os.path.exists("user_profiles") and not os.listdir("user_profiles"):
        os.rmdir("user_profiles")


def main():
    """Run all personality engine tests."""
    try:
        test_personality_engine()
        test_contextual_response()
        test_learning_from_interaction()
        test_conversation_history()
        print("All personality engine tests passed successfully!")
    finally:
        cleanup_test_files()


if __name__ == "__main__":
    main()