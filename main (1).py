import requests
from bs4 import BeautifulSoup

#Send a Get request to the request website

url = 'https://yahoo.com'

#Replace the URL of the website we want to scrape

response = requests.get(url)

#Create a bs4 object to parse the HTML content

soup = BeautifulSoup(response.content, 'html.parser')

#Findand extract the specific data that we want from the website. 
#Replace all the lines with the elements 

title = soup.find('h1').text
paragraphs = soup.find_all('p')

#print the data extracted

print('Title:', title)
print('Paragraphs:')
for p in paragraphs:
    print(p.text)



