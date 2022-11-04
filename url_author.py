import requests
from bs4 import BeautifulSoup

page = requests.get('https://www.journals.elsevier.com/artificial-intelligence/most-downloaded-articles')
soup = BeautifulSoup(page.text,'html.parser')
dtable = soup.find('ul',class_ = 'sc-9zxyh7-0 ffmPq')
print(dtable)
urls = []
  
# For loop that iterates over all the <li> tags
for h in dtable.findAll('li'):
    
    # looking for anchor tag inside the <li>tag
    a = h.find('a')
    try:
        
        # looking for href inside anchor tag
        if 'href' in a.attrs:
            
            # storing the value of href in a separate variable
            url = a.get('href')
              
            # appending the url to the output list
            urls.append(url)
              
    # if the list does not has a anchor tag or an anchor tag
    # does not has a href params we pass
    except:
        pass
  
# print all the urls stored in the urls list
for url in urls:
    print(url)
for li in dtable.findAll('li')[1:12]:
  # tds = a.findAll('h2')
  # td=p.findAll('span')
  title = li.find('h2',class_ ='sc-1qrq3sd-1 MKjKb sc-1nmom32-0 sc-1nmom32-1 hqhUYH ebTA-dR').text
  author = li.find('span',class_ ='sc-1w3fpd7-0 pgLAT').text
  public_date = li.find('span',class_ ='sc-1thf9ly-2 bKddwo').text
  # url = li.find('href',class_ ='sc-5smygv-0 nrDZj').tag
  print(title,author,public_date,url)
  
