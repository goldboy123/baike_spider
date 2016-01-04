#-*- coding: UTF-8 -*-
import urllib2
from cookielib import Cookie
import cookielib

class HtmlDownloader(object):
    
    
    def download(self,url):
        if url is None:
            return
        cj = cookielib.CookieJar()
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
        urllib2.install_opener(opener)
        response = urllib2.urlopen(url)
        if response.getcode()!=200:
            return None
        return response.read()


'''
#-*- coding: UTF-8 -*-
import urllib2
from cookielib import Cookie
import cookielib

class HtmlDownloader(object):
    
    
    def download(self,url):
        if url is None:
            return
        cj = cookielib.CookieJar()
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
        urllib2.install_opener(opener)
        response = urllib2.urlopen(url)
        if response.getcode():
            return None
        return response
'''



