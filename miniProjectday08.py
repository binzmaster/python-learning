import pandas as pd

repairs = [
    {"id": 2001, "device": "Computer", "department": "IT", "status": "รอดำเนินการ", "cost": 4500},
    {"id": 2002, "device": "Printer", "department": "HR", "status": None, "cost": 1800},
    {"id": 2003, "device": "Notebook", "department": "Finance", "status": "กำลังซ่อม", "cost": None},
    {"id": 2004, "device": "Monitor", "department": "IT", "status": "เสร็จสิ้น", "cost": 1200},
    {"id": 2004, "device": "Monitor", "department": "IT", "status": "เสร็จสิ้น", "cost": 1500},
    {"id": 2005, "device": "Server", "department": "IT", "status": "รอดำเนินการ", "cost": 12000},
    {"id": 2006, "device": "Printer", "department": "Finance", "status": "รอดำเนินการ", "cost": 2500}
]

df = pd.DataFrame(repairs)

missing_values = df.isna().sum()
duplicate_count = df.duplicated(subset=["id"]).sum()
df["status"] = df["status"].fillna("รอตรวจสอบ")
clean_repairs = df.dropna(subset=["cost"])
final_repairs = clean_repairs.drop_duplicates(subset=["id"],keep="last")

print(clean_repairs)
print(final_repairs)