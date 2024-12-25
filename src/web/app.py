from flask import Flask, render_template, request, redirect, url_for
from database.mongodb import insert_trending_topics, get_latest_trending_topics
from scraper.twitter_scraper import scrape_trending_topics

app = Flask(__name__)

@app.route('/')
def index():
    trend = get_latest_trending_topics()
    return render_template('index.html', trend=trend)

@app.route('/scrape', methods=['POST'])
def scrape():
    try:
        trending_topics = scrape_trending_topics()
        insert_trending_topics(trending_topics)
    except Exception as e:
        print(f"Error during scraping: {e}")
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)