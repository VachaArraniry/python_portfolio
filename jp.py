import requests
from bs4 import BeautifulSoup

url = 'https://www.thejakartapost.com'

jp_request = requests.get(url)

jp_response = jp_request.text

#print(jp_response)

soup = BeautifulSoup(jp_response, 'html.parser')

#print(soup.head.title.get_text())

all_title_news = soup.select('.titleNews')

title_news = all_title_news[0]

print(title_news.text.strip())

the_latest = soup.select('.theLatest')

#print(len(the_latest))

latest_news_detials = the_latest.select('.latestDetail')

for n in the_latest:
    print(n.text.get_text())
