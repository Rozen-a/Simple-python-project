# 二维码
# 二维码是用于将数据编码和解码为机器可读的方法。
# 包含一个白色背景上的黑色方块网格，可以被任何成像设备(如手机)读取，并进行处理以从图案中提取所需的数据。

# QR码生成器库
# https://blog.csdn.net/lb245557472/article/details/91042892
import pyqrcode

# 设置二维码信息
s = "https://www.baidu.com"

# 生成二维码
url = pyqrcode.create(s)

# 保存二维码
url.svg("baidu.svg", scale=8)
