import time

class Test:
    def __init__(self):
        print('Object Initialization')
    def __del__(self):
        print('Performing clean up activitives')

t1 = Test()
print('Using the object T1 for my technical purpose')
time.sleep(5)
print('End of Application')