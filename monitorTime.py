from grove_rgb_lcd import *
from datetime import datetime

if __name__ == '__main__':
    setRGB(255,255,255)
    while True:
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S.%f")[:-3]

        setText_norefresh(current_time)
        #time.sleep(0.001)
