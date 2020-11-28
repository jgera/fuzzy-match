import urllib.request
from bs4 import BeautifulSoup
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
from retry import retry
from urlread import urlread_retry 

# ==================== Logger =====================
import logging 
import os
log = "log.txt"
if os.path.exists(log):
    os.remove(log)

logging.basicConfig(filename= "log.txt", level=logging.DEBUG,format="%(asctime)s, %(levelname)s: %(message)s")


downloaded = open('downloaded.txt','r').readlines()
downloaded = [d.strip() for d in downloaded]
 
urls = open('urls.txt').readlines()
out =  open('out.csv','w+') 
out.write("url,title,ratio,score,partial,partial_score,token_sort,token_sort_score,token_set,token_set_score\n")


for url in urls:
       try:
              url = url.strip()
              print("Getting:" + url)
              html = urlread_retry(url)
              soup = BeautifulSoup(html, 'html.parser')
              title = soup.title.string.replace(","," ")
              print(title)    
              ratio,score = process.extractOne(title,downloaded,scorer=fuzz.ratio)
              partial,score = process.extractOne(title,downloaded,scorer=fuzz.partial_ratio)
              token_sort,token_sort_score = partial_ratio,partial_ratio_score = process.extractOne(title,downloaded,scorer=fuzz.token_sort_ratio)
              token_set,token_set_score = process.extractOne(title,downloaded,scorer=fuzz.token_set_ratio)
              d = "{},{},{},{},{},{},{},{},{},{}".format(url,title,ratio,score, partial,score, token_sort,token_sort_score, token_set,token_set_score)   
              out.write(d + "\n")
              out.flush()
       except:
              logging.debug(url)

out.close()