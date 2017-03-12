import requests
from bs4 import BeautifulSoup


# We've now imported the two packages that will do the heavy lifting
# for us, reqeusts and BeautifulSoup

# This is the URL that we want to scrap
url_to_scrape = 'https://ncreportcards.ondemand.sas.com/src/reports/190LEA_2016_LEA.html'

# Tell the requests package to retreive the contents our page (it'll be 
# grabbing what you see when you use the View Source feature in your browser)
r = requests.get(url_to_scrape)

# We now have the source HTML of the page. Let's ask BeaultifulSoup
# to parse it for us.
soup = BeautifulSoup(r.text, "lxml")

# Let's print all of the hyperlinks found in this web page
for link in soup.find_all('a'):
    print(link.get('href'))
    