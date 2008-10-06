#! usr/bin/python
# -*- coding:utf-8 -*-
#Boa:Frame:FrameRandom
# otherrrr@gmail.com
# 复式机选面板（即：高级机选面板）

import wx
import locale
import random

datas_random = ''

def create(parent):
    return FrameRandom(parent)

[wxID_FRAMERANDOM, wxID_FRAMERANDOMBUTTON1, wxID_FRAMERANDOMBUTTON2, 
 wxID_FRAMERANDOMCOMBOBOX1, wxID_FRAMERANDOMCOMBOBOX2, wxID_FRAMERANDOMPANEL1, 
 wxID_FRAMERANDOMTEXTCTRL1, wxID_FRAMERANDOMTEXTCTRL2, 
] = [wx.NewId() for _init_ctrls in range(8)]

class FrameRandom(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAMERANDOM, name=u'FrameRandom',
              parent=prnt, pos=wx.Point(331, 184), size=wx.Size(400, 358),
              style=wx.DEFAULT_FRAME_STYLE, title=u'\u590d\u5f0f\u673a\u9009')
        self.SetClientSize(wx.Size(392, 331))
        self.SetIcon(wx.Icon(u'pic/pen.ico',wx.BITMAP_TYPE_ICO))

        self.panel1 = wx.Panel(id=wxID_FRAMERANDOMPANEL1, name='panel1',
              parent=self, pos=wx.Point(0, 0), size=wx.Size(392, 331),
              style=wx.TAB_TRAVERSAL)

        self.textCtrl1 = wx.TextCtrl(id=wxID_FRAMERANDOMTEXTCTRL1,
              name='textCtrl1', parent=self.panel1, pos=wx.Point(48, 112),
              size=wx.Size(312, 192), style=wx.TE_MULTILINE,
              value=u'\u63d0\u793a\u6587\u672c\u6846')

        self.comboBox1 = wx.ComboBox(choices=['6', '7', '8', '9', '10', '11',
              '12', '13', '14', '15', '16'], id=wxID_FRAMERANDOMCOMBOBOX1,
              name='comboBox1', parent=self.panel1, pos=wx.Point(48, 32),
              size=wx.Size(100, 22), style=0,
              value=u'\u7ea2\u7403\u4e2a\u6570')
        self.comboBox1.SetLabel(u'\u7ea2\u7403\u4e2a\u6570')

        self.comboBox2 = wx.ComboBox(choices=['1', '2', '3', '4', '5', '6', '7',
              '8', '9', '10', '11', '12', '13', '14', '15', '16', ],
              id=wxID_FRAMERANDOMCOMBOBOX2, name='comboBox2',
              parent=self.panel1, pos=wx.Point(48, 64), size=wx.Size(100, 22),
              style=0, value=u'\u7bee\u7403\u4e2a\u6570')
        self.comboBox2.SetLabel(u'\u7bee\u7403\u4e2a\u6570')

        self.textCtrl2 = wx.TextCtrl(id=wxID_FRAMERANDOMTEXTCTRL2,
              name='textCtrl2', parent=self.panel1, pos=wx.Point(208, 32),
              size=wx.Size(75, 24), style=0, value=u'\u51e0\u6ce8')

        self.button1 = wx.Button(id=wxID_FRAMERANDOMBUTTON1,
              label=u'\u5f00\u59cb', name='button1', parent=self.panel1,
              pos=wx.Point(208, 64), size=wx.Size(75, 24), style=0)
        self.button1.Bind(wx.EVT_BUTTON, self.OnButton1Button,
              id=wxID_FRAMERANDOMBUTTON1)

        self.button2 = wx.Button(id=wxID_FRAMERANDOMBUTTON2,
              label=u'\u4fdd\u5b58', name='button2', parent=self.panel1,
              pos=wx.Point(308, 64), size=wx.Size(75, 24), style=0)
        self.button2.Bind(wx.EVT_BUTTON, self.OnButton2Button,
              id=wxID_FRAMERANDOMBUTTON2)
        
    def __init__(self, parent):
        self._init_ctrls(parent)
        #命令行提示
        print (u'FrameRandom启动').encode(locale.getdefaultlocale()[1])
        #窗口显示更新
        self.textCtrl1.Clear()
        self.textCtrl1.AppendText(u'请选择对应设置！\n') 

    def OnButton1Button(self, event):
        '''开始机选'''
        # 判断符，判断得到的都是不是数字
        option = True
        red_num = 6 # default=6
        blue_num = 1 # default=1
        num_num = 10 # default=10
        try:
            red_num = int(str(self.comboBox1.GetValue()))
            blue_num = int(str(self.comboBox2.GetValue()))
            num_num = int(str(self.textCtrl2.GetValue()))
        except:
            option = False
        if option == False:
            self.textCtrl1.Clear()
            self.textCtrl1.AppendText(u'直接读取默认值：（6红+1蓝）×10注\n')
            red_num = 6 
            blue_num = 1 
            num_num = 10 
        else:
            self.textCtrl1.Clear()
            self.textCtrl1.AppendText(u'开始机选：（%s红+%s蓝）×%s注\n'%(red_num,blue_num,num_num))
        # 机选
        tmp = 0 # 判断注数的临时控制符
        for i in range(0, num_num): # 注数
            while True:
                red_ball = []
                blue_ball = []
                for j in range(0, red_num): # 红球
                    red_ball.append(random.randint(1,33))
                option = True
                for j in range(0, red_num-1): # 判断红球是不是一个比一个大
                    if red_ball[j]>=red_ball[j+1]:
                        option = False
                        break
                if option == False:
                    continue
                for j in range(0, blue_num): # 篮球
                    blue_ball.append(random.randint(1,16))
                option = True
                if blue_num>1: # 判断篮球是不是一个比一个大
                    for j in range(0, blue_num-1): 
                        if blue_ball[j]>=blue_ball[j+1]:
                            option = False
                            break
                if option == False:
                    continue                    
                # 显示
                for j in range(0, red_num):
                    self.textCtrl1.AppendText(u'%.2d'%red_ball[j])
                    if j == red_num-1:
                        break
                    else:
                        self.textCtrl1.AppendText(u',')
                self.textCtrl1.AppendText(u'+')
                for j in range(0, blue_num):
                    self.textCtrl1.AppendText(u'%.2d'%blue_ball[j])
                    if j== blue_num-1:
                        break
                    else:
                        self.textCtrl1.AppendText(u',')
                self.textCtrl1.AppendText(u'\n')
                break
        # 传递值，用于写文件
        global datas_random
        datas_random = '\n'.join(self.textCtrl1.GetValue().encode('mbcs').split('\n')[1:])
        
        event.Skip()

    def OnButton2Button(self, event):
        '''保存数据'''
        #保存的文件类型设置
        wildcard = u"文本文档(*.txt)|*.txt|"     \
                   u"所有文件|*.*"
        #显示文件选择框
        dlg = wx.FileDialog(
            self, message=u"另存为",
            defaultFile="",
            wildcard = wildcard, 
            style=wx.SAVE
            )
        #设置保存的默认文件名
        dlg.SetFilename(u'__log__random_30')
        #点击“打开”按钮
        if dlg.ShowModal()==wx.ID_OK:        
            #写入数据
	    if wx.Platform == '__WXMSW__':
		f = open(dlg.GetPath().encode('mbcs'), 'w') #强制编码一下可防止“放置于桌面出错”问题
	    else:
		f = open(dlg.GetPath(), 'w')
            f.write(datas_random)
            f.close()
            #窗口显示一下
            self.textCtrl1.AppendText(u'已保存数据')
        #关闭    
        dlg.Destroy()
        
        event.Skip()
