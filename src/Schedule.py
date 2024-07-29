import schedule
import time
import CvApp

def job():
    CvApp.detectDifference()

# schedule.every(5).minutes.do(job) 
schedule.every(5).seconds.do(job) 

while True:
    schedule.run_pending() 
    time.sleep(1) 