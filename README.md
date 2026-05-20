# Notes TG

A lightweight, efficient Telegram bot designed to manage personal notes directly through the Telegram interface.

## Description
Notes TG is a self-hosted Telegram bot that allows users to create, view, and organize notes. By leveraging the Telegram API, it provides a seamless mobile-first experience for capturing quick thoughts, to-do items, or snippets of information without leaving your messaging app.

## Features
*   **Quick Capture:** Save text notes instantly via chat.
*   **Persistent Storage:** Notes are stored securely in a local database.
*   **Simple Retrieval:** Easily list and view your existing notes.
*   **Minimalist:** Focused functionality with low resource overhead.
*   **Self-Hosted:** Full control over your data.

## Installation

### Prerequisites
*   Python 3.9+
*   A Telegram Bot Token (obtainable via [@BotFather](https://t.me/botfather))

### Setup
1.  **Clone the repository:**
    ```bash
    git clone https://github.com/maksymrusanov/notes_tg.git
    cd notes_tg
    ```

2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Configure environment variables:**
    Create a `.env` file in the root directory and add your credentials:
    ```env
    BOT_TOKEN=your_telegram_bot_token_here
    ```

4.  **Run the bot:**
    ```bash
    python main.py
    ```

## Usage
Once the bot is running, start a chat with it on Telegram:
*   **`/start`**: Initialize the bot.

## Contributing
Contributions are welcome! If you would like to improve the bot, please follow these steps:
1.  Fork the repository.
2.  Create a feature branch (`git checkout -b feature/AmazingFeature`).
3.  Commit your changes (`git commit -m 'Add some AmazingFeature'`).
4.  Push to the branch (`git push origin feature/AmazingFeature`).
5.  Open a Pull Request.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
