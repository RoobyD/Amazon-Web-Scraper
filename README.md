# Amazon Web Scraper
This Python code analyzes reviewer profiles and estimates bias in order to evaluate the reliability of product reviews on Amazon. The script assesses the possibility of biased reviews for a certain product by using Selenium for web scraping.

# Features
Automated Web Scraping: Extracts customer reviews and reviewer profiles by automatically scanning websites using Selenium.

Reviewer Bias Estimation: This method determines the probability of bias by examining each reviewer's work. The 1-star and 5-star rating distribution is taken into account by the script as an indicator.

Calculates the Adjusted Average Score, taking into account the estimated bias of each reviewer, and outputs an adjusted average score for the product reviews.

# Getting Started
Clone the repository:

git clone https://github.com/RoobyD/Amazon-Web-Scraper.git

Install Dependencies:

pip install selenium webdriver_manager

Run the Program:

python main.py

Follow On-screen Instructions.

Choose to analyze the default product or enter a custom product URL. The script will output results, including biased users and overall statistics.

# Disclaimer
The goals of this project are research and education. Please abide by the terms of service of the websites being scraped and be mindful of the ethical and legal ramifications of web scraping.

Developed Fall '24.
