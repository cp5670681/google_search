import urllib.request as urllib2
import urllib
from flask import Flask, request
from flask import redirect

app = Flask(__name__)
headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}

@app.route('/')
def index():
    return redirect('/search')

# 直接用url来搜索，q表示搜索内容，start表示从第几个结果开始显示
@app.route('/<search>/<num>')
def google(search,num):
    argv=urllib.parse.quote(search)
    url="https://www.google.com/search?q=" + argv + "&start=" + num
    req = urllib2.Request(url, headers = headers)
    response = urllib2.urlopen(req)
    return response.read()

# 获取网址的q和start参数，重组成google的对应url，服务器下载，返回
@app.route('/search')
def google_2():
    url="https://www.google.com/search?"
    for key, value in request.args.items():
        if key=='q' or key=='start':
            value2=urllib.parse.quote(value)
            url = url + key+"="+value2+"&"
    req = urllib2.Request(url, headers = headers)
    response = urllib2.urlopen(req)
    return response.read()
