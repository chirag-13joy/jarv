"""
Natural Language Processing module for Jarvis AI.
Handles intent classification, entity extraction, and sentiment analysis.
"""

import re
from typing import Dict, List, Tuple, Any
from utils.logger import logger


class NLPProcessor:
    """Processes natural language input to extract meaning and intent."""
    
    def __init__(self):
        """Initialize the NLP processor."""
        self.intents = {
            'greeting': [
                r'\b(hello|hi|hey|greetings|namaste|namaskar|pranam)\b',
                r'\b(good morning|good afternoon|good evening|shubh prabhat|shubh sandhya|shubh raatri)\b',
                r'\b(namaste|namaskar|pranam|aadab|sat shri akaal|vanakkam)\b'
            ],
            'question': [
                r'\b(what|how|when|where|why|who|which)\b.*\?',
                r'\b(could|would|can|will|shall)\b',
                r'\b(kya|kaise|kab|kahan|kyun|kaun|kis)\b.*\?',
                r'\b(kya|kya aap|kya mein|kya hum)\b'
            ],
            'command': [
                r'\b(open|close|start|stop|run|execute)\b',
                r'\b(set|change|update|modify)\b',
                r'\b(kholo|band karo|shuru karo|ruk jao|chala do)\b',
                r'\b(set karo|badlo|update karo|modify karo)\b'
            ],
            'information': [
                r'\b(tell me about|explain|describe)\b',
                r'\b(what is|who is|where is)\b',
                r'\b(batao|samjhao|vistar se batao)\b',
                r'\b(kya hai|kaun hai|kahan hai)\b'
            ]
        }
        
        self.entities = {
            'time': r'\b(\d{1,2}:\d{2}\s*(AM|PM)?)\b',
            'date': r'\b(\d{1,2}/\d{1,2}/\d{4})\b',
            'number': r'\b\d+\b',
            'email': r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        }
        
        # Hindi positive and negative words for sentiment analysis
        self.hindi_positive_words = [
            'accha', 'acha', 'bahut accha', 'bahut acha', 'shandar', 'badiya', 
            'mazaboot', 'kamaal', 'badi mazaboot', 'kamaal ka', 'pyaar', 'pasand'
        ]
        
        self.hindi_negative_words = [
            'bura', 'buraa', 'bekar', 'bekaar', 'ghatiya', 'ghatiyaa', 
            'nafrat', 'nafrat', 'ganda', 'gandaa', 'pareshan', 'pareshaan'
        ]
        
    def classify_intent(self, text: str) -> str:
        """Classify the intent of the input text."""
        text_lower = text.lower()
        
        for intent, patterns in self.intents.items():
            for pattern in patterns:
                if re.search(pattern, text_lower):
                    return intent
                    
        # Default intent if no patterns match
        return 'statement'
        
    def extract_entities(self, text: str) -> Dict[str, List[str]]:
        """Extract entities from the input text."""
        entities = {}
        
        for entity_type, pattern in self.entities.items():
            matches = re.findall(pattern, text, re.IGNORECASE)
            if matches:
                # Handle different group matching patterns
                if isinstance(matches[0], tuple):
                    entities[entity_type] = [match[0] for match in matches]
                else:
                    entities[entity_type] = matches
                    
        return entities
        
    def analyze_sentiment(self, text: str) -> str:
        """Perform basic sentiment analysis on the input text."""
        positive_words = [
            'good', 'great', 'excellent', 'amazing', 'wonderful', 
            'fantastic', 'awesome', 'brilliant', 'perfect', 'love'
        ]
        
        negative_words = [
            'bad', 'terrible', 'awful', 'horrible', 'hate',
            'disgusting', 'worst', 'annoying', 'frustrating'
        ]
        
        text_lower = text.lower()
        positive_count = sum(1 for word in positive_words if word in text_lower)
        negative_count = sum(1 for word in negative_words if word in text_lower)
        
        # Check for Hindi positive words
        for word in self.hindi_positive_words:
            if word in text_lower:
                positive_count += 1
                
        # Check for Hindi negative words
        for word in self.hindi_negative_words:
            if word in text_lower:
                negative_count += 1
        
        if positive_count > negative_count:
            return 'positive'
        elif negative_count > positive_count:
            return 'negative'
        else:
            return 'neutral'
            
    def detect_language(self, text: str) -> str:
        """Detect if the text is in Hindi or English."""
        # Simple heuristic: check for common Hindi characters
        hindi_chars = set("ऀँंःऄअआइईउऊऋऌऍऎएऐऑऒओऔकखगघङचछजझञटठडढणतथदधनऩपफबभमयरऱलळऴवशषसहऺऻ़ऽािीुूृॄॅॆेैॉॊोौ्ॎॏॐ॒॑॓॔ॕॖॗक़ख़ग़ज़ड़ढ़फ़य़ॠॡॢॣ।॥०१२३४५६७८९॰ॱॲॳॴॵॶॷॸॹॺॻॼॽॾॿ")
        text_chars = set(text)
        
        hindi_char_count = len(text_chars.intersection(hindi_chars))
        total_char_count = len(text_chars)
        
        if total_char_count > 0 and (hindi_char_count / total_char_count) > 0.3:
            return 'hindi'
        else:
            return 'english'
            
    def process(self, text: str) -> Dict[str, Any]:
        """Process text through the full NLP pipeline."""
        logger.info(f"Processing text: {text}")
        
        # Detect language
        language = self.detect_language(text)
        
        intent = self.classify_intent(text)
        entities = self.extract_entities(text)
        sentiment = self.analyze_sentiment(text)
        
        result = {
            'original_text': text,
            'language': language,
            'intent': intent,
            'entities': entities,
            'sentiment': sentiment
        }
        
        logger.info(f"NLP processing result: {result}")
        return result


# Global NLP processor instance
nlp_processor = NLPProcessor()