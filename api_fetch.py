import requests
API_KEY = '8d8b5c6be6974ed290d65ab2779ccca7'
url = 'https://newsapi.org/v2/top-headlines'
def fetch_headlines(country="us", category="general", pageSize=10):
    params={'country':country, 'category':category, 'pageSize':pageSize, 'apiKey':API_KEY}
    try:
        response=requests.get(url, params=params)
        response.raise_for_status()
        return  [article['title'] for article in response.json().get('articles', [])]
    except requests.exceptions.RequestException:
         print(f"Error fetching headlines: {e}")

def display_headlines(headlines):
    if headlines:
        print("Top Headlines:")
        for i, headline in enumerate(headlines, 1):
            print(f"{i}. {headline}")
    else:
        print("No headlines available.")

headlines = fetch_headlines('us', 'technology')
display_headlines(headlines)