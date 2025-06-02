"""
Agentec - Generate Markdown-based agent tasks from NLP prompts with optional OpenAI enhancement.
"""

__version__ = "0.1.0"
__author__ = "Ahmed Hanoon"
__email__ = "ahmedhanoon02@gmail.com"

from .core import TaskSpec, OpenAI

__all__ = ["TaskSpec", "OpenAI"]
