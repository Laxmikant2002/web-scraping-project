from flask import Flask, render_template, request, redirect, url_for
from scraper.twitter_scraper import scrape_trending_topics

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', trend=None)

@app.route('/scrape', methods=['POST'])
def scrape():
    trend_data = scrape_trending_topics()
    return render_template('index.html', trend=trend_data)

if __name__ == '__main__':
    app.run(debug=True)