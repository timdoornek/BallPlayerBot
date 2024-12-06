from bs4 import BeautifulSoup
from urllib.request import Request, urlopen, urlretrieve
import re
from time import sleep

LINK_BEGINNING = 'https://www.baseball-reference.com'
HEADSHOT_DIRECTORY = './player_headshots/'

main_req = Request('https://www.baseball-reference.com/players/a/')
html_page = urlopen(main_req).read()
soup = BeautifulSoup(html_page, 'html.parser')

for link in soup.findAll('a', attrs={'href': re.compile("^/players/.{5,}")}):
    name = link.get_text()
    link_href = link.get('href')
    full_link = LINK_BEGINNING + link_href
    player_req = Request(full_link)
    player_page = urlopen(player_req).read()
    player_soup = BeautifulSoup(player_page, 'html.parser')

    headshot_tag = player_soup.find('img', attrs={'src': re.compile("https://www.baseball-reference.com")})
    if headshot_tag:
        print(name)
        print(headshot_tag.get('src'))
        urlretrieve(headshot_tag.get('src'), HEADSHOT_DIRECTORY + name +'.jpg')
        sleep(5)

