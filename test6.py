import requests

from lxml import etree


def download_page(url):
    """获取url地址页面内容"""
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'
    }
    data = requests.get(url, headers=headers)
    return data.content


def main():
    DOWNLOAD_URL = 'http://yuedu.163.com/book_reader/8355808f10e0459fbe97d5a4b88a83bd_4/671110c69d3d485686194174e78f7605_5';
    url = DOWNLOAD_URL
    titles = []
    contents = []
    issuing_times = []

    doc = download_page(url)
    # //span[contains(@class,'vote-post-up')]
    # html = etree.HTML(doc);

    htmldata = """
            <div>
                <ul>
                     <li class="item-0"><a href="link1.html">first item</a></li>
                     <li class="item-1"><a href="link2.html">second item</a></li>
                     <li class="item-inactive"><a href="link3.html">third item</a></li>
                     <li class="item-1"><a href="link4.html">fourth item</a></li>
                     <li class="item-0"><a href="link5.html">fifth item</a>
                 </ul>
             </div>
            """

    html = etree.HTML(doc);
    html_data = html.xpath('//div[@class="article-content"]')
    print(html)
    for i in html_data:
        print(i.text)

    with open("test10.html", "wb") as code:
        code.write(doc)


if __name__ == '__main__':
    main()
