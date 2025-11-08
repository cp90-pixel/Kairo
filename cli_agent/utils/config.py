# Configuration Utilities
# Manages loading configuration from environment variables and .env file

import os
from dotenv import load_dotenv

def load_config():
    """
    Load configuration from .env file and environment variables.
    Returns a dictionary with configuration values.
    """
    load_dotenv()  # Load .env file

    config = {
        'google_ai_api_key': os.getenv('GOOGLE_AI_API_KEY'),
        'log_level': os.getenv('LOG_LEVEL', 'INFO'),
        'max_tokens': int(os.getenv('MAX_TOKENS', 1000)),
    }

    # Validate required config
    if not config['google_ai_api_key']:
        raise ValueError("GOOGLE_AI_API_KEY is required. Please set it in your .env file.")

    return config