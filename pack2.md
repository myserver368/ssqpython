# Introduction #

使用Pyinstaller将Python源文件打包成exe文件


# Details #

#下载及安装
下载请到http://pyinstaller.hpcf.upr.edu/
注意对应Python的版本
解压缩到C:\pyinstaller

#生成spec文件
在SSQPython目录下执行：
python C:\pyinstaller\Makespec.py SSQPython.py --onefile --windowed --icon=SSQPython.ico
生成的spec文件应该是这样的：
a = Analysis([os.path.join(HOMEPATH,'support\\_mountzlib.py'), os.path.join(HOMEPATH,'support\\useUnicode.py'), 'SSQPython.py'],
> pathex=['F:\\Misc\\pycode\\SSQPython'])
pyz = PYZ(a.pure)
exe = EXE( pyz,
> a.scripts,
> a.binaries,
> name='SSQPython.exe',
> debug=False,
> strip=False,
> upx=False,
> console=False , icon='SSQPython.ico')_

#生成exe文件
运行python C:\pyinstaller\build.py SSQPython.spec
得到SSQPython.exe了。