#! usr/bin/env python
# -*- coding:utf-8 -*-
# otherrrr@gmail.com
# 主程序

import wx
import modules.FrameMain

class SSQPythonApp(wx.App):
    def OnInit(self):
        self.main = modules.FrameMain.create(None)
        self.main.Show()
        self.SetTopWindow(self.main)
        return True
    
def main():
    application = SSQPythonApp(0) #修改显示之后可以了
    #application = SSQPythonApp(1) #改为1之后，在Windows系统双击才能显示
                                  #怀疑是print u''加u之后的缘故
    application.MainLoop()

if __name__ == '__main__':
    main()
