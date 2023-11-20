import requests
import bs4

url = 'http://quotes.toscrape.com'
response = requests.get(url)

bsText = bs4.BeautifulSoup(response.text, 'html.parser')

quotes = bsText.find_all('span', class_='text')

for i, quote in enumerate(quotes):
    print(f'Quote {i+1}: {quote.get_text()}')









# html_content = '<html><body><p>Hello world!</p></body></html>'
#
# text = bs4.BeautifulSoup(html_content, 'html.parser')
#
# text = text.find('p').get_text()
# print(text)

#
# url = 'https://google.com'
# response = requests.get(url)
#
# print(response.text)


# pip install beautifulsoup4
