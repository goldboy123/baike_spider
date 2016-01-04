#-*- coding: UTF-8 -*-

from Spider import url_manager
from Spider import html_downloader
from Spider import html_parser
from Spider import html_output



class SpiderMain(object):
    def __init__(self):      
        self.downloader = html_downloader.HtmlDownloader()
        self.outputer = html_output.HtmlOutputer()  
        self.urls = url_manager.UrlManager()
        self.parser = html_parser.HtmlParser()
    
    def craw(self,root_url):
        count = 1
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                print("craw %d : %s" %(count, new_url))
                html_cont = self.downloader.download(new_url)
                new_urls, new_data = self.parser.paser(new_url, html_cont)
                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(new_data)
                if count == 10:
                    break
                count = count + 1
            except:
                print('craw failed')
            
        self.outputer.output_html()


if __name__ =="__main__":
    root_url="http://baike.baidu.com/view/21087.htm"
    obj_spider=SpiderMain()
    obj_spider.craw(root_url)