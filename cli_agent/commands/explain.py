# Explain Command Module
# Implements code explanation functionality

from cli_agent.commands.base import BaseCommand


class ExplainCommand(BaseCommand):
    """Command for explaining code or programming concepts."""

    def prepare_prompt(self, prompt: str) -> str:
        """
        Prepare a specialized prompt for code explanation.

        Args:
            prompt: The user-provided prompt containing code or concept to explain

        Returns:
            The prepared prompt string optimized for code explanation
        """
        return f"""Explain the following code or programming concept in a clear, detailed manner. Break down complex parts and provide context.

Request: {prompt}

Please include:
- Step-by-step explanation of what the code does
- Key concepts and principles being used
- Any important patterns or best practices demonstrated
- Potential improvements or considerations
- Examples if helpful for clarification

Focus on being educational and thorough in your explanation."""