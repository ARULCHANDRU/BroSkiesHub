# scraper.py
import requests
from bs4 import BeautifulSoup

def scrape_bbc_news_headlines():
    """
    Scrapes the top headlines from the BBC News website and saves them to a file.
    """
    # URL of the website we want to scrape
    URL = "https://www.bbc.com/news"
    
    # A User-Agent header makes our request look like it's coming from a real browser.
    # This can help avoid being blocked by some websites.
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    print("Fetching headlines from BBC News...")

    try:
        # Step 1: Use requests to fetch the HTML content of the page
        response = requests.get(URL, headers=headers)
        
        # Check if the request was successful (HTTP status code 200)
        response.raise_for_status() 

        # Step 2: Use BeautifulSoup to parse the HTML
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find all h2 tags, as headlines on BBC are often in <h2> elements.
        # Note: Website structures change! If this doesn't work, we might need to inspect the page
        # and find the correct tag or class for headlines.
        headlines_tags = soup.find_all('h2')
        
        headlines = []
        for tag in headlines_tags:
            # .text gets the clean text content of the tag, removing HTML.
            headline_text = tag.text.strip()
            if headline_text: # Ensure we don't add empty headlines
                headlines.append(headline_text)

        if not headlines:
            print("Could not find any headlines. The website structure might have changed.")
            return

        # Step 3: Save the titles in a .txt file
        with open("headlines.txt", "w", encoding="utf-8") as file:
            file.write("Top Headlines from BBC News:\n")
            file.write("="*30 + "\n")
            for idx, title in enumerate(headlines, 1):
                file.write(f"{idx}. {title}\n")

        print("Successfully saved headlines to headlines.txt")

    except requests.exceptions.RequestException as e:
        print(f"An error occurred while fetching the URL: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Run the scraper function
if __name__ == "__main__":
    scrape_bbc_news_headlines()