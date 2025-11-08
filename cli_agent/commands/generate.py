# Generate Command Module
# Implements code generation functionality

from cli_agent.commands.base import BaseCommand


class GenerateCommand(BaseCommand):
    """Command for generating code based on user prompts."""

    def prepare_prompt(self, prompt: str) -> str:
        """
        Prepare a specialized prompt for code generation.

        Args:
            prompt: The user-provided prompt describing what code to generate

        Returns:
            The prepared prompt string optimized for code generation
        """
        return f"""Generate code based on the following request. Provide complete, working code with proper syntax and structure.

Request: {prompt}

Please include:
- Complete code implementation
- Appropriate comments and documentation
- Error handling where applicable
- Best practices for the specified language/framework

If no specific language is mentioned, assume Python unless the context suggests otherwise."""