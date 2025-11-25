"""
Integration test for the complete Jarvis AI system.
"""

import sys
import os

# Add the parent directory to the path to allow imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core import JarvisCore


def test_complete_system():
    """Test the complete Jarvis AI system."""
    print("Testing complete Jarvis AI system...")
    
    # Initialize Jarvis core
    jarvis = JarvisCore()
    jarvis.initialize_modules()
    
    print("\nSystem Modules:")
    print("-" * 15)
    for module_name, module in jarvis.modules.items():
        print(f"  {module_name}: {'✓' if module else '✗'}")
    
    print("\nTesting end-to-end processing:")
    print("-" * 30)
    
    # Test inputs
    test_inputs = [
        "Hello Jarvis, how are you today?",
        "What is the weather forecast for tomorrow?",
        "Set a reminder for my meeting at 3:30 PM",
        "Tell me about the history of artificial intelligence"
    ]
    
    for i, user_input in enumerate(test_inputs, 1):
        print(f"\nTest {i}: {user_input}")
        
        # Process the complete flow
        response = jarvis.process_input(user_input)
        print(f"  Response: {response}")
        
        # Verify that the response is meaningful
        assert isinstance(response, str), "Response should be a string"
        assert len(response) > 0, "Response should not be empty"
        assert not response.startswith("Error"), "Response should not be an error message"
        
        print("  ✓ Complete processing successful")
    
    print("\nTesting conversation history:")
    print("-" * 25)
    
    # Check conversation history
    history = jarvis.personality_engine.conversation_history
    print(f"  Conversation history entries: {len(history)}")
    assert len(history) == len(test_inputs), "Conversation history should match number of inputs"
    
    print("  ✓ Conversation history maintained")
    
    print("\nTesting user profile learning:")
    print("-" * 25)
    
    # Check that user profile was updated
    user_profile = jarvis.personality_engine.user_profile
    total_interactions = user_profile['interaction_history']['total_interactions']
    print(f"  Total interactions recorded: {total_interactions}")
    # Note: The count may be higher due to previous tests
    assert total_interactions >= len(test_inputs), "User profile should record all interactions"
    
    print("  ✓ User profile learning successful")
    
    print("\nAll integration tests passed!")


def main():
    """Run all integration tests."""
    print("Running complete system integration tests...")
    
    try:
        test_complete_system()
        print("\nAll integration tests completed successfully!")
        print("\nJarvis AI system is functioning correctly!")
    except Exception as e:
        print(f"Error during integration testing: {str(e)}")
        raise


if __name__ == "__main__":
    main()