# agentec/core.py

import os
import requests
from typing import Dict, Any
from dotenv import load_dotenv


class OpenAI:
    """Class to handle interactions with the OpenAI API"""

    def __init__(self):
        """Initialize the OpenAI API client"""
        load_dotenv()
        self.api_key = os.getenv("OPENAI_API_KEY")

        if not self.api_key:
            raise ValueError("OPENAI_API_KEY not found in environment variables")

        self.base_url = "https://api.openai.com/v1/chat/completions"
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
        }
        self.model = "gpt-4o-mini"

    def query(self, question: str) -> Dict[str, Any]:
        """Query the OpenAI API for a question using chat completions"""
        try:
            payload = {
                "model": self.model,
                "messages": [{"role": "user", "content": question}],
            }

            response = requests.post(
                self.base_url, headers=self.headers, json=payload, timeout=30
            )

            if response.status_code == 200:
                return response.json()
            else:
                print(f"Error querying OpenAI API: {response.status_code}")
                return {"error": f"API Error: {response.status_code}"}

        except Exception as e:
            print(f"Error querying question: {question}")
            print(f"Error details: {str(e)}")
            return {"error": str(e)}


class TaskSpec:
    def __init__(self, name: str, prompt: str, enhanced_content: str = None):
        self.name = name
        self.prompt = prompt
        self.enhanced_content = enhanced_content

    def to_markdown(self) -> str:
        markdown = f"# Task: {self.name}\n\n## Prompt\n{self.prompt}\n"

        if self.enhanced_content:
            markdown += f"\n## Enhanced Task Description\n{self.enhanced_content}\n"

        return markdown

    def save(self, base_dir: str = None):
        # Use current working directory if no base_dir specified
        if base_dir is None:
            base_dir = os.getcwd()

        tasks_dir = os.path.join(base_dir, "tasks")
        os.makedirs(tasks_dir, exist_ok=True)

        path = os.path.join(tasks_dir, f"{self.name}.md")
        with open(path, "w") as f:
            f.write(self.to_markdown())

        return path
