from cProfile import label
from datetime import datetime, timedelta
import json

from define import ResponseData, response_data_from_dict

print("asdf")


f = open("./data.json", "r", encoding="UTF-8")

resp= response_data_from_dict(json.load(f))

# 최근 접속일 기준
items = sorted(resp.items, key=lambda item: item.last_battle_time)

# 하루 전투수 기준
# items = sorted(resp.items, key=lambda item: item.battles_per_day)
# items.reverse()

for item in items:
    print(f"{item.name.rjust(30)}\t{datetime.fromtimestamp(item.last_battle_time).strftime('%Y-%m-%d %H:%M:%S')}\t{item.battles_per_day}")

# for i in range(0, 10):
#     item = items[i]
#     print(f"{item.name}\t{datetime.fromtimestamp(item.last_battle_time).strftime('%Y-%m-%d %H:%M:%S')}")

