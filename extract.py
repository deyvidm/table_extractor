from collections import Counter
from bs4 import BeautifulSoup
import requests

soup = BeautifulSoup(requests.get('https://prosettings.net/rainbow-6-pro-settings-gear-list/').text, 'html.parser')
rows = soup.find_all('table')[0].find_all('tr')

props = []
data = []
for header in rows[0].find_all('th'):
    props.append(header.text)

for row in rows[1:]:
    data.append(dict((props[i], cell.text) for i, cell in enumerate(row.find_all('td'))))

for prop in props: 
    print prop
    for i, item in  enumerate(Counter(d[prop] for d in data).most_common()[:5]):
        print i+1,"  count: ", item[1], "\t", item[0]
    print ""
