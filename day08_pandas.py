import pandas as pd

repairs = [
    {"id": 1001, "device": "Computer", "status": "รอดำเนินการ", "cost": 3500},
    {"id": 1002, "device": "Printer", "status": "เสร็จสิ้น", "cost": 1200},
    {"id": 1002, "device": "Printer", "status": "กำลังตรวจสอบ", "cost": 1500},
    {"id": 1003, "device": "Notebook", "status": "รอดำเนินการ", "cost": 5500}
]

df = pd.DataFrame(repairs)

latest_repairs = df.drop_duplicates(subset=["id"],keep="last")

print(latest_repairs)