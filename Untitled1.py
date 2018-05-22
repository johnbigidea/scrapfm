
# coding: utf-8

# In[ ]:


from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
import random

r =  range(1,41)
c=0
b=[]
n=2000
headers = {'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'}

for a in r:
    url = 'http://www.mafengwo.cn/yj/10959/1-0-'+str(a)+'.html'
    print(url)

    html = urlopen(url).read().decode('utf-8')


    soup = BeautifulSoup(html,features='lxml')
    sub_links = soup.find_all('a', {'href': re.compile('/i/.*?\.html')})
    for sub in sub_links:
        if sub['href'] in b:
            continue
        else:
            b.append(sub['href'])

for d in b:
    url2= 'http://www.mafengwo.cn'+str(d)
    print(url2)
    try:
        html2 = urlopen(url2).read().decode('utf-8')
        soup2 = BeautifulSoup(html2,features='lxml')
        img_links = soup2.find_all('img', {'data-src': re.compile('.*?\.jpeg')})
        for link in img_links:
            print(link['data-src'])
            content= urlopen(link['data-src']).read()
            with open(str(n)+'.jpeg','wb') as f:
                f.write(content)
                n+=1
    except:
        continue



