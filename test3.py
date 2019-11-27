# 单页面xpath爬虫
import requests
from lxml import etree
url = "http://www.my2852.com/xdmj/luxun/nahan/018.htm"
data = requests.get(url).content.decode('gbk', 'ignore')
print(data);
html = etree.HTML(wb_data)
b = html.xpath('//table//td[@colspan="2"]')
print(b)
print(b[0])




