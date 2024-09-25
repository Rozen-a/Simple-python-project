# 加密和解密
# 密码术意味着更改消息的文本，以便不知道你秘密的人永远不会理解你的消息。
# 下面创建一个GUI应用程序，使用Python进行加密和解密。
# 在这里，我们需要编写使用无限循环的代码，代码将不断询问用户是否要加密或解密消息。

# Tkinter是Python的标准GUI库，Python使用Tkinter可以快速创建GUI应用程序
# messagebox：消息框
# simpledialog：对话框
# Tk：tkinter的主窗口类，用于创建应用程序的根窗口。
from tkinter import messagebox, simpledialog, Tk


# 判断偶数或0
def is_even(number):
    return number % 2 == 0


# 将偶数位置的字母添加到even_letters列表中
def get_even_letters(message):
    even_letters = []

    # range()用于生成特定范围的整数序列，常用于 for 循环中来控制循环的次数和步进方式
    # 语法：range(start, stop, step)
    for counter in range(0, len(message)):  # counter为for的循环变量
        if is_even(counter):
            even_letters.append(message[counter])   # list.append(item)方法：向list的末尾添加元素item

    return even_letters


# 将偶数位置（包含第0位）的字母添加到odd_letters列表中
def get_odd_letters(message):
    odd_letters = []
    for counter in range(0, len(message)):
        if not is_even(counter):    # "if not ..." = "if ... is not Ture" = "if ... is False" = "if !(...)"
            odd_letters.append(message[counter])
    return odd_letters


# 对文本进行加密（加密方式为交换相邻两字母）
def swap_letter(message):
    letter_list = []

    # 文本长度为奇数末尾添加'x'
    if not is_even(len(message)):
        message = message + '#'

    # 分别获得偶数、奇数位字母列表
    even_letters = get_even_letters(message)
    odd_letters = get_odd_letters(message)

    # 将奇数、偶数位字母交替放入letter_list中（即交换原文本中相邻两字母）
    for counter in range(0, int(len(message) / 2)):
        letter_list.append(odd_letters[counter])
        letter_list.append(even_letters[counter])

    # 解密时删除补加的'#'字符
    if task == '解密' and letter_list[len(message)-1]=='#':
        del letter_list[len(message)-1]

    # join()是Python字符串方法，用来将一个可迭代对象（如列表、元组）中的元素通过指定的字符串连接起来，形成一个新的字符串。
    # 在这个例子中，使用的是空字符串 ''，意味着在连接元素时不插入任何字符，直接将所有元素无缝拼接在一起。
    # ''.join(letter_list) 就是将 letter_list 中的元素连接为一个字符串，以空字符串 '' 作为各元素的连接符。
    new_message = ''.join(letter_list)

    return new_message


# 询问是否加密或解密信息
# simpledialog提供了简单的对话框功能，允许用户输入信息
# askstring(title, prompt)：这是 simpledialog 中的一个函数，用于显示一个对话框，用户可以在其中输入字符串。
# 如果用户在对话框中点击“确定”，输入的字符串将被返回；如果用户点击“取消”，则返回 None
#     title：对话框的标题，显示在对话框的顶部。在这个例子中，标题是 '任务'。
#     prompt：对话框中显示的提示信息，告诉用户需要输入什么内容。在这个例子中，提示信息是 '你是否想要加密或解密信息?'。
# task变量用于存储用户在对话框中输入的字符串。
def get_task():
    task = simpledialog.askstring('任务', '你是否想要加密或解密信息?(输入“加密”或“解密”)')
    return task


# 获取待处理的文本内容
def get_message():
    message = simpledialog.askstring('信息', '请输入待处理的文本内容')
    return message


# root = Tk()：这行代码创建了一个 Tkinter 的主窗口对象，命名为 root。
# Tk() 是 Tkinter 的一个类，用于初始化主窗口。所有的 Tkinter 窗口和控件都将基于这个主窗口。
root = Tk()

while True:
    task = get_task()
    if task == '加密':
        message = get_message()     # 待机密文本
        encrypted = swap_letter(message)    # 加密后文本

        # messagebox：显示一个对话框信息框
        # showinfo(title, message)：显示一个信息对话框，通常用于提供成功或普通信息。
        messagebox.showinfo('加密的密文内容', encrypted)
    elif task == '解密':      # Python 不支持使用 else if, 使用elif
        message = get_message()
        decrypted = swap_letter(message)
        messagebox.showinfo('解密的明文内容', decrypted)
    else:
        break

# root.mainloop()：进入 Tkinter 的主事件循环，开始监听用户的事件（如鼠标点击、键盘输入等），保持窗口的响应性。
# 程序将一直运行，直到用户关闭窗口或选择退出。
root.mainloop()
