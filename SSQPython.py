# -*- coding: cp936 -*-
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
    application = SSQPythonApp(0)
    application.MainLoop()

if __name__ == '__main__':
    main()
