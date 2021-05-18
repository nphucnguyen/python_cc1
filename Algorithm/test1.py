import time
import threading

class MyThread(threading.Thread):
    def __init__(self, name, counter, delay):
        threading.Thread.__init__(self)
        self.name = name
        self.counter = counter
        self.delay = delay
    def run(self):
        print('Ready to run' + self.name)
        while self.counter:
            time.sleep(self.delay)
            print('{} : {}'.format(self.name, time.ctime()))
            self.counter -=1
        print ('End of loop')

try:
    thread1 = MyThread('Thread1', 10, 0.2)
    thread2 = MyThread('Thread2', 10, 0.3)
    thread1.start()
    thread2.start()
except:
    print('error while running the program')

