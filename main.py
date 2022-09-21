import json
from cProfile import label
from datetime import datetime
from typing import Callable

from define import Item, response_data_from_dict

print("asdf")

is_not_new: Callable[[Item], bool] = lambda i: i.days_in_clan > 30


with open("./data.json", "r", encoding="UTF-8") as f:
    resp = response_data_from_dict(json.load(f))

    # 최근 접속일 기준
    # items = sorted(resp.items, key=lambda item: item.last_battle_time)

    # 하루 전투수 기준
    items = sorted(resp.items, key=lambda item: item.battles_per_day)
    itmes = list(filter(is_not_new, items))
    items = items[-10:]

    for item in items:
        print(f"{item.name.rjust(30)}\t{datetime.fromtimestamp(item.last_battle_time).strftime('%Y-%m-%d %H:%M:%S')}\t{item.battles_per_day}")

    # for i in range(0, 10):
    #     item = items[i]
    #     print(f"{item.name}\t{datetime.fromtimestamp(item.last_battle_time).strftime('%Y-%m-%d %H:%M:%S')}")
