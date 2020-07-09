import requests
from bs4 import BeautifulSoup
import pprint

res = requests.get('https://news.ycombinator.com/newest')
soup = BeautifulSoup(res.text, 'html.parser')
links = soup.select('.storylink')
subtext = soup.select('.subtext')

def sorted_hn(hnlist) :
    return sorted(hnlist, key = lambda k : k['points'], reverse=True)

def create_custom_hn(links, subtext) :
    hn = []
    for idx, items in enumerate(links) :
        title = links[idx].getText()
        href = links[idx].get('href', 'none')
        votes = subtext[idx].select('.score')
        if len(votes) :
            points = votes[0].getText().split(' ')

        point = points[0]
        hn.append({'Title': title, 'link': href, 'points': point})
    return sorted_hn(hn)

pprint.pprint(create_custom_hn(links,subtext))