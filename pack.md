# Introduction #

对如何将源文件打包成exe可执行文件做简短说明。


# Details #

本软件使用py2exe 0.6.6将python源程序打包为exe文件。

py2exe的使用方法请参见其官方网站：www.py2exe.org。

这里做一下步骤说明：
#到http://sourceforge.net/projects/py2exe/去下载py2exe的程序
#选择对应Python版本的安装文件，我用的是py2exe-0.6.6.win32-py2.5.exe
#下载下来，双击，安装，一路Next即可
#py2exe会作为一个module安装在Python目录C:\Python25\Lib\site-packages\py2exe下
#现在我们就开始用吧，具体如何使用可参考setup.py
#我们只需要在命令行下执行：python setup.py即可
#生成的exe等文件在dist目录下
#注意：运行之前需要安装Python和wxPython