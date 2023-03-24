#import libraries
import requests
from bs4 import BeautifulSoup 
import json

#scrape goat for new and upcoming releases

# url to scrape
url = "https://ac.cnstrc.com/browse/group_id/sneakers?c=ciojs-client-2.29.12&key=key_XT7bjdbvjgECO5d8&i=6b02deaa-56d2-4180-91ae-4e75e4721d34&s=2&page=1&num_results_per_page=24&filters%5Brelease_date%5D=20230101-20230331&sort_by=relevance&sort_order=descending&fmt_options%5Bhidden_fields%5D=gp_lowest_price_cents_3&fmt_options%5Bhidden_fields%5D=gp_instant_ship_lowest_price_cents_3&fmt_options%5Bhidden_facets%5D=gp_lowest_price_cents_3&fmt_options%5Bhidden_facets%5D=gp_instant_ship_lowest_price_cents_3&_dt=1679627722812"
# send get request
response = requests.get(url=url)
# parse the response content rec'd
output = json.loads(response.text)
# print sneaker title
print('Title: ' + output["response"]['results'][0]['value'])
# print sKU
print('SKU: ' + output["response"]['results'][0]['data']['sku'])
# print colorway
print('Color: ' +output["response"]['results'][0]['data']['color'])
# print image url
print('Image: ' +output["response"]['results'][0]['data']['image_url'])
# print release date
release_MMDD = str(output["response"]['results'][0]['data']['release_date'])
release_YY = str(output["response"]['results'][0]['data']['release_date_year'])
print('Release Date: ' + release_MMDD[4:6]+ "-" + release_MMDD[6:]+ "-" +release_YY)
# print retail price
retail_cents= output["response"]['results'][0]['data']['retail_price_cents']
retail_dollars = retail_cents/100
print('Retail $: ' +str(retail_dollars))











# find all items on the page
# create a empty list to store the items
# item_list = []
#loop through each item to find the information

#print results
# print(item_list)


# response > results > [i]> data > color, image url, id, value, release_date , retail_price_cents

