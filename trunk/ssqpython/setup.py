# -*- coding: cp936 -*-
# otherrrr@gmail.com
from distutils.core import setup

import py2exe

#�������д������У�python setup.py py2exe --bundle 1
    
setup(       
        windows = [
                {
                    "script":"SSQPython.py",
                    "icon_resources": [(1, "SSQPython.ico")]
                }
                   ],
        data_files=[("pic", ["pic/logo.ico","pic/red.ico","pic/report.ico"]),
                    ("", ["�̶�Ͷע.txt","��������.txt","��������.txt","˵���ĵ�.txt"])
                    ],
    )
