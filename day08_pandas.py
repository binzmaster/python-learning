import pandas as pd

repairs = [
    {"id": 1001, "device": "Computer", "status": "รอดำเนินการ", "cost": 3500},
    {"id": 1002, "device": "Printer", "status": None, "cost": 1200},
    {"id": 1003, "device": "Notebook", "status": "รอดำเนินการ", "cost": None},
    {"id": 1004, "device": "Monitor", "status": "เสร็จสิ้น", "cost": 800}
]

df = pd.DataFrame(repairs)
missing_before = df.isna().sum()
df["status"] = df["status"].fillna("รอตรวจสอบ")     
clean_repairs= df.dropna(subset=["cost"])
missing_after = clean_repairs.isna().sum()
print(missing_before)
print(clean_repairs)
print(missing_after)