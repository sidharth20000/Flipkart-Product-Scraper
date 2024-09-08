# Flipkart Product Scraper

This Python script scrapes product information from Flipkart based on a user-provided search term and stores the data in a MongoDB database.

## Features

- Scrapes product data from Flipkart search results
- Handles pagination to scrape data from multiple pages
- Extracts detailed information for each product including name, price, rating, and feature ratings
- Stores the scraped data in a MongoDB database

## Requirements

- Python 3.x
- BeautifulSoup4
- requests
- pymongo

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/flipkart-scraper.git
   cd flipkart-scraper
   ```

2. Install the required packages:
   ```
   pip install beautifulsoup4 requests pymongo
   ```

3. Ensure you have MongoDB installed and running on your local machine.

## Usage

1. Run the script:
   ```
   python Flipkart.py
   ```

2. When prompted, enter the product you want to search for on Flipkart.

3. The script will scrape data from all available pages for that search term and store it in a MongoDB database named `Flipkart` in a collection named after your search term.

## Data Structure

The script collects the following information for each product:

- Product Name
- Price
- Rating
- Feature Ratings (detailed ratings for specific features of the product)

## Note

This script is for educational purposes only. Please be respectful of Flipkart's terms of service and robots.txt file. Consider implementing proper rate limiting and error handling for production use.
