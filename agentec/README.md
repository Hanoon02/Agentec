# Agentec

Generate Markdown-based agent tasks from NLP prompts with optional OpenAI enhancement.

## Installation

```bash
pip install agentec
```

## Usage

### Basic Usage
```bash
agentec "Summarize product reviews"
```

### With OpenAI Enhancement
Set your OpenAI API key for enhanced task descriptions:

```bash
export OPENAI_API_KEY="your-api-key-here"
agentec "Create a data analysis pipeline"
```

Or add it to a `.env` file in your current directory:
```
OPENAI_API_KEY=your-api-key-here
```

## Features

- **Generate structured task files** from natural language prompts
- **Optional OpenAI integration** for enhanced, detailed task descriptions
- **Saves tasks in Markdown format** in your current directory under `tasks/`
- **Cross-platform compatibility** - works on Windows, macOS, and Linux
- **Simple CLI interface** - just provide your prompt and go

## Example Output

### Basic Task (without OpenAI)
```markdown
# Task: summarize_product_reviews

## Prompt
Summarize product reviews
```

### Enhanced Task (with OpenAI)
```markdown
# Task: summarize_product_reviews

## Prompt
Summarize product reviews

## Enhanced Task Description
### Overview
This task involves analyzing and summarizing product reviews to extract key insights...

### Objectives
- Extract key themes from customer feedback
- Identify common complaints and praise
- Provide actionable insights for product improvement

### Steps/Requirements
1. Collect product reviews from various sources
2. Clean and preprocess the review data
3. Apply sentiment analysis
...
```

## Requirements

- Python 3.7+
- Optional: OpenAI API key for enhanced task generation

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Author

Ahmed Hanoon - [ahmedhanoon02@gmail.com](mailto:ahmedhanoon02@gmail.com)
