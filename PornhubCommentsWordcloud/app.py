import pornhub

#request_manager = pornhub_comments_wordcloud.utils.request_manage

def run():
   request_manager.get_videos()
    page = requests.get("https://www.pornhub.com/view_video.php?viewkey=ph58c466aa61bc5")
    #print (page.content)
    soup = bs(page.content, 'html.parser')
    #comments = soup.find_all(class_='commentMessage')
    comments = soup.select('.commentMessage > span')
    text = " ".join(comment.get_text() for comment in comments)
    print ("There are {} words in the combination of all comments.".format(len(text)))

    # Generate a word cloud image
    mnwordcloud = WordCloud(width=1600, height=800, colormap="inferno", background_color="white").generate(text)
    wordcloud.to_file("img/test.png")

    # Display the generated image:
    # the matplotlib way:
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.show()
    print (comments[123])
    for comment in comments:
       print (comment.get_text())

    print (soup.prettify())
