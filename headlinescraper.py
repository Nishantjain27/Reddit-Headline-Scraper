import urllib2
from bs4 import BeautifulSoup

date = raw_input('Enter date in YYYY/MM/DD format. eg: 2017/dec/27     ')
print("\n")
page_source = 'http://news.rediff.com/commentary/'+ date + '/liveupdates.htm'
page = urllib2.urlopen(page_source)
soup = BeautifulSoup(page,'html.parser')
headlines = soup.find_all('a' , attrs = {'class':'black'})
for link in headlines[0:9]:
    head = link.contents[0]
    print(head)
    print("\n")
    