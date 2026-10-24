count = {}
for dept in ["IT", "HR", "IT", "IT", "HR", "GIS"]:
    count[dept] = count.get(dept, 0) + 1
print(count)

statuses = ["done", "pending", "done", "cancel", "pending", "done"]
result = {}
for s in statuses:
    result[s] = result.get(s, 0)+1
print(result)

stock = {"paper": 10, "ink": 3, "toner": 5}

item = "cable"
qty = 4
if item in stock:
    stock[item] = qty+stock[item]
else:
    stock[item] = qty

print (stock)