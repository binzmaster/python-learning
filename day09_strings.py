raw_text = "  IT , hr, FINANCE ,gis  "

departments_cleans = raw_text.split(",")

number = 1
for departments_clean in departments_cleans:
    de_clean = departments_clean.upper().strip()
    print(f"แผนก {number}: {de_clean}")
    
    
    number = number+1

