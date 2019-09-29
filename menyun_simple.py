import requests
import re
import codecs
from bs4 import BeautifulSoup
from openpyxl import Workbook

wb = Workbook()
dest_filename = '电影2.xlsx'
ws1 = wb.active
ws1.title = "电影top250"

DOWNLOAD_URL = 'http://www.my2852.com/wgwx/dpxs/001.htm'
DOWNLOAD_URL1 = 'http://www.my2852.com/wgwx/dpxs/'


def download_page(url):
    """获取url地址页面内容"""
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'
    }
    data = requests.get(url, headers=headers).content.decode('gbk', 'ignore')
    return data


def get_li(doc):
    soup = BeautifulSoup(doc, 'html.parser')
    titles = []  # 文章名字
    contents = []  # 文章内容
    issuing_time = []  # 文章发表时间
    # title = soup.find('td', class_='tt2')
    test = soup.select('center>table>tr+tr');
    title_t = test[0].get_text().strip()
    content_t = str(test[2].contents[1]).replace('<br/>','\r\n')
    content_t = content_t.replace('<br/>','\r\n')

    page_html = test[5]
    next_html = page_html.find_all('a')
    url = None

    for index, every in enumerate(next_html):
        if (every.get_text() == '下一页' or every.get_text() == '后一页'):
            url = DOWNLOAD_URL1 + every['href'].replace('\r\n','')
            url = url.replace('\r\n','')

    print(title_t)
    print(content_t)
    exit;

    return titles, contents, issuing_time, url


def main():
    url = DOWNLOAD_URL
    titles = []
    contents = []
    issuing_times = []

    while url:
        doc = download_page(url)
        title, content, issuing_time, url = get_li(doc)
        titles = titles + title
        contents = contents + content
        issuing_times = issuing_times + issuing_time
    for (i, m, o) in zip(title, contents, issuing_times):
        col_A = 'A%s' % (titles.index(i) + 1)
        print('title')
        print(i)
        print('content')
        print(m)
        col_B = 'B%s' % (titles.index(i) + 1)
        col_C = 'C%s' % (titles.index(i) + 1)
        ws1[col_A] = i
        ws1[col_B] = m
        ws1[col_C] = o
    wb.save(filename=dest_filename)


if __name__ == '__main__':
    main()
