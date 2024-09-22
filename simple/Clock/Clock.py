# 闹钟
# 闹钟是一种具有可以在预先设定的时间被激活以响铃的功能的时钟，用于唤醒打工人们。
# 使用Python中的DateTime模块来创建闹钟，并用Python中的subprocess库来播放闹钟声音。
# 项目来源：https://blog.csdn.net/pdcfighting/article/details/125669955

from datetime import datetime
import subprocess   # 调用操作系统的音频播放器播放音频文件

# 输入
alarm_time = input("请输入闹钟时间，示例：09:50:00 am\n")
# 时
alarm_hour = alarm_time[0:2]
# 分
alarm_minute = alarm_time[3:5]
# 秒
alarm_seconds = alarm_time[6:8]
# 时段
alarm_period = alarm_time[9:11].upper()     # upper()方法：将字符串中的小写字母转为大写字母
print("闹钟设置成功！")

while True:
    now = datetime.now()
    # strftime()函数：将日期和时间格式化成指定的字符串格式
    current_hour = now.strftime("%I")       # 以补零后的十进制数表示的小时（12 小时制）
    current_minute = now.strftime("%M")     # 补零后，以十进制数显示的分钟
    current_seconds = now.strftime("%S")    # 补零后，以十进制数显示的秒
    current_period = now.strftime("%p")     # 本地化的 AM 或 PM

    # 时间判断
    if alarm_period == current_period:
        if alarm_hour == current_hour:
            if alarm_minute == current_minute:
                if alarm_seconds == current_seconds:
                    print("设定的闹钟时间已到！！！")
                    # 闹钟响铃
                    subprocess.Popen(['start', 'audio.mp3'], shell=True)
                    break
