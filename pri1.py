import threading
import time
import queue
import subprocess
q = queue.Queue()

def geip():
    for i in range(255):
        ip = '172.25.2.{}'.format(i)
        ping_ip = 'ping -c 1 ' + ip
        q.put(ping_ip)
def getip():
    while True:
        ip = q.get()
        if subprocess.call(ip,shell = True)==0:
            print('%s is alive'%(ip))
        else:
            print('%s is unconnection'%ip)
        q.task_done()
qq= geip()



t1 = threading.Thread(target = getip)
t2 = threading.Thread(target = getip)
t3 = threading.Thread(target = getip)
t4 = threading.Thread(target = getip)
t5 = threading.Thread(target = getip)
t1.setDaemon(True)
t2.setDaemon(True)
t3.setDaemon(True)
t4.setDaemon(True)
t5.setDaemon(True)
t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
q.join()
print('over')
