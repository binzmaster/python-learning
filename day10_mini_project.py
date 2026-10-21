jobs_day1 = [2001, 2002, 2003, 2002, 2004]
jobs_day2 = [2003, 2005, 2006, 2005]
costs = [4500, 1800, 12000, 1200, 2500, 3300]
jobs_day1 = set(jobs_day1)
jobs_day2 = set(jobs_day2)

print(f"วันที่ 1: {len(set(jobs_day1))} งาน")
print(f"วันที่ 2: {len(set(jobs_day2))} งาน")

print(f"งานที่ค้างข้ามวัน: {sorted(jobs_day1 & jobs_day2)}")
print(f"งานใหม่วันที่ 2: {sorted(jobs_day2-jobs_day1)}")

print(f"รวมค่าใช้จ่าย: {sum(costs):,} บาท")
print(f"ค่าเฉลี่ย: {sum(costs)/len(costs):,.2f} บาท")
print(f"แพงที่สุด 3 อันดับ: {sorted(costs,reverse=True)[:3]}")

print (f"รายการที่แพงที่สุดอยู่ตำแหน่ง index: {costs.index(max(costs))}")