def greet():
    print("来自 example 模块的问候！")

if __name__ == "__main__":
    print("该脚本正在直接运行。")
    greet()
else:
    print("该脚本作为模块被导入。")

# PS> python .\26Python__name__\example.py
# 该脚本正在直接运行。
# 来自 example 模块的问候！