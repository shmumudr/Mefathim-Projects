import requests
import sys
import csv
from tqdm import tqdm

HN_PREFIX = 'https://hacker-news.firebaseio.com/v0'
HN_ITEMID = '/item/{}.json?print=pretty'
x = requests.get('https://hacker-news.firebaseio.com/v0/maxitem.json?print=pretty')
x1 = (x.json())
item = requests.get(HN_PREFIX + HN_ITEMID.format(x1))
# item2 = (item.json())
# print (item2)

HN_TOP_STORIES = requests.get('https://hacker-news.firebaseio.com/v0/topstories.json?print=pretty')


# item3 = (HN_TOP_STORIES.json())
# print(item3)

def get_top_stories_ids():
    response = HN_TOP_STORIES
    if response.status_code == 200:
        return response.json()
    else:
        pass


def get_top_stories_info(top_stories_id_list):
    result = []
    for i in top_stories_id_list[:5]:
        item = requests.get(HN_PREFIX + HN_ITEMID.format(i))
        result.append(item.json())
        # print(result)
    return result

def save_info_into_csv(result, file_name):
    keysList = set().union(*[d.keys() for d in result])
    # keysList = list(result[0].keys())
    # print(keysList)
    with open (file_name, 'w') as file:
        writer = csv.DictWriter(file, keysList)
        writer.writeheader()
        writer.writerows(result)


a = get_top_stories_ids()
b= get_top_stories_info(a)
c= save_info_into_csv(b, 'g.csv')

