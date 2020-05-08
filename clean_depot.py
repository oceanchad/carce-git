import pandas as pd
import warnings

path = "/Users/chad/visualprojects/carce/carce-git/"
depot_raw = pd.read_csv(path+ "output3.csv")

depot_address = depot_raw["formatted_address"]
depot_name = depot_raw["name"]

# 從output.csv 中的店名去除各品牌

car_list = ["LEXUS", "HYUNDAI","現代","BMW","客運","NISSAN", "Suzuki", "SUZUKI", "匯豐", "滙豐", "賓士", "MIT", "honda", "LUXGEN", "Mazda", "mazda", "kia", "PGO", "pgo", "volvo"
, "三菱", "audi", "VOLVO", "TOYOTA", "Tesla"]
moto_list = ["kymco", "KYMCO", "yamaha", "YAMAHA", "宏佳騰", "sym", "SYM", "三陽", "gogoro", "捷安特", "重機", "山葉"]
other_list = ["加油", "展示", "驗", "服務", "電動", "車勢", "鍍膜", "玻璃", "機車", "神腦", "國小", "機器", "咖啡", "選物"]

# 從output.csv 中的店名去除各連鎖
chain_store = ["慶通" , "中油", "歐特耐", "車得適", "車麗屋", "真便宜", "新焦點", "黃帽", "耐途耐"]

region_rm = ["大安區", "北投區", "中山區", "中正區", "板橋區", "新莊區", "蘆洲區", "土城區", "金門", "澎湖", "馬公", "中國", "連江"]

name_filter = car_list + moto_list + other_list + chain_store
address_filter = region_rm

for item in name_filter:
    indexNames_item = depot_name.str.contains(item)
    depot_raw = depot_raw[~indexNames_item]

for item in address_filter:
    indexNames_item = depot_address.str.contains(item)
    depot_raw = depot_raw[~indexNames_item]
                
print(depot_raw["name"].value_counts())
submission = pd.DataFrame(depot_raw)
submission.to_csv("test2.csv", index=False)

