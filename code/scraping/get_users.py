from selenium import webdriver
from bs4 import BeautifulSoup
import time


class user(object):
    """user object"""
    def __init__(self, name=None, visite=None, user_page=None, sets=None, where=None):
        super(user, self).__init__()
        self.name = name
        self.visite = visite
        self.url_name = user_page
        self.url_set = sets
        self.where = where


class scrape_users(object):
    """web browsing class for scraping"""
    def __init__(self):
        super(scrape_users, self).__init__()
        self.url = 'https://www.polyvore.com/cgi/search.users'
        self.driver = webdriver.Chrome('./chromedriver')
        self.base_url = 'https://www.polyvore.com'

    def get_boxes(self):
        self.driver.get(self.url)
        for i in range(1000):
            self.driver.execute_script(
                "window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(1)
        html = self.driver.page_source
        self.driver.close()
        return html

    def get_views(self, usr):
        n_vi = usr.find_all("li", class_='meta')[-1].text
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

    def get_users(self):
        html = self.get_boxes()
        user_html = BeautifulSoup(html, 'html.parser')
        user_list = user_html.find_all("div", class_="rec_follow clearfix")
        users = []
        for usr in user_list:
            box = usr.find('a', class_="left buddy_icon")
            sets = usr.find_all('li', class_="size_s2 last_row")
            arg = {'name': box.find('img')['alt'],
                   'user_page': self.base_url + box['href'][2:],
                   'sets': [self.base_url + s.find('a')['href'][2:]
                            for s in sets],
                   'visite': self.get_views(usr),
                   'where': self.get_where(usr)
                   }
            users.append(user(**arg))
        return users


if __name__ == '__main__':
    su = scrape_users()
    usrs = su.get_users()
    for usr in usrs:
        print(usr.__dict__)
