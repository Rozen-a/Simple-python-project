# 猜字游戏
# 在这个游戏中，你必须一个字母一个字母的猜出秘密单词。
# 如果你猜错了一个字母，你将丢掉一条命。
# 正如游戏名那样，你需要仔细选择字母，因为你的生命数量非常有限。
# 项目来源：https://blog.csdn.net/pdcfighting/article/details/125669955

import random

# 生命次数
lives = 3  # 创建变量，变量被自动指定为int型

# 神秘单词，随机选择
words = ['pizza', 'fairy', 'teeth', 'shirt', 'otter', 'plane']
secret_word = random.choice(words)  # random库的choice用于从序列（列表）中获取一个随机元素

# list()是一个 Python 内置函数,此处将字符串中的每个字符单独提取出来，并生成一个列表
# https://blog.csdn.net/TCatTime/article/details/82947385
clue = list('?????')
right = 0   # 已猜对的字母数

# 心形符号
# 在 Python 2 中，u 前缀用于表示 Unicode 字符串。
# 在 Python 3 中，所有字符串都是 Unicode，不需要 u 前缀，但仍可用于兼容 Python 2。
heart_symbol = u'\u2764'

# 标记玩家是否成功猜出了单词
guessed_word_correctly = False


# 函数update_clue()
# 当玩家猜对某个字母时，将 clue 中的问号替换为玩家猜对的字母
def update_clue(guessed_letter, secret_word, clue):
    index = 0
    while index < len(secret_word):
        if guessed_letter == secret_word[index]:
            clue[index] = guessed_letter
        index += 1


while lives > 0:
    print(clue)
    print('剩余生命次数：' + heart_symbol * lives)
    guess = input('猜测字母或是整个单词：')

    if guess == secret_word:
        guessed_word_correctly = True
        break

    if guess in secret_word:
        update_clue(guess, secret_word, clue)
        print('你猜对了一个字母！\n')
        right += 1
        if right == 5:
            guessed_word_correctly = True
            break
    else:
        print('错误。你失去了一条命\n')
        lives -= 1

if guessed_word_correctly:
    print('你赢了！答案是：' + secret_word)
else:
    print('你输了！答案是：' + secret_word)
