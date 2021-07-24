import requests
from bs4 import BeautifulSoup

url = 'https://www.thejakartapost.com'

jp_request = requests.get(url)

jp_response = jp_request.text

soup = BeautifulSoup(jp_response, 'html.parser')

jp_request = requests.get(url)

the_latest_detail = soup.find_all('div', attrs={'class' : 'latestDetail'})
#latest_detail_link = soup.find_all('a', href=True)

for div in the_latest_detail:
    print(div.a['href'])


#for data in soup.find_all('div', attrs={'latestDetail'}):
#    for div in data.find_all_next('a'):
#        print(div.get('href'))

#the_latest_detail = soup.find_all('div', attrs={'class' : 'latestDetail'})

#for div in the_latest_detail:
#    print(div.a['href'])
