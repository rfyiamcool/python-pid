#coding:utf-8
from functools import wraps
import fcntl
import os

def PidFileDeco(path):
    def repl(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            f_status = PidFile(path)
            f_status.acquire()
            return f(*args, **kwargs)
        return wrapper
    return repl

class PidFile(object):

    def __init__(self, path):
        self.path = path
        self.pidfile = None

    def acquire(self):
        self.__enter__()

    def release(self):
        self.__exit__()

    def __enter__(self):
        self.pidfile = open(self.path, "a+")
        try:
            fcntl.flock(self.pidfile.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
        except IOError:
            fpid = open(self.path, "r").read()
            raise SystemExit("Process id %s Already running , pid to "%fpid + self.path)
        self.pidfile.seek(0)
        self.pidfile.truncate()
        self.pidfile.write(str(os.getpid()))
        self.pidfile.flush()
        self.pidfile.seek(0)
        return self.pidfile

    def __exit__(self, exc_type=None, exc_value=None, exc_tb=None):
        try:
            self.pidfile.close()
        except IOError as err:
            if err.errno != 9:
                raise
        os.remove(self.path)


if __name__ == "__main__":
    import time
    f = PidFile("mydaemon")
    f.acquire()
    time.sleep(100)
    f.release()
   
