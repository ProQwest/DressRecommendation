from selenium import webdriver
from bs4 import BeautifulSoup
import pickle
import time
import os

      
        
class scrape_sets(object):
    """web browsing class for scraping"""

    def __init__(self, n_scroll=250, url=''):
        super(scrape_sets, self).__init__()
        self.url = url
        self.driver = webdriver.Chrome('./chromedriver')
        self.base_url = 'https://www.polyvore.com'
        self.users = []
        self.n_scroll = n_scroll

    def get_boxes(self):
        self.driver.get(self.url)
        for i in range(self.n_scroll):
            self.driver.execute_script(
                "window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(0.1)
        html = self.driver.page_source
        self.driver.close()
        return html

    def get_views(self, usr):
        n_vi = usr.find_all("li", class_='meta')[-1].text
        n_vi = n_vi.replace('visite', '')
        n_vi = n_vi.replace('M', '000')
        n_vi = n_vi.replace('K', '00')
        n_vi = n_vi.replace('.', '')
        return int(n_vi.split(' ')[0])

    def get_where(self, usr):
        where_list = usr.find_all("li", class_='meta')
        if len(where_list) > 1:
            where = where_list[0].text
        else:
            where = None
        return where

    def get_set_link(self):
        html = self.get_boxes()
        user_html = BeautifulSoup(html, 'html.parser')
        set_list = user_html.find_all("div", class_="grid_item hover_container type_set span2w span2h")
        set_urls = [self.base_url + usr.find('a')['href'][2:] for usr in set_list]
        set_imgs = [usr.find('img')['src'] for usr in set_list]
        return {'url':set_urls,'img':set_imgs}

    def get_set_details(self):
        links = self.get_set_link()
        for link in links:
            html = link.get_boxes()
            link_html = BeautifulSoup(link, 'html.parser')
            box = link_html.find('div', class_="grid_item hover_container type_thing span1w span1h")
            arg = {'dress_combo': box.findall('img')['title'],
                   'likes': box.find('span',class_='fav_count')
                   }
            self.links.append(user(**arg))
            return self

    def save_obj(self, filename='users.pickle'):
        pickle_out = open(filename, "wb")
        dictionary = [user.__dict__ for user in self.users]
        pickle.dump(dictionary, pickle_out)
        pickle_out.close()
        
