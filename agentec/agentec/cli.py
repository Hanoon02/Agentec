# agentec/cli.py

import os
import typer
from agentec.core import TaskSpec, OpenAI
from dotenv import load_dotenv


def generate_task(
    prompt: str = typer.Argument(
        ..., help="The natural-language prompt to convert into a Markdown task file."
    )
):
    """
    Take a free‐form NLP prompt and write a `tasks/{name}.md` for it.
    """
    # Check for OpenAI API key
    load_dotenv()
    api_key = os.getenv("OPENAI_API_KEY")

    enhanced_content = None

    if not api_key:
        typer.echo("🔑 You don't have OpenAI API key set.", err=True)
        typer.echo(
            "To set it, use: export OPENAI_API_KEY='your-api-key-here'", err=True
        )
        typer.echo(
            "You can also add it to a .env file in your current directory.", err=True
        )

        proceed = typer.confirm("Do you want to proceed without OpenAI integration?")
        if not proceed:
            typer.echo("❌ Exiting. Please set your OpenAI API key and try again.")
            raise typer.Exit(1)

        typer.echo("⚠️  Proceeding without OpenAI integration...")
    else:
        # Use OpenAI to enhance the prompt
        typer.echo("🤖 Enhancing task with OpenAI...")
        try:
            openai_client = OpenAI()
            enhancement_prompt = f"""
            Take this user prompt and create a detailed, structured task description in Markdown format.
            Include sections like:
            - Overview
            - Objectives
            - Steps/Requirements
            - Deliverables
            - Success Criteria (if applicable)
            
            User prompt: "{prompt}"
            
            Provide a comprehensive task breakdown that would help someone understand and execute this task effectively.
            """

            response = openai_client.query(enhancement_prompt)

            if "error" not in response and "choices" in response:
                enhanced_content = response["choices"][0]["message"]["content"]
                typer.echo("✨ Task enhanced with AI!")
            else:
                typer.echo(
                    "⚠️  Could not enhance task with AI, proceeding with basic version..."
                )

        except Exception as e:
            typer.echo(f"⚠️  Error using OpenAI: {str(e)}")
            typer.echo("Proceeding with basic version...")

    # Turn the prompt into a filesystem‐safe name (snake_case, max 30 chars).
    name = prompt.lower().replace(" ", "_")[:30]
    task = TaskSpec(name=name, prompt=prompt, enhanced_content=enhanced_content)
    saved_path = task.save()
    typer.echo(f"✅ Saved: {saved_path}")


def main():
    typer.run(generate_task)


if __name__ == "__main__":
    main()
