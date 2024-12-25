from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from pymongo import MongoClient
import os
import time
from dotenv import load_dotenv

load_dotenv()

def get_proxymesh_driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run in headless mode
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    
    # ProxyMesh configuration
    proxymesh_user = os.getenv('proxymesh_user')
    proxymesh_pass = os.getenv('proxymesh_pass')
    proxy = f"http://{proxymesh_user}:{proxymesh_pass}@proxy.proxymesh.com:31280"
    chrome_options.add_argument(f'--proxy-server={proxy}')
    
    service = Service('path/to/chromedriver')  # Update with your chromedriver path
    driver = webdriver.Chrome(service=service, options=chrome_options)
    return driver

def login_to_twitter(driver):
    driver.get("https://twitter.com/login")
    time.sleep(3)  # Wait for the page to load

    email_input = driver.find_element(By.NAME, "text")
    email_input.send_keys(os.getenv('X_EMAIL'))
    email_input.send_keys(Keys.RETURN)
    time.sleep(3)

    password_input = driver.find_element(By.NAME, "password")
    password_input.send_keys(os.getenv('X_PASS'))
    password_input.send_keys(Keys.RETURN)
    time.sleep(5)  # Wait for login to complete

def scrape_trending_topics(driver):
    driver.get("https://twitter.com/explore/tabs/trending")
    time.sleep(5)  # Wait for the page to load

    trends = driver.find_elements(By.XPATH, '//div[@data-testid="trend"]')
    trending_topics = [trend.text for trend in trends[:5]]  # Get top 5 trends
    return trending_topics

def insert_trends_to_mongodb(trending_topics):
    client = MongoClient(os.getenv('MONGODB_URI'))
    db = client['twitter_trends']
    collection = db['trends']
    
    record = {
        "trends": trending_topics,
        "date": time.strftime("%Y-%m-%d %H:%M:%S"),
        "ip_address": os.getenv('proxymesh_user')  # Assuming this is the IP used
    }
    collection.insert_one(record)

def main():
    driver = get_proxymesh_driver()
    try:
        login_to_twitter(driver)
        trending_topics = scrape_trending_topics(driver)
        insert_trends_to_mongodb(trending_topics)
    finally:
        driver.quit()

if __name__ == "__main__":
    main()