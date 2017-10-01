from bs4 import BeautifulSoup
import urllib.request


class dress_item(object):
    """docstring fos"""

    def __init__(self, href=None, desc=None, price=None, fav_cnt=None):
        self.image_link = href
        self.description = desc
        self.price = price
        self.likes = fav_cnt


class web_page(object):
    """load the html file form a web page"""

    def __init__(self, url=''):
        super(web_page, self).__init__()
        self.url = url
        self.html_doc = self.read_html_page
        self.set = scraping(self.html_doc).element

    @property
    def read_html_page(self):
        fp = urllib.request.urlopen(self.url)
        mybytes = fp.read()
        fp.close()
        return mybytes.decode("utf8")


class scraping(object):
    """docstring for screaping"""

    def __init__(self, html_doc):
        super(scraping, self).__init__()
        self.html_doc = html_doc
        self.element = self.allocate_items()

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
            try:
                atr = {'href': item.find("img")['src'],
                       'desc': item.find("img")['title'],
                       'price': item.find("span", class_="price").text,
                       'fav_cnt': item.find("span", class_="fav_count").text}
                items.append(dress_item(**atr))
            except:
                pass
        return items


if __name__ == '__main__':
    address = "https://www.polyvore.com/arcane_work_outfit/set?id=188730024"
    scr = web_page(url=address).set
    import pdb
    pdb.set_trace()
    print(scr)
