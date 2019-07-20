import requests
import numpy as np
import pandas as pd
from os import path
from os import listdir
from PIL import Image
from bs4 import BeautifulSoup as bs
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

import matplotlib.pyplot as plt

BASE_URL	         = "https://pornhub.com"
MOST_VIEWED_ALL_TIME = "/video?o=mv&t=a"

MOST_VIEWED_LINKS_CACHE_FILE_LOCATION   = "PornhubCommentsWordcloud/resources/most_viewed_links.txt"
COMMENTS_CACHE_FILE_LOCATION            = "PornhubCommentsWordcloud/resources/pornhub_comments.csv"
STOPWORDS_FILE_LOCATION                 = "PornhubCommentsWordcloud/resources/stopwords.txt"
IMAGE_SAVE_LOCATION                     = "PornhubCommentsWordcloud/data/word_cloud.png"