records = [
    "  aarav sharma | cs101 | 78.4  ",
    "DIYA VERMA|cs101|91.2",
    "Aarav Sharma | ma102 | 85.0",
    "kabir nair | PH103 | 93.6",
    "invalid_entry_without_score",
]
up_records=[i.split("|") for i in records]
print(up_records)