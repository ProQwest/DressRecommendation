from bs4 import BeautifulSoup
import urllib.request


class Set(object):
    """docstring for Set"""
    def __init__(self, author=None, likes=None, items=None, url_set=None):
        super(Set, self).__init__()
        self.author = author
        self.likes = likes
        self.items = items
        self.url_set = url_set


class dress_item(object):
    """docstring fos"""

    def __init__(self, href=None, desc=None, price=None, fav_cnt=None):
        self.image_link = href
        self.description = desc
        self.price = price
        self.likes = fav_cnt


class web_page(object):
    """load the html file form a web page"""

    def __init__(self, address=
        "https://www.polyvore.com/arcane_work_outfit/set?id=188730024"):
        super(web_page, self).__init__()
        self.address = address
        self.html_doc = self.read_html_page

    @property
    def read_html_page(self):
        fp = urllib.request.urlopen(self.address)
        mybytes = fp.read()
        fp.close()
        return mybytes.decode("utf8")


class scraping(object):
    """docstring for screaping"""

    def __init__(self, html_doc):
        super(scraping, self).__init__()
        self.html_doc = html_doc
        self.items = self.allocate_items()

    @property
    def soup(self):
        return BeautifulSoup(self.html_doc, 'html.parser')

    @property
    def bottom_table(self):
        return self.soup.find_all("div", class_=
            "grid_item hover_container type_thing span1w span1h")

    def allocate_items(self):
        items = []
        for item in self.bottom_table:
            atr = {'href': item.find("img")['src'],
                   'desc': item.find("img")['title'],
                   'price': item.find("span", class_="price").text,
                   'fav_cnt': item.find("span", class_="fav_count").text}
            items.append(dress_item(**atr))
        return items



if __name__ == '__main__':
    mod = web_page()
    scr = scraping(mod.html_doc)

    for s in scr.items:
        print(s.__dict__)
