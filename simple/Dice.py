# 骰子模拟器
# 可以通过选择1到6之间的随机整数，来完成骰子模拟
# 项目来源：https://blog.csdn.net/pdcfighting/article/details/125669955

import random

# 设置最大值和最小值
min_val = 1
max_val = 6

# 是否继续
roll_again = "Y"

# 循环
while roll_again == "Y":
    num = int(input("\n请输入掷出骰子数量："))
    print("\n开始掷骰子..")
    print("\n骰子的数值为：")

    i = 0
    while i < num:
        print(random.randint(min_val, max_val))
        i += 1

    # 是否继续
    roll_again = input("\n是否继续掷骰子？请输入Y或者N：")

print("\n--游戏结束--")
