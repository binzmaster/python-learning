import pandas as pd

repairs = [
    {"id": 1001, "device": "Computer", "department": "IT", "status": "รอดำเนินการ", "cost": 3500},
    {"id": 1002, "device": "Printer", "department": "HR", "status": "เสร็จสิ้น", "cost": None},
    {"id": 1003, "device": "Notebook", "department": "IT", "status": None, "cost": 5500},
    {"id": 1003, "device": "Notebook", "department": "IT", "status": None, "cost": 5500},
    {"id": 1004, "device": "Monitor", "department": "HR", "status": "เสร็จสิ้น", "cost": 800}
]

df = pd.DataFrame(repairs)
df["status"] = df["status"].fillna("รอตรวจสอบ")
clean_repairs = df.dropna(subset=["cost"])

duplicate_count= clean_repairs.duplicated(subset=["id"]).sum()
final_repairs = clean_repairs.drop_duplicates(subset=["id"],keep="last")
summary_by_department = final_repairs.groupby("department")["cost"].agg(
    ["sum", "mean", "min", "max"]
    )

print (summary_by_department)
