#!/usr/bin/python

import requests, re
from bs4 import BeautifulSoup

url = 'http://support.apple.com/en-us/HT1237'

req = requests.get(url)
soup = BeautifulSoup(req.content, 'html.parser')

models = ('mbp',
          'mba',
          'macbook',
          'imac',
          'macmini',
          'macpro',
          'xserve'
          )

d = {}

for model in models:
    table = soup.find('section', id=model)
    rows = table.find_all('tr')
    for row in rows:
        data = row.find_all('td')
        print len(data)
        if len(data) == 4:
            d[data[1].get_text()] = data[2].get_text()

for k, v in sorted(d.items()):
    print '%-20s \t%s' % (k.strip(), v.strip())