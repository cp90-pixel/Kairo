# Ask Command Module
# Implements general question answering functionality

from cli_agent.commands.base import BaseCommand


class AskCommand(BaseCommand):
    """Command for answering general coding questions."""

    def prepare_prompt(self, prompt: str) -> str:
        """
        Prepare a specialized prompt for general coding questions.

        Args:
            prompt: The user-provided question

        Returns:
            The prepared prompt string optimized for general coding questions
        """
        return f"""Answer the following coding-related question comprehensively and accurately.

Question: {prompt}

Please provide:
- Clear, direct answer to the question
- Relevant examples or code snippets when applicable
- Additional context or related information that might be helpful
- Best practices or recommendations where appropriate

Be thorough but concise, and focus on practical, actionable information."""