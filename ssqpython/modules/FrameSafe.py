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
data_d = [] #被缩掉的数据
date = [] #日期
safe_nums = [] #选择的稳胆号码

def create(parent):
    return FrameSafe(parent)

[wxID_FRAMESAFE, wxID_FRAMESAFEBUTTON1, wxID_FRAMESAFEBUTTON2, 
 wxID_FRAMESAFEBUTTON3, wxID_FRAMESAFEBUTTON4, wxID_FRAMESAFECHECKLISTBOX1, 
 wxID_FRAMESAFEPANEL1, wxID_FRAMESAFEPANEL2, wxID_FRAMESAFEPANEL3, 
 wxID_FRAMESAFETEXTCTRL1, 
] = [wx.NewId() for _init_ctrls in range(10)]

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
              pos=wx.Point(180, 8), size=wx.Size(75, 24), style=0)
        self.button1.Bind(wx.EVT_BUTTON, self.OnButton1Button,
              id=wxID_FRAMESAFEBUTTON1)

        self.button2 = wx.Button(id=wxID_FRAMESAFEBUTTON2,
              label=u'\u7f29\u6c34', name='button2', parent=self.panel3,
              pos=wx.Point(94, 8), size=wx.Size(75, 24), style=0)
        self.button2.Bind(wx.EVT_BUTTON, self.OnButton2Button,
              id=wxID_FRAMESAFEBUTTON2)

        self.button3 = wx.Button(id=wxID_FRAMESAFEBUTTON3,
              label=u'\u6253\u5f00', name='button3', parent=self.panel3,
              pos=wx.Point(8, 8), size=wx.Size(75, 24), style=0)
        self.button3.Bind(wx.EVT_BUTTON, self.OnButton3Button,
              id=wxID_FRAMESAFEBUTTON3)

        self.button4 = wx.Button(id=wxID_FRAMESAFEBUTTON4,
              label=u'\u4fdd\u5b58\uff08\u53cd\uff09', name='button4',
              parent=self.panel3, pos=wx.Point(264, 8), size=wx.Size(75, 24),
              style=0)
        self.button4.Bind(wx.EVT_BUTTON, self.OnButton4Button,
              id=wxID_FRAMESAFEBUTTON4)

        self._init_sizers()

    def __init__(self, parent):
        self._init_ctrls(parent)
        #命令行提示
        print (u'FrameSafe启动').encode(locale.getdefaultlocale()[1])

        #显示面板清空
        #self.textCtrl1.Clear()

        #显示面板清空
        self.textCtrl1.Clear()
        #提示
        self.textCtrl1.AppendText(u'请先选择需要被过滤的文件！\n')
        #读取开奖数据
        data_array = readDataFileToArray()
        #最新一期的期号
        global date #保存数据时会用到，故global        
        date = int(data_array[0][0])        
##        #读取过滤数据
##        global predict_data #生成缩水条件1时会用到过滤数据，故global
##        predict_data, predict_filter, select_num =readPredictData(date+1)
##        self.textCtrl1.AppendText(u'已读取过滤后数据“%s过滤数据.txt”'%(date+1))
##        self.textCtrl1.AppendText(u'（%d组）\n'%len(predict_data))
##        
##        global data_s #调用总的过滤后数据
##        data_s = predict_data #初始时，过滤后数据等于预测数据
        
        global safe_nums #稳胆号码初始化均为False
        for i in range(0, 33):
            safe_nums.append(False)        

    def OnButton1Button(self, event): #保存
        '''保存数据'''
##        #写出生成数据
##        f = open(u'%s/%s稳胆数据.txt'%(date+1,date+1), 'w')
##        #写数据
##        for i in range(0, len(data_s)):
##            f.write('%s %s %s %s %s %s\n'\
##                    %(data_s[i][0],data_s[i][1],data_s[i][2],data_s[i][3],data_s[i][4],data_s[i][5]))
##        f.close()
##
##        #显示一下
##        self.textCtrl1.AppendText(u'数据保存到“%s/%s稳胆数据.txt”\n'%(date+1,date+1))
        #保存的文件类型设置
        wildcard = u"文本文档(*.txt)|*.txt|"     \
                   u"所有文件|*.*"
        #显示文件选择框
        dlg = wx.FileDialog(
            self, message=u"另存为",
            #defaultDir=os.getcwd()+"\%s"%(date+1), ##改为默认打开过滤、缩水数据文件夹 #linux 20071129
            defaultFile="",
            wildcard = wildcard, #加一个过滤条件，默认保存为文本文件
            style=wx.SAVE
            )
        #设置保存的默认文件名
        dlg.SetFilename(u'%s稳胆数据.txt'%(date+1))
        #点击“打开”按钮
        if dlg.ShowModal()==wx.ID_OK:
            #写入数据
	    if wx.Platform == '__WXMSW__':
		f = open(dlg.GetPath().encode('mbcs'), 'w') #强制编码一下可防止“放置于桌面出错”问题
	    else:
		f = open(dlg.GetPath(), 'w')
            for i in range(0, len(data_s)):
                f.write('%s %s %s %s %s %s\n'\
                        %(data_s[i][0],data_s[i][1],data_s[i][2],\
                          data_s[i][3],data_s[i][4],data_s[i][5]))
            f.close()
            #窗口显示一下
            self.textCtrl1.AppendText(u'已保存数据\n')
	    if wx.Platform == '__WXMSW__': #windows
                self.textCtrl1.AppendText('%s\n'%(dlg.GetPath().encode('mbcs')))
            else: #linux
                self.textCtrl1.AppendText('%s\n'%(dlg.GetPath()))
        #关闭    
        dlg.Destroy()
        
        event.Skip()

    def OnButton2Button(self, event): #缩水 
        safe_numbers = [] #稳胆号码而不是错对
        for i in range(len(safe_nums)):
            if safe_nums[i]==True:
                safe_numbers.append('%.2d'%(i+1))

        if len(safe_numbers)==0:
            self.textCtrl1.AppendText(u'请选择至少一个稳胆号码！\n')
        else:
            global data_s
            global data_d
            data_s_new = []
            for i in range(len(data_s)):
                option = False
                for j in range(len(safe_numbers)):
                    if safe_numbers[j] in data_s[i]:
                        option = True
                        break
                if option:
                    data_s_new.append(data_s[i])
                else:
                    data_d.append(data_s[i])
            data_s = data_s_new

            #显示一下
            self.textCtrl1.AppendText(u'选择稳胆号码：')
            for i in range(0, len(safe_numbers)):
                self.textCtrl1.AppendText(u'%s '%safe_numbers[i])
            self.textCtrl1.AppendText(u'\n')
            self.textCtrl1.AppendText(u'缩水后数据为%d组\n'%(len(data_s)))
            self.textCtrl1.AppendText(u'被缩掉的数据%d组\n'%(len(data_d)))
            
        event.Skip()

    def OnButton3Button(self, event): #打开
        '''加载数据'''
        global data_s
        #数据清空
        data_s = []
        #显示文件选择框
        dlg = wx.FileDialog(
            self, message=u"选择需要加载的文件",
            defaultFile="",
            style=wx.OPEN
            )
        #点击“打开”按钮
        if dlg.ShowModal()==wx.ID_OK:         
            #读取选择文件中的数据
            f = open(dlg.GetPaths()[0], 'r') 
            s = f.readlines()
            f.close()
            #数据格式转换
            for st in s:
                data_s.append([st[0:2],st[3:5],st[6:8],\
                              st[9:11],st[12:14],st[15:17]])
            #窗口显示一下
            self.textCtrl1.AppendText(u'加载文件：\n')
	    if wx.Platform == '__WXMSW__': #windows
                self.textCtrl1.AppendText('%s\n'%(dlg.GetPaths()[0].encode('mbcs')))
            else: #linux
                self.textCtrl1.AppendText('%s\n'%(dlg.GetPaths()[0])) 
            self.textCtrl1.AppendText(u'共%d组数据\n'%len(data_s))
        #关闭    
        dlg.Destroy()
        
        event.Skip()

    def OnCheckListBox1Checklistbox(self, event): #修改稳胆号码组
        global safe_nums
        #是非对错谁知道
        if safe_nums[event.GetSelection()]==False:
            safe_nums[event.GetSelection()] = True
        else:
            safe_nums[event.GetSelection()] = False
            
        event.Skip()

    def OnButton4Button(self, event):#保存反向数据
        '''保存反向数据'''
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
        dlg.SetFilename(u'%s去胆数据.txt'%(date+1))
        #点击“打开”按钮
        if dlg.ShowModal()==wx.ID_OK:
            #写入数据
	    if wx.Platform == '__WXMSW__':
		f = open(dlg.GetPath().encode('mbcs'), 'w')
	    else:
		f = open(dlg.GetPath(), 'w')
            for i in range(0, len(data_d)):
                f.write('%s %s %s %s %s %s\n'\
                        %(data_d[i][0],data_d[i][1],data_d[i][2],\
                          data_d[i][3],data_d[i][4],data_d[i][5]))
            f.close()
            #窗口显示一下
            self.textCtrl1.AppendText(u'已保存数据\n')
	    if wx.Platform == '__WXMSW__': 
                self.textCtrl1.AppendText('%s\n'%(dlg.GetPath().encode('mbcs')))
            else: #linux
                self.textCtrl1.AppendText('%s\n'%(dlg.GetPath()))
        #关闭    
        dlg.Destroy()
        
        event.Skip()
