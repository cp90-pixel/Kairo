# Gemini API Client Module
# Implements client for interacting with Google's Gemini AI API

import google.generativeai as genai
from typing import Optional, Dict, Any
import logging

logger = logging.getLogger(__name__)

class GeminiClient:
    def __init__(self, api_key: str, model_name: str = "gemini-1.5-flash"):
        """
        Initialize the Gemini API client.

        Args:
            api_key: Google AI API key
            model_name: Name of the Gemini model to use
        """
        self.api_key = api_key
        self.model_name = model_name
        genai.configure(api_key=self.api_key)
        self.model = genai.GenerativeModel(self.model_name)

    def generate_response(self, prompt: str, max_tokens: int = 1000, temperature: float = 0.7) -> str:
        """
        Generate a response from the Gemini API.

        Args:
            prompt: The user prompt to generate a response for
            max_tokens: Maximum number of tokens in the response
            temperature: Controls randomness in the response (0.0 to 1.0)

        Returns:
            The generated response text

        Raises:
            Exception: If API call fails
        """
        try:
            generation_config = genai.types.GenerationConfig(
                max_output_tokens=max_tokens,
                temperature=temperature,
            )

            response = self.model.generate_content(
                prompt,
                generation_config=generation_config
            )

            if response.text:
                return response.text.strip()
            else:
                raise Exception("Empty response from Gemini API")

        except Exception as e:
            error_msg = f"Gemini API error: {str(e)}"
            logger.error(error_msg)

            # Handle specific API errors
            if "quota" in str(e).lower() or "rate limit" in str(e).lower():
                raise Exception("API rate limit exceeded. Please try again later.")
            elif "invalid" in str(e).lower() and "key" in str(e).lower():
                raise Exception("Invalid API key. Please check your GOOGLE_AI_API_KEY in .env file.")
            elif "permission" in str(e).lower() or "unauthorized" in str(e).lower():
                raise Exception("API access denied. Please check your API key permissions.")
            else:
                raise Exception(f"Failed to generate response: {str(e)}")