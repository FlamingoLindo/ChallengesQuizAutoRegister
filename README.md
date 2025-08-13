# Quiz Automation Project

A Python project that automates quiz registration and management by reading quiz data from Excel files and interacting with a web-based quiz platform using Selenium.

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Project Structure](#project-structure)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Excel File Format](#excel-file-format)
- [Configuration](#configuration)
- [Contributing](#contributing)

## 🎯 Overview

This project automates the process of:

1. Reading quiz questions and answers from Excel files
2. Processing the data using pandas
3. Automatically registering quizzes on a web platform using Selenium WebDriver

## ✨ Features

- **Excel Processing**: Read and parse quiz data from Excel files (.xlsx format)
- **Data Validation**: Robust error handling for file reading and data extraction
- **Web Automation**: Automated login and quiz registration on web platforms
- **Modular Design**: Separated concerns with dedicated modules for different functionalities
- **Flexible Data Access**: Extract specific quiz questions by row index

## 📁 Project Structure

```bash
tedesafio/
├── main.py              # Main execution script
├── excel.py             # Excel file processing functions
├── automate.py          # Selenium web automation functions
├── example.xlsx         # Sample Excel file with quiz data
├── .venv/              # Virtual environment
└── README.md           # Project documentation
```

## 📦 Requirements

- Python 3.7+
- pandas
- selenium
- Chrome WebDriver

## 🚀 Installation

1. **Clone or download the project:**

   ```bash
   cd tedesafio
   ```

2. **Create and activate virtual environment:**

   ```bash
   python -m venv .venv
   .venv\Scripts\activate  # On Windows
   # source .venv/bin/activate  # On macOS/Linux
   ```

3. **Install required packages:**

   ```bash
   pip install pandas selenium
   ```

4. **Download Chrome WebDriver:**
   - Download ChromeDriver from [https://chromedriver.chromium.org/](https://chromedriver.chromium.org/)
   - Ensure it's in your system PATH or place it in the project directory

## 💻 Usage

### Basic Usage

1. **Prepare your Excel file** with quiz data (see format below)
2. **Update configuration** in `main.py` if needed
3. **Run the main script:**

   ```bash
   python main.py
   ```

### Using Individual Modules

#### Excel Processing

```python
from excel import get_dataframe, get_values_from_columns

# Load Excel file
df = get_dataframe('your_quiz_file.xlsx')

# Extract data from specific row
values = get_values_from_columns(df, row_index=0)
if values:
    pergunta, alt_a, alt_b, alt_c, alt_d, correta, dificuldade, pontos = values
```

#### Web Automation

```python
from automate import automate_quiz_registration

# Automate quiz registration
automate_quiz_registration(
    'https://your-quiz-platform.com/login',
    'your_email@example.com',
    'your_password',
    df  # DataFrame with quiz data
)
```

## 📊 Excel File Format

Your Excel file should have the following columns (in order):

| Column | Description |
|--------|-------------|
| PERGUNTA | The quiz question |
| ALTERNATIVA 1 | First answer option |
| ALTERNATIVA 2 | Second answer option |
| ALTERNATIVA 3 | Third answer option |
| ALTERNATIVA 4 | Fourth answer option |
| ALTERNATIVA CORRETA | Correct answer (a, b, c, or d) |
| NÍVEL DE DIFICULDADE | Difficulty level |
| QUANTIDADE DE PONTOS | Points for the question |

### Example Row

```bash
Question: "What is the capital of France?"
Alternative 1: "London"
Alternative 2: "Paris"
Alternative 3: "Berlin"
Alternative 4: "Madrid"
Correct Answer: "b"
Difficulty: "Medium"
Points: 100
```

## ⚙️ Configuration

### Main Configuration (`main.py`)

Update the following variables in `main.py`:

```python
# Excel file name
excel_file = 'your_quiz_file.xlsx'

# Web platform credentials
master_url = 'https://your-quiz-platform.com/login'
master_login = 'your_email@example.com'
master_password = 'your_password'
```

### Web Platform Settings

The automation is currently configured for:

- URL: `https://challenges-quiz-master.netlify.app/login-master`
- Email field: `name="email"`
- Password field: `name="password"`

Modify `automate.py` if your platform uses different selectors.

## 📝 Notes

- Ensure Chrome browser is installed and up to date
- The virtual environment (.venv) is included for dependency management
- Always test with sample data before running on production quiz files
- Web automation may need adjustments based on the target platform's structure

## 🐛 Troubleshooting

### Common Issues

1. **ChromeDriver not found**: Ensure ChromeDriver is in your PATH or project directory
2. **Excel file not loading**: Check file path and ensure the file is not open in Excel
3. **Web automation fails**: Verify the website structure hasn't changed and credentials are correct

### Error Handling

The project includes robust error handling for:

- File not found errors
- Invalid Excel formats
- Web element not found
- Network timeouts

---

**Project Type**: Data Processing & Web Automation  
**Language**: Python  
**Last Updated**: August 2025
