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
total_rows = final_repairs.shape[0]
total_columns = final_repairs.shape[1]
minimum_cost = final_repairs["cost"].min()
maximum_cost = final_repairs["cost"].max()
average_cost = final_repairs["cost"].mean()
high_cost_repairs = final_repairs[final_repairs["cost"]>3000]

urgent_repairs =  final_repairs[(final_repairs["status"] == "รอดำเนินการ") & (final_repairs["cost"] > 3000)]
urgent_count = urgent_repairs.shape[0]

final_repairs.loc[final_repairs["id"] == 2005, "status"] = "กำลังซ่อม"
final_repairs.loc[final_repairs["id"] == 2006, "cost"] = 3000

updated_pending = final_repairs[final_repairs["status"] == "รอดำเนินการ"]
updated_pending_total = updated_pending["cost"].sum()

updated_summary = final_repairs.groupby("department")["cost"].agg(
    ["sum","mean","min","max"]
    )
sorted_data = final_repairs.sort_values("cost", ascending=False)
most_expensive_repair = sorted_data.iloc[0]
sorted_data_min = final_repairs.sort_values("cost", ascending=True)
cheapest_repair = sorted_data_min.iloc[0]

cost_data = final_repairs[final_repairs["cost"]>3000]
selected_repairs = cost_data[["device", "department", "cost"]]

department_cost_data = final_repairs[(final_repairs["department"] == "IT") & (final_repairs["cost"]>3000)]

it_high_cost = department_cost_data[["id", "device" , "cost"]]

department_IT_Finance = final_repairs[(final_repairs["department"]=="IT") | (final_repairs["department"]=="Finance")]

selected_departments =  department_IT_Finance[["id", "device" , "cost"]]

department_IT_Cost = final_repairs[(final_repairs["department"]=="IT") & ((final_repairs["cost"]>=3000) & (final_repairs["cost"] <=10000) )]

it_medium_cost = department_IT_Cost[["id", "device" , "cost"]]

it_medium_count = it_medium_cost.shape[0]
it_medium_total = it_medium_cost["cost"].sum()


print(pending_repairs)
print(pending_total)
print(summary_by_department)
print(sorted_repairs)
print(final_sorted_repairs)

print (status_count)
print(total_rows)
print(total_columns)

print(minimum_cost)
print(maximum_cost)
print(average_cost)
print(high_cost_repairs)
print(urgent_repairs)
print (urgent_count)
print (final_repairs)
print(updated_pending)
print(updated_pending_total)
print(updated_summary)
print(most_expensive_repair)
print(cheapest_repair)

print(selected_repairs)
print(it_high_cost)
print(selected_departments)
print (department_IT_Cost)
print(it_medium_count)
print(it_medium_total)

# =========================
# Day 8 Final Challenge
# =========================

repairs_final = [
    {"id": 3001, "device": "Computer", "department": "IT", "status": "รอดำเนินการ", "cost": 4200},
    {"id": 3002, "device": "Printer", "department": "HR", "status": None, "cost": 1600},
    {"id": 3003, "device": "Notebook", "department": "Finance", "status": "กำลังซ่อม", "cost": None},
    {"id": 3004, "device": "Monitor", "department": "IT", "status": "เสร็จสิ้น", "cost": 900},
    {"id": 3004, "device": "Monitor", "department": "IT", "status": "กำลังตรวจสอบ", "cost": 1300},
    {"id": 3005, "device": "Server", "department": "IT", "status": "รอดำเนินการ", "cost": 15000},
    {"id": 3006, "device": "Printer", "department": "Finance", "status": "รอดำเนินการ", "cost": 3200},
    {"id": 3007, "device": "Scanner", "department": "HR", "status": "เสร็จสิ้น", "cost": 2200}
]

df_final = pd.DataFrame(repairs_final)

missing_final = df_final.isna().sum()
df_final["status"] = df_final["status"].fillna("รอตรวจสอบ")  
clean_final =  df_final.dropna(subset=["cost"])
final_data =  clean_final.drop_duplicates(subset=["id"], keep= "last")
important_repairs = final_data[(final_data["status"] =="รอดำเนินการ") & (final_data["cost"]> 3000)]
important_count = important_repairs.shape[0]
important_total = important_repairs["cost"].sum()
department_summary = final_data.groupby(["department"])["cost"].agg(
    ["sum", "mean", "min", "max"]
    )
print(missing_final)
print(clean_final)
print(final_data)
print(important_repairs)
print(important_count)
print(important_total)
print(department_summary)

