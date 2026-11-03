stock = {
    "หมึกพิมพ์": 5,
    "กระดาษ A4": 0,
    "สายแลน": 12,
    "เมาส์": 3,
    "แบตเตอรี่": 0,
    "ปากกา": 8
}
low_stock = []

for name,amount in stock.items():
    print (f"{name}: เหลือ {amount} ชิ้น")
    if(amount) < 5:
        low_stock.append(name)
print(f"รวมทั้งหมด :{ sum(stock.values())}  ใกล้หมด:{low_stock}")

