#coding:utf-8
import time
from python_pid import PidFileDeco

@PidFileDeco('my')
def main():
    time.sleep(1000)

if __name__ == "__main__":
    main()
