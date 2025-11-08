# CLI Interface Module
# Implements CLI interface using argparse and rich for output

import argparse
import sys
try:
    from rich.console import Console
    from rich.panel import Panel
    from rich.syntax import Syntax
    RICH_AVAILABLE = True
except ImportError:
    RICH_AVAILABLE = False

from cli_agent.core.agent import AICodingAgent

if RICH_AVAILABLE:
    console = Console()
else:
    console = None

def display_output(title, content, style="bold blue"):
    """Display formatted output using rich if available, otherwise plain text."""
    if RICH_AVAILABLE:
        # Try to detect if content contains code and apply syntax highlighting
        if _contains_code(content):
            # Try to detect language from content for better syntax highlighting
            language = _detect_language(content)
            # Create a syntax-highlighted version
            syntax = Syntax(content, language, theme="monokai", line_numbers=False)
            panel = Panel.fit(syntax, title=title, border_style=style)
        else:
            panel = Panel.fit(content, title=title, border_style=style)
        console.print(panel)
    else:
        print(f"=== {title} ===")
        print(content)
        print("=" * (len(title) + 8))


def _detect_language(content: str) -> str:
    """Detect programming language from content for syntax highlighting."""
    content_lower = content.lower()

    # SQL indicators (check first as SQL keywords are distinctive)
    if any(indicator in content_lower for indicator in ['select ', 'insert ', 'update ', 'create table', 'where ', 'join ', ' from ', 'delete ']):
        return "sql"

    # Java indicators (check before Python as they might have 'public class')
    if any(indicator in content_lower for indicator in ['public class', 'system.out.println', 'import java', 'private ', 'protected ']):
        return "java"

    # Python indicators
    if any(indicator in content_lower for indicator in ['def ', 'import ', 'from ', 'class ', 'if __name__', 'print(', 'elif ', 'self.']):
        return "python"

    # JavaScript indicators
    if any(indicator in content_lower for indicator in ['function', 'const ', 'let ', 'var ', 'console.log', '=>', 'document.', 'window.']):
        return "javascript"

    # HTML indicators
    if any(indicator in content_lower for indicator in ['<!doctype', '<html>', '<div>', '<script>', '</', '<body>']):
        return "html"

    # C/C++ indicators
    if any(indicator in content_lower for indicator in ['#include', 'int main', 'printf(', 'std::cout']):
        return "cpp"

    # Default to python if we can't detect
    return "python"


def _contains_code(content: str) -> bool:
    """Simple heuristic to detect if content contains code."""
    code_indicators = [
        'def ', 'class ', 'import ', 'from ', 'if __name__',
        'function', 'const ', 'let ', 'var ', 'public class',
        'package ', '#include', '<?php', '<!DOCTYPE', '<html>',
        'SELECT ', 'INSERT ', 'UPDATE ', 'CREATE TABLE',
        '```', 'print(', 'console.log', 'System.out.println'
    ]
    content_lower = content.lower()
    return any(indicator.lower() in content_lower for indicator in code_indicators)

def main():
    parser = argparse.ArgumentParser(
        prog="cli-agent",
        description="CLI AI Coding Agent for code generation and assistance"
    )

    subparsers = parser.add_subparsers(dest="subcommand", help="Available subcommands")

    # Generate subcommand
    generate_parser = subparsers.add_parser("generate", help="Generate code based on a prompt")
    generate_parser.add_argument("prompt", nargs="?", help="The prompt for code generation")
    generate_parser.add_argument("--prompt", "-p", dest="prompt_option", help="Prompt via option")

    # Explain subcommand
    explain_parser = subparsers.add_parser("explain", help="Explain code or concepts")
    explain_parser.add_argument("prompt", nargs="?", help="The prompt for explanation")
    explain_parser.add_argument("--prompt", "-p", dest="prompt_option", help="Prompt via option")

    # Ask subcommand
    ask_parser = subparsers.add_parser("ask", help="Ask general questions")
    ask_parser.add_argument("prompt", nargs="?", help="The prompt for the question")
    ask_parser.add_argument("--prompt", "-p", dest="prompt_option", help="Prompt via option")

    args = parser.parse_args()

    if not args.subcommand:
        parser.print_help()
        return

    # Get prompt from positional or option
    prompt = args.prompt or getattr(args, 'prompt_option', None)
    if not prompt:
        if RICH_AVAILABLE:
            console.print("[red]Error: No prompt provided. Use positional argument or --prompt option.[/red]")
        else:
            print("Error: No prompt provided. Use positional argument or --prompt option.")
        return

    # Initialize agent and process request
    try:
        agent = AICodingAgent()
        response = agent.process_request(args.subcommand, prompt)
        display_output(f"{args.subcommand.capitalize()} Result", response)
    except ValueError as e:
        # Configuration errors (missing API key, etc.)
        display_output("Configuration Error", f"Please check your configuration: {str(e)}", "bold red")
    except Exception as e:
        # API errors, network issues, etc.
        display_output("Error", f"An error occurred: {str(e)}", "bold red")