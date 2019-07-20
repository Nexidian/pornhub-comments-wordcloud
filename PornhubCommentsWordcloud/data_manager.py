# -*- coding: utf-8 -*-
from .core import *
from .request_manager import RequestManager
import csv
import re
import string


class DataManager(object):

    def __init__(self, *args):
        pass

    def _file_cache_exists(self):
        return path.isfile(MOST_VIEWED_LINKS_CACHE_FILE_LOCATION)

    def _get_most_viewed_links_from_cache(self):
        return list(line.strip() for line in open(MOST_VIEWED_LINKS_CACHE_FILE_LOCATION))

    def _scrap_most_viewed(self, soup_data):
        """
        Get the most viewed videos of all time 

        :param soup_data: a BS4 object containing HTML from a request
        """
        video_links = soup_data.select('.container a.linkVideoThumb')
        links = list()
        for link in video_links:
            links.append(link['href'])
        print("Got {} most viewed links".format(len(links)))
        return links

    def _cache_most_viewed_links(self, links_to_cache):
        """
        Write the most viewed links to a file for faster loading and fewer http requests
        """
        if len(links_to_cache) <= 0:
            print("Nothing to cache.")
        else:
            f = open(MOST_VIEWED_LINKS_CACHE_FILE_LOCATION, "w+")
            for link in links_to_cache:
                print("Writing link {} to cache".format(link))
                f.write(link + '\n')

    def _scrap_comments(self, soup_data):
        """
        Extract and parse the comments

        :param soup_data: a BS4 object containing HTML from a request
        """
        parsed_text = ""
        # todo: Tidy this up, I had problems with the wordcloud api which 
        # foced me to split this logic out into multiple for each loops
        raw_comments = soup_data.select('.commentMessage > span')
        for comment in raw_comments:
            text = comment.get_text()
            for word in text.split():
                if not word.startswith('https') and not word.startswith('http'):
                    parsed_text += word + " "
        parsed_text = parsed_text.replace('\n', ' ').replace('\r', ' ')
        # the wordcloud module has a hard time seperating punctuation, so take it out here
        parsed_text = parsed_text.translate(str.maketrans('', '', string.punctuation))
        return parsed_text.encode('ascii', errors='ignore')

    def _get_comments(self, link):
        """
        Get comments for a single video

        :param link: A single link to a video
        """
        request_manager = RequestManager()
        return self._scrap_comments(request_manager.get_video(link))

    def _write_csv(self, links):
        """
        Writes the comments to a cache file for faster loading and less http requests

        :param links: A list of links that we should retreive comments for
        """
        print ('Writing CSV')
        f = open(COMMENTS_CACHE_FILE_LOCATION, mode='w', newline='')
        index = 0
        writer = csv.writer(f, delimiter=',', quotechar='"',
                            quoting=csv.QUOTE_MINIMAL)
        writer.writerow(['id', 'link', 'comments'])
        for link in links:
            comments = self._get_comments(link)
            writer.writerow([index, link, comments])
            index += 1

    def _create_word_cloud(self):
        """
        Read from the CSV and generate the wordcloud
        """
        df = pd.read_csv(COMMENTS_CACHE_FILE_LOCATION, index_col=0)
        text = " ".join(comment for comment in df.comments)
        print("There are {} words in the combination of all comments.".format(len(text)))

        stopwords = set(line.strip() for line in open(STOPWORDS_FILE_LOCATION))

        wordcloud = WordCloud(width=1600, height=800, colormap="magma",
                              stopwords=stopwords, background_color="white", relative_scaling=0, prefer_horizontal=1, collocations=False).generate(text)
        wordcloud.to_file(IMAGE_SAVE_LOCATION)
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis("off")
        plt.show()

    def generate_wordcloud(self, video_count, use_cache):
        """
        Generate the word cloud based on comments

        :param video_count: How many videos to use
        :param use_cache: Should we utilise file cache to lessen requests
        """
        request_manager = RequestManager()
        video_links = list()

        if self._file_cache_exists() and use_cache:
            print("Getting links from cache")
            video_links = self._get_most_viewed_links_from_cache()
        else:
            print("Not using cache")
            page_num = 1
            while len(video_links) < video_count:
                links_retrieved = self._scrap_most_viewed(
                    request_manager.get_most_viewed_links(page_num))
                print(links_retrieved)
                for link in links_retrieved:
                    video_links.append(link)
                    page_num += 1
            video_links = video_links[0:video_count]
            self._cache_most_viewed_links(video_links)
            self._write_csv(video_links[0:video_count])

        self._create_word_cloud()
