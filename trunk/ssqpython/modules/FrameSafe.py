#! usr/bin/python
# -*- coding:utf-8 -*-
#Boa:Frame:FrameSafe
# otherrrr@gmail.com
# 稳胆缩水面板

import wx
import locale

from DataFileIO import readDataFileToArray
from PredictFileIO import readPredictData

predict_data = [] #过滤后的数据（从文件中读出来的）
data_s = [] #缩水后的数据
date = [] #日期
safe_nums = [] #选择的稳胆号码

def create(parent):
    return FrameSafe(parent)

[wxID_FRAMESAFE, wxID_FRAMESAFEBUTTON1, wxID_FRAMESAFEBUTTON2, 
 wxID_FRAMESAFECHECKLISTBOX1, wxID_FRAMESAFEPANEL1, wxID_FRAMESAFEPANEL2, 
 wxID_FRAMESAFEPANEL3, wxID_FRAMESAFETEXTCTRL1, 
] = [wx.NewId() for _init_ctrls in range(8)]

class FrameSafe(wx.Frame):
    def _init_coll_boxSizer1_Items(self, parent):
        # generated method, don't edit

        parent.AddWindow(self.panel2, 80, border=0,
              flag=wx.EXPAND | wx.ALIGN_LEFT)
        parent.AddWindow(self.checkListBox1, 20, border=0,
              flag=wx.EXPAND | wx.ALL | wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT)

    def _init_coll_boxSizer2_Items(self, parent):
        # generated method, don't edit

        parent.AddWindow(self.textCtrl1, 90, border=0,
              flag=wx.EXPAND | wx.ALIGN_TOP | wx.ALL)
        parent.AddWindow(self.panel3, 10, border=0,
              flag=wx.EXPAND | wx.ALIGN_BOTTOM)

    def _init_sizers(self):
        # generated method, don't edit
        self.boxSizer1 = wx.BoxSizer(orient=wx.HORIZONTAL)

        self.boxSizer2 = wx.BoxSizer(orient=wx.VERTICAL)

        self._init_coll_boxSizer1_Items(self.boxSizer1)
        self._init_coll_boxSizer2_Items(self.boxSizer2)

        self.panel1.SetSizer(self.boxSizer1)
        self.panel2.SetSizer(self.boxSizer2)

    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAMESAFE, name=u'FrameSafe',
              parent=prnt, pos=wx.Point(291, 250), size=wx.Size(445, 372),
              style=wx.DEFAULT_FRAME_STYLE, title=u'\u7a33\u80c6\u7f29\u6c34')
        self.SetClientSize(wx.Size(437, 345))
        self.SetIcon(wx.Icon(u'pic/red.ico',wx.BITMAP_TYPE_ICO))

        self.panel1 = wx.Panel(id=wxID_FRAMESAFEPANEL1, name='panel1',
              parent=self, pos=wx.Point(0, 0), size=wx.Size(437, 345),
              style=wx.TAB_TRAVERSAL)

        self.panel2 = wx.Panel(id=wxID_FRAMESAFEPANEL2, name='panel2',
              parent=self.panel1, pos=wx.Point(0, 0), size=wx.Size(349, 345),
              style=wx.TAB_TRAVERSAL)

        self.checkListBox1 = wx.CheckListBox(choices=['01', '02', '03', '04',
              '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15',
              '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26',
              '27', '28', '29', '30', '31', '32', '33'],
              id=wxID_FRAMESAFECHECKLISTBOX1, name='checkListBox1',
              parent=self.panel1, pos=wx.Point(349, 0), size=wx.Size(88, 345),
              style=0)
        self.checkListBox1.Bind(wx.EVT_CHECKLISTBOX,
              self.OnCheckListBox1Checklistbox, id=wxID_FRAMESAFECHECKLISTBOX1)

        self.textCtrl1 = wx.TextCtrl(id=wxID_FRAMESAFETEXTCTRL1,
              name='textCtrl1', parent=self.panel2, pos=wx.Point(0, 0),
              size=wx.Size(349, 310), style=wx.TE_MULTILINE,
              value=u'\u6587\u672c\u663e\u793a')

        self.panel3 = wx.Panel(id=wxID_FRAMESAFEPANEL3, name='panel3',
              parent=self.panel2, pos=wx.Point(0, 310), size=wx.Size(349, 35),
              style=wx.TAB_TRAVERSAL)

        self.button1 = wx.Button(id=wxID_FRAMESAFEBUTTON1,
              label=u'\u4fdd\u5b58', name='button1', parent=self.panel3,
              pos=wx.Point(64, 8), size=wx.Size(75, 24), style=0)
        self.button1.Bind(wx.EVT_BUTTON, self.OnButton1Button,
              id=wxID_FRAMESAFEBUTTON1)

        self.button2 = wx.Button(id=wxID_FRAMESAFEBUTTON2,
              label=u'\u7f29\u6c34', name='button2', parent=self.panel3,
              pos=wx.Point(227, 8), size=wx.Size(75, 24), style=0)
        self.button2.Bind(wx.EVT_BUTTON, self.OnButton2Button,
              id=wxID_FRAMESAFEBUTTON2)

        self._init_sizers()

    def __init__(self, parent):
        self._init_ctrls(parent)
        #命令行提示
        print (u'FrameSafe启动').encode(locale.getdefaultlocale()[1])

        #显示面板清空
        #self.textCtrl1.Clear()

        #显示面板清空
        self.textCtrl1.Clear()
        #读取开奖数据
        data_array = readDataFileToArray()
        #最新一期的期号
        global date #保存数据时会用到，故global        
        date = int(data_array[0][0])        
        #读取过滤数据
        global predict_data #生成缩水条件1时会用到过滤数据，故global
        predict_data, predict_filter, select_num =readPredictData(date+1)
        self.textCtrl1.AppendText(u'已读取过滤后数据“%s过滤数据.txt”'%(date+1))
        self.textCtrl1.AppendText(u'（%d组）\n'%len(predict_data))
        
        global data_s #调用总的过滤后数据
        data_s = predict_data #初始时，过滤后数据等于预测数据
        
        global safe_nums #稳胆号码初始化均为False
        for i in range(0, 33):
            safe_nums.append(False)        

    def OnButton1Button(self, event): #保存
        '''保存数据'''
        #写出生成数据
        f = open(u'%s/%s稳胆数据.txt'%(date+1,date+1), 'w')
        #写数据
        for i in range(0, len(data_s)):
            f.write('%s %s %s %s %s %s\n'\
                    %(data_s[i][0],data_s[i][1],data_s[i][2],data_s[i][3],data_s[i][4],data_s[i][5]))
        f.close()

        #显示一下
        self.textCtrl1.AppendText(u'数据保存到“%s/%s稳胆数据.txt”\n'%(date+1,date+1))
        
        event.Skip()

    def OnButton2Button(self, event): #缩水 
        safe_numbers = [] #稳胆号码而不是错对
        for i in range(len(safe_nums)):
            if safe_nums[i]==True:
                safe_numbers.append('%.2d'%(i+1))
                
        global data_s
        data_s_new = []
        for i in range(len(data_s)):
            option = False
            for j in range(len(safe_numbers)):
                if safe_numbers[j] in data_s[i]:
                    option = True
                    break
            if option:
                data_s_new.append(data_s[i])                    
        data_s = data_s_new

        #显示一下
        self.textCtrl1.AppendText(u'选择稳胆号码：')
        for i in range(0, len(safe_numbers)):
            self.textCtrl1.AppendText(u'%s '%safe_numbers[i])
        self.textCtrl1.AppendText(u'\n')
        self.textCtrl1.AppendText(u'缩水后数据为%d组\n'%(len(data_s))) 
        
        event.Skip()

    def OnCheckListBox1Checklistbox(self, event): #修改稳胆号码组
        global safe_nums
        #是非对错谁知道
        if safe_nums[event.GetSelection()]==False:
            safe_nums[event.GetSelection()] = True
        else:
            safe_nums[event.GetSelection()] = False
            
        event.Skip()
