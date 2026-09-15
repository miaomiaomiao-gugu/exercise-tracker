import csv
import os
# -------- 加载数据-------
def load_exercises(filename):
    if not os.path.exists(filename):
        print(f"{filename}不存在")
        return []
    records = []
    try:
        with open(filename,"r",encoding="utf-8")as f:
             reader = csv.DictReader(f)
             for row in reader:
                 row["duration_minutes"] = int(row["duration_minutes"])
                 row["calories"] = int(row["calories"])
                 records.append(row)
             print(f"已保存{len(records)}条记录")
    except(ValueError,KeyError)as e:
        print(f"文件格式错误{e}")
    return records
# ---------------- 导入数据 ----------
def save_exercise(records,filename):
    fields = ["date","exercise_type","duration_minutes","calories","intensity"]
    with open(filename,"w",newline="",encoding="utf-8")as f:
         writer = csv.DictWriter(f,fieldnames=fields)
         writer.writeheader()  # 把首行做标题
         writer.writerows(records)
    print(f"已保存{len(records)}记录")


