# Web Scraping Terms of Service Checker

This tool allows users to input the URL of an e-commerce website and check whether the website's terms of service prohibit web scraping. The tool searches for terms of service documents in various common slugs and provides feedback on whether web scraping is mentioned, including relevant paragraphs if found.

## Features

- Accepts a URL as input.
- Searches for terms of service in common slugs and nested paths.
- Analyzes the content for mentions of web scraping.
- Provides feedback on whether web scraping is mentioned and highlights relevant paragraphs.
- Produces a link to a TOS page if found.

## Installation and Setup

Follow these steps to install and run the application:

### Prerequisites

- Python 3.x
- pip (Python package installer)
- Flask

### Steps

1. Clone the repository:
    ```sh
    git clone https://github.com/twittt/TOSScraper.git
    cd TOSScraper
    ```

2. Run the setup script to install the dependencies and start the server:
    ```sh
    ./setup.sh
    ```

### Launch Backend Server

The `setup.sh` script installs the required Python packages and starts the Flask server.

```sh
#!/bin/bash

cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py
```

### Launch Frontend Web App

```sh
#!/bin/bash

cd frontend
npm install or npm i
npm run start
```


## Usage

1. Open a web browser and go to `http://127.0.0.1:5000/`.
2. Enter the URL of an e-commerce website in the input field.
3. Click "Find Terms of Service" to analyze the terms of service.
4. The tool will display whether web scraping is mentioned in the terms of service, turn the result text red if it is mentioned, green if not, and show the relevant paragraphs.
