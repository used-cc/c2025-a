import time
import os
import sys

def running(letter="python", v=0.03):
    try:
        console_width = os.get_terminal_size().columns
    except:
        console_width = 80 

    position = 0
    direction = 1  
    
    try:
        while True:
            sys.stdout.write('\033[2J\033[H')
            
            # 计算单词左侧空格
            left_spaces = " " * position
            
            # 输出字母
            sys.stdout.write(left_spaces + letter + '\r')
            sys.stdout.flush()
            
            # 更新
            position += direction

            # 左边界
            if position <= 0:
                position = 0
                direction = 1 
            # 右边界
            elif position >= console_width - len(letter):
                position = console_width - len(letter)
                direction = -1 
            
            time.sleep(v)  

    except KeyboardInterrupt:
        print("\n程序停止")

if __name__ == "__main__":
    running()