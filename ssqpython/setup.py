# -*- coding: cp936 -*-
# otherrrr@gmail.com
# 将python打包成exe
from distutils.core import setup

import py2exe

import sys

#在命令行下执行：python setup.py

if len(sys.argv) == 1:
    sys.argv.append("py2exe")
    
setup(       
        windows = [
            {
                "script":"SSQPython.py",
                "icon_resources": [(1, "SSQPython.ico")]
                }
                   ],
        data_files=[("pic", ["pic/logo.ico","pic/red.ico","pic/report.ico",\
                             "pic/splash.jpg","pic/blue.ico","pic/advice.png",\
                             "pic/pen.ico","pic/flash.swf","pic/flashC.swf"]),
                    ("data", ["data/固定投注.txt","data/过滤条件.txt","data/开奖数据.txt",\
                              "data/说明文档.txt","data/代理设置.ini","data/缩水条件.txt",\
                              "data/自选条件.txt"]),
                    ("", ["README.txt","gdiplus.dll","msvcp71.dll"])
                    ],
        options = {'py2exe': {'optimize': 2,'compressed':1,"bundle_files": 1,"dll_excludes": ["w9xpopen.exe"]}},
        zipfile=None,
    )

#修改dist下面的data下面的“代理设置.ini”
f = open('dist/data/代理设置.ini', 'w')
f.write("#主机名\nserver:proxy.edu.cn\n#端口\nport:8080\n#用户名\nusername:anonymous\n#密码\npassword:null\n#代理类型\nprotocol:http")
f.close()
