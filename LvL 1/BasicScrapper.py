# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 14:32:25 2024

@author: User
"""

from bs4 import BeautifulSoup #import beautiful soup for parsing HTML and XML docs, helps avoid crashes in case of broken html
import requests

url = "https://www.newegg.ca/asus-geforce-rtx-4070-ti-tuf-rtx4070ti-o12g-gaming/p/N82E16814126606?Item=N82E16814126606"


result = requests.get(url) # Sends a GET request to the URL
doc = BeautifulSoup(result.text, "html.parser")# Parses the HTML text of the web page


prices = doc.find_all(string="$") #lloks for $ 

if prices:
    parent = prices[0].parent  # Get the parent element of the first occurrence
    strong = parent.find("strong")  # Find the <strong> tag within the parent element
    # Modification: Check if the <strong> element was found to avoid AttributeError
    if strong:
        print(strong.string)  # Print the string content of the <strong> element
    else:
        print("Price format changed, or <strong> tag not found.") #in case its not un USD or has the expected format
else:
    print("No prices found.")#in case its sold out or price not stated
