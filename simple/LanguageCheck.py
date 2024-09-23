# 语言检测
# 当你需要处理包含不同语言数据，且数据非常大的时候，语言检测就派上用场了。
# 使用Python中的langdetect包，可以在几行代码内检测超过55种不同的语言。
# 项目来源：https://blog.csdn.net/pdcfighting/article/details/125669955

# langdetect包简介：https://blog.csdn.net/quiet_girl/article/details/79653037
from langdetect import detect

text = input("输入信息：")
print("此段信息使用的语言是：" + detect(text))
