stock = {
    "หมึกพิมพ์": 5,
    "กระดาษ A4": 0,
    "สายแลน": 12,
    "เมาส์": 3,
    "แบตเตอรี่": 0,
    "ปากกา": 8
}

total = 0
outofstock =[]
for name in stock:
    total = stock[name]+ total
    if stock[name] == 0:
        outofstock.append(name)


for name in outofstock:
    stock.pop(name)

print(f"สินค้าทั้งหมด {total}")
print("สินค้าที่หมด:", outofstock)

print(stock)


