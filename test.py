#coding:utf-8
import time
from python_pid import PidFileDeco
from python_pid import PidFile

@PidFileDeco('my')
def test_deco():
    time.sleep(1000)

def test_func():
    f = PidFile("mydaemon")
    f.acquire()
    time.sleep(100)
    f.release()

def test_with():
    with PidFile("mydaemon"):
        time.sleep(100)
        print 'blog: xiaorui.cc'

if __name__ == "__main__":
    test_deco()
