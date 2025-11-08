# CLI AI Coding Agent

A command-line interface tool that leverages Google's Gemini AI to assist with code generation, explanation, and general coding questions.

## Features

- **Code Generation**: Generate code snippets based on natural language prompts
- **Code Explanation**: Get detailed explanations of code or programming concepts
- **General Q&A**: Ask coding-related questions and get comprehensive answers
- **Rich Output**: Beautifully formatted output with syntax highlighting (when Rich library is available)
- **Multiple Languages**: Support for Python, JavaScript, Java, SQL, HTML, C++, and more

## Installation

### Prerequisites

- Python 3.8+
- Google AI API key (get one from [Google AI Studio](https://makersuite.google.com/app/apikey))

### Install from Source

1. Clone the repository:
```bash
git clone <repository-url>
cd kairo
```

2. Create a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install the package:
```bash
pip install -e .
```

4. Set up your API key:
```bash
echo "GOOGLE_AI_API_KEY=your_api_key_here" > .env
```

## Usage

### Basic Commands

```bash
# Generate code
cli-agent generate "Write a Python function to calculate factorial"

# Explain code
cli-agent explain "def factorial(n): return 1 if n <= 1 else n * factorial(n-1)"

# Ask questions
cli-agent ask "What is recursion in programming?"
```

### Command Options

Each subcommand supports both positional arguments and the `--prompt` option:

```bash
cli-agent generate --prompt "Write a hello world in JavaScript"
cli-agent explain "What does this regex do: \d{3}-\d{2}-\d{4}"
```

### Help

```bash
cli-agent --help
cli-agent generate --help
```

## Configuration

The application uses the following environment variables (configured via `.env` file):

- `GOOGLE_AI_API_KEY`: Your Google AI API key (required)
- `LOG_LEVEL`: Logging level (default: INFO)
- `MAX_TOKENS`: Maximum tokens for API responses (default: 1000)

## Error Handling

The application provides clear error messages for common issues:

- **Missing API Key**: Prompts to set `GOOGLE_AI_API_KEY` in `.env`
- **Invalid API Key**: Indicates API key validation failure
- **Network Issues**: Handles connection problems gracefully
- **Invalid Commands**: Shows proper usage information

## Dependencies

- `google-genai`: Google Gemini AI API client
- `rich`: Enhanced terminal output (optional, falls back to plain text)
- `python-dotenv`: Environment variable management

## Development

### Project Structure

```
cli_agent/
├── cli/
│   └── main.py          # CLI interface and output formatting
├── core/
│   ├── agent.py         # Main agent orchestration
│   └── gemini_client.py # Gemini API client
├── commands/
│   ├── base.py          # Command base class
│   ├── generate.py      # Code generation command
│   ├── explain.py       # Code explanation command
│   └── ask.py           # General Q&A command
├── utils/
│   └── config.py        # Configuration management
└── __main__.py          # Entry point
```

### Testing

Run the application with various inputs to test functionality:

```bash
# Test error handling
cli-agent generate  # No prompt provided
cli-agent invalid   # Invalid command

# Test with different languages
cli-agent generate "Write a Java class for a Person"
cli-agent generate "Create an HTML form"
cli-agent generate "Write a SQL query to find users"
```

## License

See LICENSE file for details.