import requests

urls = [
    "https://www.google.com",
    "https://www.github.com",
    "https://www.spideronsite.com" 
]

def check_website_status(url):
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            return f"Website {url} is UP."
        else:
            return f"Website {url} is DOWN. Status code: {response.status_code}"
    except requests.exceptions.RequestException as e:
        return f"Website {url} is DOWN. Error: {e}"
    
def monitor_websites(urls):
    for url in urls:
        print(check_website_status(url))

if __name__ == "__main__":
    monitor_websites(urls)
