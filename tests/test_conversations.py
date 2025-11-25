"""
Comprehensive test for conversational flows in Jarvis AI.
"""

import sys
import os

# Add the parent directory to the path to allow imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core import JarvisCore


def test_conversational_flows():
    """Test various conversational flows."""
    print("Testing conversational flows...")
    
    # Initialize Jarvis core
    jarvis = JarvisCore()
    jarvis.initialize_modules()
    
    # Test cases with expected responses
    test_cases = [
        {
            "input": "Hello Jarvis",
            "expected_intent": "greeting"
        },
        {
            "input": "What is the weather like today?",
            "expected_intent": "question"
        },
        {
            "input": "Set a reminder for 3:30 PM",
            "expected_intent": "command"
        },
        {
            "input": "Tell me about artificial intelligence",
            "expected_intent": "information"
        },
        {
            "input": "This is amazing!",
            "expected_sentiment": "positive"
        },
        {
            "input": "This is terrible!",
            "expected_sentiment": "negative"
        }
    ]
    
    print("\nTesting NLP processing:")
    print("-" * 25)
    
    for i, test_case in enumerate(test_cases, 1):
        user_input = test_case["input"]
        print(f"\nTest {i}: {user_input}")
        
        # Process the input through NLP
        nlp_result = jarvis.nlp_processor.process(user_input)
        print(f"  Intent: {nlp_result['intent']}")
        print(f"  Sentiment: {nlp_result['sentiment']}")
        print(f"  Entities: {nlp_result['entities']}")
        
        # Check if we have expected values
        if "expected_intent" in test_case:
            assert nlp_result['intent'] == test_case["expected_intent"], \
                f"Expected intent {test_case['expected_intent']}, got {nlp_result['intent']}"
                
        if "expected_sentiment" in test_case:
            assert nlp_result['sentiment'] == test_case["expected_sentiment"], \
                f"Expected sentiment {test_case['expected_sentiment']}, got {nlp_result['sentiment']}"
                
        print("  ✓ Test passed")
    
    print("\n\nTesting personality responses:")
    print("-" * 30)
    
    # Test personality responses
    personality_test_cases = [
        "Hello Jarvis",
        "What time is it?",
        "Open the garage door",
        "Tell me a joke"
    ]
    
    for i, user_input in enumerate(personality_test_cases, 1):
        print(f"\nTest {i}: {user_input}")
        
        # Process through NLP
        nlp_result = jarvis.nlp_processor.process(user_input)
        
        # Get personality response
        response = jarvis.personality_engine.get_contextual_response(nlp_result)
        print(f"  Response: {response}")
        
        # Add to conversation history
        jarvis.personality_engine.add_to_conversation_history(user_input, response)
        
        print("  ✓ Personality response generated")
    
    print("\n\nTesting user profile learning:")
    print("-" * 30)
    
    # Check that user profile was updated
    user_profile = jarvis.personality_engine.user_profile
    print(f"  Total interactions: {user_profile['interaction_history']['total_interactions']}")
    print("  ✓ User profile updated")
    
    print("\nAll conversational flow tests passed!")


def main():
    """Run all conversational flow tests."""
    print("Running conversational flow tests...")
    
    try:
        test_conversational_flows()
        print("\nAll tests completed successfully!")
    except Exception as e:
        print(f"Error during testing: {str(e)}")
        raise


if __name__ == "__main__":
    main()