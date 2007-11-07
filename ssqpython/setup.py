# -*- coding: cp936 -*-
# otherrrr@gmail.com
from distutils.core import setup

import py2exe

#在命令行窗口运行：python setup.py py2exe --bundle 1
    
setup(       
        windows = [
                {
                    "script":"SSQPython.py",
                    "icon_resources": [(1, "SSQPython.ico")]
                }
                   ],
        data_files=[("pic", ["pic/logo.ico","pic/red.ico","pic/report.ico",\
                             "pic/splash.jpg","pic/blue.ico","pic/advice.png"]),
                    ("data", ["data/固定投注.txt","data/过滤条件.txt","data/开奖数据.txt",\
                              "data/说明文档.txt","data/代理设置.ini","data/缩水条件.txt"]),
                    ("flash", ["flash/flash.swf"]),
                    ("", ["readme.txt"])
                    ],
    )
