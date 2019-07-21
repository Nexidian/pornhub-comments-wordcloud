# -*- coding: utf-8 -*-
from .core import *


class RequestManager(object):

    def __init__(self, *args):
        pass

    def get_most_viewed_links(self, page_num):
        """
        Get the most viewed videos of all time.

        :param quantity: Number of video links to return
        """
        cookies = requests.head('https://www.pornhub.com/video?o=mv&t=a')
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'
        }

        page_num = page_num if page_num >= 1 else 1
        payload = {"page": page_num}
        response = requests.get(BASE_URL + MOST_VIEWED_ALL_TIME, cookies=cookies, headers=headers, params=payload)
        html = response.text

        return bs(html, 'html.parser')

    def get_video(self, specific_video):
        print("Requesting page: {}".format(BASE_URL + specific_video))
        response = requests.get(BASE_URL + specific_video)
        html = response.text
        return bs(html, 'html.parser')

