# notes_tg

A Telegram bot designed for personal note-taking and management directly within the messaging app.

## Description
`notes_tg` is a lightweight Telegram bot that allows users to capture, store, and manage notes through a chat interface. It acts as a personal productivity assistant, enabling quick text-based note creation without leaving Telegram.

## Tech Stack
*   **Language:** Python 3.x
*   **API Framework:** `aiogram` (Asynchronous Telegram Bot API wrapper)
*   **Database:** `Postgres` (Asynchronous interface for SQLite)

## Features
*   **Asynchronous Processing:** Built with `aiogram` for high-performance, non-blocking operations.
*   **Persistent Storage:** Utilizes SQLite for reliable note persistence.
*   **Note Management:** Capability to add and store text notes via chat commands.
*   **Async Database Integration:** Uses `aiosqlite` to ensure the bot remains responsive during database I/O operations.

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/maksymrusanov/notes_tg.git
   cd notes_tg
   ```

2. **Create a virtual environment (recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Configure Environment Variables:** Create a `.env` file in the root directory (see *Environment Variables* section).
2. **Run the bot:**
   ```bash
   python main.py
   ```
3. **Interact:** Open your Telegram bot and send '/start' message to trigger the command handlers defined in the source code.

## Environment Variables
The application requires the following environment variables. Ensure these are defined in a `.env` file:

* `API_TOKEN`: Your Telegram Bot API token obtained from [@BotFather](https://t.me/botfather).

## Project Structure
* `main.py`: Entry point of the application; initializes the bot and dispatcher.
* `db.py`: Contains database connection logic and schema management.
* `handlers.py`: Contains the command handlers and message processing logic.
* `requirements.txt`: Project dependencies.

## Contributing
Contributions are welcome. Please fork the repository, create a feature branch, and submit a pull request for any enhancements or bug fixes.

## License
This project is open-source. Please check the repository for the specific license file.
