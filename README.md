# exercise-tracker
个人运动健身管理系统
# 个人运动健身记录管理系统

一个用 Python 编写的命令行运动记录管理工具，支持多模块结构。

## 功能

- 添加运动记录
- 查看所有记录
- 按运动类型筛选
- 按日期范围筛选
- 按消耗卡路里排序
- 运动数据统计
- 月度报表导出

## 技术栈

- Python 3
- csv 模块（CSV 读写）
- 多模块结构（file_utils / tool_utils / stats_utils）

## 项目结构
exercise_project/
├── main.py # 主程序入口
├── file_utils.py # 文件读写
├── tool_utils.py # 记录操作
├── stats_utils.py # 统计分析
├── run.py # 启动脚本
└── .gitignore
