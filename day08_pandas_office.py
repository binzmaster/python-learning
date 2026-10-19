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

pending_repairs = final_repairs[
    final_repairs["status"] == "รอดำเนินการ"
]

pending_total = pending_repairs["cost"].sum()

summary_by_department = final_repairs.groupby(["department"])["cost"].agg(
    ["sum", "mean", "min", "max"]
    )
sorted_repairs = final_repairs.sort_values(by=['cost'], ascending=[False])
final_sorted_repairs = sorted_repairs.reset_index(drop=True)

status_count = final_repairs.value_counts(["status"])
print(pending_repairs)
print(pending_total)
print(summary_by_department)
print(sorted_repairs)
print(final_sorted_repairs)

print (status_count)

