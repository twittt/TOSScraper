from flask import Flask, request
from flask_socketio import SocketIO, emit
import requests
from bs4 import BeautifulSoup
import re

app = Flask(__name__)
app.config["SECRET_KEY"] = "aFYHJ9]7C$=v"
socketio = SocketIO(app, cors_allowed_origins="*")


@app.route("/")
def home():
    return "Checker is running!"

@socketio.on("check")
def handleNumber(url):
    print("Number received from Number:", url)

    if not url.startswith("http"):
        url = "http://" + url  # Add the scheme if not provided

    prohibited, mentions, found_page = check_scraping_prohibition(url)

    data = {
        'prohibited': prohibited,
        'mentions': mentions,
        'found_page': found_page
    }
    emit("result", data)

# Words to search for on TOS
SCRAPING_KEYWORDS = [
    "scraping",
    "crawl",
    "crawler",
    "scrape",
    "spider",
    "automated",
    "bot",
    "robot",
    "data extraction",
    "harvesting",
    "monitoring"
]

# Common slugs where ToS might be located
TOS_SLUGS = [
    "/term",
    "/terms",
    "/terms-of-use",
    "/terms-of-service",
    "/terms-and-conditions",
    "/tos",
    "/legal/terms",
    "/legal/terms-of-use",
    "/legal/terms-of-service",
    "/legal/terms-and-conditions",
    "/info/terms",
    "/info/terms-of-service",
    "/about/terms",
    "/about/terms-of-service",
    "/pages/terms",
    "/pages/terms-of-use",
    "/pages/terms-of-service",
    "/pages/terms-and-conditions",
    "/acceptable-use-policy",
    "/usage-policy",
    "/access-policy",
]

def fetch_tos_page(base_url):
    """
    Fetch the terms of service page from possible slugs.
    """
    for slug in TOS_SLUGS:
        try:
            url = base_url.rstrip('/') + slug
            print(f"Checking {url}")
            response = requests.get(url)
            response.raise_for_status()
            return response.text, url
        except requests.RequestException:
            print(f"Page doesn't exist")
            continue
    return None, None

def parse_tos_for_scraping(tos_content):
    """
    Parse the ToS content to check for keywords related to web scraping.
    """
    soup = BeautifulSoup(tos_content, 'html.parser')
    text = soup.get_text().lower()
    
    scraping_mentions = []
    paragraphs = soup.find_all(['p', 'li', 'div'])
    for paragraph in paragraphs:
        paragraph_text = paragraph.get_text().lower()
        for keyword in SCRAPING_KEYWORDS:
            if re.search(r'\b' + re.escape(keyword) + r'\b', paragraph_text):
                scraping_mentions.append(paragraph.get_text())
                break
    
    return scraping_mentions

def check_scraping_prohibition(base_url):
    """
    Check if the given URL's terms of service prohibit web scraping.
    """
    tos_content, found_page = fetch_tos_page(base_url)
    
    if tos_content:
        scraping_mentions = parse_tos_for_scraping(tos_content)
        if scraping_mentions:
            return True, scraping_mentions, found_page
        else:
            return False, ["Found Terms, No Mention of Scraping Prohibition"], found_page
    else:
        return False, ["Could Not Find Terms of Use Page"], None

if __name__ == "__main__":
    socketio.run(app, debug=True)
