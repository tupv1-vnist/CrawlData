import requests
import time
import random
import pandas as pd

# cookies = {
#     'TIKI_GUEST_TOKEN': '8jWSuIDBb2NGVzr6hsUZXpkP1FRin7lY',
#     'TOKENS': '{%22access_token%22:%228jWSuIDBb2NGVzr6hsUZXpkP1FRin7lY%22%2C%22expires_in%22:157680000%2C%22expires_at%22:1763654224277%2C%22guest_token%22:%228jWSuIDBb2NGVzr6hsUZXpkP1FRin7lY%22}',
#     'amp_99d374': 'eSc-_0HT1um7cb57E7dwA0...1enloc6a2.1enlpc1q6.b.i.t',
#     'amp_99d374_tiki.vn': 'eSc-_0HT1um7cb57E7dwA0...1enloc6a2.1enlp8817.3.1.1',
#     '_gcl_au': '1.1.559117409.1605974236',
#     '_ants_utm_v2': '',
#     '_pk_id.638735871.2fc5': 'b92ae025fbbdb31f.1605974236.1.1605975278.1605974236.',
#     '_pk_ses.638735871.2fc5': '*',
#     '_trackity': '70e316b0-96f2-dbe1-a2ed-43ff60419991',
#     '_ga_NKX31X43RV': 'GS1.1.1605974235.1.1.1605975326.0',
#     '_ga': 'GA1.1.657946765.1605974236',
#     'ai_client_id': '11935756853.1605974227',
#     'an_session': 'zizkzrzjzlzizqzlzqzjzdzizizqzgzmzkzmzlzrzmzgzdzizlzjzmzqzkznzhzhzkzdzizhzdzizlzjzmzqzkznzhzhzkzdzizlzjzmzqzkznzhzhzkzdzjzdzhzqzdzizd2f27zdzjzdzlzmzmznzq',
#     'au_aid': '11935756853',
#     'dgs': '1605975268%3A3%3A0',
#     'au_gt': '1605974227146',
#     '_ants_services': '%5B%22cuid%22%5D',
#     '__admUTMtime': '1605974236',
#     '__iid': '749',
#     '__su': '0',
#     '_bs': 'bb9a32f6-ab13-ce80-92d6-57fd3fd6e4c8',
#     '_gid': 'GA1.2.867846791.1605974237',
#     '_fbp': 'fb.1.1605974237134.1297408816',
#     '_hjid': 'f152cf33-7323-4410-b9ae-79f6622ebc48',
#     '_hjFirstSeen': '1',
#     '_hjIncludedInPageviewSample': '1',
#     '_hjAbsoluteSessionInProgress': '0',
#     '_hjIncludedInSessionSample': '1',
#     'tiki_client_id': '657946765.1605974236',
#     '__gads': 'ID=ae56424189ecccbe-227eb8e1d6c400a8:T=1605974229:RT=1605974229:S=ALNI_MZFWYf2BAjzCSiRNLC3bKI-W_7YHA',
#     'proxy_s_sv': '1605976041662',
#     'TKSESSID': '8bcd49b02e1e16aa1cdb795c54d7b460',
#     'TIKI_RECOMMENDATION': '21dd50e7f7c194df673ea3b717459249',
#     'cto_bundle': 'V9Dkml9NVXNkQmJ6aEVLcXNqbHdjcVZoQ0l5RXpOMlRybjdDT0JrUnNxVXc2bHd0N2J3Y2FCdmZVQXdYY1QlMkJYUmxXSHZ2UEFwd3IzRHhzRWJYMlQlMkJsQjhjQlA1JTJCcExyRzlUQk5CYUdMdjl2STNQanVsa3cycHd3SHElMkJabnI3dzNhREpZcFVyandyM1d1QWpJbWYxT1UyWDdHZyUzRCUzRA',
#     'TIKI_RECENTLYVIEWED': '58259141',
#     '_ants_event_his': '%7B%22action%22%3A%22view%22%2C%22time%22%3A1605974691247%7D',
#     '_gat': '1',
# }

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'Referer': 'https://tiki.vn/thoi-trang-nam/c915',
    'x-guest-token': 'zQMefwYvjquxRsaEB5UdiKlNGg8kXhAC',
    'Connection': 'keep-alive',
    'TE': 'Trailers',
}

params = {
    'limit': '40',
    'include': 'advertisement',
    'aggregations': '2',
    'version': 'home-persionalized',
    'trackity_id': '127e24c6-fe2a-0c1a-799d-1a1ead20aeae',
    'category': '1686',
    'page': '1',
    'urlKey':  'giay-dep-nam',
}

def parser_product(json):
    d = dict()
    d['display_value'] = json.get('display_value')
    d['query_value'] = json.get('query_value')
    d['url_key'] = json.get('url_key')
    d['url_path'] = json.get('url_path')
    return d
categories=[]
response = requests.get('https://tiki.vn/api/personalish/v1/blocks/listings', headers=headers, params=params)

if response.status_code == 200:
    print('request success!!!')
    filters = response.json().get('filters', [])
    for filter_data in filters:
        display_name = filter_data.get('display_name')
        if display_name and display_name.lower() == "danh mục sản phẩm":
            values = filter_data.get('values', [])
            for value in values:
                categories.append(parser_product(value))

time.sleep(random.randrange(3, 10))

df = pd.DataFrame(categories)
df.to_csv('categories.csv', index=False)
