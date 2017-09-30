# Naver-Comments-Scrape V 0.1.0
Naver Comments Scrape for News, Weptoon, and etc.

V 0.1.0 add NNCS (Naver News Comments Scrape)

## Requirements
requests, time, and json packages

# Naver News Comments Scrape
NNCS is Naver News Scraping Function

## Usage
```python
def NNCS(url, sort = 'favorite', pageSize = 100, page = 1, scrapeAll = True, dtype = 'list'):
    '''
        pageSize = 100
        page = 1
        sort = "favorite", "reply", "old", "new"
        scrapeAll = True, False
        dtype = "list", "json"
    ''' 
```
url is news url like 'http://news.naver.com/main/read.nhn?mode=LSD&mid=shm&sid1=105&oid=028&aid=0002381762'

sort options are "favorite", "reply", "old", "new". Default is "favorite"

pageSize can be from 1 to 100, and default is 100.

scrapeAll is True or False. 

dtype means return type. default is just list of comments. But if you want to all information of comments, select "json"

## Example

```python
# First copy NCS.py

import NCS

url = 'http://news.naver.com/main/read.nhn?mode=LSD&mid=shm&sid1=105&oid=028&aid=0002381762'
NCS.NNCS(url)   # Use default setting
NCS.NNCS(url, dtype = 'json')   # return json type
```
