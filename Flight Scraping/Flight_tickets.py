from time import sleep
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import os
import requests
import json


r = requests.get('https://serpapi.com/search.json?engine=google_flights&departure_id=PEK&arrival_id=AUS&outbound_date=2024-04-28&return_date=2024-05-04&currency=USD&hl=en')

import serpapi

params = {
  "engine": "google_flights",
  "departure_id": "ALB",
  "arrival_id": "BQN",
  "outbound_date": "2024-07-18",
  "return_date": "2024-07-25",
  "currency": "USD",
  "hl": "en",
  "api_key": "ced838a8b3bbbfab06a1ace2fedae5861c000f70741a82c08c33adb613f7dffa"
}



search = serpapi.search(params)
results = search.as_dict()

json_file = json.dumps(results,indent=4)

print (json_file)
with open("flight.json","w") as outfile:
    outfile.write(json_file)

