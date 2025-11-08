# Core Agent Module
# Implements AI agent core functionality with Gemini API integration

import logging
from cli_agent.utils.config import load_config
from cli_agent.core.gemini_client import GeminiClient
from cli_agent.commands import GenerateCommand, ExplainCommand, AskCommand

logger = logging.getLogger(__name__)

class AICodingAgent:
    def __init__(self):
        """
        Initialize the AI coding agent with Gemini API client and command handlers.
        """
        try:
            config = load_config()
            self.api_client = GeminiClient(
                api_key=config['google_ai_api_key'],
                model_name="gemini-1.5-flash"
            )
            self.max_tokens = config['max_tokens']

            # Initialize command handlers
            self.commands = {
                'generate': GenerateCommand(),
                'explain': ExplainCommand(),
                'ask': AskCommand()
            }

            logger.info("AICodingAgent initialized successfully")
        except Exception as e:
            logger.error(f"Failed to initialize AICodingAgent: {str(e)}")
            raise

    def process_request(self, subcommand: str, prompt: str) -> str:
        """
        Process a user request using the appropriate command handler.

        Args:
            subcommand: The subcommand type ('generate', 'explain', 'ask')
            prompt: The user-provided prompt

        Returns:
            AI-generated response string

        Raises:
            Exception: If API call fails or other errors occur
        """
        try:
            logger.info(f"Processing {subcommand} request: {prompt[:100]}...")

            # Get the appropriate command handler
            if subcommand not in self.commands:
                raise ValueError(f"Unknown subcommand: {subcommand}")

            command = self.commands[subcommand]

            # Prepare the specialized prompt
            prepared_prompt = command.prepare_prompt(prompt)

            # Generate response using Gemini API
            response = self.api_client.generate_response(
                prompt=prepared_prompt,
                max_tokens=self.max_tokens,
                temperature=0.7
            )

            logger.info("Successfully generated response")
            return response

        except Exception as e:
            error_msg = f"Failed to process request: {str(e)}"
            logger.error(error_msg)

            # Re-raise with more specific error handling if needed
            # The GeminiClient already handles specific API errors
            raise