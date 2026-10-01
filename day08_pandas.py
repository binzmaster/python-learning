import pandas as pd

repairs = [
    {"id": 1001, "device": "Computer", "status": "รอดำเนินการ", "cost": 3500},
    {"id": 1002, "device": "Printer", "status": "เสร็จสิ้น", "cost": 1200},
    {"id": 1003, "device": "Notebook", "status": None, "cost": 5500},
    {"id": 1004, "device": "Monitor", "status": "เสร็จสิ้น", "cost": 800}
]

df = pd.DataFrame(repairs)

missing_status = df["status"].isna()
print(missing_status)