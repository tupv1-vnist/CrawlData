import pandas as pd
import requests
import time
import random
from tqdm import tqdm

cookies = {
    
    "_ga": "GA1.1.1849613058.1700793484",
    "_fbp": "fb.1.1700793484151.839633581",
    "_ga_W6PZ1YEX5L": "GS1.1.1700793483.1.1.1700794858.0.0.0",
    "_trackity": "127e24c6-fe2a-0c1a-799d-1a1ead20aeae",
    "_gcl_aw": "GCL.1700800072.CjwKCAiAjfyqBhAsEiwA-UdzJJgVXmmGxsJvQCHgmpfqVR6JfUMhBeeunE8bauJgobw7gdrjzSz2hhoC_SEQAvD_BwE",
    "_gcl_au": "1.1.1352377059.1700800072",
    "__uidac": "01656026489b4411005775a7c0df330c",
    "dtdz": "ed0e0bbc-3941-4dc8-99d8-e760356edcde",
    "__RC": "4",
    "__R": "1",
    "TOKENS": "{\"access_token\":\"zQMefwYvjquxRsaEB5UdiKlNGg8kXhAC\"}",
    "_hjSessionUser_522327": "eyJpZCI6IjljN2E3NGFlLTM0ZmEtNTEyOS1hY2E3LTNkOThkMWMxNDk1YyIsImNyZWF0ZWQiOjE3MDA4MDAwNzI2NzgsImV4aXN0aW5nIjp0cnVlfQ==",
    "__iid": "749",
    "__su": "0",
    "__tb": "0",
    "TKSESSID": "755a0a6897a8701eb5c6641cdb137a07",
    "delivery_zone": "Vk4wMzQwMjQwMTM=",
    "tiki_client_id": "1849613058.1700793484",
    "_hjIncludedInSessionSample_522327": "0",
    "_hjSession_522327": "eyJpZCI6ImYwYmQwYjk2LTc5YTQtNDBmOS05NGY5LTZmYTljZGVjNGI0YSIsImMiOjE3MDQ2NDExMzAzNDEsInMiOjAsInIiOjAsInNiIjowfQ==",
    "_hjAbsoluteSessionInProgress": "1",
    "__IP": "1897343787",
    "amp_99d374": "0mIrlDbJ8D8blratjRgDNv...1hji8emtf.1hji8guvc.2m.44.6q",
    "__uif": "__uid%3A1480285911984199185%7C__ui%3A2%252C5%7C__create%3A1678028591",
    "cto_bundle": "vOlR3V9GRk5PaTZMUmR2RWt3bW1iRjlDTVdWT01ZVTJEdGpwN2ptdEcxa212QXRtUDI2MmhvSGd2Sk8zTmlCOHAwdmE1bkx4dVR1OXUwRnBKcGxUSWdNR3ZBZXhjcEhCcGF6MUkwQ2J5NjR2a1JGN1ZLdDdGY0szMDJ1OHQxeXkzcGZwS3Z4VDJvQ1hGaUVldGpSa1Q4cmlpNFElM0QlM0Q",
    "_ga_S9GLR1RQFJ": "GS1.1.1704641126.7.1.1704642014.60.0.0"
}



headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'Referer': 'https://tiki.vn/combo-3-ao-thun-nam-mau-moi-logo-truo-c-ngu-c-db3qc16-p22610869.html?itm_campaign=SRC_YPD_TKA_PLA_UNK_ALL_UNK_UNK_UNK_UNK_X.264410_Y.1846730_Z.3821569_CN.Combo-3-Ao-Thun-nam-HANG-HIEU-da-phong-cach---%C4%90B3QC16-05%2F08%2F2023&itm_medium=CPC&itm_source=tiki-ads&spid=23503245',
    'x-guest-token': 'zQMefwYvjquxRsaEB5UdiKlNGg8kXhAC',
    'Connection': 'keep-alive',
    'TE': 'Trailers',
}

params = (
    ('platform', 'web'),
    ('spid', 56919858),
    ('version',3)
    #('include', 'tag,images,gallery,promotions,badges,stock_item,variants,product_links,discount_tag,ranks,breadcrumbs,top_features,cta_desktop'),
)

def parser_product(json):
    d = dict()
    d['id'] = json.get('id')
    d['sku'] = json.get('sku')
    d['name']=json.get('name')
    d['day_ago_created']=json.get('day_ago_created')
    d['short_description'] = json.get('short_description')
    d['price'] = json.get('price')
    d['list_price'] = json.get('list_price')
    d['price_usd'] = json.get('price_usd')
    d['all_time_quantity_sold']=json.get('all_time_quantity_sold')
    d['discount'] = json.get('discount')
    d['discount_rate'] = json.get('discount_rate')
    d['review_count'] = json.get('review_count')
    d['rating_average']=json.get('rating_average')
    d['order_count'] = json.get('order_count')
    d['inventory_status'] = json.get('inventory_status')
    d['is_visible'] = json.get('is_visible')
    d['stock_item_qty'] = json.get('stock_item',{}).get('qty',0)
    d['stock_item_max_sale_qty'] = json.get('stock_item',{}).get('max_sale_qty',{})
    d['product_name'] = json.get('meta_title')
    d['brand_id'] = json.get('brand').get('id')
    d['brand_name'] = json.get('brand').get('name')
    d['categories_id']=json.get('categories',{}).get('id',{})
    d['categories_name']=json.get('categories',{}).get('name',{})

    return d


df_id = pd.read_csv('product_id.csv')
p_ids = df_id.id.to_list()
print(p_ids)
result = []
for pid in tqdm(p_ids, total=len(p_ids)):
    response = requests.get('https://tiki.vn/api/v2/products/{}'.format(pid), headers=headers, params=params, cookies=cookies)
    
    if response.status_code == 200:
        try:
            data = response.json()
            result.append(parser_product(data))
            print('Crawl data {} success !!!'.format(pid))
        except requests.exceptions.JSONDecodeError:
            print('Error decoding JSON for {}. Response content is not in JSON format.'.format(pid))
    else:
        print(f'Request for {pid} failed with status code {response.status_code}.')

    # time.sleep(random.randrange(3, 5))

df_product = pd.DataFrame(result)
df_product.to_csv('crawled_data_ncds.csv', index=False)
