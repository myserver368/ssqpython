#! usr/bin/python
# -*- coding:utf-8 -*-
#Boa:Frame:FrameBlue
# otherrrr@gmail.com
# 蓝球推荐面板

import wx
import locale

from DataFileIO import readDataFileToArray
from DataCompute import blueCoumpute
import FrameAdvice

data_array = [] #开奖数据
blue_times = [] #蓝球的出球频率
blue_step = [] #蓝球的出球步长
blue_drop = [] #蓝球的遗漏值（即多少期未出现）
now_date = 0 #当前期号

def create(parent):
    return FrameBlue(parent)

[wxID_FRAMEBLUE, wxID_FRAMEBLUEBITMAPBUTTONADVICE, wxID_FRAMEBLUEBUTTON1, 
 wxID_FRAMEBLUEBUTTON2, wxID_FRAMEBLUEPANEL1, 
] = [wx.NewId() for _init_ctrls in range(5)]

class FrameBlue(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAMEBLUE, name=u'FrameBlue',
              parent=prnt, pos=wx.Point(278, 221), size=wx.Size(608, 357),
              style=wx.DEFAULT_FRAME_STYLE,
              title=u'\u84dd\u7403\uff08\u4e0d\u5305\u62ec\u5feb\u4e50\u661f\u671f\u5929\u548c\u5feb\u4e50\u5047\u65e5\uff09')
        self.SetClientSize(wx.Size(600, 330))
        self.SetIcon(wx.Icon(u'pic/blue.ico',wx.BITMAP_TYPE_ICO))
        self.Bind(wx.EVT_CHAR, self.OnFrameBlueChar)

        self.panel1 = wx.Panel(id=wxID_FRAMEBLUEPANEL1, name='panel1',
              parent=self, pos=wx.Point(0, 0), size=wx.Size(600, 330),
              style=wx.TAB_TRAVERSAL)
        self.panel1.Bind(wx.EVT_PAINT, self.OnPanel1Paint)

        self.button1 = wx.Button(id=wxID_FRAMEBLUEBUTTON1,
              label=u'\u524d\u4e00\u671f', name='button1', parent=self.panel1,
              pos=wx.Point(432, 20), size=wx.Size(75, 24), style=0)
        self.button1.Bind(wx.EVT_BUTTON, self.OnButton1Button,
              id=wxID_FRAMEBLUEBUTTON1)

        self.button2 = wx.Button(id=wxID_FRAMEBLUEBUTTON2,
              label=u'\u540e\u4e00\u671f', name='button2', parent=self.panel1,
              pos=wx.Point(520, 20), size=wx.Size(75, 24), style=0)
        self.button2.Bind(wx.EVT_BUTTON, self.OnButton2Button,
              id=wxID_FRAMEBLUEBUTTON2)

        self.bitmapButtonadvice = wx.BitmapButton(bitmap=wx.Bitmap(u'pic/advice.png',
              wx.BITMAP_TYPE_PNG), id=wxID_FRAMEBLUEBITMAPBUTTONADVICE,
              name=u'bitmapButtonadvice', parent=self.panel1, pos=wx.Point(16,
              16), size=wx.Size(24, 24), style=wx.BU_AUTODRAW)
        self.bitmapButtonadvice.Bind(wx.EVT_BUTTON,
              self.OnBitmapButtonadviceButton,
              id=wxID_FRAMEBLUEBITMAPBUTTONADVICE)

    def __init__(self, parent):
        self._init_ctrls(parent)
        #命令行提示
        print (u'FrameBlue启动').encode(locale.getdefaultlocale()[1])
        
        #调整位置
        self.Center()
        
        global data_array, blue_times, blue_step, blue_drop
        #读取开奖数据
        data_array = readDataFileToArray()
        #蓝球数据统计及计算
        blue_times, blue_step, blue_drop = blueCoumpute(data_array)   

        #设置焦点（主要是为了捕捉键盘输入）
        self.SetFocus()
        
    def OnPanel1Paint(self, event):
        #绘制图表
        pdc = wx.PaintDC(self.panel1)
        try:
            dc = wx.GCDC(pdc)
        except:
            dc = pdc

        #绘制说明
        dc.DrawText(u'%s'%(data_array[now_date][0]), 45, 20)
        dc.SetTextForeground('#0033FF')
        dc.DrawText(u'球号', 95, 20)
        dc.SetTextForeground('#FF0000')
        dc.DrawText(u'步长', 125, 20)
        dc.SetTextForeground('#FF00FF') 
        dc.DrawText(u'出球次数', 155, 20)
        dc.SetTextForeground('#00CC00')  
        dc.DrawText(u'遗漏值', 210, 20)
        dc.SetTextForeground('#0099FF')
        dc.DrawText(u'遗漏值减步长的差值', 255, 20)
        
        #绘制坐标轴
        dc.SetPen(wx.Pen('#0066FF', 2))
        dc.DrawLine(5,290,595,290) #横线x        
        #-----------------------------------------------------------------------
        #画出每个球的步长
        value_average = 0 #平均值
        value_max = 0 #最大值（即上限，要比最大值大一些）
        for i in range(0, len(blue_step)):
            value_average = value_average + blue_step[i]
        value_average = float(value_average)/16
        value_max = int(value_average*4)
        dc.SetPen(wx.Pen(wx.Colour(178, 34, 34, wx.ALPHA_OPAQUE))) 
        dc.SetBrush(wx.Brush(wx.Colour(178, 34, 34, 100))) #100就是那个“透明度”的值        
        for i in range(0, len(blue_step)):    
            rect = wx.Rect(14+i*36, 290-300*blue_step[i]/value_max, 14, 300*blue_step[i]/value_max) #左上x,左上y,宽,高
            dc.DrawRoundedRectangleRect(rect, 1) #1是那个“角度”
   
        #标注具体的出球步长
        dc.SetTextForeground('#FF0000') 
        for i in range(0, len(blue_step)):
            dc.DrawText('%2d'%blue_step[i], 14+i*36-12, 290-(300*blue_step[i]/value_max)-5) 

        #-----------------------------------------------------------------------
        #画出每个球的次数
        value_average = 0 #平均值
        value_max = 0 #最大值（即上限，要比最大值大那么一点点）
        for i in range(0, len(blue_times)):
            value_average = value_average + blue_times[i]
        value_average = float(value_average)/16
        value_max = int(value_average*4)
        dc.SetPen(wx.Pen(wx.Colour(0, 0, 139, wx.ALPHA_OPAQUE))) 
        dc.SetBrush(wx.Brush(wx.Colour(0, 0, 139, 100))) #100就是那个“透明度”的值        
        for i in range(0, len(blue_times)):    
            rect = wx.Rect(14+i*36+6, 290-300*blue_times[i]/value_max, 14, 300*blue_times[i]/value_max) #左上x,左上y,宽,高
            dc.DrawRoundedRectangleRect(rect, 1) #1是那个“角度”
   
        #标注具体的出球次数
        dc.SetTextForeground('#FF00FF') 
        for i in range(0, len(blue_times)):
            dc.DrawText('%2d'%blue_times[i], 14+i*36+6-12, 290-(300*blue_times[i]/value_max)-5) 
        
        #-----------------------------------------------------------------------
        #画出每个球的遗漏值
        value_average = 0 #平均值
        value_max = 0 #最大值
        for i in range(0, len(blue_drop)):
            value_average = value_average + blue_drop[i]
        value_average = float(value_average)/16
        value_max = int(value_average*4)
        dc.SetPen(wx.Pen(wx.Colour(35, 142, 35, wx.ALPHA_OPAQUE))) 
        dc.SetBrush(wx.Brush(wx.Colour(35, 142, 35, 100)))            
        for i in range(0, len(blue_drop)):    
            rect = wx.Rect(14+i*36+12, 290-300*blue_drop[i]/value_max, 14, 300*blue_drop[i]/value_max) #左上x,左上y,宽,高
            dc.DrawRoundedRectangleRect(rect, 1)
            
        #标注具体的遗漏值
        dc.SetTextForeground('#00CC00')        
        for i in range(0, len(blue_drop)):
            dc.DrawText('%2d'%blue_drop[i], 14+i*36+12-12, 290-(300*blue_drop[i]/value_max)-5) 
        #-----------------------------------------------------------------------
        #在坐标轴下方标注具体的号码
        dc.SetTextForeground('#0033FF')
        dc.SetFont(wx.Font(9, wx.SWISS, wx.NORMAL, wx.NORMAL)) 
        for i in range(0, 16):
            dc.DrawText('%.2d'%(i+1), 14+i*36, 295) 
        #-----------------------------------------------------------------------
        #在号码下方标注（遗漏值－步长）的差值
        dc.SetTextForeground('#0099FF')
        dc.SetFont(wx.Font(9, wx.SWISS, wx.NORMAL, wx.NORMAL)) 
        for i in range(0, 16):
            dc.DrawText('%d'%(blue_drop[i]-blue_step[i]), 14+i*36, 305)             

    def OnButton1Button(self, event):
        '''查看前一期的图形'''
        global now_date, blue_times, blue_step, blue_drop
        #+1
        now_date = now_date + 1
        #蓝球数据重新统计
        blue_times, blue_step, blue_drop = blueCoumpute(data_array[now_date:])  
        #刷新
        self.Refresh() 
        
        event.Skip()

    def OnButton2Button(self, event):
        '''查看后一期的图形'''
        global now_date, blue_times, blue_step, blue_drop
        if now_date==0:
            pass
        else:
            #-1
            now_date = now_date - 1            
            #蓝球数据重新统计
            blue_times, blue_step, blue_drop = blueCoumpute(data_array[now_date:])
            #刷新
            self.Refresh()
        
        event.Skip()

    def OnBitmapButtonadviceButton(self, event):
        '''查看篮球推荐情况'''
        _FrameAdvice = FrameAdvice.create(None)
        _FrameAdvice.Show()
        event.Skip()

    def OnFrameBlueChar(self, event):
        '''快捷键'''
        #得到键值
        keycode = event.GetKeyCode()
        #print keycode

        #输入t就直接弹出推荐情况
        if keycode==116: #t=116
            self.OnBitmapButtonadviceButton(event)
            
        event.Skip()

            
            

            
