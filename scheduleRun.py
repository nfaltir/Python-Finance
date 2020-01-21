#schedule script to run at a specific time



import schedule
import time



def helloWorld():
  print("Hello World")


schedule.every(5).seconds.do(helloWorld)

#set loop count
while 1:
  schedule.run_pending()
  time.sleep(1)