from pymongo import MongoClient
import os
from dotenv import load_dotenv
from datetime import datetime
import requests

load_dotenv()

class MongoDB:
    def __init__(self):
        self.client = MongoClient(os.getenv("MONGODB_URI"))
        self.db = self.client['twitter_trends']
        self.collection = self.db['trending_topics']

    def insert_trending_topics(self, topics):
        record = {
            "topics": topics,
            "date": datetime.now(),
            "ip_address": self.get_ip_address()
        }
        self.collection.insert_one(record)

    def get_latest_trending_topics(self):
        return list(self.collection.find().sort("date", -1).limit(1))

    def get_ip_address(self):
        try:
            response = requests.get('https://api.ipify.org?format=json')
            return response.json()['ip']
        except requests.RequestException as e:
            print(f"Error retrieving IP address: {e}")
            return None