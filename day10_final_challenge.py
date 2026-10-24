devices = ["Printer", "Monitor", "Server", "Printer", "Notebook", "Monitor", "Printer"]
costs = [1800, 1200, 12000, 2500, 4500, 1500, 900]

devices_result = sorted(set(devices),reverse=False )

print(f"ประเภทอุปกรณ์ที่ไม่ซ้ำ: {devices_result} ({len(devices_result)} ประเภท)")

count = 0
total = 0
count_index = 0
for device in devices:
    if  device == "Printer":
        total = total+ costs[count_index]
        count = count+1
    count_index = count_index+1


print(f"Printer ซ่อม {count} ครั้ง")
print(f"ค่าซ่อม Printer รวม {total :,} บาท")

print(f"แพงที่สุด: {devices[costs.index(max(costs))]} {(max(costs)):,} บาท")
cost = sorted(costs)
print(f"ถูกที่สุด 3 อันดับ: {cost[:3]}")
