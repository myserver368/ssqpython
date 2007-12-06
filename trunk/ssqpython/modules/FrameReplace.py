#! usr/bin/python
# -*- coding:utf-8 -*
#Boa:Frame:FrameReplace
# otherrrr@gmail.com
# 替换过滤条件面板

import wx
import os
import locale

def create(parent):
    return FrameReplace(parent)

[wxID_FRAMEREPLACE, wxID_FRAMEREPLACEBUTTONCHANGE, 
 wxID_FRAMEREPLACEBUTTONCOMPARE, wxID_FRAMEREPLACEBUTTONCOPY, 
 wxID_FRAMEREPLACEBUTTONEXIT, wxID_FRAMEREPLACEBUTTONOPEN, 
 wxID_FRAMEREPLACEBUTTONSAVE, wxID_FRAMEREPLACEPANEL1, 
 wxID_FRAMEREPLACETEXTCTRL1, wxID_FRAMEREPLACETEXTCTRL2, 
] = [wx.NewId() for _init_ctrls in range(10)]

class FrameReplace(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAMEREPLACE, name=u'FrameReplace',
              parent=prnt, pos=wx.Point(250, 213), size=wx.Size(562, 469),
              style=wx.DEFAULT_FRAME_STYLE,
              title=u'\u8fc7\u6ee4\u6761\u4ef6\u66ff\u6362')
        self.SetClientSize(wx.Size(554, 442))
        self.SetIcon(wx.Icon(u'pic/red.ico',wx.BITMAP_TYPE_ICO))

        self.panel1 = wx.Panel(id=wxID_FRAMEREPLACEPANEL1, name='panel1',
              parent=self, pos=wx.Point(0, 0), size=wx.Size(554, 442),
              style=wx.TAB_TRAVERSAL)

        self.textCtrl1 = wx.TextCtrl(id=wxID_FRAMEREPLACETEXTCTRL1,
              name='textCtrl1', parent=self.panel1, pos=wx.Point(8, 28),
              size=wx.Size(248, 380),
              style=wx.TE_DONTWRAP | wx.TE_LINEWRAP | wx.TE_MULTILINE | wx.TE_RICH,
              value=u'\u65b0\u8fc7\u6ee4\u6761\u4ef6')

        self.textCtrl2 = wx.TextCtrl(id=wxID_FRAMEREPLACETEXTCTRL2,
              name='textCtrl2', parent=self.panel1, pos=wx.Point(304, 28),
              size=wx.Size(240, 380),
              style=wx.TE_DONTWRAP | wx.TE_READONLY | wx.TE_MULTILINE | wx.TE_RICH,
              value=u'\u65e7\u8fc7\u6ee4\u6761\u4ef6')

        self.buttonchange = wx.Button(id=wxID_FRAMEREPLACEBUTTONCHANGE,
              label=u'-->', name=u'buttonchange', parent=self.panel1,
              pos=wx.Point(260, 104), size=wx.Size(40, 24), style=0)
        self.buttonchange.SetToolTipString(u'\u4f7f\u7528\u65b0\u6761\u4ef6\u66ff\u6362\u65e7\u6761\u4ef6')
        self.buttonchange.Bind(wx.EVT_BUTTON, self.OnButtonchangeButton,
              id=wxID_FRAMEREPLACEBUTTONCHANGE)

        self.buttoncopy = wx.Button(id=wxID_FRAMEREPLACEBUTTONCOPY,
              label=u'<--', name=u'buttoncopy', parent=self.panel1,
              pos=wx.Point(260, 154), size=wx.Size(40, 24), style=0)
        self.buttoncopy.SetToolTipString(u'\u76f4\u63a5\u590d\u5236\u65e7\u6761\u4ef6')
        self.buttoncopy.Bind(wx.EVT_BUTTON, self.OnButtoncopyButton,
              id=wxID_FRAMEREPLACEBUTTONCOPY)

        self.buttoncompare = wx.Button(id=wxID_FRAMEREPLACEBUTTONCOMPARE,
              label=u'<->', name=u'buttoncompare', parent=self.panel1,
              pos=wx.Point(260, 204), size=wx.Size(40, 24), style=0)
        self.buttoncompare.SetToolTipString(u'\u6bd4\u8f83\u65b0\u65e7\u8fc7\u6ee4\u6761\u4ef6\u7684\u4e0d\u540c')
        self.buttoncompare.Bind(wx.EVT_BUTTON, self.OnButtoncompareButton,
              id=wxID_FRAMEREPLACEBUTTONCOMPARE)
              
        self.buttonopen = wx.Button(id=wxID_FRAMEREPLACEBUTTONOPEN,
              label=u'\u6253\u5f00(&O)', name=u'buttonopen', parent=self.panel1,
              pos=wx.Point(16, 416), size=wx.Size(56, 24), style=0)
        self.buttonopen.Bind(wx.EVT_BUTTON, self.OnButtonopenButton,
              id=wxID_FRAMEREPLACEBUTTONOPEN)

        self.buttonsave = wx.Button(id=wxID_FRAMEREPLACEBUTTONSAVE,
              label=u'\u4fdd\u5b58(&S)', name=u'buttonsave', parent=self.panel1,
              pos=wx.Point(88, 416), size=wx.Size(56, 24), style=0)
        self.buttonsave.Bind(wx.EVT_BUTTON, self.OnButtonsaveButton,
              id=wxID_FRAMEREPLACEBUTTONSAVE)

        self.buttonexit = wx.Button(id=wxID_FRAMEREPLACEBUTTONEXIT,
              label=u'\u9000\u51fa(&X)', name=u'buttonexit', parent=self.panel1,
              pos=wx.Point(472, 416), size=wx.Size(56, 24), style=0)
        self.buttonexit.Bind(wx.EVT_BUTTON, self.OnButtonexitButton,
              id=wxID_FRAMEREPLACEBUTTONEXIT)

    def __init__(self, parent):
        self._init_ctrls(parent)
        #命令行显示一下
        print (u'FrameReplace启动').encode(locale.getdefaultlocale()[1])
        
        #读取旧过滤条件
        print (u'读取过滤条件').encode(locale.getdefaultlocale()[1])
        f = open(u'data/过滤条件.txt', 'r')
        old_filters = f.read()
        f.close()
        
        #窗口显示更新
        self.textCtrl1.Clear()
        wx.StaticText(self.panel1, -1, u"新过滤条件", pos=(70, 8))
        self.textCtrl2.Clear()
        wx.StaticText(self.panel1, -1, u"旧过滤条件", pos=(390, 8))
        #怀疑前3位有东西，未确认 20071202
        self.textCtrl2.AppendText(old_filters.decode('utf-8')[1:])
        self.textCtrl2.SetInsertionPoint(0)
        
        self.buttoncopy.SetFocus()

#-------------------------------------------------------------------------------
#----按钮----

    def OnButtonchangeButton(self, event): #替换按钮
        '''使用新条件替换旧条件'''
        #给个提示框
        dlg = wx.MessageDialog(self, u'操作会覆盖当前的过滤文件！', 
                               u'确认过滤条件更新',
                               wx.OK | wx.CANCEL | wx.ICON_INFORMATION
                               )
        if dlg.ShowModal() == wx.ID_OK:
            #写文件
            f = open(u'data/过滤条件.txt', 'w')
            f.write(str(self.textCtrl1.GetValue().encode('utf-8'))) 
            f.close()          
            #刷新窗口
            self.textCtrl2.Clear()
            if wx.Platform == '__WXMSW__':
                self.textCtrl2.AppendText(str(self.textCtrl1.GetValue().encode('mbcs')))
            else:
                self.textCtrl2.AppendText(str(self.textCtrl1.GetValue().encode('utf-8'))) 
            self.textCtrl2.SetInsertionPoint(0)
        dlg.Destroy()       
            
        event.Skip()

    def OnButtoncopyButton(self, event): #复制按钮
        '''直接复制旧条件，用于修改'''
        #左侧窗口显示
        self.textCtrl1.Clear()
        if wx.Platform == '__WXMSW__': #windows
            self.textCtrl1.AppendText(str(self.textCtrl2.GetValue().encode('mbcs'))) 
        else: #linux
            self.textCtrl1.AppendText(str(self.textCtrl2.GetValue().encode('utf-8'))) 
	
        self.textCtrl1.SetInsertionPoint(0)
        
        event.Skip()

    def OnButtoncompareButton(self, event): #比较按钮
        '''比较新旧条件的不同''' 
        for i in range(1, self.textCtrl1.GetNumberOfLines()):
            if self.textCtrl1.GetLineText(i)!=self.textCtrl2.GetLineText(i):
                self.textCtrl1.SetStyle(self.textCtrl1.XYToPosition(0,i), \
                                        self.textCtrl1.XYToPosition(0,i)+len(self.textCtrl1.GetLineText(i)), \
                                        wx.TextAttr("RED"))
            else:
                self.textCtrl1.SetStyle(self.textCtrl1.XYToPosition(0,i), \
                                        self.textCtrl1.XYToPosition(0,i)+len(self.textCtrl1.GetLineText(i)), \
                                        wx.TextAttr("BLACK"))
        event.Skip()
        
    def OnButtonopenButton(self, event): #打开按钮
        '''打开新条件'''
        #显示文件选择框
        dlg = wx.FileDialog(
            self, message=u"打开新过滤条件",
            defaultDir=os.getcwd(), 
            defaultFile="",
            style=wx.OPEN
            )
        #点击“打开”按钮
        if dlg.ShowModal()==wx.ID_OK:
            #打开并读取文件
            if wx.Platform == '__WXMSW__':
                f = open(dlg.GetPath().encode('mbcs'), 'r')
            else:
                f = open(dlg.GetPath(), 'r')
            new_filters = f.read()
            f.close()
            #左侧窗口显示
            self.textCtrl1.Clear()
            self.textCtrl1.AppendText(new_filters.decode('utf-8'))            
        #关闭    
        dlg.Destroy()    

        #比较新旧条件的不同，不同则标红
        for i in range(1, self.textCtrl1.GetNumberOfLines()):
            if self.textCtrl1.GetLineText(i)!=self.textCtrl2.GetLineText(i):
                self.textCtrl1.SetStyle(self.textCtrl1.XYToPosition(0,i), \
                                        self.textCtrl1.XYToPosition(0,i)+len(self.textCtrl1.GetLineText(i)), \
                                        wx.TextAttr("RED"))
            else:
                self.textCtrl1.SetStyle(self.textCtrl1.XYToPosition(0,i), \
                                        self.textCtrl1.XYToPosition(0,i)+len(self.textCtrl1.GetLineText(i)), \
                                        wx.TextAttr("BLACK"))
        ##位置放在开始位置哦～
        self.textCtrl1.SetInsertionPoint(0)
                
        event.Skip()

    def OnButtonsaveButton(self, event): #保存按钮
        '''保存修改后的新条件'''
        wildcard = u"文本文档(*.txt)|*.txt|"     \
                   u"所有文件|*.*"        
        #显示文件选择框
        dlg = wx.FileDialog(
            self, message=u"保存修改后的过滤条件",
            #defaultDir=os.getcwd(), 
            defaultFile="",
            wildcard=wildcard,
            style=wx.SAVE
            )
        #点击“保存”按钮
        if dlg.ShowModal()==wx.ID_OK:
            #保存文件
            ##打开
            if wx.Platform == '__WXMSW__':
                f = open(dlg.GetPath().encode('mbcs'), 'w')
            else:
                f = open(dlg.GetPath(), 'w')
            ##写
            f.write(str(self.textCtrl1.GetValue().encode('utf-8'))) 
            f.close()
        #关闭    
        dlg.Destroy() 
                   
        event.Skip()

    def OnButtonexitButton(self, event): #退出按钮
        '''退出此窗口'''
        self.Close()
        
        event.Skip()
