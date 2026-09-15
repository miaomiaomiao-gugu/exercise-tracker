
def add_exercise(records):
    while True:
        add_date = input("请输入日期:")
        if not add_date :
           print("日期不能为空")
        else:
            break
    while True:
          add_exercise_type = input("请输入类型（跑步/游泳/骑行/瑜伽/力量）:")
          if add_exercise_type not in ["跑步","游泳","骑行","瑜伽","力量"]:
              print("类型错误请重新输入")
          else:
               break
    while True:
       try:
            add_duration_minutes = int(input("请输入运动时长/minutes:"))
            if 1<= add_duration_minutes <= 600 :
                print("输入成功")
                break
            print("输入错误请重新输入")
       except ValueError:
              print("请输入整数！")
    while True:
        try:
            add_calories = int(input("请输入消耗的卡路里:"))
            if 1<= add_calories <= 3000:
                print("输入成功")
                break
            print("输入错误请重新输入")
        except ValueError:
               print("请输入整数！")
    while True:
          add_intensity = input("请输入强度类型（低/中/高）:")
          if add_intensity not in ["低","中","高"]:
              print("类型输入错误")
          else:
              break
    print("添加成功！")
    new_record = {"date":add_date,"exercise_type":add_exercise_type,"duration_minutes":add_duration_minutes,"calories":add_calories ,"intensity":add_intensity}
    records.append(new_record)

def view_exercises(records):
    if not records:
        print("暂无数据")
        return
    for record in records:
        print(f"日期:{record['date']},类型:{record['exercise_type']},时长:{record['duration_minutes']},卡路里:{record['calories']},强度:{record['intensity']}")

def delete_record(records):
    print("\n--- 删除记录 ---")
    date = input("输入要删除的日期：").strip()
    etype = input("输入要删除的运动类型：").strip()

    for i, record in enumerate(records):
        if record["date"] == date and record["exercise_type"] == etype:
            records.pop(i)
            print("✅ 删除成功")
            return
    print("❌ 未找到匹配的记录")