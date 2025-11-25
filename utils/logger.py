"""
Logging utility for Jarvis AI system.
Provides centralized logging functionality.
"""

import logging
import os
from datetime import datetime
from typing import Optional


class JarvisLogger:
    """Centralized logging system for Jarvis AI."""
    
    def __init__(self, name: str = "JarvisAI", log_file: str = "jarvis.log"):
        """Initialize the logger."""
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.INFO)
        
        # Create logs directory if it doesn't exist
        log_dir = "logs"
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)
            
        # Create file handler
        file_handler = logging.FileHandler(os.path.join(log_dir, log_file))
        file_handler.setLevel(logging.INFO)
        
        # Create console handler
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)
        
        # Create formatter
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)
        
        # Add handlers to logger
        if not self.logger.handlers:
            self.logger.addHandler(file_handler)
            self.logger.addHandler(console_handler)
            
    def info(self, message: str):
        """Log an info message."""
        self.logger.info(message)
        
    def warning(self, message: str):
        """Log a warning message."""
        self.logger.warning(message)
        
    def error(self, message: str):
        """Log an error message."""
        self.logger.error(message)
        
    def debug(self, message: str):
        """Log a debug message."""
        self.logger.debug(message)


# Global logger instance
logger = JarvisLogger()