filename = "  ITA_REPORT.PDF  "

filename_clean = filename.strip().lower()
if filename_clean.endswith(".pdf"):
    print ("ไฟล์นี้เป็น PDF")
else:
    print("ไม่ใช่ไฟล์ PDF")
