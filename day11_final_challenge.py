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



stock = {
    "หมึกพิมพ์": 5,
    "กระดาษ A4": 0,
    "สายแลน": 12,
    "เมาส์": 3
}

item = "คีย์บอร์ด"
amount = 1

if item in stock:
    if stock[item] < amount:
        print(f"{item} ไม่พอ มีแค่ {stock[item]} ชิ้น")
    else:
        stock[item] = stock[item]- amount
        if stock[item] == 0:
            stock.pop(item)
            print(f"เบิก {item} {amount} ชิ้น หมดสต็อก ลบออกจากระบบแล้ว")
        else:
            print(f"เบิก {item} {amount} ชิ้น เหลือ {stock[item]} ชิ้น")
else:
    print(f"{item} ไม่มีในระบบ")

print(stock)    


nums = [4, 2, 4, 7]
s = set(nums)
d = {"a": 1, "b": 2}

print(len(nums)) # นับค่าใน nums ได้ 4
print(len(s)) # set คือการเอาค่าที่ซ้ำให้เหลือตัวเดียว จะได้ 3
print(4 in s) # คืนค่าได้ true 
print(1 in d) # คืนค่าได้ false
print(d.get("c", 0)) # ได้ค่า defalut เพราะ c ไม่มีค่าใน nums
print(d.pop("a")) # ลบ value a ออก
print(d) # จะเหลือแค่ {"b": 2}