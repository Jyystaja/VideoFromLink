import requests
from bs4 import BeautifulSoup

def get_iframe_src(url):
    try:
        # Mimic a real browser by setting headers
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
            "Accept-Language": "en-US,en;q=0.9",
            "Referer": url,  # Some sites check the referer
            "Connection": "keep-alive",
            "DNT": "1",  # Do Not Track header
            "Upgrade-Insecure-Requests": "1"
        }

        # Fetch the webpage
        response = requests.get(url, headers=headers, timeout=10)

        # Check if request was successful
        if response.status_code != 200:
            print(f"Failed to fetch the page. Status code: {response.status_code}")
            return None

        # Parse the HTML
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find the first iframe
        iframe = soup.find("iframe")
        if iframe:
            iframe_src = iframe.get("src")
            if iframe_src:
                print(f"Found iframe source: {iframe_src}")
                return iframe_src
            else:
                print("Iframe found, but no src attribute.")
        else:
            print("No iframe found on this page.")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching the page: {e}")

    return None

if __name__ == "__main__":
    url = input("Enter the URL to fetch: ")
    iframe_src = get_iframe_src(url)
