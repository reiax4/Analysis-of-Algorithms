import re

# ฟังก์ชันช่วยเลือกเฉพาะคอลัมน์ที่ต้องการ
def filter_columns(values, keep_columns):
    # แปลงข้อมูลใน VALUES(...) เป็นลิสต์
    columns = [col.strip() for col in values.split(",")]
    # เลือกเฉพาะคอลัมน์ที่อยู่ในลำดับ keep_columns
    filtered = [columns[i] for i in keep_columns]
    return filtered

# ใช้ with เพื่อเปิดไฟล์
with open("amphoe.sql", "r", encoding="utf-8") as sql_file, open("amphoe.txt", "w", encoding="utf-8") as txt_file:
    for line in sql_file:
        # ใช้ regex ดึงเฉพาะข้อมูลใน VALUES(...)
        match = re.search(r"VALUES\s*\((.+)\);", line)
        if match:
            # ดึงค่าที่อยู่ในวงเล็บ VALUES(...)
            values = match.group(1)
            
            # เลือกเฉพาะคอลัมน์ mcode (0) และ mname (1)
            keep_columns = [0, 1]  # คอลัมน์ที่ต้องการ
            filtered_values = filter_columns(values, keep_columns)
            
            # ลบ ' ออกจาก mcode และคงเลขศูนย์ไว้
            acode = filtered_values[0].replace("'", "")
            
            # ลบ ' ออกจาก mname
            aname = filtered_values[1].replace("'", "")
            
            # เขียนค่าที่ทำความสะอาดแล้วลงไฟล์ .txt
            txt_file.write(f"{acode} {aname}\n")