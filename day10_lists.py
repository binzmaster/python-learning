tasks = ["ตรวจเมล", "ประชุม", "เขียนรายงาน"]

tasks.append("ส่งไฟล์")
tasks.insert(0,"ดื่มกาแฟ")
tasks.remove("ประชุม")
print(tasks)

tasks = ["ตรวจเมล", "ประชุม", "เขียนรายงาน"]
target = "ประชุม"
current = tasks.pop(0)


print(f"กำลังทำ: {current}")
print(f"คิวที่เหลือ: {tasks}")
if target in tasks:
    tasks.remove(target)
    print(f"ลบ {target} แล้ว")
else:
    print(f"ไม่พบ {target} ใน List")

costs = [4500, 1800, 12000, 1200, 2500]       # [60, 70, 80, 95]

costs.sort()
print(costs)
costs.sort(reverse=True)
print(costs)
costs = [4500, 1800, 12000, 1200, 2500]       # [60, 70, 80, 95]
news_costs = sorted(costs)
print(costs)
print(news_costs)

#--- 10.4 slicing ---
data = [5, 8, 5, 9, 5, 7]
print(data[1:3]) # ค่าที่ได้ 8,5 
print(data[-3:]) # ค่าที่ได้ 9 ,5 ,7
print(data.count(5)) # ค่าที่ได้ 2
print(data.index(9)) # ค่าที่ได้ index  3
#--- 10.4 slicing ---
scores = [70, 95, 80, 60, 85, 95]
print(scores[0:3])
print(scores[-2:])
print(scores.count(95))
target=80
if target in scores:
    print(f"ตำแหน่งใน index เป็น {scores.index(target)}")
else :
    print(f"ไม่พบ {target}")
#10_list
costs = [4500, 1800, 12000, 1200, 2500]
print (sum(costs))
print(f"สูงสุด {max(costs)} ต่ำสุด {min(costs)}")
print(f"ค่าเฉลี่ย {sum(costs)/len(costs):,.2f} บาท")
count = 0
for cost in costs:
    if cost == max(costs):
        print (f"ตำแหน่ง index {count}")
    count = count+1

# --- 10.6 tuple/set ---
point = (13.75, 100.50)       # พิกัด (ละติจูด, ลองจิจูด)
point[0] = 14.0               # TypeError: 'tuple' object does not support item assignment
point.append(5)               # AttributeError: ไม่มี append