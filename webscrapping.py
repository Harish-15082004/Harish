import requests
from bs4 import BeautifulSoup
import pandas as pd

# Function to fetch data from Flipkart
def fetch_flipkart_data(search_query, num_pages=1):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    base_url = "https://www.flipkart.com/search?q="

    product_list = []

    for page in range(num_pages):
        url = base_url + search_query + "&page=" + str(page + 1)
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.content, "html.parser")

        # Find all product containers
        products = soup.find_all("div", class_="_1AtVbE")

        for product in products:
            try:
                # Get product name
                name = product.find("a", class_="IRpwTa").text
            except AttributeError:
                name = None

            try:
                # Get product price
                price = product.find("div", class_="_30jeq3").text
            except AttributeError:
                price = None

            try:
                # Get product rating
                rating = product.find("div", class_="_3LWZlK").text
            except AttributeError:
                rating = None

            if name and price:
                product_list.append({
                    "Product Name": name,
                    "Product Price": price,
                    "Product Rating": rating
                })

    return product_list

# Search for products
search_query = "laptop"  # Replace with your search query
num_pages = 2  # Number of pages to scrape

data = fetch_flipkart_data(search_query, num_pages)

# Save to CSV file
df = pd.DataFrame(data)
df.to_csv("flipkart_products.csv", index=False)

print("Data has been written to flipkart_products.csv")
