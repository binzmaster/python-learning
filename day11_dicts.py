count = {}
for dept in ["IT", "HR", "IT", "IT", "HR", "GIS"]:
    count[dept] = count.get(dept, 0) + 1
print(count)

statuses = ["done", "pending", "done", "cancel", "pending", "done"]
result = {}
for s in statuses:
    result[s] = result.get(s, 0)+1
print(result)

stock = {"paper": 10, "ink": 3, "toner": 5}
item = "cable"
qty = 4
if item in stock:
    stock[item] = qty+stock[item]
else:
    stock[item] = qty

print (stock)


repair = {"id": "R02", "item": "pc", "dept": "GIS"}
print(repair["item"])
print(repair.get("owner","ยังไม่ระบุ"))
print(repair.get("status"))


repair = {"id": "R02", "item": "pc", "dept": "GIS"}

repair["owner"] = "สมชาย"
repair["dept"] = "IT"
repair["urgent"] = True

print(repair)


repair = {"id": "R02", "item": "pc", "dept": "IT"}

repair["owner"] = "สมชาย"
if "owner" in repair:
    print(repair["owner"])
else:
    print("ยังไม่มีผู้รับผิดชอบ")

repair = {"id": "R01", "item": "printer", "note": "ทดสอบ", "urgent": True}
old_note = repair.pop("note")
old_phone = repair.pop("phone","ไม่มี")
print(old_note)
print(old_phone)
print(repair)

repair = {"id": "R03", "item": "scanner", "dept": "GIS", "note": "รอตรวจ"}
print(repair.get("owner","ยังไม่ระบุ"))
repair["owner"] = "สมหญิง"
repair["dept"] = "IT"
if "note" in repair:
    deleted_note = repair.pop("note")
    print(f"ลบ note แล้ว: {deleted_note}")
else:
    print("ไม่มี note")

print(repair)


job = {"id": "J09", "dept": "HR", "status": "pending"}

a = job.get("owner", "ไม่มี")
b = "HR" in job
c = "dept" in job
d = job.pop("status")
e = job.pop("status", "หายแล้ว")

print(a) # ไม่มี
print(b) # Error
print(c) # HR
print(d) # {"id": "J09", "dept": "HR"}
print(e) #  หายแล้ว
print(job) # {"id": "J09", "dept": "HR"}

stock = {
    "หมึกพิมพ์": 5,
    "กระดาษ A4": 0,
    "สายแลน": 12,
    "เมาส์": 3
}
item ="คีย์บอร์ด"
if item in stock:
    if stock[item] == 0:
        stock.pop(item)
        print(f"ลบ {item} ออกจากระบบแล้ว")
    else:
        print (f"{item} ยังเหลือ {stock[item]} ชิ้น ลบไม่ได้")
else: 
    print(f"{item} ไม่มีในระบบ")
print(stock)