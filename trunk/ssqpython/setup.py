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
        data_files=[("pic", ["pic/logo.ico","pic/red.ico","pic/report.ico"]),
                    ("", ["固定投注.txt","过滤条件.txt","开奖数据.txt","说明文档.txt"])
                    ],
    )
