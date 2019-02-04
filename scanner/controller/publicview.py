from ..app import app,render_template,request,re,Markup,plugins,session
from ..orm import db_session
from ..model.user import User
from ..plugins.gwhatcms.gwhatcms import gwhatweb

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/whatcms', methods=['get', 'post'])
def whatcms():
    return render_template('whatcms.html', title='whatcms')
    '''
    url = request.form.get("url","http://www.baidu.com")
    #url = request.url
    try:
        whatcmsresult = gwhatweb(url).whatweb(1000)
        #whatcmsresult={"url":"aaa","totle":"bbb"}
        return render_template('whatcms.html', data=whatcmsresult, title='CMS识别')
    except:
        whatcmsresult = {'total': 'bbb', 'url': 'aaa'}
        return render_template('whatcms.html', data=whatcmsresult, title='CMS识别')
'''

@app.route('/information')
def information_scan():
    return render_template('information.html', title='信息泄露', data=Markup(list(plugins.angelsword['informationpocdict'].keys())))

@app.route('/industrial')
def industrial_scan():
    return render_template('industrial.html', title='工控安全', data=Markup(list(plugins.angelsword['industrialpocdict'].keys())))

@app.route('/hardware')
def hardware_scan():
    return render_template('hardware.html', title='物联网安全', data=Markup(list(plugins.angelsword['hardwarepocdict'].keys())))

@app.route('/system')
def system_scan():
    return render_template('system.html', title='system安全', data=Markup(list(plugins.angelsword['systempocdict'].keys())))

@app.route('/cms')
def cms_scan():
    return render_template('cms.html', title='cms安全检测', data=Markup(list(plugins.angelsword['cmspocdict'].keys())))

@app.route('/AngelSword')
def AngelSword_scan():
    return render_template('AngelSword.html', title='AngelSword安全检测', data=Markup((list(plugins.angelsword['cmspocdict'].keys()))+(list(plugins.angelsword['systempocdict'].keys()))+(list(plugins.angelsword['hardwarepocdict'].keys()))+(list(plugins.angelsword['hardwarepocdict'].keys()))))

def subdomain():
    return render_template('subdomain.html',title='子域名获取')

@app.route('/getdomain')
def getdomin():
    return render_template('getdomain.html', title='旁站/C段')

@app.route('/hackertarget')
def hackertarget():
    return render_template('hackertarget.html',title='利用hackertarget的api接口进行扫描')

@app.route('/nmap')
def nmap():
    return render_template('nmap.html',title='nmap扫描')


@app.route('/login',methods=['get','post'])
def login():
    if request.method == 'POST':
        pass
    else:
        return render_template('login.html',data={"type":1})

@app.route('/reg',methods=['get','post'])
def reg():
    if request.method == 'POST':
        username=request.form.get("username")
        password=request.form.get("password")
        User(username,password).commit()
        render_template("login.html",msg="注册成功",data={"type":1})
    else:
        return render_template('login.html',data={"type":0})

# 会话控制
@app.teardown_request
def shutdown_session(exception=None):
    db_session.remove()