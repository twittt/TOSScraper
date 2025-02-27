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

2. Launch Backend Server:
    ```sh
    cd backend
    python -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    python app.py
    ```
3. Launch Frontend Web App:
    ```sh
    cd frontend
    npm install or npm i
    npm run start
    ```

## Usage

1. Open a web browser and go to `http://localhost:3000/`.
2. Enter the URL of an e-commerce website in the input field.
3. Click "Find Terms of Service" to analyze the terms of service.
4. The tool will display whether web scraping is mentioned in the terms of service, turn the result text red if it is mentioned, green if not, and show the relevant paragraphs.


## Note

I run on a M1 Mac so setup instructions may vary by machine.

## Demo

https://github.com/user-attachments/assets/4784be94-bdf5-40ca-8fa9-6f8c2c26a105

## A Little More About my Thought Process

To build this I started by asking Github Copilot what the common slugs for terms of service and terms of use are. It gave me a few and I asked it to build a crawler for those and search for keywords to indicate that scraping was prohibited. 

From there, I tested it on a few of my favorite online stores and found that the terms were often nested under other pages. I expanded the pages and keywords to include addiotnal common findings. Then I spent awhile shopping accidentally... oops...

Then I tried some big stores like Amazon or Etsy. These stores have TONS of pages and their terms are almost intentionally hiding. I couldn't find a logical rule for where they were, so I thought what if I just crawl the whole site, ya know? This takes forever, and while I developed a working implementation, the improvement didn't feel worth it for the compute and time cost. If this was going to be a real product, maybe performing such a crawl would be an improvement to consider. For now, it works with most of the regular ecommerce stores I tested. 

Then, it was on to the frontend. I developed a simple react app and then got slapped with timeouts for http requests. I decided to work around this with web sockets which took me longer than I'd like to admit to get working. I made GH Copilot write most of the CSS because *I hate it*. 

I made a few improvements like returning the found page if there was one, allowing a user to reset, returning paragraphs that mentioned crawling, etc. I also added a favicon because I'm annoying. 

## Room For Improvments
* I didn't do absolutely anything to strip the existing path on the backend, this could definitely get annoying when copying and pasting in URLs so I would love to add it at some point
* There are definitely more common page patterns to be added
* As mentioned above, we could always scrape the entire website to find the Ts & Cs, while understanding that the lag could be a lot longer
* Right now the pages get tested one after the other, multithreading could increase processing speed immensly


