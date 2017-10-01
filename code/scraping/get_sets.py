import pandas as pd
from scraper import web_page
from tqdm import tqdm
import pickle

class Set(object):
    """docstring for Set"""

    def __init__(self, author=None, likes=None, items=None, url_set=None):
        super(Set, self).__init__()
        self.author = author
        self.likes = likes
        self.set = items
        self.url_set = url_set


class Sets(object):
    """docstring for Sets"""

    def __init__(self, users_pickle='users.pickle'):
        super(Sets, self).__init__()
        self.users_file = users_pickle
        self.users = pd.read_pickle(users_pickle)
        self.sets = self.get_sets()

    def get_sets(self):
        sets = []
        for usr in tqdm(self.users):
            for url in usr['url_set']:
                arg = {'author': usr['name'],
                       'url_set': url,
                       'items': [obj.__dict__
                                 for obj in web_page(url=url).set],
                       'likes': None}
                sets.append(Set(**arg))
        return sets

    def save_obj(self, filename='sets.pickle'):
        pickle_out = open(filename, "wb")
        dictionary = [s.__dict__ for s in self.sets]
        pickle.dump(dictionary, pickle_out)
        pickle_out.close()


if __name__ == '__main__':
    sets = Sets(users_pickle='users.pickle')
    sets.save_obj(filename='sets.pickle')
