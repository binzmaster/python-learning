text = "  GIS-Project-2569  "

clean = text.strip()
print(clean[0])
print(clean[-4:])
print(len(clean))
print(clean.lower().replace("-", "_"))
print("2569" in clean)
print(clean.split("-"))