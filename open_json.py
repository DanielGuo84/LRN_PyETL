#建立圖的索引
import json
person1 = {"name":"Elwing", "height":175}
person2 = {"name":"Bob", "height":180}
saved = [person1, person2]

f = open("result.json", "w", encoding="utf-8")
json.dump(saved, f)
f.close()