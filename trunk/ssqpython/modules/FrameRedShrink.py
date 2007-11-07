#Boa:Frame:FrameRedShrink
# -*- coding: cp936 -*-
# otherrrr@gmail.com
# ������ˮ���

import wx
import os
import random

from DataFileIO import readDataFileToArray
from PredictFileIO import readPredictData

predict_data = [] #���˺�����ݣ����ļ��ж������ģ�
data_s = [] #��ˮ�������
date = [] #����

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
        #��������ʾ
        print 'FrameRedShrink����'
        
        #��ʾ������
        self.textCtrl1.Clear()
        #��ȡ��������
        data_array = readDataFileToArray()
        #����һ�ڵ��ں�
        global date #��������ʱ���õ�����global        
        date = int(data_array[0][0])        
        #��ȡ��������
        global predict_data #������ˮ����1ʱ���õ��������ݣ���global
        predict_data, predict_filter, select_num =readPredictData(date+1)
        self.textCtrl1.AppendText('�Ѷ�ȡ���˺����ݡ�%s��������.txt��'%(date+1))
        self.textCtrl1.AppendText('��%d�飩\n'%len(predict_data))
        
        global data_s #�����ܵĹ��˺�����
        data_s = predict_data #��ʼʱ�����˺����ݵ���Ԥ������
        
    def OnButton1Button(self, event):
        '''��1����ˮ����'''
        self.textCtrl1.AppendText('ʹ����ˮ����1�����ȷֲ���\n')
        #��õ�1����ˮ����
        t_num = [] #33������
        t_times = [] #33������ĳ��ִ���
        for i in range(1, 33+1): #��ʼ��
            t_num.append('%.2d'%i)
            t_times.append(0)
        for i in range(0, len(predict_data)): #��ô���
            for j in range(0, len(t_num)):
                if t_num[j] in predict_data[i]:
                    t_times[j] = t_times[j] + 1
        for t1 in range(0, len(t_times)-1): #���մ�������
            for t2 in range(len(t_times)-2, t1-1, -1):
                if t_times[t2]>t_times[t2+1]:
                    tmp_t = t_times[t2]
                    t_times[t2] = t_times[t2+1]
                    t_times[t2+1] = tmp_t
                    tmp_n = t_num[t2]
                    t_num[t2] = t_num[t2+1]
                    t_num[t2+1] = tmp_n
        c_num = t_num[:11] #���
        w_num = t_num[11:22] #�º�
        h_num = t_num[22:] #�Ⱥ�
        self.textCtrl1.AppendText('1����%s\n'%(str(c_num)))
        self.textCtrl1.AppendText('2����%s\n'%(str(w_num)))
        self.textCtrl1.AppendText('3����%s\n'%(str(h_num)))
        self.textCtrl1.AppendText('ÿһ���ֲ�������0��4֮��\n')
        #ʹ�õ�1����ˮ����
        global data_s #�����ܵ���ˮ������
        print len(data_s) #��������ʾһ��
        data_s1 = [] #ʹ����ˮ����1�������
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
        print len(data_s1) #��������ʾһ��
        self.textCtrl1.AppendText('����ˮ������ݣ�%d�飩\n'%len(data_s1))
        #����ֵ
        data_s = data_s1
        #�ж��Ƿ���������10��������10����ʾ
        if len(data_s)>10:
            pass
        else:
            for i in range(0, len(data_s)):
                self.textCtrl1.AppendText('%s\n'%str(data_s[i]))
      
        event.Skip()

    def OnButton2Button(self, event):
        '''��2����ˮ����'''
        self.textCtrl1.AppendText('ʹ����ˮ����2����Ԫ��ˮ��\n')
        #��õ�2����ˮ����
        f = open('data/��ˮ����.txt', 'r')
        s = f.readlines()
        f.close()
        m4 = []
        for i in range(0, len(s)):
            t = []
            for j in range(0, 4):
                t.append(s[i][j*3:j*3+2])
            m4.append(t)
        self.textCtrl1.AppendText('��Ԫ�������%d\n'%len(m4))
        self.textCtrl1.AppendText('ÿ����Ԫ��ֲ�������0��2֮��\n')
        #ʹ�õ�2����ˮ����
        global data_s #�����ܵ���ˮ������
        print len(data_s) #��������ʾһ��
        data_s2 = [] #ʹ����ˮ����2�������
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
        print len(data_s2) #��������ʾһ��
        self.textCtrl1.AppendText('����ˮ������ݣ�%d�飩\n'%len(data_s2))
        #����ֵ      
        data_s = data_s2        
        #�ж��Ƿ���������10��������10����ʾ
        if len(data_s)>10:
            pass
        else:
            for i in range(0, len(data_s)):
                self.textCtrl1.AppendText('%s\n'%str(data_s[i]))
      
        event.Skip()

    def OnButton3Button(self, event):
        '''��3����ˮ����'''
        self.textCtrl1.AppendText('ʹ����ˮ����3����6��4��\n')       
        #ʹ�õ�3����ˮ����
        global data_s #�����ܵ���ˮ������
        print len(data_s) #��������ʾһ��
        data_s3 = [] #ʹ����ˮ����3�������
        while True:
            t = data_s[random.randint(0, len(data_s)-1)]
            data_s3.append(t) #���
            data_s.remove(t) #ɾ��
            t_del = [] #Ҫɾ��������
            for i in range(0, len(data_s)): #ѭ�����
                option = 0
                for j in range(0, len(t)):
                    if t[j] in data_s[i]:
                        option = option + 1
                if option>=4:
                    t_del.append(data_s[i])
            for i in range(0, len(t_del)): #ѭ��ɾ��
                data_s.remove(t_del[i])
            print len(data_s),len(data_s3) #��������ʾһ��
            #�ж��Ƿ�ֻʣ���һע
            if len(data_s)==1:
                data_s3.append(data_s[0])
                break
            #����Ѿ�ȫ���������ˣ���ֱ���˳�
            if len(data_s)==0:
                break
        self.textCtrl1.AppendText('����ˮ������ݣ�%d�飩\n'%len(data_s3))
        #����ֵ
        data_s = data_s3
        #�ж��Ƿ���������10��������10����ʾ
        if len(data_s)>10:
            pass
        else:
            for i in range(0, len(data_s)):
                self.textCtrl1.AppendText('%s\n'%str(data_s[i]))
        
        event.Skip()

    def OnButton4Button(self, event):
        '''��������'''
        #д����������
        f = open('%s/%s��ˮ����.txt'%(date+1,date+1), 'w')
        #д����
        for i in range(0, len(data_s)):
            #�������ʹ��һ����ѭ���Ļ����Ứ�Ѹ���ʱ��
            f.write('%s %s %s %s %s %s\n'\
                    %(data_s[i][0],data_s[i][1],data_s[i][2],data_s[i][3],data_s[i][4],data_s[i][5]))
        f.close()
        #�ر�ҳ��
        self.Close()
        #����Ӧ�ļ���
        os.startfile('%s'%(date+1))
        
        event.Skip()
