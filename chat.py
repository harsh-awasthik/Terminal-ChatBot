from dotenv import load_dotenv
from pyfiglet import figlet_format
from rich.console import Console
from rich.markdown import Markdown
from rich.panel import Panel
from rich.prompt import Prompt
from PIL import Image
from io import BytesIO
from textwrap import dedent
from google import genai
from google.genai import types
console = Console()
load_dotenv()

CHATBOT_NAME = "ChatBot"
SYSTEM_INSTRUCTION = "You are a helpful ChatBot."


def main():
    # Load environment variables and set up console
    
    console.print(figlet_format(CHATBOT_NAME, font="univers"))
    with console.status("[bold green] Loading Model..."):
        # Initialize client
        client = genai.Client()

    # Menu
    while True:
        bot("""
        What do you want to do:
        1. Just Chat.
        2. Generate Image.

        _Select 1 or 2_
        """)
        opt = Prompt.ask("[bold red]Select Option[/]")

        if opt.strip() in ("1", "2"):
            break
        bot("*Hey Man! Please select either 1 or 2.*")

    # Chat Mode
    if opt == "1":
        bot("# Chat")
        chat = client.chats.create(
            model="gemini-2.5-flash",
            config=types.GenerateContentConfig(system_instruction=SYSTEM_INSTRUCTION),
        )

        while True:
            try:
                query = user_input()
                if query.lower() in ("exit", "quit"):
                    bot("Goodbye! 👋")
                    break

                with console.status("[bold green]Thinking..."):
                    response = chat.send_message(query)
                bot(response.text)

            except KeyboardInterrupt:
                bot("Goodbye! 👋")
                break

    # Image Generation Mode
    else:
        bot("# Genearate Image")
        query = user_input()
        if query.lower() in ("exit", "quit"):
            bot("Goodbye! 👋")
        else:
            with console.status("[bold green]Generating..."):
                response = client.models.generate_content(
                    model="gemini-2.0-flash-preview-image-generation",
                    contents=query,
                    config=types.GenerateContentConfig(response_modalities=['TEXT', 'IMAGE'])
                )

            for part in response.candidates[0].content.parts:
                if part.text:
                    bot(part.text)
                elif part.inline_data:
                    try:
                        image = Image.open(BytesIO(part.inline_data.data))
                        image.save('gemini-native-image.png')
                        image.show()
                    except Exception as e:
                        bot(f"Failed to render image: {e}")

# Bot display function
def bot(msg):
    console.print(Panel(Markdown(dedent(msg)), title="🤖"))

# User input function
def user_input():
    return Prompt.ask("[bold cyan]👤 Prompt[/]")

if __name__ == "__main__":
    main()