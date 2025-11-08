# Base Command Module
# Defines base command class for AI coding agent commands

class BaseCommand:
    """Base class for all command types in the AI coding agent."""

    def prepare_prompt(self, prompt: str) -> str:
        """
        Prepare the prompt for the Gemini API based on the command type.

        Args:
            prompt: The user-provided prompt

        Returns:
            The prepared prompt string
        """
        raise NotImplementedError("Subclasses must implement prepare_prompt method")