import json
import bs4
import requests
import re
import logging as log
from abc import ABCMeta, abstractmethod
import sys

url_string = "https://www.instagram.com/explore/tags/food/"
response = bs4.BeautifulSoup(requests.get(url_string).text, "html.parser")
potential_query_ids = self.get_query_id(response)
shared_data = self.extract_shared_data(response)

media = shared_data['entry_data']['TagPage'][0]['tag']['media']
posts = []
for node in media['nodes']:
    post = self.extract_recent_instagram_post(node)
    posts.append(post)
self.save_results(posts)

end_cursor = media['page_info']['end_cursor']

# figure out valid queryId
success = False
for potential_id in potential_query_ids:
    url = "https://www.instagram.com/graphql/query/?query_id=%s&tag_name=%s&first=12&after=%s" % (
        potential_id, tag, end_cursor)
    try:
        data = requests.get(url).json()
        if 'hashtag' not in data['data']:
            # empty response, skip
            continue
        query_id = potential_id
        success = True
        break
    except json.JSONDecodeError as de:
        # no valid JSON retured, most likely wrong query_id resulting in 'Oops, an error occurred.'
        pass
if not success:
    log.error("Error extracting Query Id, exiting")
    sys.exit(1)

while end_cursor is not None:
    url = "https://www.instagram.com/graphql/query/?query_id=%s&tag_name=%s&first=12&after=%s" % (
    query_id, tag, end_cursor)
    data = json.loads(requests.get(url).text)
    end_cursor = data['data']['hashtag']['edge_hashtag_to_media']['page_info']['end_cursor']
    posts = []
    for node in data['data']['hashtag']['edge_hashtag_to_media']['edges']:
        posts.append(self.extract_recent_query_instagram_post(node['node']))
    self.save_results(posts)