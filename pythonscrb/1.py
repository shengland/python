import urllib.request
import urllib.error

def download(url):
    print('Download:',url)
    try:
        html = urllib.request.urlopen(url).read()
    except urllib.error as e:
        print('download error:',e.reason)
        html = None
    return html
a = download('https://www.baidu.com/')
print(a)


