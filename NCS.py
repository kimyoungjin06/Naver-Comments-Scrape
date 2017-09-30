def NNCS(url, sort = 'favorite', pageSize = 100, page = 1, scrapeAll = True):
    '''
        pageSize = 100
        page = 1
        sort = "favorite", "reply", "old", "new"
        scrapeAll = True, False
    ''' 
    params = []
    for i in url.split('?')[1].split('&'):
        params.append(i.split('='))
    params = dict(params)
    url = "https://apis.naver.com/commentBox/cbox/web_naver_list_jsonp.json?ticket=news&templateId=view_politics&pool=cbox5&lang=ko&country=KR&objectId=news"+\
            params['oid']+ "%2C"+ params['aid']+ "&categoryId=&pageSize="+\
            str(pageSize)+ "&indexSize=10&groupId=&page="+ str(page)+ "&initialize=true&useAltSort=true&replyPageSize=30&moveTo=&sort="+\
            sort
    header = {
        "Referer": 'http://www.naver.com'
    }
    res = rq.get(url, headers = header)
    commentSize = json.loads('('.join(res.text.split('(')[1:])[:-2])['result']['count']['comment']
    comments = [x['contents'] for x in json.loads('('.join(res.text.split('(')[1:])[:-2])['result']['commentList']]
    
    if scrapeAll == True:
        for page in range(2,int(commentSize/100)+2):
            url = "https://apis.naver.com/commentBox/cbox/web_naver_list_jsonp.json?ticket=news&templateId=view_politics&pool=cbox5&lang=ko&country=KR&objectId=news"+\
                params['oid']+ "%2C"+ params['aid']+ "&categoryId=&pageSize="+\
                str(pageSize)+ "&indexSize=10&groupId=&page="+ str(page)+ "&initialize=true&useAltSort=true&replyPageSize=30&moveTo=&sort="+\
                sort
            res = rq.get(url, headers = header)
            comments = comments + [x['contents'] for x in json.loads('('.join(res.text.split('(')[1:])[:-2])['result']['commentList']]
            print("%.2f" % (len(comments)/commentSize),"percent complete...")
            time.sleep(2)
    
    return comments