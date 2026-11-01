import time
import sched

sch = sched.scheduler(time.time,time.sleep)

def monitor():
    print('Saving pokemon . . .')

def task1():
    print('Task One >>')

def task2():
    print('Task two <<')

run_time = time.time() + 3

sch.enter(9,3,monitor)
sch.enter(6,2,task1)
sch.enter(3,1,task2)
sch.run()
print('All exicutions done')