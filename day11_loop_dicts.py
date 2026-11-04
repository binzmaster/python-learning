stock = {
    "หมึกพิมพ์": 5,
    "กระดาษ A4": 0,
    "สายแลน": 12,
    "เมาส์": 3,
    "แบตเตอรี่": 0,
    "ปากกา": 8
}

best_name = ""
best_amount = 0

for name,piece in stock.items():
    if piece > best_amount:
        best_name = name
        best_amount = piece 

print (f"เหลือมากสุด:{best_name} ({best_amount} ชิ้น) ")

items = [
    {"name": "หมึกพิมพ์",  "qty": 5,  "price": 450},
    {"name": "กระดาษ A4", "qty": 0,  "price": 120},
    {"name": "สายแลน",    "qty": 12, "price": 35},
    {"name": "เมาส์",      "qty": 3,  "price": 250},
    {"name": "แบตเตอรี่",  "qty": 0,  "price": 90}
]
name_item = []
qty_result=[]
total_result = 0
for item in items:
    print(f"name:{item["name"]} {item["qty"]} ชิ้น ราคา{item["price"]} บาท")
    total_result = (item["qty"]*item["price"])+ total_result
    if item["qty"] == 0:
        name_item.append(item["name"])
print(f"มูลค่าสต็อกรวม: {total_result} บาท และ ของหมด: {name_item}")
