
# coding: utf-8

# In[1]:

import get_users as gu
import get_sets as gs
import pandas as pd
import get_sets_from_userpage
import scraper


# In[2]:

#Read users from pickle
users = pd.read_pickle('./users.pickle')
DFusr = pd.DataFrame(users)
del DFusr['url_set']


# In[40]:

#Save all sets in DataFrame

df_dress = pd.DataFrame(columns=['user','profile_url','followers','location','set_link','set_img','dress_combo'])

for usr in DFusr['name'].get_values():    
    usr_url = DFusr.loc[DFusr['name']==usr, 'url_name'].get_values()[0]
    get_usr_set = get_sets_from_userpage.scrape_sets(url=usr_url)
    dict_list = get_usr_set.get_set_link()
    df_dict_list = pd.DataFrame(dict_list)
    followers = DFusr.loc[DFusr['name']==usr,'visite'].get_values()[0]
    location = DFusr.loc[DFusr['name']==usr,'where'].get_values()[0]           
    for url in df_dict_list['url'].get_values():
        img = df_dict_list.loc[df_dict_list['url']==url,'img'].get_values()[0]
        page = scraper.web_page(url=url).set 
        dress_combo = []
        for item in page: dress_combo.append(item.__dict__)
        df_dress = df_dress.append(pd.DataFrame({'dress_combo':dress_combo,
                                                 'set_link':url,
                                                'set_img':img,
                                                'user':usr,
                                                'profile_url':usr_url,
                                                'followers':followers,
                                                'location':location}))
        df_dress.to_csv('./set_db.csv',sep=',',index=False)


# In[ ]:



