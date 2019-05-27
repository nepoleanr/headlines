from flask import Flask, render_template, request
import feedparser

# Application to retrieve rss feeds from select news websites

app = Flask(__name__)

RSS_FEEDS = {'bbc': 'http://feeds.bbci.co.uk/news/rss.xml',
    'cnn': 'http://rss.cnn.com/rss/edition.rss',
    'fox': 'http://feeds.foxnews.com/foxnews/latest',
    'dailymail': 'https://www.dailymail.co.uk/news/index.rss',
    'ndtv': 'http://feeds.feedburner.com/ndtvnews-top-stories',
    'timesnow': 'https://timesofindia.indiatimes.com/rssfeedstopstories.cms'
}

@app.route("/", methods=['GET', 'POST'])
#@app.route("/<publication>")
def get_news():
    query = request.form.get("publication")
    if not query or query.lower() not in RSS_FEEDS:
        publication = "bbc"
    else:
        publication = query.lower()
    feed = feedparser.parse(RSS_FEEDS[publication])
    #first_article = feed['entries'][0]
    return render_template("home.html", articles=feed['entries'])

if __name__ == "__main__":
    app.run(port=5000, debug=True)