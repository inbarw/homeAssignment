# Selenium Python Assignement 

## Introduction
This project contains automated tests for a web application using Selenium WebDriver with Python and pytest. It includes both UI tests and API tests, organized in a structured manner for ease of maintenance and scalability.

## Getting Started

### Prerequisites
- Python 3.x
- pip (Python package installer)
- Chrome browser
- ChromeDriver

### Install Dependencies
1. Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

2. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

### Configuring WebDriver
Download the ChromeDriver that matches your Chrome browser version from
(https://sites.google.com/a/chromium.org/chromedriver/downloads) and place it in a directory included in your system's PATH.

## Running Tests
### Run All Tests
To run all tests, execute:
```bash
pytest

