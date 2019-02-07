import os
import requests
s=requests.get("http://api.hackertarget.com/reversedns/?q=http://www.baidu.com")
print s.text