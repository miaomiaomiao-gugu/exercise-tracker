import file_utils
import tool_utils
import stats_utils
def main():
    filename = "exercises_person.csv"
    records = file_utils.load_exercises(filename)
    print("====个人运动健身记录管理系统====")
    print("\n1.添加运动记录\n2.查看所有记录\n3.按运动类型筛选\n4,按日期范围筛选\n5.按消耗排序\n6.运动统计\n7.删除任务\n8.退出")
    while True:
        choice = input("请选择你需要实现的功能:")
        if choice == "1":
            tool_utils.add_exercise(records)
        elif choice == "2":
            tool_utils.view_exercises(records)
        elif choice == "3":
            stats_utils.filter_by_type(records)
        elif choice == "4":
            stats_utils.filter_by_date(records)
        elif choice == "5":
             stats_utils.sort_by_calories(records)
        elif choice == "6":
            stats_utils.show_stats(records)
        elif choice == "7":
            tool_utils.delete_record(records)
        elif choice == "8":
             file_utils.save_exercise(records,filename)
             print("退出成功")
             break
        else:
            print("无效选项")
if __name__ == "__main__":
    main()
