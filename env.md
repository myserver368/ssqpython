# Introduction #

针对软件在不同运行环境下所需要进行的设置，本文做分类介绍。


# Details #

本软件使用Python+wxPython编写，因此提供了良好的跨平台性。

1）Windows平台
(a)在Windows 2000/XP/2003下，请直接下载最高版本的SSQPython\_x.x.x\_exe.zipp包，解压缩之后双击SSQPython.exe即可。
(b)下载SSQPython\_x.x.x\_src.zip包，即源代码版本，解压缩之后双击SSQPython.pyw，若未出现任何显示，请依次安装Python(www.python.org)和wxPython(www.wxPython.org)。安装Python之后，还需要在环境变量[我的电脑—右键—属性—高级—环境变量]的Path条目中添加Python所在的目录名。也可在命令提示符下输入：python ssqpython.py。
(c)Windows 98/Me系统在下载包之后，如出现运行错误，有可能还需要在主程序同目录下存在w9xpopen.exe文件。在1.0.3版本之后我不再在zip包中提供这个文件，可发信给我索取，或从之前的zip包中提取。


2）Linux平台
Linux平台请直接下载SVN源代码，地址为http://ssqpython.googlecode.com/svn/trunk/ssqpython-read-only。在终端中进入到对应的文件夹，输入：python SSQPython.py。请注意前4个字母为大写！如果出现错误，大概会是以下3种情况：
(a)Python版本过低。若Python版本低于2.0.0，有可能会出现某些问题。因为大多数Linux都内置Python，因此在终端中直接输入：python，可看到Python的版本。若低于2.0.0版本，可参考www.python.org网站说明进行升级。
(b)未安装wxPython。ubuntu 7.10用户请执行：sudo apt-get install python-wxgtk2.8。其他Linux发行版本用户请参考www.wxPython.org网站说明进行安装。
(c)wxPython版本较低。若wxPython版本低于2.8.0.0，有可能会出现某些问题，请参考(b)进行升级。


3）Mac平台
理论上支持SSQPython\_x.x.x\_code.zip源代码版本，未测试！

**注**欢迎反馈:otherrrr@gmail.com