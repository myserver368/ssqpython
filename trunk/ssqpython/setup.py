# -*- coding: cp936 -*-
# otherrrr@gmail.com
# ��python�����exe
from distutils.core import setup

import py2exe

import sys

#����������ִ�У�python setup.py

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
                             "pic/pen.ico","pic/flash.swf"]),
                    ("data", ["data/�̶�Ͷע.txt","data/��������.txt","data/��������.txt",\
                              "data/˵���ĵ�.txt","data/��������.ini","data/��ˮ����.txt",\
                              "data/��ѡ����.txt"]),
                    ("", ["README.txt","gdiplus.dll","msvcp71.dll"])
                    ],
        options = {'py2exe': {'optimize': 2,'compressed':1,"bundle_files": 1,"dll_excludes": ["w9xpopen.exe"]}},
        zipfile=None,
    )

#�޸�dist�����data����ġ���������.ini��
f = open('dist/data/��������.ini', 'w')
f.write("#������\nserver:proxy.edu.cn\n#�˿�\nport:8080\n#�û���\nusername:anonymous\n#����\npassword:null\n#��������\nprotocol:http")
f.close()
