from ..app import json,requests,request,make_response,socket,jsonify,Blueprint,plugins
from ..plugins.gwhatcms.gwhatcms import gwhatweb

api = Blueprint('api', __name__)

def getjson():
    return json.loads(request.get_data().decode("utf-8"))
# webscan.cc结果查询

@api.route('/query', methods=['post'])
def query_c():
    post_json = getjson()
    request_json_raw = requests.get('http://api.hackertarget.com/httpheaders/?q=%s' % post_json[0]['ip'])
    return request_json_raw.content


# domain2ip
@api.route('/domain2ip', methods=['POST'])
def return_json():
    domain_json = getjson()
    ip = socket.gethostbyname(domain_json[0]['domain'].split('/')[2])
    j_ip = [{"ip": ip}]
    return jsonify(j_ip)


@api.route('/hackertartget_Alls', methods=['post'])
def hackertartget_Alls():
    traceRoute_json = getjson()
    if(traceRoute_json[0]["type"] == "1"):
        try:
            request_json_raw = requests.get('http://api.hackertarget.com/httpheaders/?q=%s' % traceRoute_json[0]['url'])
            a1 = request_json_raw.text
            return jsonify(a1)
        except Exception as e:
            pass
    if (traceRoute_json[0]["type"] == "2"):
        try:
            request_json_raw = requests.get('http://api.hackertarget.com/reverseiplookup/?q=%s' % traceRoute_json[0]['url'])
            a2 = request_json_raw.text
            return jsonify(a2)
        except Exception as e:
            pass
    if (traceRoute_json[0]["type"] == "3"):
        try:
            request_json_raw = requests.get('http://api.hackertarget.com/mtr/?q=%s' % traceRoute_json[0]['url'])
            a3 = request_json_raw.text
            return jsonify(a3)
        except Exception as e:
            pass
    if (traceRoute_json[0]["type"] == "4"):
        try:
            request_json_raw = requests.get('http://api.hackertarget.com/whois/?q=%s' % traceRoute_json[0]['url'])
            a4 = request_json_raw.text
            return jsonify(a4)
        except Exception as e:
            pass
    if (traceRoute_json[0]["type"] == "5"):
        try:
            request_json_raw = requests.get('http://api.hackertarget.com/dnslookup/?q=%s' % traceRoute_json[0]['url'])
            a5 = request_json_raw.text
            return jsonify(a5)
        except Exception as e:
            pass
    if (traceRoute_json[0]["type"] == "6"):
        try:
            request_json_raw = requests.get('http://api.hackertarget.com/reversedns/?q=%s' % traceRoute_json[0]['url'])
            a6 = jsonify(request_json_raw.text)
            return jsonify(a6)
        except Exception as e:
            pass
    if (traceRoute_json[0]["type"] == "7"):
        try:
            request_json_raw = requests.get('http://api.hackertarget.com/geoip/?q=%s' % traceRoute_json[0]['url'])
            a7 = jsonify(request_json_raw.text)
            return jsonify(a7)
        except Exception as e:
            pass
    if (traceRoute_json[0]["type"] == "8"):
        try:
            request_json_raw = requests.get('http://api.hackertarget.com/nmap/?q=%s' % traceRoute_json[0]['url'])
            a8 = jsonify(request_json_raw.text)
            return jsonify(a8)
        except Exception as e:
            pass
    if (traceRoute_json[0]["type"] == "9"):
        try:
            request_json_raw = requests.get('http://api.hackertarget.com/findshareddns/?q=%s' % traceRoute_json[0]['url'])
            a9 = jsonify(request_json_raw.text)
            return jsonify(a9)
        except Exception as e:
            pass
    if (traceRoute_json[0]["type"] == "10"):
        try:
            request_json_raw = requests.get('http://api.hackertarget.com/pagelinks/?q=%s' % traceRoute_json[0]['url'])
            a10 = jsonify(request_json_raw.text)
            return jsonify(a10)
        except Exception as e:
            pass



# cms本地识别
@api.route('/whatcms', methods=['post'])
def whatcms_api():
    whatcms_load = getjson()
    whatcms_url = whatcms_load[0]['url']
    whatcms_result=gwhatweb(whatcms_url).whatweb(1000)
    #whatcms_result_2={"url":whatcms_url,"totle":whatcms_result}
    #whatcms_result= {"url": "aaa", "totle": "bbb"}
    return jsonify([whatcms_result])


# 信息泄露
@api.route('/information', methods=['post'])
def information_api():
    information_load = getjson()
    information_url = information_load['url']
    information_type = information_load['type']
    information_poc_result = list(plugins.angelsword['informationpocdict'].values())[information_type](information_url).run()
    if "[+]" in information_poc_result:
        information_poc_status = 1
    else:
        information_poc_status = 0
    return jsonify({"status": information_poc_status, "pocresult": information_poc_result})


# 工控安全
@api.route('/industrial', methods=['post'])
def industrial_api():
    industrial_load = getjson()
    industrial_url = industrial_load['url']
    industrial_type = industrial_load['type']
    industrial_poc_result = list(plugins.angelsword['industrialpocdict'].values())[industrial_type](industrial_url).run()
    if "[+]" in industrial_poc_result:
        industrial_poc_status = 1
    else:
        industrial_poc_status = 0
    return jsonify({"status": industrial_poc_status, "pocresult": industrial_poc_result})


# 物联网安全
@api.route('/hardware', methods=['post'])
def hardware_api():
    hardware_load = getjson()
    hardware_url = hardware_load['url']
    hardware_type = hardware_load['type']
    hardware_poc_result = list(plugins.angelsword['hardwarepocdict'].values())[hardware_type](hardware_url).run()
    if "[+]" in hardware_poc_result:
        hardware_poc_status = 1
    else:
        hardware_poc_status = 0
    return jsonify({"status": hardware_poc_status, "pocresult": hardware_poc_result})


# system安全
@api.route('/system', methods=['post'])
def system_api():
    system_load = getjson()
    system_url = system_load['url']
    system_type = system_load['type']
    system_poc_result = list(plugins.angelsword['systempocdict'].values())[system_type](system_url).run()
    if "[+]" in system_poc_result:
        system_poc_status = 1
    else:
        system_poc_status = 0
    return jsonify({"status": system_poc_status, "pocresult": system_poc_result})


# cms漏洞利用
@api.route('/cms', methods=['post'])
def cms_api():
    cmsexp_load = getjson()
    cmsexp_url = cmsexp_load['url']
    cmsexp_type = cmsexp_load['type']
    cmsexp_poc_result = list(plugins.angelsword['cmspocdict'].values())[cmsexp_type](cmsexp_url).run()
    if cmsexp_poc_result is not None:
        if "[+]" in cmsexp_poc_result:
            cmsexp_poc_status = 1
        else:
            cmsexp_poc_status = 0
    else:
        cmsexp_poc_result = "[-]no vuln"
        cmsexp_poc_status = 0
    return jsonify({"status": cmsexp_poc_status, "pocresult": cmsexp_poc_result})


@api.route('/Angelsword', methods=['post'])
def Angelsword_api():
    Angelsword_load = getjson()
    Angelsword_url = Angelsword_load['url']
    Angelsword_type = Angelsword_load['type']
    Angelsword_poc_result =(((list(plugins.angelsword['cmspocdict'].values()))+(list(plugins.angelsword['systempocdict'].values()))+(list(plugins.angelsword['hardwarepocdict'].values()))+(list(plugins.angelsword['hardwarepocdict'].values()))))[Angelsword_type](Angelsword_url).run()
    if Angelsword_poc_result is not None:
        if "[+]" in Angelsword_poc_result:
            Angelsword_poc_status = 1
        else:
            Angelsword_poc_status = 0
    else:
        Angelsword_poc_result = "[-]no vuln"
        Angelsword_poc_status = 0
    return jsonify({"status": Angelsword_poc_status, "pocresult": Angelsword_poc_result})


@api.route('/subdomain',methods=['post'])
def subdomain_api():
    domain_json=getjson()
    return requests.get("http://ce.baidu.com/index/getRelatedSites?site_address={domain}".format(domain=domain_json['domain'])).text

@api.route('/nmap',methods=['post'])
def nmap_api():
    target_json=getjson()
    return jsonify({'data':requests.get("https://api.hackertarget.com/nmap/?q={target}".format(target=target_json['target'].replace("http:","").replace("https:","").replace("/",""))).text})
