import time
# create a python program to create a countdown timer   
def countdown(time_sec):
    while time_sec:
        mins, secs = divmod(time_sec, 60)
        timeformat = '{:02d}:{:02d}'.format(mins,secs)
        print(timeformat, end='\r')
        time.sleep(1)
        time_sec -= 1
    print ("Stop ")
timecount=int(input("Set your Timer in Seconds: "))
countdown(timecount)