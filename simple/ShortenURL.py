# URL缩短器
# 短网址由于易于记忆和输入，因此在数字营销领域非常受欢迎。
# 这里给大家介绍一下，如何使用Python创建URL缩短器。

# from __future__ import *这样的语句的作用就是将新版本的特性引进当前版本中，也就是说我们可以在当前版本使用新版本的一些特性
# 使得较旧的 Python 版本也能够使用上下文管理器（context managers）。在 Python 3 中这行是多余的，因为 with 是默认支持的。
from __future__ import with_statement

# 这个模块包含工具函数来简化上下文管理器的使用
import contextlib

# 使用try...except解构以兼容 Python 2 和 Python 3 的不同模块
# 在 Python 2 中，urlencode 和 urlopen 分别位于 urllib 和 urllib2 模块，
# 而在 Python 3 中它们被整合到了 urllib.parse 和 urllib.request 模块中。
# 因此，代码通过 try...except 捕获导入错误，确保在不同的 Python 版本下都能正常工作。

# urllib.parse 是 Python 3 中用于处理 URL 的模块。
# urlencode 函数用于将字典或元组形式的参数转换为 URL 编码的查询字符串。
try:
    from urllib.parse import urlencode
except ImportError:
    from urllib import urlencode

# urllib.request 模块是 Python 3 中用于处理 HTTP 请求的模块
# urlopen 是一个用于打开 URL 并返回响应数据的函数，常用于向服务器发起 HTTP/HTTPS 请求。
try:
    from urllib.request import urlopen
except ImportError:
    from urllib2 import urlopen

# sys 包是 Python 的标准库模块之一，它提供了与 Python 解释器及其环境交互的接口。
# 通过 sys 模块，程序可以访问与运行时环境相关的变量和函数，控制程序的运行行为，处理输入输出流等。
import sys


# 缩短URL
def make_tiny(url):
    # 构造 TinyURL 请求 URL
    # urlencode 是一个函数，用于将字典或元组形式的参数编码成 URL 查询字符串。
    # 例如，如果传入的 url 是 https://example.com, 它将被编码为 url=https%3A%2F%2Fexample.com。
    # http://tinyurl.com/api-create.php? 是 TinyURL API 的请求地址。
    # 'url=' + url表示将长网址作为查询参数传递给TinyURL API服务器。
    # 整体拼接生成的 requests_url 可能类似于：
    # http://tinyurl.com/api-create.php?url=https%3A%2F%2Fexample.com
    requests_url = ('http://tinyurl.com/api-create.php?' + urlencode({'url': url}))

    # 发送 HTTP 请求并读取响应
    # urlopen 是一个用于发送 HTTP 请求并获取服务器响应的函数。这里，它向 requests_url 发送请求并返回一个响应对象。
    # contextlib.closing() 是一个上下文管理器，确保当 urlopen 返回的响应对象不再需要时，它会自动关闭，以释放系统资源。
    # response 是服务器返回的响应对象，包含了缩短后的 URL 等信息
    with contextlib.closing(urlopen(requests_url)) as response:
        # response.read()：从服务器的响应中读取内容，通常是一个字节流。
        # decode('utf-8')：服务器返回的内容是字节流，需要用 UTF-8 编码将其转换为字符串。
        # TinyURL API 返回的内容就是缩短后的 URL。
        return response.read().decode('utf-8')


def main():
    initial_url = []  # 待处理URL列表

    # 获取待处理URL
    print("请输入需缩短的URL(一行输入一个,输入'#'完成输入)")
    while True:
        input_url = input()
        if input_url == '#':
            break
        else:
            initial_url.append(input_url)

    print("处理中...\n")

    # map() 是一个内建函数，用于将 make_tiny 函数应用到列表中的每个元素。
    tinyurl_list = list(map(make_tiny, initial_url))
    print("\n---处理完成---")

    print("\nURL缩短结果：")
    # 遍历输出结果
    for tinyurl in tinyurl_list:
        print(tinyurl)


# 确保当脚本作为主程序运行时才会调用 main() 函数。如果该脚本被当作模块导入到其他程序中，则不会执行 main() 函数。
# 每个Python文件（不管是被执行的脚本还是被导入的模块）都有一个内置的__name__属性。
# 当文件被直接执行时，__name__的值会被设置为'__main__'，而当文件被导入到其他文件时，__name__的值则会被设置为文件的名字。
# https://blog.csdn.net/weixin_72959097/article/details/137581451
if __name__ == '__main__':
    main()
