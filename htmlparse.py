from bs4 import BeautifulSoup

tag_p = """
<p>
    目标文本
    <a>子节点文本</a>
</p>
"""
bs4_p = BeautifulSoup(tag_p)
print(bs4_p.p.contents)
print(bs4_p.p.contents[0].strip())