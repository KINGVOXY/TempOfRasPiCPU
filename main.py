'''
ラズパイのCPU温度のログをとる
@author Daruo
@date 2020-09-26
'''
import subprocess
import time
import datetime

'''
get_now
現在の年月日、時刻を返す
フォーマットは %Y/%m/%d,%H:%M:%S
@return now
'''
def get_now():
    now = datetime.datetime.now().strftime("%Y/%m/%d,%H:%M:%S")
    return now

'''
get_temp
CPU温度を返す
@return temp
'''
def get_temp():
    cmd_txt=subprocess.run(["vcgencmd","measure_temp"],stdout = subprocess.PIPE)
    temp=cmd_txt.stdout.decode("utf8").replace("temp=","").replace("'C","")  # 数値のみにしている
    return temp

while True:
    with open('[main.pyがあるディレクトリの絶対パス]/log/temp_log.csv', 'a') as f:
        now=get_now()  # 年/月/日,時:分:秒
        temp=get_temp().replace("\n","")  # 現在のCPU温度
        print(now+","+temp,file=f)  # ログをcsvファイルに書き込む
    time.sleep(60)