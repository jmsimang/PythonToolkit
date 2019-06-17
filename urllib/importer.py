import requests
from bs4 import BeautifulSoup

# url = "https://www.wikipedia.org/"
url = "https://www.datacamp.com/teach/documentation"

r = requests.get(url)
html_doc = r.text
# print(html_doc)

# Beautify tag soup
soup = BeautifulSoup(html_doc, features="lxml")
pretty_soup = soup.prettify()
# print(pretty_soup)

# Turn html into data
page_title = soup.title
print(page_title)
page_text = soup.get_text()
print(page_text)

# Get hyperlinks and print them
a_tags = soup.find_all('a')
for link in a_tags:
    print(link.get('href'))
