#! usr/bin/python
# -*- coding:utf-8 -*-
#Boa:Frame:FrameRedShrink
# otherrrr@gmail.com
# 红球缩水面板

import wx
import os
import random
import locale

from DataFileIO import readDataFileToArray
from PredictFileIO import readPredictData

predict_data = [] #过滤后的数据（从文件中读出来的）
data_s = [] #缩水后的数据
date = [] #日期

def create(parent):
    return FrameRedShrink(parent)

[wxID_FRAMEREDSHRINK, wxID_FRAMEREDSHRINKBUTTON1, wxID_FRAMEREDSHRINKBUTTON2, 
 wxID_FRAMEREDSHRINKBUTTON3, wxID_FRAMEREDSHRINKBUTTON4, 
 wxID_FRAMEREDSHRINKPANEL1, wxID_FRAMEREDSHRINKTEXTCTRL1, 
] = [wx.NewId() for _init_ctrls in range(7)]

class FrameRedShrink(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAMEREDSHRINK, name=u'FrameRedShrink',
              parent=prnt, pos=wx.Point(312, 191), size=wx.Size(461, 335),
              style=wx.DEFAULT_FRAME_STYLE, title=u'\u7ea2\u7403\u7f29\u6c34')
        self.SetClientSize(wx.Size(453, 308))
        self.SetIcon(wx.Icon(u'pic/red.ico',wx.BITMAP_TYPE_ICO))

        self.panel1 = wx.Panel(id=wxID_FRAMEREDSHRINKPANEL1, name='panel1',
              parent=self, pos=wx.Point(0, 0), size=wx.Size(453, 308),
              style=wx.TAB_TRAVERSAL)

        self.textCtrl1 = wx.TextCtrl(id=wxID_FRAMEREDSHRINKTEXTCTRL1,
              name='textCtrl1', parent=self.panel1, pos=wx.Point(16, 8),
              size=wx.Size(424, 248), style=wx.TE_MULTILINE,
              value=u'\u7f29\u6c34\u6570\u636e\u663e\u793a\u7a97\u53e3')

        self.button1 = wx.Button(id=wxID_FRAMEREDSHRINKBUTTON1,
              label=u'\u5747\u5300\u5206\u5e03', name='button1',
              parent=self.panel1, pos=wx.Point(30, 272), size=wx.Size(75, 24),
              style=0)
        self.button1.Bind(wx.EVT_BUTTON, self.OnButton1Button,
              id=wxID_FRAMEREDSHRINKBUTTON1)

        self.button2 = wx.Button(id=wxID_FRAMEREDSHRINKBUTTON2,
              label=u'\u56db\u5143\u7f29\u6c34', name='button2',
              parent=self.panel1, pos=wx.Point(130, 272), size=wx.Size(75, 24),
              style=0)
        self.button2.Bind(wx.EVT_BUTTON, self.OnButton2Button,
              id=wxID_FRAMEREDSHRINKBUTTON2)

        self.button3 = wx.Button(id=wxID_FRAMEREDSHRINKBUTTON3,
              label=u'\u4e2d6\u4fdd4', name='button3',
              parent=self.panel1, pos=wx.Point(230, 272), size=wx.Size(75, 24),
              style=0)
        self.button3.Bind(wx.EVT_BUTTON, self.OnButton3Button,
              id=wxID_FRAMEREDSHRINKBUTTON3)

        self.button4 = wx.Button(id=wxID_FRAMEREDSHRINKBUTTON4,
              label=u'\u4fdd\u5b58\u6570\u636e', name='button4',
              parent=self.panel1, pos=wx.Point(330, 272), size=wx.Size(75, 24),
              style=0)
        self.button4.Bind(wx.EVT_BUTTON, self.OnButton4Button,
              id=wxID_FRAMEREDSHRINKBUTTON4)

    def __init__(self, parent):
        self._init_ctrls(parent)
        #命令行提示
        print (u'FrameRedShrink启动').encode(locale.getdefaultlocale()[1])
        
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
        
    def OnButton1Button(self, event):
        '''第1个缩水条件'''
        self.textCtrl1.AppendText(u'使用缩水条件1（均匀分布）\n')
        #求得第1个缩水条件
        t_num = [] #33个号码
        t_times = [] #33个号码的出现次数
        for i in range(1, 33+1): #初始化
            t_num.append('%.2d'%i)
            t_times.append(0)
        for i in range(0, len(predict_data)): #求得次数
            for j in range(0, len(t_num)):
                if t_num[j] in predict_data[i]:
                    t_times[j] = t_times[j] + 1
        for t1 in range(0, len(t_times)-1): #按照次数排序
            for t2 in range(len(t_times)-2, t1-1, -1):
                if t_times[t2]>t_times[t2+1]:
                    tmp_t = t_times[t2]
                    t_times[t2] = t_times[t2+1]
                    t_times[t2+1] = tmp_t
                    tmp_n = t_num[t2]
                    t_num[t2] = t_num[t2+1]
                    t_num[t2+1] = tmp_n
        c_num = t_num[:11] #冷号
        w_num = t_num[11:22] #温号
        h_num = t_num[22:] #热号
        self.textCtrl1.AppendText(u'1区：%s\n'%(str(c_num)))
        self.textCtrl1.AppendText(u'2区：%s\n'%(str(w_num)))
        self.textCtrl1.AppendText(u'3区：%s\n'%(str(h_num)))
        self.textCtrl1.AppendText(u'每一区分布个数在0～4之间\n')
        #使用第1个缩水条件
        global data_s #调用总的缩水后数据
        print len(data_s) #命令行显示一下
        data_s1 = [] #使用缩水条件1后的数据
        for i in range(0, len(data_s)):
            c_t = 0
            w_t = 0
            h_t = 0
            for t1 in range(0, 11):
                if c_num[t1] in data_s[i]:
                    c_t = c_t + 1
                if w_num[t1] in data_s[i]:
                    w_t = w_t + 1
                if h_num[t1] in data_s[i]:
                    h_t = h_t + 1
            if 0<=c_t<=4 and 0<=w_t<=4 and 0<=h_t<=4:
                data_s1.append(data_s[i])
        print len(data_s1) #命令行显示一下
        self.textCtrl1.AppendText(u'（缩水后的数据：%d组）\n'%len(data_s1))
        #传递值
        data_s = data_s1
        #判断是否组数大于10，若大于10则不显示
        if len(data_s)>10:
            pass
        else:
            for i in range(0, len(data_s)):
                self.textCtrl1.AppendText('%s\n'%str(data_s[i]))
      
        event.Skip()

    def OnButton2Button(self, event):
        '''第2个缩水条件'''
        self.textCtrl1.AppendText(u'使用缩水条件2（四元缩水）\n')
        #求得第2个缩水条件
        f = open(u'data/缩水条件.txt', 'r')
        s = f.readlines()
        f.close()
        m4 = []
        for i in range(0, len(s)):
            t = []
            for j in range(0, 4):
                t.append(s[i][j*3:j*3+2])
            m4.append(t)
        self.textCtrl1.AppendText(u'四元组个数：%d\n'%len(m4))
        self.textCtrl1.AppendText(u'每个四元组分布个数在0～2之间\n')
        #使用第2个缩水条件
        global data_s #调用总的缩水后数据
        print len(data_s) #命令行显示一下
        data_s2 = [] #使用缩水条件2后的数据
        for i in range(0, len(data_s)):
            Judge = True
            for j in range(0, len(m4)):
                option = 0
                for k in range(0, 4):
                    if m4[j][k] in data_s[i]:
                        option = option + 1
                if option>2:  
                    Judge = False
                    break
            if Judge:
                data_s2.append(data_s[i])
            if i%1000==0:
                print i, len(data_s2)
        print len(data_s2) #命令行显示一下
        self.textCtrl1.AppendText(u'（缩水后的数据：%d组）\n'%len(data_s2))
        #传递值      
        data_s = data_s2        
        #判断是否组数大于10，若大于10则不显示
        if len(data_s)>10:
            pass
        else:
            for i in range(0, len(data_s)):
                self.textCtrl1.AppendText('%s\n'%str(data_s[i]))
      
        event.Skip()

    def OnButton3Button(self, event):
        '''第3个缩水条件'''
        self.textCtrl1.AppendText(u'使用缩水条件3（中6保4）\n')       
        #使用第3个缩水条件
        global data_s #调用总的缩水后数据
        print len(data_s) #命令行显示一下
        data_s3 = [] #使用缩水条件3后的数据
        while True and len(data_s)!=0:
            t = data_s[random.randint(0, len(data_s)-1)]
            data_s3.append(t) #添加
            data_s.remove(t) #删除
            t_del = [] #要删除的数据
            for i in range(0, len(data_s)): #循环添加
                option = 0
                for j in range(0, len(t)):
                    if t[j] in data_s[i]:
                        option = option + 1
                if option>=4:
                    t_del.append(data_s[i])
            for i in range(0, len(t_del)): #循环删除
                data_s.remove(t_del[i])
            print len(data_s),len(data_s3) #命令行显示一下
            #判断是否只剩最后一注
            if len(data_s)==1:
                data_s3.append(data_s[0])
                break
            #如果已经全部过滤完了，就直接退出
            if len(data_s)==0:
                break
        self.textCtrl1.AppendText(u'（缩水后的数据：%d组）\n'%len(data_s3))
        #传递值
        data_s = data_s3
        #判断是否组数大于10，若大于10则不显示
        if len(data_s)>10:
            pass
        else:
            for i in range(0, len(data_s)):
                self.textCtrl1.AppendText('%s\n'%str(data_s[i]))
        
        event.Skip()

    def OnButton4Button(self, event):
        '''保存数据'''
        #写出生成数据
        f = open(u'%s/%s缩水数据.txt'%(date+1,date+1), 'w')
        #写数据
        for i in range(0, len(data_s)):
            #这里如果使用一个子循环的话，会花费更多时间
            f.write('%s %s %s %s %s %s\n'\
                    %(data_s[i][0],data_s[i][1],data_s[i][2],data_s[i][3],data_s[i][4],data_s[i][5]))
        f.close()
        #关闭页面
        self.Close()
        #打开相应文件夹
        if wx.Platform == '__WXMSW__': #windows
            os.startfile('%s'%(date+1))
        else: #linux
            print (u'缩水数据文件已保存！').encode(locale.getdefaultlocale()[1])
        
        event.Skip()
