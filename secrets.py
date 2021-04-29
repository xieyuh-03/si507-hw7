import requests

api_key = '5JUwYxpVEUrd8v5oBknSIPHZO57wXrrJ'


url = f'https://api.nytimes.com/svc/topstories/v2/technology.json?api-key={api_key}'
    
results = requests.get(url).json()

headlines = []
i = 1
for item in results['results']:
    if i < 6:
        title = item['title']
        headlines.append(title)
        i += 1


print(headlines)