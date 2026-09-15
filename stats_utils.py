
def filter_by_type(records):
    if not records:
        print("暂无数据")
    print("\n--- 按类型筛选 ---")
    type_choice = input("请输入你要筛选的类型:")
    if type_choice not in ["跑步","游泳","骑行","瑜伽","力量"]:
        print("暂无该类型")
        return
    result = [r for r in records if type_choice == r["exercise_type"]]  # 列表推导式
    if not result:
         print(f"未找到 关于{type_choice}的记录")
         return
    print(f"\n找到 {len(result)} 条记录：")
    for r in result:  # 相当于遍历了两遍
        print(f"日期：{r['date']}, 类型:{r['exercise_type']},"
              f"时长:{r['duration_minutes']},卡路里:{r['calories']},强度:{r['intensity']}")

def filter_by_date(records):
    if not records:
        print("暂无该数据")
        return
    print("\n----按日期筛选----")
    strat = input("起始日期(YYYY-MM-DD):")
    end = input("结束日期(YYYY-MM-DD):")
    if not strat or not end:
        print("日期不能为空")
        return
    result = [r for r in records if strat <= r['date'] <= end] # 列表推导式
    if not result:
        print(f"未找到{strat}到{end}之间的记录")
        print(f"已找到{len(records)}条记录")
    for r in result:
        print(f"日期：{r['date']}, 类型:{r['exercise_type']},"
              f"时长:{r['duration_minutes']},卡路里:{r['calories']},强度:{r['intensity']}")

def show_stats(records):
    sum_minutes = 0
    sum_calories = 0
    for record in records:
        sum_minutes += record['duration_minutes']
        sum_calories += record['calories']
    print(f"总记录数{len(records)}")
    print(f"总时长:{sum_minutes}")
    print(f"总卡路里:{sum_calories}")
    print(f"平均每次时长:{sum_minutes/len(records)}")
    #  ------各类型次数------

def stats_by_month(records):
    if not records:
        print("暂无该数据")
        return {}
    groups = {}
    for r in records:
        month = r['date'][:7]
        if month not in groups:
            groups[month] = []
        groups[month].append(r)

    result ={}
    for month,items in groups.items():
        n = len(items)
        result[month] = {
            "记录数": n,
            "总时长": (sum(r["duration_minutes"] for r in items)),  # for r in items/2 处理平均值
            "总卡路里": (sum(r["calories"] for r in items)),
            "平均卡路里": round(sum(r["calories"] for r in items) / n, 1),
        }
    print(f"\n按月统计：")
    print(f"{'月份':<10}{'记录数':<8}{'总时长':<12}{'总卡路里':<12}{'平均卡路里':<12}")  # 格式处理方式
    print("-" * 60)
    for month in sorted(result):
        s = result[month]  # 处理格式
        print(f"{month:<10}{s['记录数']:<8}{s['总时长']:<12.2f}"
              f"{s['总卡路里']:<12.2f}{s['平均卡路里']:<12.1f}")
    return result

def sort_by_calories(records):
    if not records:
        print("暂无数据")
        return
    sorted_records = sorted(records, key=lambda b: b['calories'], reverse=True)  # 排序函数
    for record in sorted_records:
        print( f"日期:{record['date']},类型:{record['exercise_type']},时长:{record['duration_minutes']},卡路里:{record['calories']},强度:{record['intensity']}")

