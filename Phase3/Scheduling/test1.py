import time
import sched

sch = sched.scheduler(time.time,time.sleep)

count = 0
def backup():
    global count
    print('Backing Up Pokemon Data')
    if count < 4:
        count += 1
        sch.enter(5,1,backup)

def test():
    print('Bacup System Is Running')

sch.enter(2,1,test)
sch.enter(3,1,backup)
sch.run()
