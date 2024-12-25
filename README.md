# Project Title: Twitter Trending Topics Scraper

## Description
This project is a web scraping application that uses Selenium and ProxyMesh to fetch the top 5 trending topics from Twitter. The scraped data is stored in MongoDB and displayed on a beautifully designed HTML webpage using Flask.

## Setup Instructions
1. **Clone the repository:**
   ```
   git clone <repository-url>
   cd web-scraping-project
   ```

2. **Create a virtual environment:**
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies:**
   ```
   pip install -r requirements.txt
   ```

4. **Configure environment variables:**
   Create a `.env` file in the root directory and add your ProxyMesh credentials, Twitter account details, and MongoDB URI:
   ```
   proxymesh_user=your_proxymesh_username
   proxymesh_pass=your_proxymesh_password
   X_EMAIL=your_TWITTER_email
   X_PASS=your_TWITTER_password
   X_USER=your_TWITTER_username
   MONGODB_URI=your_mongoDB_URI
   ```

5. **Run the application:**
   ```
   python src/main.py
   ```

6. **Access the application:**
   Open your web browser and go to `http://127.0.0.1:5000`.

## Usage
- Click the "Scrape Data" button to fetch the top 5 trending topics from Twitter.
- The results will be displayed on the same page, including the trending topics and the IP address used for the query.

## Features
- Utilizes Selenium for web scraping.
- Stores data in MongoDB.
- Beautifully designed HTML interface using Bootstrap.
- Error handling for network requests and data extraction.
- Displays the IP address used for the query.

## Contributing
Feel free to submit issues or pull requests for improvements or bug fixes.
