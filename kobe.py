#import libraries
import requests
from bs4 import BeautifulSoup 
import json

# url to scrape
url = "https://ac.cnstrc.com/browse/group_id/sneakers?c=ciojs-client-2.29.12&key=key_XT7bjdbvjgECO5d8&i=6b02deaa-56d2-4180-91ae-4e75e4721d34&s=2&page=1&num_results_per_page=24&filters%5Brelease_date%5D=20230101-20230331&sort_by=relevance&sort_order=descending&fmt_options%5Bhidden_fields%5D=gp_lowest_price_cents_3&fmt_options%5Bhidden_fields%5D=gp_instant_ship_lowest_price_cents_3&fmt_options%5Bhidden_facets%5D=gp_lowest_price_cents_3&fmt_options%5Bhidden_facets%5D=gp_instant_ship_lowest_price_cents_3&_dt=1679627722812"
# send get request
response = requests.get(url=url)
# parse the response rec'd
soup = BeautifulSoup(response.content, "html.parser")
print(soup)


