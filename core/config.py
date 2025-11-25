"""
Configuration management for Jarvis AI system.
Handles loading and managing system configurations.
"""

import json
import os
from typing import Dict, Any, Optional


class ConfigManager:
    """Manages configuration for the Jarvis AI system."""
    
    def __init__(self, config_path: str = "config.json"):
        """Initialize the configuration manager."""
        self.config_path = config_path
        self.config = self._load_config()
        
    def _load_config(self) -> Dict[str, Any]:
        """Load configuration from file or create default configuration."""
        if os.path.exists(self.config_path):
            try:
                with open(self.config_path, 'r') as f:
                    return json.load(f)
            except (json.JSONDecodeError, IOError):
                return self._get_default_config()
        else:
            # Create default config file
            default_config = self._get_default_config()
            self._save_config(default_config)
            return default_config
            
    def _get_default_config(self) -> Dict[str, Any]:
        """Get default configuration values."""
        return {
            "system": {
                "name": "Jarvis",
                "version": "1.0.0",
                "debug": False
            },
            "nlp": {
                "language": "en",
                "confidence_threshold": 0.7
            },
            "voice": {
                "input_device": "default",
                "output_device": "default",
                "wake_word": "jarvis"
            },
            "personality": {
                "formality": "professional",
                "humor": "subtle",
                "empathy": "moderate"
            }
        }
        
    def _save_config(self, config: Dict[str, Any]):
        """Save configuration to file."""
        try:
            with open(self.config_path, 'w') as f:
                json.dump(config, f, indent=2)
        except IOError:
            print("Warning: Could not save configuration file.")
            
    def get(self, key: str, default: Any = None) -> Any:
        """Get a configuration value."""
        keys = key.split('.')
        value = self.config
        for k in keys:
            if isinstance(value, dict) and k in value:
                value = value[k]
            else:
                return default
        return value
        
    def set(self, key: str, value: Any):
        """Set a configuration value."""
        keys = key.split('.')
        config = self.config
        for k in keys[:-1]:
            if k not in config:
                config[k] = {}
            config = config[k]
        config[keys[-1]] = value
        self._save_config(self.config)
        
    def reload(self):
        """Reload configuration from file."""
        self.config = self._load_config()


# Global configuration manager instance
config_manager = ConfigManager()