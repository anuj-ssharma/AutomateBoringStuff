#lucky.py - Opens several Google search results

import requests,sys,webbrowser,bs4

res = requests.get('http://google.com/search?q='+' '.join(sys.argv[1:]))
try:
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text,'html.parser')
    searchLinks = soup.select('.r a')
    numOpen = min(5,len(searchLinks))
    for i in range(numOpen):
        webbrowser.open('http:google.com'+searchLinks[i].get('href'))
except Exception as exc:
    print str(exc)