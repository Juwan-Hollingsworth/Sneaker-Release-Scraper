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

#loop through each result found in results for:
for result in output["response"]["results"]:
    print('------------------------------')
    print('Title: ' +result['value'])
    print('SKU: ' + result['data']['sku'])
    print('Color: ' + result['data']['color'])
    print('Image: ' +result['data']['image_url'])
    release_MMDD = str(result['data']['release_date'])
    release_YY = str(result['data']['release_date_year'])
    # 4:6 = capture 4-6 characters 6: =  
    print('Release Date: ' + release_MMDD[4:6] + "-" + release_MMDD[6:]+ "-" + release_YY)
    retail_cents= result['data']['retail_price_cents']
    retail_dollars= retail_cents/100
    print('Retail $:' + str(retail_dollars))
    print('------------------------------') 
