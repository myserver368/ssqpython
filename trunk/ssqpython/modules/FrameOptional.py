#! usr/bin/python
# -*- coding:utf-8 -*-
#Boa:Frame:FrameOptional
# otherrrr@gmail.com
# 自选过滤面板

import wx
import os
import locale

from DataFileIO import readDataFileToArray

datas = [] #需要过滤的数据
data_array = []   #数据（数组格式）

def create(parent):
    return FrameOptional(parent)

[wxID_FRAMEOPTIONAL, wxID_FRAMEOPTIONALBUTTONLOAD, 
 wxID_FRAMEOPTIONALBUTTONMODIFY, wxID_FRAMEOPTIONALBUTTONSAVE, 
 wxID_FRAMEOPTIONALBUTTONSTART, wxID_FRAMEOPTIONALPANEL1, 
 wxID_FRAMEOPTIONALTEXTCTRL1, 
] = [wx.NewId() for _init_ctrls in range(7)]

class FrameOptional(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAMEOPTIONAL, name=u'FrameOptional',
              parent=prnt, pos=wx.Point(337, 269), size=wx.Size(436, 365),
              style=wx.DEFAULT_FRAME_STYLE, title=u'\u81ea\u9009\u8fc7\u6ee4')
        self.SetClientSize(wx.Size(428, 338))
        self.SetIcon(wx.Icon(u'pic/pen.ico',wx.BITMAP_TYPE_ICO))

        self.panel1 = wx.Panel(id=wxID_FRAMEOPTIONALPANEL1, name='panel1',
              parent=self, pos=wx.Point(0, 0), size=wx.Size(428, 338),
              style=wx.TAB_TRAVERSAL)

        self.buttonload = wx.Button(id=wxID_FRAMEOPTIONALBUTTONLOAD,
              label=u'\u52a0\u8f7d\u6570\u636e(&O)', name=u'buttonload',
              parent=self.panel1, pos=wx.Point(16, 304), size=wx.Size(75, 24),
              style=0)
        self.buttonload.Bind(wx.EVT_BUTTON, self.OnButtonloadButton,
              id=wxID_FRAMEOPTIONALBUTTONLOAD)

        self.buttonmodify = wx.Button(id=wxID_FRAMEOPTIONALBUTTONMODIFY,
              label=u'\u4fee\u6539\u6761\u4ef6(&M)', name=u'buttonmodify',
              parent=self.panel1, pos=wx.Point(120, 304), size=wx.Size(75, 24),
              style=0)
        self.buttonmodify.Bind(wx.EVT_BUTTON, self.OnButtonmodifyButton,
              id=wxID_FRAMEOPTIONALBUTTONMODIFY)

        self.buttonstart = wx.Button(id=wxID_FRAMEOPTIONALBUTTONSTART,
              label=u'\u5f00\u59cb\u8fc7\u6ee4(&T)', name=u'buttonstart',
              parent=self.panel1, pos=wx.Point(224, 304), size=wx.Size(75, 24),
              style=0)
        self.buttonstart.Bind(wx.EVT_BUTTON, self.OnButtonstartButton,
              id=wxID_FRAMEOPTIONALBUTTONSTART)

        self.buttonsave = wx.Button(id=wxID_FRAMEOPTIONALBUTTONSAVE,
              label=u'\u4fdd\u5b58\u6570\u636e(&S)', name=u'buttonsave',
              parent=self.panel1, pos=wx.Point(328, 304), size=wx.Size(75, 24),
              style=0)
        self.buttonsave.Bind(wx.EVT_BUTTON, self.OnButtonsaveButton,
              id=wxID_FRAMEOPTIONALBUTTONSAVE)

        self.textCtrl1 = wx.TextCtrl(id=wxID_FRAMEOPTIONALTEXTCTRL1,
              name='textCtrl1', parent=self.panel1, pos=wx.Point(8, 8),
              size=wx.Size(408, 280), style=wx.TE_MULTILINE,
              value=u'\u663e\u793a\u7a97\u53e3')

    def __init__(self, parent):
        self._init_ctrls(parent)
        #命令行提示
        print (u'FrameOptional启动').encode(locale.getdefaultlocale()[1])
        #数据读取
        global data_array
        data_array = readDataFileToArray()
        #窗口显示更新
        self.textCtrl1.Clear()
        self.textCtrl1.AppendText(u'开始自选过滤吧……\n')
        #数据清空
        global datas
        datas = []
        
#-------------------------------------------------------------------------------
#----按钮

    def OnButtonloadButton(self, event):
        '''加载数据'''
        global datas
        #数据清空
        datas = []
        #数据最新一期的期号
        date = int(data_array[0][0])
        #显示文件选择框
        dlg = wx.FileDialog(
            self, message=u"选择需要加载的文件",
            #defaultDir=os.getcwd()+"\%s"%(date+1), ##改为默认打开过滤、缩水数据文件夹 #linux 20071128
            defaultFile="",
            #wildcard="", #通配符（可以限制文件类型）
            style=wx.OPEN
            #style=wx.OPEN  | wx.CHANGE_DIR #如果可改目录，则再打开文件错误
            #style=wx.OPEN | wx.MULTIPLE | wx.CHANGE_DIR #不要多选文件功能
            )
        #点击“打开”按钮
        if dlg.ShowModal()==wx.ID_OK:         
            #读取选择文件中的数据
            f = open(dlg.GetPaths()[0], 'r') 
            s = f.readlines()
            f.close()
            #数据格式转换
            for st in s:
                datas.append([st[0:2],st[3:5],st[6:8],\
                              st[9:11],st[12:14],st[15:17]])
            #窗口显示一下
            self.textCtrl1.AppendText(u'加载了%d组数据\n'%len(datas))
        #关闭    
        dlg.Destroy()
                
        event.Skip()

    def OnButtonmodifyButton(self, event):
        '''修改数据'''   
        #打开data目录下的“自选条件.txt”
        if wx.Platform == '__WXMSW__': #windows
            os.startfile(u'data/自选条件.txt')
        else: #linux
            os.popen2(u'gedit data/自选条件.txt')
        
        event.Skip()

    def OnButtonstartButton(self, event):
        '''开始过滤'''
        global datas
        #读取data目录下的“自选条件.txt”
        f = open(u'data/自选条件.txt', 'r')
        s = f.readlines()
        f.close()
        #转换数据
        options = []
        for s_t in s:
            if len(s_t)<5: #防止空行
                break
            else:
                option = {'nums':[], 'least':0, 'most':6} #每组数据的构成:号码,下限,上限            
                option['nums'] = s_t.split(':')[0].split(' ')
                option['least'] = int(s_t.split(':')[1].split('-')[0])
                option['most'] = int(s_t.split(':')[1].split('-')[1].split('\n')[0])
                options.append(option)
        #窗口提示一下过滤前数据及自选条件组数
        self.textCtrl1.AppendText(u'使用了%d组自选条件\n'%len(options))
        #过滤
        for i in range(0, len(options)):
            self.textCtrl1.AppendText(u'使用第%d组条件'%(i+1))
            new_datas = [] #定义空列表
            for j in range(0, len(datas)):
                option = 0
                for k in range(0, len(options[i]['nums'])):
                    if options[i]['nums'][k] in datas[j]:
                        option = option + 1
                if options[i]['least']<=option<=options[i]['most']:
                    new_datas.append(datas[j])           
            datas = new_datas
            self.textCtrl1.AppendText(':-->%d\n'%len(datas))

        if 0<len(datas):            
            if len(datas)<=20:
                self.textCtrl1.AppendText(u'过滤后数据如下：\n')
                for i in range(0, len(datas)):
                    self.textCtrl1.AppendText('%s %s %s %s %s %s\n'\
                                              %(datas[i][0],datas[i][1],datas[i][2],\
                                                datas[i][3],datas[i][4],datas[i][5]))
            else:
                self.textCtrl1.AppendText(u'过滤后数据如下：(前20组)\n')
                for i in range(0, 20):
                    self.textCtrl1.AppendText('%s %s %s %s %s %s\n'\
                                              %(datas[i][0],datas[i][1],datas[i][2],\
                                                datas[i][3],datas[i][4],datas[i][5]))
        event.Skip()

    def OnButtonsaveButton(self, event):
        '''保存数据'''
        #数据最新一期的期号
        date = int(data_array[0][0])
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
        dlg.SetFilename(u'%s自选数据.txt'%(date+1))
        #点击“打开”按钮
        if dlg.ShowModal()==wx.ID_OK:
            #写入数据
	    if wx.Platform == '__WXMSW__':
		f = open(dlg.GetPath().encode('mbcs'), 'w') #强制编码一下可防止“放置于桌面出错”问题
	    else:
		f = open(dlg.GetPath(), 'w')
            for i in range(0, len(datas)):
                f.write('%s %s %s %s %s %s\n'\
                        %(datas[i][0],datas[i][1],datas[i][2],\
                          datas[i][3],datas[i][4],datas[i][5]))
            f.close()
            #窗口显示一下
            self.textCtrl1.AppendText(u'已保存数据')
	    if wx.Platform == '__WXMSW__': #windows
                self.textCtrl1.AppendText('%s\n'%(dlg.GetPath().encode('mbcs')))
            else: #linux
                self.textCtrl1.AppendText('%s\n'%(dlg.GetPath()))
        #关闭    
        dlg.Destroy()
                        
        event.Skip()
