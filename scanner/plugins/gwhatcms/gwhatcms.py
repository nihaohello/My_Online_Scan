#coding=utf-8
import gevent
from gevent import monkey
gevent.monkey.patch_all()
import requests
import json, hashlib, sys
import os
from gevent.queue import Queue
import time

current_path = os.path.abspath(os.path.dirname(__file__))
class gwhatweb(object):
    def __init__(self, url):
        self.whatcms_result = []
        self.tasks = Queue()
        self.url = url.rstrip("/")
        data_file_name=current_path + '/data.json'
        fp = open(data_file_name,encoding="utf-8")
        webdata = json.load(fp, encoding="utf-8")
        for i in webdata:
            self.tasks.put(i)
        fp.close()
        #print("webdata total:%d" % len(webdata))

    def _GetMd5(self, body):
        m2 = hashlib.md5()
        m2.update(body.encode("utf8"))
        return m2.hexdigest()

    def _clearQueue(self):
        while not self.tasks.empty():
            self.tasks.get()

    def _worker(self):
        data = self.tasks.get()
        test_url = self.url + data["url"]
        rtext = ''
        try:
            r = requests.get(test_url, timeout=10)
            if (r.status_code != 200):
                return
            rtext = r.text
            if rtext is None:
                return
        except:
            rtext = ''

        if data["re"]:
            if (rtext.find(data["re"]) != -1):
                result = data["name"]
                #print("CMS:%s Judge:%s re:%s" % (result, test_url, data["re"]))
                self.whatcms_result.append(result)
                self.whatcms_result.append(test_url)
                self.whatcms_result.append(data["re"])
                self._clearQueue()
                return True
        else:
            md5 = self._GetMd5(rtext)
            if (md5 == data["md5"]):
                result = data["name"]
                #print("CMS:%s Judge:%s md5:%s" % (result, test_url, data["md5"]))
                self.whatcms_result.append(result)
                self.whatcms_result.append(test_url)
                self.whatcms_result.append(data["md5"])
                self._clearQueue()
                return True

    def _boss(self):
        while not self.tasks.empty():
            self._worker()

    def whatweb(self, maxsize=100):
        start = time.time()
        allr = [gevent.spawn(self._boss) for i in range(maxsize)]
        gevent.joinall(allr)
        end = time.time()
        #print ("cost: %f s" % (end - start))
        whatcms_time=(end-start)
        self.whatcms_result.append("耗费时间：")
        self.whatcms_result.append(whatcms_time)
        return {'total':self.whatcms_result,"url":self.url}
#return {'total':1424,'url':self.url,'result':"CMS: "+content['CMS']+",JavaScript Frameworks: "+content['JavaScript Frameworks'][0]+",Web Servers: "+content["Web Servers"][0],'time':'%.3f s' % self.time}
#print(current_path)
#a=gwhatweb("http://www.naivete.online").whatweb(1000)
#print(a)



