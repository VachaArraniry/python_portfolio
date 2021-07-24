from bs4 import BeautifulSoup
import requests

url = 'https://www.thejakartapost.com'

jp_request = requests.get(url)

jp_response = jp_request.text

soup = BeautifulSoup(jp_response, 'html.parser')

jp_request = requests.get(url)

the_latest = soup.select('.theLatest')

link = soup.a

print(link)