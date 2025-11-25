"""
Tests for the NLP module of Jarvis AI.
"""

import sys
import os

# Add the parent directory to the path to allow imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from modules.nlp import NLPProcessor


def test_intent_classification():
    """Test intent classification functionality."""
    nlp = NLPProcessor()
    
    # Test greeting intent
    result = nlp.classify_intent("Hello, how are you?")
    assert result == "greeting", f"Expected 'greeting', got '{result}'"
    
    # Test question intent
    result = nlp.classify_intent("What is the weather like today?")
    assert result == "question", f"Expected 'question', got '{result}'"
    
    # Test command intent
    result = nlp.classify_intent("Open the door")
    assert result == "command", f"Expected 'command', got '{result}'"
    
    # Test information intent
    result = nlp.classify_intent("Tell me about artificial intelligence")
    assert result == "information", f"Expected 'information', got '{result}'"
    
    print("All intent classification tests passed!")


def test_entity_extraction():
    """Test entity extraction functionality."""
    nlp = NLPProcessor()
    
    # Test time entity extraction
    result = nlp.extract_entities("Set a reminder for 3:30 PM")
    assert "time" in result, "Time entity not detected"
    assert "3:30 PM" in result["time"], f"Expected '3:30 PM' in result, got {result['time']}"
    
    # Test email entity extraction
    result = nlp.extract_entities("My email is test@example.com")
    assert "email" in result, "Email entity not detected"
    assert "test@example.com" in result["email"], f"Expected 'test@example.com' in result, got {result['email']}"
    
    print("All entity extraction tests passed!")


def test_sentiment_analysis():
    """Test sentiment analysis functionality."""
    nlp = NLPProcessor()
    
    # Test positive sentiment
    result = nlp.analyze_sentiment("This is amazing and wonderful!")
    assert result == "positive", f"Expected 'positive', got '{result}'"
    
    # Test negative sentiment
    result = nlp.analyze_sentiment("This is terrible and awful!")
    assert result == "negative", f"Expected 'negative', got '{result}'"
    
    # Test neutral sentiment
    result = nlp.analyze_sentiment("The sky is blue.")
    assert result == "neutral", f"Expected 'neutral', got '{result}'"
    
    print("All sentiment analysis tests passed!")


def test_full_nlp_pipeline():
    """Test the full NLP processing pipeline."""
    nlp = NLPProcessor()
    
    # Test complete processing
    text = "Hello Jarvis, can you tell me what time it is?"
    result = nlp.process(text)
    
    assert result["original_text"] == text, "Original text mismatch"
    assert "intent" in result, "Intent missing from result"
    assert "entities" in result, "Entities missing from result"
    assert "sentiment" in result, "Sentiment missing from result"
    
    print("Full NLP pipeline test passed!")


if __name__ == "__main__":
    test_intent_classification()
    test_entity_extraction()
    test_sentiment_analysis()
    test_full_nlp_pipeline()
    print("All NLP tests passed successfully!")