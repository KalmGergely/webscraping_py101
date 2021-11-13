import requests
import bs4

keyword = 'facebook'
last_page = 10
pages = tuple(range(1,last_page+1))

for page in pages:
    url = f'https://www.economist.com/search?q={keyword}&page={page}'
    res = requests.get(url)
    html = bs4.BeautifulSoup(res.text, features="html.parser")
    ol = html.find('ol', {'id': 'search-results'})
    for article in ol.children:
        title = article.find('span', {'class': '_headline'}).get_text
        link = article.find('a', {'class': '_search-result'}).attrs['href']
        description = article.find('p', {'class': '_snippet'}).get_text()
        result = {'title': title, 'url': link, 'description': description}
        print(result)
        print('##')
    print('-------------------------------------')