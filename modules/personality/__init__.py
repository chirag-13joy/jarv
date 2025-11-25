"""
Personality engine for Jarvis AI.
Handles contextual responses and user interaction personalization.
"""

import json
import os
from typing import Dict, Any, List
from utils.logger import logger


class PersonalityEngine:
    """Manages the personality and contextual responses for Jarvis AI."""
    
    def __init__(self, user_id: str = "default"):
        """Initialize the personality engine."""
        self.user_id = user_id
        self.user_profile = self._load_user_profile()
        self.conversation_history: List[Dict[str, Any]] = []
        self.personality_traits = {
            "formality": "professional",  # professional, casual, informal
            "humor": "subtle",            # none, subtle, moderate, heavy
            "empathy": "moderate",        # low, moderate, high
            "responsiveness": "concise"   # verbose, moderate, concise
        }
        
        # Hindi responses for different intents
        self.hindi_responses = {
            'greeting': {
                'new': "नमस्ते। मैं जार्विस हूँ, आपका वर्चुअल सहायक। मैं आपकी किस प्रकार सहायता कर सकता हूँ?",
                'returning': "वापसी पर स्वागत है। मैं आपकी किस प्रकार सहायता कर सकता हूँ?"
            },
            'question': "यह एक उत्कृष्ट प्रश्न है। मैं आपको आवश्यक जानकारी प्रदान करूंगा।",
            'command': "स्वीकृत। मैं तुरंत वह निर्देश निष्पादित करूंगा।",
            'information': "मुझे खुशी होगी कि वह विषय आपको समझाऊं।",
            'positive': "मुझे आपके सकारात्मक दृष्टिकोण की सराहना है।",
            'negative': "मुझे कुछ निराशा का एहसास हो रहा है। मैं इस मामले को हल करने में आपकी किस प्रकार सहायता कर सकता हूँ?",
            'statement': "मैं समझ गया। मैं आपकी किस प्रकार और सहायता कर सकता हूँ?"
        }
        
    def _load_user_profile(self) -> Dict[str, Any]:
        """Load user profile from file or create default."""
        profile_path = f"user_profiles/{self.user_id}.json"
        
        # Create user_profiles directory if it doesn't exist
        profile_dir = "user_profiles"
        if not os.path.exists(profile_dir):
            os.makedirs(profile_dir)
            
        if os.path.exists(profile_path):
            try:
                with open(profile_path, 'r') as f:
                    return json.load(f)
            except (json.JSONDecodeError, IOError):
                return self._get_default_profile()
        else:
            # Create default profile
            default_profile = self._get_default_profile()
            self._save_user_profile(default_profile)
            return default_profile
            
    def _get_default_profile(self) -> Dict[str, Any]:
        """Get default user profile."""
        return {
            "preferences": {
                "communication_style": "professional",
                "topics_of_interest": [],
                "interaction_frequency": "daily"
            },
            "interaction_history": {
                "total_interactions": 0,
                "first_interaction": None,
                "last_interaction": None
            },
            "learned_context": {}
        }
        
    def _save_user_profile(self, profile: Dict[str, Any]):
        """Save user profile to file."""
        profile_path = f"user_profiles/{self.user_id}.json"
        try:
            with open(profile_path, 'w') as f:
                json.dump(profile, f, indent=2)
        except IOError:
            logger.warning("Could not save user profile.")
            
    def update_personality_trait(self, trait: str, value: str):
        """Update a personality trait."""
        if trait in self.personality_traits:
            self.personality_traits[trait] = value
            logger.info(f"Updated personality trait '{trait}' to '{value}'")
            
    def add_to_conversation_history(self, user_input: str, jarvis_response: str):
        """Add an interaction to the conversation history."""
        interaction = {
            "user_input": user_input,
            "jarvis_response": jarvis_response,
            "timestamp": __import__('datetime').datetime.now().isoformat()
        }
        self.conversation_history.append(interaction)
        
        # Keep only the last 50 interactions to manage memory
        if len(self.conversation_history) > 50:
            self.conversation_history = self.conversation_history[-50:]
            
    def get_contextual_response(self, nlp_result: Dict[str, Any]) -> str:
        """Generate a contextual response based on NLP analysis and personality."""
        intent = nlp_result['intent']
        sentiment = nlp_result['sentiment']
        entities = nlp_result['entities']
        language = nlp_result.get('language', 'english')
        
        # Adjust response based on personality traits
        formality = self.personality_traits['formality']
        humor = self.personality_traits['humor']
        empathy = self.personality_traits['empathy']
        
        # Base responses
        if language == 'hindi':
            # Hindi responses
            if intent == 'greeting':
                if len(self.conversation_history) == 0:
                    response = self.hindi_responses['greeting']['new']
                else:
                    response = self.hindi_responses['greeting']['returning']
            elif intent == 'question':
                response = self.hindi_responses['question']
            elif intent == 'command':
                response = self.hindi_responses['command']
            elif intent == 'information':
                response = self.hindi_responses['information']
            else:
                # For statements, consider sentiment
                if sentiment == 'positive':
                    response = self.hindi_responses['positive']
                elif sentiment == 'negative':
                    response = self.hindi_responses['negative']
                else:
                    response = self.hindi_responses['statement']
        else:
            # English responses (existing functionality)
            if intent == 'greeting':
                if len(self.conversation_history) == 0:
                    response = "Good day. I am JARVIS, your virtual assistant. How may I be of service to you today?"
                else:
                    response = "Welcome back. How can I assist you?"
            elif intent == 'question':
                response = "That is an excellent inquiry. Allow me to provide you with the information you seek."
            elif intent == 'command':
                response = "Acknowledged. I shall execute that directive immediately."
            elif intent == 'information':
                response = "I would be delighted to share information on that subject."
            else:
                # For statements, consider sentiment
                if sentiment == 'positive':
                    response = "I appreciate your positive outlook."
                elif sentiment == 'negative':
                    response = "I sense some frustration. How might I assist in resolving this matter?"
                else:
                    response = "I understand. How else may I be of assistance?"
                
        # Apply personality modifiers
        if humor != "none" and intent == 'greeting' and len(self.conversation_history) > 0:
            if language == 'hindi':
                if humor == "subtle":
                    response += " ऐसा लगता है कि हम फिर से मिले हैं।"
                elif humor == "moderate":
                    response += " समय पर, मैं देखता हूँ।"
            else:
                if humor == "subtle":
                    response += " It appears we meet again."
                elif humor == "moderate":
                    response += " Right on schedule, I see."
                
        # Update user profile with interaction
        self.user_profile['interaction_history']['total_interactions'] += 1
        self.user_profile['interaction_history']['last_interaction'] = \
            __import__('datetime').datetime.now().isoformat()
            
        if self.user_profile['interaction_history']['first_interaction'] is None:
            self.user_profile['interaction_history']['first_interaction'] = \
                __import__('datetime').datetime.now().isoformat()
                
        self._save_user_profile(self.user_profile)
        
        return response
        
    def learn_from_interaction(self, user_input: str, nlp_result: Dict[str, Any]):
        """Learn from the interaction to personalize future responses."""
        # Extract topics of interest
        if 'entities' in nlp_result:
            for entity_type, entity_list in nlp_result['entities'].items():
                if entity_type not in self.user_profile['learned_context']:
                    self.user_profile['learned_context'][entity_type] = []
                for entity in entity_list:
                    if entity not in self.user_profile['learned_context'][entity_type]:
                        self.user_profile['learned_context'][entity_type].append(entity)
                        
        # Save updated profile
        self._save_user_profile(self.user_profile)


# Global personality engine instance
personality_engine = PersonalityEngine()