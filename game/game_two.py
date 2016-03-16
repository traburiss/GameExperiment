# Created by Traburiss on 2016/3/16
from Tools.my_dj_memory import MyDjMemory

db = MyDjMemory()
db.insert("101100010", 2, 122, 231)
# value = db.search()
value = db.search_by_face_state("101100010")
print(len(value))
for item in value:
    print(item)
