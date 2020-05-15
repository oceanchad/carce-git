from os import listdir
from os.path import isfile, join, expanduser
from os import environ
import pandas as pd
import warnings
import time
warnings.filterwarnings("ignore")

print("需要輸入以下資料的路徑\n1. 欲過濾*清單*所在資料夾\n2. 欲過濾*區域*所在資料夾\n3. 資料所在資料夾路徑\n4. 資料名稱\n")

path_depot = input("請輸入欲過濾清單(以絕對路徑的資料夾表示)\n備註： 會自動載入資料夾中所有清單(eg. /Users/chad/visualprojects/carce/carce-git/filter/)\n")
path_region = input("請輸入欲過濾區域(以絕對路徑的資料夾表示)\n備註： 會自動載入資料夾中所有清單\n")
data_path = input("請輸入資料所在資料夾路徑\n")
file = input("請輸入資料名稱\n備註：檔案需是csv格式\n")

depot_raw = pd.read_csv(data_path+ file+".csv")

depot_address = depot_raw["formatted_address"]
depot_name = depot_raw["name"]

print("處理中...")
time.sleep(2)

for filename in listdir(path_depot):
    with open(join(path_depot, filename), 'r') as f:
        lines = f.readlines()
    lines = [line.replace(" ", "") for line in lines]
    with open(join(path_depot, filename), "w") as f:
        f.writelines(lines)

all_list = []
for filename in listdir(path_depot):
    with open(join(path_depot, filename), 'r') as f:
        lines = f.readlines()
        all_list.extend(lines)
new_all_list = [x.replace("\n", "") for x in all_list]

for filename in listdir(path_region):
    with open(join(path_region, filename), 'r') as f:
        lines = f.readlines()
    lines = [line.replace(" ", "") for line in lines]
    with open(join(path_region, filename), "w") as f:
        f.writelines(lines)

region_list = []
for filename in listdir(path_region):
    with open(join(path_region, filename), 'r') as f:
        lines = f.readlines()
        region_list.extend(lines)
new_region_list = [x.replace("\n", "") for x in region_list]

for item in new_all_list:
    indexNames_item = depot_name.str.contains(item)
    depot_raw = depot_raw[~indexNames_item]

for item in new_region_list:
    indexNames_item = depot_address.str.contains(item)
    depot_raw = depot_raw[~indexNames_item]
                
print(depot_raw["name"].value_counts())
print("data 已清理完...\n將輸出到桌面...\n")
time.sleep(1)
output_name = input("請輸入輸出的檔名\n")
desktop =expanduser("~/Desktop/")

submission = pd.DataFrame(depot_raw)
submission.to_csv(desktop+output_name+".csv", index=False)

