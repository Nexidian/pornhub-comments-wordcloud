"""
    pornhub comments wordcloud generator
    ----------
    Simple App to grab the top 100 videos from Pornhub and generate a wordcloud from the comments
    :copyright: (c) 2019 by Luke Jennings
"""

from .core import *
from .request_manager import RequestManager
from .data_manager import DataManager


class PornhubCommentsWordcloud(DataManager):

    def __init__(self, *args):
        DataManager.__init__(self, *args)

    def generate_wordcloud(self, video_count = 100, use_cache = True):
        DataManager.generate_wordcloud(self , video_count, use_cache)
        #DataManager.hello(self)


__copyright__ = "Copyright 2016 by Luke Jennings"
__authors__ = ["Luke Jennings"]
__source__ = "https://github.com/Nexidian/pornhub-comments-wordcloud/"
__license__ = "MIT"

__all__ = ['PornhubCommentsWordcloud', ]
