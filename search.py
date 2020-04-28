import googlemaps
import os
import pandas as pd
import time

gmaps = googlemaps.Client(key='AIzaSyBP5NrygNOIbmWPbXxZ8pyOY9UeCL__qCk')

# "臺北市","新北市","桃園市","基隆市","新竹市","新竹縣",
# "臺中市","臺南市","高雄市","嘉義市", "苗栗縣","彰化縣","南投縣","雲林縣","嘉義縣","屏東縣","宜蘭縣","花蓮縣","臺東縣"
cities= ["臺北市","新北市","桃園市","基隆市","新竹市","新竹縣"]


ids = []
for city in cities:
    results = []
    # Geocoding an address
    geocode_result = gmaps.geocode(city)
    loc = geocode_result[0]['geometry']['location']
    query_result = gmaps.places_nearby(keyword="車廠",location=loc, radius=10000)
    results.extend(query_result['results'])
    while query_result.get('next_page_token'):
        time.sleep(2)
        query_result = gmaps.places_nearby(page_token=query_result['next_page_token'])
        results.extend(query_result['results'])    
    # print("找到以"+city+"為中心半徑10000公尺的車廠店家數量(google mapi api上限提供60間): "+str(len(results)))
    for place in results:
        ids.append(place['place_id'])

stores_info = []
# 去除重複id
ids = list(set(ids)) 
for id in ids:
    stores_info.append(gmaps.place(place_id=id, language="zh-TW")['result'])

output = pd.DataFrame.from_dict(stores_info)

output.to_csv('output.csv', index=False, encoding="utf-8")


# 從output.csv 中的店名去除各品牌

car_list = ["LEXUS", "HYUNDAI", ]

# 從output.csv 中的店名去除各連鎖
Chain_store = ["慶通" , "中油", "歐特耐", "車得適", "車麗屋", "真便宜", "新焦點", "黃帽", "耐途耐"]

