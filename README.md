# pornhub-comments-wordcloud
This is a small python app that gets the most viewed videos, globabally, from Pornhub. It then gets the comments from the videos and generates a word cloud from them. This allows us to the most prevalent words that appear in the comment section.


This script uses the fantastic [wordcloud generator](https://github.com/amueller/word_cloud) go check it out!

There is not too much to this script, i have commented the parts which arnt as clear, but if you have any questions or issues please let me know! 


# Usage


## **Create the client**
```python
import PornhubCommentsWordcloud
app = PornhubCommentsWordcloud.PornhubCommentsWordcloud()
```

## **Query and generate a word cloud**
```python
app.generate_wordcloud(video_count=100, use_cache=True)
```
If ```use_cache``` is true the script will attempt to read from files generated from a previous run. This is useful if you already have completed data retrival and just want to mess with the word cloud generation. If this is set to false it will attempt the http requests regardless of if there is a cached file present.

# **Making changes**
## **data_manager.py**
This is where the bulk of the code lays. If you wanted to make changes to the word cloud generation parameters this would be the place to do it. 

## **stopwords.txt**
I have included a list of stopwords that i felt needed removing from weighting consideration. These includes words like:
```text
We
that
them
then
what
because
or
get
```
If you would like to remove, or add your own words to be removed from the final image, this is the place to do it. 

# License


## **MIT License**