# python-pid 

## 简单描述

一个关于python pid管理的模块

[更多python-pid的介绍](http://xiaorui.cc)

## 安装方法
方法1.
```
pip install python-pid
```

方法2
```
git clone git@github.com:rfyiamcool/python-pid.git
cd python-pid
python setup.py install
```

## 使用方法


可以在你的主函数加一个装饰器，可以传递pidfile的文件路径.
```

#coding:utf-8
@PidFileDeco('my')
def main():
    import time
    time.sleep(1000)

```
或者是直接调用，acquire是锁定，release()是释放

```
import time
from python_pid import PidFile

f = PidFile("mydaemon")
f.acquire()
time.sleep(100)
f.release()
```

使用with关键词,调用__enter__ , __exit__
```
with PidFile("mydaemon"):
    time.sleep(100)
    print 123
```

END... ...
