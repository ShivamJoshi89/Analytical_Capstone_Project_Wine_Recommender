# Analytical_Capstone_Project_Wine_Recommender
 Customers often struggle to find the perfect wine for different occasions, meals, and personal preferences. With a vast selection of wines, making an informed choice can be overwhelming. This project aims to solve this problem by creating an AI-powered chatbot that provides personalized wine recommendations based on user preferences and occasions.


# Wine Data Scraper
This Python script is designed to scrape wine-related data from the Vivino website. It extracts detailed information about various wines, including their taste characteristics, descriptions, prices, ratings, and more. Additionally, it downloads images of the wine labels and saves all the collected data into a CSV file.

Features
Web Scraping: Extracts wine data from multiple pages of the Vivino website.

Batch Processing: Processes wine links in batches to manage large datasets efficiently.

Image Downloading: Downloads wine label images and saves them locally.

Data Export: Saves the scraped data into a CSV file for further analysis.

Resume Capability: Can resume scraping from the last processed index in case of interruptions.

Error Handling: Includes robust error handling to manage network issues and unexpected webpage structures.

Requirements
Python 3.x

Libraries: requests, BeautifulSoup, pandas, re, time, os, random, tqdm

Installation
Clone the Repository:

bash
Copy
git clone https://github.com/yourusername/wine-data-scraper.git
cd wine-data-scraper
Install Required Libraries:

bash
Copy
pip install requests beautifulsoup4 pandas tqdm
Usage
Run the Script:

bash
Copy
python wine_scraper.py
Configuration:

BATCH_SIZE: Number of links to process at a time. Default is 100.

START_INDEX: Index to resume scraping from. Default is 0.

image_folder: Folder to save downloaded wine images. Default is "wine_images".

Output:

wine_data_with_images.csv: CSV file containing all scraped wine data.

wine_images/: Folder containing downloaded wine label images.

Code Overview
Main Components
Web Scraping:

The script starts by scraping the main webpage to extract product links.

It then navigates through pagination to collect all available wine links.

Data Extraction:

For each wine link, the script extracts detailed information such as winery, wine name, price, rating, country, region, wine type, grape type, and more.

It also extracts taste characteristics and food pairings.

Image Downloading:

The script downloads wine label images and saves them in the specified folder.

Batch Processing:

The script processes wine links in batches to manage large datasets and avoid overloading the server.

Data Saving:

The scraped data is saved into a CSV file. If the script is interrupted, it can resume from the last processed index.

Functions
extract_score(style_string): Extracts the score from taste characteristics.

extract_taste_characteristics(product_link, headers): Extracts taste characteristics from a wine product page.

download_image(image_url, wine_name): Downloads and saves wine label images.

Example Output
The CSV file (wine_data_with_images.csv) will contain the following columns:

Product Link: URL of the wine product page.

Winery: Name of the winery.

Wine Name: Name of the wine including vintage.

Country: Country of origin.

Region: Region of origin.

Wine Type: Type of wine (e.g., Red, White).

Grape Type: Type of grapes used.

Price: Current price of the wine.

Rating: Average rating of the wine.

Wine Description 1: Description from the wine facts table.

Wine Description 2: Editor's note description.

Food Pairing: Recommended food pairings.

Alcohol Content: Alcohol content percentage.

Allergens: List of allergens.

Bottle Closure: Type of bottle closure (e.g., Cork).

Image URL: URL of the wine label image.

Image Path: Local path to the downloaded image.

Taste Characteristics: Scores for various taste characteristics (e.g., Acidity, Tannin).

Notes
User-Agent Rotation: The script rotates User-Agent headers to avoid being blocked by the server.

Random Delays: Random delays are introduced between requests to mimic human behavior and avoid overloading the server.

Error Handling: The script includes error handling to manage network issues and unexpected webpage structures.

License
This project is licensed under the MIT License. See the LICENSE file for details.

Contributing
Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

Acknowledgments
Thanks to Vivino for providing a rich source of wine data.

Thanks to the developers of requests, BeautifulSoup, pandas, and tqdm for their excellent libraries.

The data is Scrapped from the following links from Vivino Website:
1. https://www.vivino.com/explore?e=eJw1zUEOwiAQheHbzLrWJq5m5w2MK2MMBWrQ0jYMrfb2Ig9W70-YfPjAB_Ju4oa8-nLbkN55FdJ8vZxpSY_PgTcVnI1qpDkYNlY0zf3OvZX4WJx-C33i7Z5O87SYI6bDnMpbl3hJ8f8hhwo11hqxhB5LDPXG2BKu3iw1rJDw9CLYgKGChAcMEhgYGfgBgjBa-Q%3D%3D

2. https://www.vivino.com/explore?e=eJw1zUEOwiAQheHbzLrWJq5m5w2MK2MMBWrQ0jYMrfb2Ig9W70-YfPjAB_Ju4rYhr77cNaR3XoU0Xy9nWtLrc-BNBWejGmkOho0VTXO_c28lPhan30KfeLun0zwt5ojpMKfy1iVeUvx_yKFCjbVGLKHHEkO9MbaEqzdLDSskPL0INmCoIOEBgwQGRgZ-ubNbLQ%3D%3D

3. https://www.vivino.com/explore?e=eJw1ysEOwiAMxvG36XlOoqfefAPjyRjDCkuIsBEKzr29ZNDT_5f2MxFn7dlCSHiC4BZUAwT9w8sAhI_7DWK9fwlhTQaNZYJ12nGynN_R0Ydhw6V4D1t-vuryyNhyblEt1_5TQDtXFO7QSVAEuYN8xywbYzucbKLA8h-qa0Zq


4. https://www.vivino.com/explore?e=eJw1zcsOwiAQheG3mTW1TVzNzjcwrowxFKhBewtD1b69yIHV-RMmH1PghiY_c6MUTfrLTavI7LwJGb6cT7Sm98fAbx28i3qkJVi2Tgwt_c69k3hfvXkJfeL1lk7zHDAtpsMcy1uXeEnx_yGHDjW2GrGEGUsM9ca6Er7erDWckPD8JNiAoYKEBwwSGBgZ-AEhFVuM


5. https://www.vivino.com/explore?e=eJw1zUEOgjAQheHbzJoKCavZeQPjyhhTSjFVCqRTUG5v5bWr9yedfPWBFXk3saor8vrLqq3I7LwKGb5ezrSk9-fAmw7ORj3SHHrurRiau507K_GxOPMW-sTbPZ0ec8LUmAbT5rcm8ZLi_8MROpRYS8QcZswxlJve5nDlZilhhYSnF8EGDBUkPGCQwMA4gB8oEVuT