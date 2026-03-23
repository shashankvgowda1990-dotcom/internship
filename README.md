# Python CLI Projects Collection

A professional, well-structured collection of 8 beginner-friendly Python Command Line Interface (CLI) applications. This project is designed to showcase clean code, modular architecture, error handling, and terminal styling using Python best practices.

## 🚀 Features

This single comprehensive project includes the following 8 applications, all accessible from a central interactive menu:

1. **🧮 Simple Calculator**: Basic arithmetic operations with division-by-zero handling.
2. **🎲 Number Guessing Game**: Fun mini-game with retry logic and hints.
3. **📖 Contact Book**: CRUD operations for contacts, saving data persistently to a `contacts.json` file.
4. **📁 File Renaming Automation**: Bulk renamer to add prefixes to files in a given directory safely.
5. **🔒 Password Strength Checker**: Uses Regular Expressions (Regex) to validate password length, case, numbers, and special characters.
6. **📥 YouTube Video Downloader**: Downloads videos reliably using `yt-dlp` with link validation.
7. **⛅ Weather App**: Real-time weather data fetching via the OpenWeather API, including comprehensive error handling for network limits and 404s.
8. **🤖 Simple Rule-Based Chatbot**: A regex-driven conversational agent that responds to greetings, queries about time/date, and even tells jokes.

## 🏗️ Project Structure

The codebase is organized modularly to keep concerns separated:

```text
python_cli_projects/
│
├── src/
│   ├── apps/                   # Individual application modules
│   │   ├── calculator.py
│   │   ├── chatbot.py
│   │   ├── contact_book.py
│   │   ├── file_renamer.py
│   │   ├── number_guessing.py
│   │   ├── password_checker.py
│   │   ├── weather_app.py
│   │   └── yt_downloader.py
│   └── utils/                  # Shared utilities
│       ├── console.py          # Colored output formatting tools
│       └── logger.py           # Standardized application logging
│
├── main.py                     # Main entry point and interactive menu
├── requirements.txt            # Project dependencies
└── README.md                   # This documentation
```

## 🛠️ Installation Requirements

**Prerequisites**: Python 3.8+ is recommended.

1. **Clone the repository** (or download the files).
2. **Navigate to the project directory**:
   ```bash
   cd python_cli_projects
   ```
3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
   > **Note**: This will install libraries like `colorama` (for colored terminal output), `requests` (for the weather API), and `yt-dlp` (for YouTube downloads).

## ⚙️ Configuration

### Weather API Key
To use the **Weather App (Option 7)**, you will need a free API key from [OpenWeatherMap](https://openweathermap.org/api).
You can provide it in two ways:
- Set it as an environment variable before running:
  - Windows: `set OPENWEATHER_API_KEY=your_api_key_here`
  - Linux/Mac: `export OPENWEATHER_API_KEY="your_api_key_here"`
- Or, simply run the app and it will prompt you to enter the key dynamically if it's missing.

## ▶️ Usage

Run the central entry point:

```bash
python main.py
```

You will be greeted with a colorful, interactive menu. Type the number corresponding to the tool you wish to run and press Enter. 

Logs are automatically generated in the `logs/` directory for debugging purposes should any unexpected errors arise.
