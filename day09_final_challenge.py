messages = [
    "  เครื่องพิมพ์เสีย ด่วน  ",
    "COMPUTER ช้า ",
    " จอภาพไม่ติด ด่วน",
    "เครื่องพิมพ์ กระดาษติด",
]

clean_messages = []
for message in messages:
    clean_messages.append(message.strip())
number = 1
printer_count = 0
urgent_count = 0

for clean_mes in clean_messages:
    if clean_mes.endswith("ด่วน"):
        urgent_count = urgent_count+1
        print(f"งาน {number}: {clean_mes} [ด่วน]")
    else :
        print (f"งาน {number}: {clean_mes}")
    if "เครื่องพิมพ์" in clean_mes:
        printer_count = printer_count+1
    number = number+1
print(f"งานเกี่ยวกับเครื่องพิมพ์: {printer_count} งาน")
print(f"งานด่วน: {urgent_count} งาน")
