# URL缩短
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


def make_tiny(url):
    requests_url = ('http://tinyurl.com/api-create.php?' + urlencode({'url': url}))
    with contextlib.closing(urlopen(requests_url)) as response:
        return response.read().decode('utf-8')


def main():
    for tinyurl in map(make_tiny, ['https://baijiahao.baidu.com/s?id=1719379508156841662']):
        print(tinyurl)


if __name__ == '__main__':
    main()
