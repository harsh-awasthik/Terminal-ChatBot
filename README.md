# Terminal-ChatBot

A simple, yet powerful terminal-based chatbot powered by Google's Gemini API. This script uses the `rich` library to create a beautiful and user-friendly command-line interface.

## Features

- **Interactive Chat:** Have a continuous conversation with the Gemini model.
- **Image Generation:** Create images from a text prompt.
- **Rich UI:** Enjoy a clean and colorful interface right in your terminal.

## Setup

1.  **API Key**
    You'll need a Google AI API key. You can get one for free from Google AI Studio.
    Create a file named `.env` in the same directory as `chat.py` and add your key like this:
    ```.env
    GOOGLE_API_KEY="YOUR_API_KEY_HERE"
    ```

2.  **Dependencies**
    Make sure you have Python installed. Then, install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

## How to Run

1.  Execute the script from your terminal:
    ```bash
    python3 chat.py
    ```
2.  When prompted, select a mode: `1` for a chat session, or `2` to generate an image.
3.  To exit the chat, simply type `exit` or `quit`.
