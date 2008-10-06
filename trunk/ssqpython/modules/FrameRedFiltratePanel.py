#! usr/bin/python
# -*- coding:utf-8 -*-
#Boa:Frame:FrameRedFiltratePanel
# otherrrr@gmail.com
# 红球过滤选号面板

import wx
import os
import time
import locale

from FilterFileIO import readFilterFileToArray
from PredictFileIO import writePredictData

from DataCompute import percentCompute, dataFiltrate

import FrameRedFiltrate

data_array = []  #数据（数组格式）
data_para_array = [] #数据的相关参数
bet_array = [] #固定投注号码
redOrder = [] #红球号码按着出球次数由大到小排列
redTimes = [] #红球对应出号次数
num_pool = [] #号码池

filter_array = [] #过滤参数
percent_array = [] #过滤条件的百分比
data_f = [] #过滤后生成的数据
msg = [] #显示信息 #这个其实可以改成dict

checkBox_list = [] #号码选择按钮组

def create(parent, choice_num, data_array, bet_array, data_para_array, redOrder, redTimes):
    return FrameRedFiltratePanel(parent, choice_num, data_array, bet_array, data_para_array, redOrder, redTimes)

[wxID_FRAMEREDFILTRATEPANEL, wxID_FRAMEREDFILTRATEPANELBUTTONDATABUILD, 
 wxID_FRAMEREDFILTRATEPANELBUTTONEXIT, wxID_FRAMEREDFILTRATEPANELBUTTONINPUT, 
 wxID_FRAMEREDFILTRATEPANELBUTTONLOAD, 
 wxID_FRAMEREDFILTRATEPANELBUTTONONESTEP, 
 wxID_FRAMEREDFILTRATEPANELCHECKBOX01, wxID_FRAMEREDFILTRATEPANELCHECKBOX02, 
 wxID_FRAMEREDFILTRATEPANELCHECKBOX03, wxID_FRAMEREDFILTRATEPANELCHECKBOX04, 
 wxID_FRAMEREDFILTRATEPANELCHECKBOX05, wxID_FRAMEREDFILTRATEPANELCHECKBOX06, 
 wxID_FRAMEREDFILTRATEPANELCHECKBOX07, wxID_FRAMEREDFILTRATEPANELCHECKBOX08, 
 wxID_FRAMEREDFILTRATEPANELCHECKBOX09, wxID_FRAMEREDFILTRATEPANELCHECKBOX10, 
 wxID_FRAMEREDFILTRATEPANELCHECKBOX11, wxID_FRAMEREDFILTRATEPANELCHECKBOX12, 
 wxID_FRAMEREDFILTRATEPANELCHECKBOX13, wxID_FRAMEREDFILTRATEPANELCHECKBOX14, 
 wxID_FRAMEREDFILTRATEPANELCHECKBOX15, wxID_FRAMEREDFILTRATEPANELCHECKBOX16, 
 wxID_FRAMEREDFILTRATEPANELCHECKBOX17, wxID_FRAMEREDFILTRATEPANELCHECKBOX18, 
 wxID_FRAMEREDFILTRATEPANELCHECKBOX19, wxID_FRAMEREDFILTRATEPANELCHECKBOX20, 
 wxID_FRAMEREDFILTRATEPANELCHECKBOX21, wxID_FRAMEREDFILTRATEPANELCHECKBOX22, 
 wxID_FRAMEREDFILTRATEPANELCHECKBOX23, wxID_FRAMEREDFILTRATEPANELCHECKBOX24, 
 wxID_FRAMEREDFILTRATEPANELCHECKBOX25, wxID_FRAMEREDFILTRATEPANELCHECKBOX26, 
 wxID_FRAMEREDFILTRATEPANELCHECKBOX27, wxID_FRAMEREDFILTRATEPANELCHECKBOX28, 
 wxID_FRAMEREDFILTRATEPANELCHECKBOX29, wxID_FRAMEREDFILTRATEPANELCHECKBOX30, 
 wxID_FRAMEREDFILTRATEPANELCHECKBOX31, wxID_FRAMEREDFILTRATEPANELCHECKBOX32, 
 wxID_FRAMEREDFILTRATEPANELCHECKBOX33, wxID_FRAMEREDFILTRATEPANELPANEL1, 
 wxID_FRAMEREDFILTRATEPANELPANEL2, wxID_FRAMEREDFILTRATEPANELRADIOBUTTONALLNO, 
 wxID_FRAMEREDFILTRATEPANELRADIOBUTTONALLYES, 
] = [wx.NewId() for _init_ctrls in range(43)]

class FrameRedFiltratePanel(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAMEREDFILTRATEPANEL,
              name=u'FrameAbnormalFiltrate', parent=prnt, pos=wx.Point(388,
              232), size=wx.Size(488, 448), style=wx.DEFAULT_FRAME_STYLE,
              title=u'\u7ea2\u7403\u8fc7\u6ee4')
        self.SetIcon(wx.Icon(u'pic/red.ico',wx.BITMAP_TYPE_ICO))
        self.SetClientSize(wx.Size(480, 414))

        self.panel1 = wx.Panel(id=wxID_FRAMEREDFILTRATEPANELPANEL1,
              name='panel1', parent=self, pos=wx.Point(0, 0), size=wx.Size(480,
              414), style=wx.TAB_TRAVERSAL)
        self.panel1.Bind(wx.EVT_PAINT, self.OnPanel1Paint)

        self.buttondatabuild = wx.Button(id=wxID_FRAMEREDFILTRATEPANELBUTTONDATABUILD,
              label=u'\u751f\u6210\u521d\u59cb\u6570\u636e(&B)',
              name=u'buttondatabuild', parent=self.panel1, pos=wx.Point(34, 32),
              size=wx.Size(120, 24), style=0)
        self.buttondatabuild.SetForegroundColour(wx.Colour(255, 0, 0))
        self.buttondatabuild.Bind(wx.EVT_BUTTON, self.OnButtondatabuildButton,
              id=wxID_FRAMEREDFILTRATEPANELBUTTONDATABUILD)

        self.buttonload = wx.Button(id=wxID_FRAMEREDFILTRATEPANELBUTTONLOAD,
              label=u'\u52a0\u8f7d\u6570\u636e(&L)', name=u'buttonload',
              parent=self.panel1, pos=wx.Point(192, 32), size=wx.Size(100, 24),
              style=0)
        self.buttonload.Bind(wx.EVT_BUTTON, self.OnButtonloadButton,
              id=wxID_FRAMEREDFILTRATEPANELBUTTONLOAD)

        self.buttononestep = wx.Button(id=wxID_FRAMEREDFILTRATEPANELBUTTONONESTEP,
              label=u'\u4e00\u6b65\u8fc7\u6ee4(&O)', name=u'buttononestep',
              parent=self.panel1, pos=wx.Point(338, 32), size=wx.Size(100, 24),
              style=0)
        self.buttononestep.SetForegroundColour(wx.Colour(128, 0, 255))
        self.buttononestep.Bind(wx.EVT_BUTTON, self.OnButtononestepButton,
              id=wxID_FRAMEREDFILTRATEPANELBUTTONONESTEP)

        self.buttoninput = wx.Button(id=wxID_FRAMEREDFILTRATEPANELBUTTONINPUT,
              label=u'\u53f7\u7801\u8f93\u5165(&I)', name=u'buttoninput',
              parent=self.panel1, pos=wx.Point(338, 364), size=wx.Size(100, 24),
              style=0)
        self.buttoninput.SetForegroundColour(wx.Colour(19, 172, 153))
        self.buttoninput.Bind(wx.EVT_BUTTON, self.OnButtoninputButton,
              id=wxID_FRAMEREDFILTRATEPANELBUTTONINPUT)

        self.buttonexit = wx.Button(id=wxID_FRAMEREDFILTRATEPANELBUTTONEXIT,
              label=u'\u9000\u51fa(&X)', name=u'buttonexit', parent=self.panel1,
              pos=wx.Point(20, 364), size=wx.Size(60, 24), style=0)
        self.buttonexit.Bind(wx.EVT_BUTTON, self.OnButtonexitButton,
              id=wxID_FRAMEREDFILTRATEPANELBUTTONEXIT)

        self.panel2 = wx.Panel(id=wxID_FRAMEREDFILTRATEPANELPANEL2,
              name='panel2', parent=self.panel1, pos=wx.Point(20, 100),
              size=wx.Size(440, 240),
              style=wx.STATIC_BORDER | wx.TAB_TRAVERSAL)
        self.panel2.SetBackgroundColour(wx.Colour(226, 219, 207))

        self.radioButtonallyes = wx.RadioButton(id=wxID_FRAMEREDFILTRATEPANELRADIOBUTTONALLYES,
              label=u'\u5168\u9009(&A)', name=u'radioButtonallyes',
              parent=self.panel2, pos=wx.Point(130, 30), size=wx.Size(96, 14),
              style=0)
        self.radioButtonallyes.SetValue(False)
        self.radioButtonallyes.Bind(wx.EVT_RADIOBUTTON,
              self.OnRadioButtonallyesRadiobutton,
              id=wxID_FRAMEREDFILTRATEPANELRADIOBUTTONALLYES)

        self.radioButtonallno = wx.RadioButton(id=wxID_FRAMEREDFILTRATEPANELRADIOBUTTONALLNO,
              label=u'\u5168\u4e0d\u9009(&N)', name=u'radioButtonallno',
              parent=self.panel2, pos=wx.Point(270, 30), size=wx.Size(96, 14),
              style=0)
        self.radioButtonallno.SetValue(True)
        self.radioButtonallno.Bind(wx.EVT_RADIOBUTTON,
              self.OnRadioButtonallnoRadiobutton,
              id=wxID_FRAMEREDFILTRATEPANELRADIOBUTTONALLNO)

        self.checkBox01 = wx.CheckBox(id=wxID_FRAMEREDFILTRATEPANELCHECKBOX01,
              label=u'01', name=u'checkBox01', parent=self.panel2,
              pos=wx.Point(80, 60), size=wx.Size(40, 14), style=0)
        self.checkBox01.SetValue(False)
        self.checkBox01.Bind(wx.EVT_CHECKBOX, self.OnCheckBox01Checkbox,
              id=wxID_FRAMEREDFILTRATEPANELCHECKBOX01)

        self.checkBox02 = wx.CheckBox(id=wxID_FRAMEREDFILTRATEPANELCHECKBOX02,
              label=u'02', name=u'checkBox02', parent=self.panel2,
              pos=wx.Point(140, 60), size=wx.Size(40, 14), style=0)
        self.checkBox02.SetValue(False)
        self.checkBox02.Bind(wx.EVT_CHECKBOX, self.OnCheckBox02Checkbox,
              id=wxID_FRAMEREDFILTRATEPANELCHECKBOX02)

        self.checkBox03 = wx.CheckBox(id=wxID_FRAMEREDFILTRATEPANELCHECKBOX03,
              label=u'03', name=u'checkBox03', parent=self.panel2,
              pos=wx.Point(200, 60), size=wx.Size(40, 14), style=0)
        self.checkBox03.SetValue(False)
        self.checkBox03.Bind(wx.EVT_CHECKBOX, self.OnCheckBox03Checkbox,
              id=wxID_FRAMEREDFILTRATEPANELCHECKBOX03)

        self.checkBox04 = wx.CheckBox(id=wxID_FRAMEREDFILTRATEPANELCHECKBOX04,
              label=u'04', name=u'checkBox04', parent=self.panel2,
              pos=wx.Point(260, 60), size=wx.Size(40, 14), style=0)
        self.checkBox04.SetValue(False)
        self.checkBox04.Bind(wx.EVT_CHECKBOX, self.OnCheckBox04Checkbox,
              id=wxID_FRAMEREDFILTRATEPANELCHECKBOX04)

        self.checkBox05 = wx.CheckBox(id=wxID_FRAMEREDFILTRATEPANELCHECKBOX05,
              label=u'05', name=u'checkBox05', parent=self.panel2,
              pos=wx.Point(320, 60), size=wx.Size(40, 14), style=0)
        self.checkBox05.SetValue(False)
        self.checkBox05.Bind(wx.EVT_CHECKBOX, self.OnCheckBox05Checkbox,
              id=wxID_FRAMEREDFILTRATEPANELCHECKBOX05)

        self.checkBox06 = wx.CheckBox(id=wxID_FRAMEREDFILTRATEPANELCHECKBOX06,
              label=u'06', name=u'checkBox06', parent=self.panel2,
              pos=wx.Point(50, 90), size=wx.Size(40, 14), style=0)
        self.checkBox06.SetValue(False)
        self.checkBox06.Bind(wx.EVT_CHECKBOX, self.OnCheckBox06Checkbox,
              id=wxID_FRAMEREDFILTRATEPANELCHECKBOX06)

        self.checkBox07 = wx.CheckBox(id=wxID_FRAMEREDFILTRATEPANELCHECKBOX07,
              label=u'07', name=u'checkBox07', parent=self.panel2,
              pos=wx.Point(110, 90), size=wx.Size(40, 14), style=0)
        self.checkBox07.SetValue(False)
        self.checkBox07.Bind(wx.EVT_CHECKBOX, self.OnCheckBox07Checkbox,
              id=wxID_FRAMEREDFILTRATEPANELCHECKBOX07)

        self.checkBox08 = wx.CheckBox(id=wxID_FRAMEREDFILTRATEPANELCHECKBOX08,
              label=u'08', name=u'checkBox08', parent=self.panel2,
              pos=wx.Point(170, 90), size=wx.Size(40, 14), style=0)
        self.checkBox08.SetValue(False)
        self.checkBox08.Bind(wx.EVT_CHECKBOX, self.OnCheckBox08Checkbox,
              id=wxID_FRAMEREDFILTRATEPANELCHECKBOX08)

        self.checkBox09 = wx.CheckBox(id=wxID_FRAMEREDFILTRATEPANELCHECKBOX09,
              label=u'09', name=u'checkBox09', parent=self.panel2,
              pos=wx.Point(230, 90), size=wx.Size(40, 14), style=0)
        self.checkBox09.SetValue(False)
        self.checkBox09.Bind(wx.EVT_CHECKBOX, self.OnCheckBox09Checkbox,
              id=wxID_FRAMEREDFILTRATEPANELCHECKBOX09)

        self.checkBox10 = wx.CheckBox(id=wxID_FRAMEREDFILTRATEPANELCHECKBOX10,
              label=u'10', name=u'checkBox10', parent=self.panel2,
              pos=wx.Point(290, 90), size=wx.Size(40, 14), style=0)
        self.checkBox10.SetValue(False)
        self.checkBox10.Bind(wx.EVT_CHECKBOX, self.OnCheckBox10Checkbox,
              id=wxID_FRAMEREDFILTRATEPANELCHECKBOX10)

        self.checkBox11 = wx.CheckBox(id=wxID_FRAMEREDFILTRATEPANELCHECKBOX11,
              label=u'11', name=u'checkBox11', parent=self.panel2,
              pos=wx.Point(350, 90), size=wx.Size(40, 14), style=0)
        self.checkBox11.SetValue(False)
        self.checkBox11.Bind(wx.EVT_CHECKBOX, self.OnCheckBox11Checkbox,
              id=wxID_FRAMEREDFILTRATEPANELCHECKBOX11)

        self.checkBox12 = wx.CheckBox(id=wxID_FRAMEREDFILTRATEPANELCHECKBOX12,
              label=u'12', name=u'checkBox12', parent=self.panel2,
              pos=wx.Point(80, 120), size=wx.Size(40, 14), style=0)
        self.checkBox12.SetValue(False)
        self.checkBox12.Bind(wx.EVT_CHECKBOX, self.OnCheckBox12Checkbox,
              id=wxID_FRAMEREDFILTRATEPANELCHECKBOX12)

        self.checkBox13 = wx.CheckBox(id=wxID_FRAMEREDFILTRATEPANELCHECKBOX13,
              label=u'13', name=u'checkBox13', parent=self.panel2,
              pos=wx.Point(140, 120), size=wx.Size(40, 14), style=0)
        self.checkBox13.SetValue(False)
        self.checkBox13.Bind(wx.EVT_CHECKBOX, self.OnCheckBox13Checkbox,
              id=wxID_FRAMEREDFILTRATEPANELCHECKBOX13)

        self.checkBox14 = wx.CheckBox(id=wxID_FRAMEREDFILTRATEPANELCHECKBOX14,
              label=u'14', name=u'checkBox14', parent=self.panel2,
              pos=wx.Point(200, 120), size=wx.Size(40, 14), style=0)
        self.checkBox14.SetValue(False)
        self.checkBox14.Bind(wx.EVT_CHECKBOX, self.OnCheckBox14Checkbox,
              id=wxID_FRAMEREDFILTRATEPANELCHECKBOX14)

        self.checkBox15 = wx.CheckBox(id=wxID_FRAMEREDFILTRATEPANELCHECKBOX15,
              label=u'15', name=u'checkBox15', parent=self.panel2,
              pos=wx.Point(260, 120), size=wx.Size(40, 14), style=0)
        self.checkBox15.SetValue(False)
        self.checkBox15.Bind(wx.EVT_CHECKBOX, self.OnCheckBox15Checkbox,
              id=wxID_FRAMEREDFILTRATEPANELCHECKBOX15)

        self.checkBox16 = wx.CheckBox(id=wxID_FRAMEREDFILTRATEPANELCHECKBOX16,
              label=u'16', name=u'checkBox16', parent=self.panel2,
              pos=wx.Point(320, 120), size=wx.Size(40, 14), style=0)
        self.checkBox16.SetValue(False)
        self.checkBox16.Bind(wx.EVT_CHECKBOX, self.OnCheckBox16Checkbox,
              id=wxID_FRAMEREDFILTRATEPANELCHECKBOX16)

        self.checkBox17 = wx.CheckBox(id=wxID_FRAMEREDFILTRATEPANELCHECKBOX17,
              label=u'17', name=u'checkBox17', parent=self.panel2,
              pos=wx.Point(50, 150), size=wx.Size(40, 14), style=0)
        self.checkBox17.SetValue(False)
        self.checkBox17.Bind(wx.EVT_CHECKBOX, self.OnCheckBox17Checkbox,
              id=wxID_FRAMEREDFILTRATEPANELCHECKBOX17)

        self.checkBox18 = wx.CheckBox(id=wxID_FRAMEREDFILTRATEPANELCHECKBOX18,
              label=u'18', name=u'checkBox18', parent=self.panel2,
              pos=wx.Point(110, 150), size=wx.Size(40, 14), style=0)
        self.checkBox18.SetValue(False)
        self.checkBox18.Bind(wx.EVT_CHECKBOX, self.OnCheckBox18Checkbox,
              id=wxID_FRAMEREDFILTRATEPANELCHECKBOX18)

        self.checkBox19 = wx.CheckBox(id=wxID_FRAMEREDFILTRATEPANELCHECKBOX19,
              label=u'19', name=u'checkBox19', parent=self.panel2,
              pos=wx.Point(170, 150), size=wx.Size(40, 14), style=0)
        self.checkBox19.SetValue(False)
        self.checkBox19.Bind(wx.EVT_CHECKBOX, self.OnCheckBox19Checkbox,
              id=wxID_FRAMEREDFILTRATEPANELCHECKBOX19)

        self.checkBox20 = wx.CheckBox(id=wxID_FRAMEREDFILTRATEPANELCHECKBOX20,
              label=u'20', name=u'checkBox20', parent=self.panel2,
              pos=wx.Point(230, 150), size=wx.Size(40, 14), style=0)
        self.checkBox20.SetValue(False)
        self.checkBox20.Bind(wx.EVT_CHECKBOX, self.OnCheckBox20Checkbox,
              id=wxID_FRAMEREDFILTRATEPANELCHECKBOX20)

        self.checkBox21 = wx.CheckBox(id=wxID_FRAMEREDFILTRATEPANELCHECKBOX21,
              label=u'21', name=u'checkBox21', parent=self.panel2,
              pos=wx.Point(290, 150), size=wx.Size(40, 14), style=0)
        self.checkBox21.SetValue(False)
        self.checkBox21.Bind(wx.EVT_CHECKBOX, self.OnCheckBox21Checkbox,
              id=wxID_FRAMEREDFILTRATEPANELCHECKBOX21)

        self.checkBox22 = wx.CheckBox(id=wxID_FRAMEREDFILTRATEPANELCHECKBOX22,
              label=u'22', name=u'checkBox22', parent=self.panel2,
              pos=wx.Point(350, 150), size=wx.Size(40, 14), style=0)
        self.checkBox22.SetValue(False)
        self.checkBox22.Bind(wx.EVT_CHECKBOX, self.OnCheckBox22Checkbox,
              id=wxID_FRAMEREDFILTRATEPANELCHECKBOX22)

        self.checkBox23 = wx.CheckBox(id=wxID_FRAMEREDFILTRATEPANELCHECKBOX23,
              label=u'23', name=u'checkBox23', parent=self.panel2,
              pos=wx.Point(80, 180), size=wx.Size(40, 14), style=0)
        self.checkBox23.SetValue(False)
        self.checkBox23.Bind(wx.EVT_CHECKBOX, self.OnCheckBox23Checkbox,
              id=wxID_FRAMEREDFILTRATEPANELCHECKBOX23)

        self.checkBox24 = wx.CheckBox(id=wxID_FRAMEREDFILTRATEPANELCHECKBOX24,
              label=u'24', name=u'checkBox24', parent=self.panel2,
              pos=wx.Point(140, 180), size=wx.Size(40, 14), style=0)
        self.checkBox24.SetValue(False)
        self.checkBox24.Bind(wx.EVT_CHECKBOX, self.OnCheckBox24Checkbox,
              id=wxID_FRAMEREDFILTRATEPANELCHECKBOX24)

        self.checkBox25 = wx.CheckBox(id=wxID_FRAMEREDFILTRATEPANELCHECKBOX25,
              label=u'25', name=u'checkBox25', parent=self.panel2,
              pos=wx.Point(200, 180), size=wx.Size(40, 14), style=0)
        self.checkBox25.SetValue(False)
        self.checkBox25.Bind(wx.EVT_CHECKBOX, self.OnCheckBox25Checkbox,
              id=wxID_FRAMEREDFILTRATEPANELCHECKBOX25)

        self.checkBox26 = wx.CheckBox(id=wxID_FRAMEREDFILTRATEPANELCHECKBOX26,
              label=u'26', name=u'checkBox26', parent=self.panel2,
              pos=wx.Point(260, 180), size=wx.Size(40, 14), style=0)
        self.checkBox26.SetValue(False)
        self.checkBox26.Bind(wx.EVT_CHECKBOX, self.OnCheckBox26Checkbox,
              id=wxID_FRAMEREDFILTRATEPANELCHECKBOX26)

        self.checkBox27 = wx.CheckBox(id=wxID_FRAMEREDFILTRATEPANELCHECKBOX27,
              label=u'27', name=u'checkBox27', parent=self.panel2,
              pos=wx.Point(320, 180), size=wx.Size(40, 14), style=0)
        self.checkBox27.SetValue(False)
        self.checkBox27.Bind(wx.EVT_CHECKBOX, self.OnCheckBox27Checkbox,
              id=wxID_FRAMEREDFILTRATEPANELCHECKBOX27)

        self.checkBox28 = wx.CheckBox(id=wxID_FRAMEREDFILTRATEPANELCHECKBOX28,
              label=u'28', name=u'checkBox28', parent=self.panel2,
              pos=wx.Point(50, 210), size=wx.Size(40, 14), style=0)
        self.checkBox28.SetValue(False)
        self.checkBox28.Bind(wx.EVT_CHECKBOX, self.OnCheckBox28Checkbox,
              id=wxID_FRAMEREDFILTRATEPANELCHECKBOX28)

        self.checkBox29 = wx.CheckBox(id=wxID_FRAMEREDFILTRATEPANELCHECKBOX29,
              label=u'29', name=u'checkBox29', parent=self.panel2,
              pos=wx.Point(110, 210), size=wx.Size(40, 14), style=0)
        self.checkBox29.SetValue(False)
        self.checkBox29.Bind(wx.EVT_CHECKBOX, self.OnCheckBox29Checkbox,
              id=wxID_FRAMEREDFILTRATEPANELCHECKBOX29)

        self.checkBox30 = wx.CheckBox(id=wxID_FRAMEREDFILTRATEPANELCHECKBOX30,
              label=u'30', name=u'checkBox30', parent=self.panel2,
              pos=wx.Point(170, 210), size=wx.Size(40, 14), style=0)
        self.checkBox30.SetValue(False)
        self.checkBox30.Bind(wx.EVT_CHECKBOX, self.OnCheckBox30Checkbox,
              id=wxID_FRAMEREDFILTRATEPANELCHECKBOX30)

        self.checkBox31 = wx.CheckBox(id=wxID_FRAMEREDFILTRATEPANELCHECKBOX31,
              label=u'31', name=u'checkBox31', parent=self.panel2,
              pos=wx.Point(230, 210), size=wx.Size(40, 14), style=0)
        self.checkBox31.SetValue(False)
        self.checkBox31.Bind(wx.EVT_CHECKBOX, self.OnCheckBox31Checkbox,
              id=wxID_FRAMEREDFILTRATEPANELCHECKBOX31)

        self.checkBox32 = wx.CheckBox(id=wxID_FRAMEREDFILTRATEPANELCHECKBOX32,
              label=u'32', name=u'checkBox32', parent=self.panel2,
              pos=wx.Point(290, 210), size=wx.Size(40, 14), style=0)
        self.checkBox32.SetValue(False)
        self.checkBox32.Bind(wx.EVT_CHECKBOX, self.OnCheckBox32Checkbox,
              id=wxID_FRAMEREDFILTRATEPANELCHECKBOX32)

        self.checkBox33 = wx.CheckBox(id=wxID_FRAMEREDFILTRATEPANELCHECKBOX33,
              label=u'33', name=u'checkBox33', parent=self.panel2,
              pos=wx.Point(350, 210), size=wx.Size(40, 14), style=0)
        self.checkBox33.SetValue(False)
        self.checkBox33.Bind(wx.EVT_CHECKBOX, self.OnCheckBox33Checkbox,
              id=wxID_FRAMEREDFILTRATEPANELCHECKBOX33)

    def __init__(self, parent, choice_num, data_arrays, bet_arrays, data_para_arrays, redOrders, redTimess):
        self._init_ctrls(parent)
        #命令行提示
        print (u'FrameRedFiltratePanel启动').encode(locale.getdefaultlocale()[1])
        if len(choice_num)!=0:
            print (u'已选择的号码').encode(locale.getdefaultlocale()[1]),choice_num #已选号码
        else:
            print (u'未预选任何号码').encode(locale.getdefaultlocale()[1])
        global filter_array, percent_array, data_f, num_pool
        global data_array, bet_array, data_para_array, redOrder, redTimes
        #接收传递过来的值
        data_array = data_arrays
        bet_array = bet_arrays
        data_para_array = data_para_arrays
        redOrder = redOrders
        redTimes = redTimess
        #调整位置
        self.Center()  
        #读取过滤条件
        filter_array = readFilterFileToArray()
        #计算百分比
        percent_array = percentCompute(filter_array, data_para_array)
        #将上一期出现的号码改为蓝色
        global checkBox_list
        checkBox_list = [self.checkBox01,self.checkBox02,self.checkBox03,\
                         self.checkBox04,self.checkBox05,self.checkBox06,\
                         self.checkBox07,self.checkBox08,self.checkBox09,\
                         self.checkBox10,self.checkBox11,self.checkBox12,\
                         self.checkBox13,self.checkBox14,self.checkBox15,\
                         self.checkBox16,self.checkBox17,self.checkBox18,\
                         self.checkBox19,self.checkBox20,self.checkBox21,\
                         self.checkBox22,self.checkBox23,self.checkBox24,\
                         self.checkBox25,self.checkBox26,self.checkBox27,\
                         self.checkBox28,self.checkBox29,self.checkBox30,\
                         self.checkBox31,self.checkBox32,self.checkBox33
                         ]
        for i in range(1, 6+1):
            checkBox_list[int(data_array[0][i])-1].SetForegroundColour('BLUE')
        #将已选择的号码显示为已选状态
        for i in range(0, len(choice_num)/3):
            checkBox_list[int(choice_num[i*3:i*3+2])-1].SetValue(True)
        #将号码池清空
        num_pool = []
        #将已选择的号码加入号码池
        for i in range(0, len(choice_num)/3):
            num_pool.append(int(choice_num[i*3:i*3+2]))   
        #测试
        
        #如果要在unicode版本的wxPython中查看汉字，就要进行unicode操作，如下：
        #print unicode(filter_array[0][1], 'mbcs')

#-------------------------------------------------------------------------------
#----数据生成按钮----

    def OnButtondatabuildButton(self, event): #初始数据生成按钮
        '''生成初始数据（若选择全部红球即为1107568组）'''
        #过滤数据原始定义
        global data_f
        data_f = []
        #判断号码池是否大于等于6个号码
        if len(num_pool)>=6:           
            #将号码池中的数字按照从小到大的顺序排列
            for i in range(len(num_pool)-1, 0, -1):
                for j in range(0, i):
                    if num_pool[j]>num_pool[j+1]:
                        tmp = num_pool[j]
                        num_pool[j] = num_pool[j+1]
                        num_pool[j+1] = tmp
            #进度条
            dlg = wx.ProgressDialog(u"初始数据生成中……",
                            u"请稍候！",
                            maximum = 1107568,
                            parent = self,
                            style = wx.PD_APP_MODAL
                            | wx.PD_ELAPSED_TIME
                            | wx.PD_REMAINING_TIME
                            )
            #1107568组数据生成
            #生成数据有两种方法，所用时间都差不多，只是算法不同而已
            #之所以用第1种，是因为这样可以很容易去掉某个号
            #第1种:（也可以看作是一种遍历）
            pos1 = 0
            for t1 in num_pool[pos1:-5]:
                pos2 = pos1 + 1
                for t2 in num_pool[pos2:-4]:
                    pos3 = pos2 + 1
                    for t3 in num_pool[pos3:-3]:
                        pos4 = pos3 + 1
                        for t4 in num_pool[pos4:-2]:
                            pos5 = pos4 + 1
                            for t5 in num_pool[pos5:-1]:
                                pos6 = pos5 + 1
                                for t6 in num_pool[pos6:]:
                                    data_f.append([t1,t2,t3,t4,t5,t6])
                                    if len(data_f)%55000==0:
                                        dlg.Update(len(data_f))
                                pos5 = pos5 + 1
                            pos4 = pos4 + 1
                        pos3 = pos3 + 1
                    pos2 = pos2 + 1
                pos1 = pos1 + 1        
            #第2种:
            '''
            for t1 in range(1, 29):
                for t2 in range(t1+1, 30):
                    for t3 in range(t2+1, 31):
                        for t4 in range(t3+1, 32):
                            for t5 in range(t4+1, 33):
                                for t6 in range(t5+1, 34):
                                    data_f.append([t1,t2,t3,t4,t5,t6])
                                    if len(data_f)%55000==0:
                                        dlg.Update(len(data_f))
                                
            '''
            #进度条关闭
            dlg.Destroy()
            #打开过滤面板并将数据传输过去!!
            ALL_datas = [data_array, redOrder, redTimes, bet_array,
                         data_para_array, filter_array, percent_array,
                         data_f, num_pool]
            _FrameRedFiltrate = FrameRedFiltrate.create(None, ALL_datas)
            _FrameRedFiltrate.Show() 
            #关闭自身
            self.Close()  
        #号码池中的号码小于6个
        else:
            #弹出提示框
            dlg = wx.MessageDialog(self, u'选中的号码少于6个！', 
                                   u'请重新选择号码',
                                   wx.OK | wx.ICON_INFORMATION
                                   )
            dlg.ShowModal()
            dlg.Destroy()   
            
        event.Skip()
        
#-------------------------------------------------------------------------------
#----加载按钮----  
    def OnButtonloadButton(self, event): #加载按钮
        '''加载已生成的数据'''
        
        #使用文件打开框
        print (u'文件选择框启动').encode(locale.getdefaultlocale()[1])

        #过滤数据原始定义
        global data_f
        data_f = []
            
        #显示文件选择框
        dlg = wx.FileDialog(
            self, message=u"选择需要加载的文件",
            #defaultDir=os.getcwd(), #linux
            defaultFile="",
            #wildcard="", #通配符（可以限制文件类型）
            style=wx.OPEN
            #style=wx.OPEN  | wx.CHANGE_DIR #如果改换目录的话，面板图标找不到
            #style=wx.OPEN | wx.MULTIPLE | wx.CHANGE_DIR #不要多选
            )
        
        if dlg.ShowModal()==wx.ID_OK:         
            #读取选择文件中的数据
            f = open(dlg.GetPaths()[0], 'r') 
            s = f.readlines()
            f.close()
            #数据格式转换
            ##其实转换的时候应该判断一下数据是否合法，但是...
            a = []
            for st in s:
                a.append([int(st[0:2]),int(st[3:5]),int(st[6:8]),\
                          int(st[9:11]),int(st[12:14]),int(st[15:17])])
            #数据加载
            for at in a:
                data_f.append(at)
            #显示一下
            print (u'加载了%d组已生成数据'%len(a)).encode(locale.getdefaultlocale()[1])

        #关闭    
        dlg.Destroy()

        if len(data_f)!=0:
            #关闭自身
            self.Close()
            #打开过滤面板并将数据传输过去!!
            ALL_datas = [data_array, redOrder, redTimes, bet_array,
                         data_para_array, filter_array, percent_array,
                         data_f, num_pool]
            _FrameRedFiltrate = FrameRedFiltrate.create(None, ALL_datas)
            _FrameRedFiltrate.Show()              
            
        event.Skip()

#-------------------------------------------------------------------------------
#----多个号码输入按钮----        
    def OnButtoninputButton(self, event): #多个号码输入按钮
        '''一组号码输入'''
        dlg = wx.TextEntryDialog(
                self, u'号码之间请用空格分隔，并保证号码均为2位',
                u'请输入一组号码', 'Python')
        #默认值
        dlg.SetValue("01 02 03 04 05 06")

        if dlg.ShowModal() == wx.ID_OK:
            #print dlg.GetValue()
            #将号码池清空
            global num_pool
            num_pool = []
            #将已选择的号码加入号码池
            for i in range(0, (len(dlg.GetValue())+1)/3):
                num_pool.append(int(dlg.GetValue()[i*3:i*3+2]))
            #显示选择了多少个球
            msg[1] = '%.2d'%(len(num_pool))
            self.Refresh()
            ##应该先将所有号码状态改为未选（也许会输入两次）
            for i in range(0, 33):
                checkBox_list[i].SetValue(False)
            #将已选择的号码显示为已选状态
            for i in range(0, (len(dlg.GetValue())+1)/3):
                checkBox_list[int(dlg.GetValue()[i*3:i*3+2])-1].SetValue(True)
            
        dlg.Destroy()
        
        event.Skip()

#-------------------------------------------------------------------------------
#----一步过滤按钮----        
    def OnButtononestepButton(self, event): #一步过滤按钮
        '''一次性过滤'''
        global data_f, num_pool,filter_array
        if len(num_pool)>=6:
            continue_f = True #是否继续进行过滤判断符
            if len(num_pool)>20:
                dlg = wx.MessageDialog(self, u'选择号码较多时，花费时间会比较长', 
                                       u'确定要一步过滤？',
                                       wx.YES_NO | wx.NO_DEFAULT | wx.ICON_INFORMATION
                                       )
                result = dlg.ShowModal()
                dlg.Destroy()
                if result==wx.ID_YES: #确定了要一步过滤
                    continue_f = True
                elif result==wx.ID_NO: #不进行一步过滤
                    continue_f = False
            if continue_f==True:
                #开始时间
                start_time = int(time.time())         
                #--进度条
                if wx.Platform == '__WXMSW__':
                    dlg = wx.ProgressDialog(u"过滤中……",
                                    u"请耐心等待！",
                                    maximum = len(filter_array) + 1 + 1,
                                    parent = self,
                                    style = wx.PD_APP_MODAL
                                    )
                #关闭当前窗口（红球过滤面板） #如果不关闭窗口，因为step的变化，窗口中内容也会跟着变化
                self.Close()           
     
                #--将号码池中的数字按照从小到大的顺序排列
                for i in range(len(num_pool)-1, 0, -1):
                    for j in range(0, i):
                        if num_pool[j]>num_pool[j+1]:
                            num_pool[j], num_pool[j+1] = num_pool[j+1], num_pool[j]
                #--生成需要被过滤的所有数据
                pos1 = 0
                for t1 in num_pool[pos1:-5]:
                    pos2 = pos1 + 1
                    for t2 in num_pool[pos2:-4]:
                        pos3 = pos2 + 1
                        for t3 in num_pool[pos3:-3]:
                            pos4 = pos3 + 1
                            for t4 in num_pool[pos4:-2]:
                                pos5 = pos4 + 1
                                for t5 in num_pool[pos5:-1]:
                                    pos6 = pos5 + 1
                                    for t6 in num_pool[pos6:]:
                                        data_f.append([t1,t2,t3,t4,t5,t6])                                                                             
                                    pos5 = pos5 + 1
                                pos4 = pos4 + 1
                            pos3 = pos3 + 1
                        pos2 = pos2 + 1
                    pos1 = pos1 + 1
                if wx.Platform == '__WXMSW__':
                    dlg.Update(1)  
                #显示原始注数
                #print len(data_f)
                #--开始过滤
                step = 0
                for i in range(0, len(filter_array)):
                    #+1
                    step = step + 1
                    #改为“是”
                    #filter_array[step-1][2] = '是' + filter_array[step-1][2][2:] #gbk10830??
                    filter_array[step-1][2] = u'是      ' #utf-8
                    #过滤
                    data_f, data_f_down = dataFiltrate(data_array, data_f, step, filter_array, redOrder, bet_array)
                    #更新进度条
                    if wx.Platform == '__WXMSW__':
                        dlg.Update(step+1)
                    #显示过滤后的注数
                    #print len(data_f)
                    #控制台输出正在进行的步骤
                    if step==1:
                        print '%.2d time=%d num=%d'%(step,int(time.time())-start_time,len(data_f))
                        last_time = int(time.time())
                    else:
                        print '%.2d time=%d num=%d'%(step,int(time.time())-last_time,len(data_f))
                        last_time = int(time.time())                    
                #--进度条关闭
                if wx.Platform == '__WXMSW__':
                    dlg.Destroy()
                #终止时间
                stop_time = int(time.time())
                #写数据
                writePredictData(data_array, data_f, filter_array, num_pool)              
                #提示生成的注数，询问是否打开对应文件夹
                if wx.Platform == '__WXMSW__': #win
                    tip_text = u'共生成%d注，花费%d秒'%(len(data_f),stop_time-start_time)
                    dlg_f = wx.MessageDialog(self, tip_text, 
                                            u'打开对应文件夹？',
                                            wx.YES_NO | wx.YES_DEFAULT | wx.ICON_INFORMATION
                                            )
                    dlg_f.Destroy()
                    open_folder = dlg_f.ShowModal()
                    if open_folder==wx.ID_YES:
                        #打开相应文件夹
                        os.startfile('%s'%(int(data_array[0][0])+1))
                    else:
                        pass
                else: #linux #不知道为什么linux下为什么会出错
                    print (u'共生成%d注，花费%d秒'%(len(data_f),stop_time-start_time)).encode(locale.getdefaultlocale()[1])
                    
        else:
            #弹出提示框
            dlg = wx.MessageDialog(self, u'选中的号码少于6个！', 
                                   u'请重新选择号码',
                                   wx.OK | wx.ICON_INFORMATION
                                   )
            dlg.ShowModal()
            dlg.Destroy()            
 
        event.Skip()

#-------------------------------------------------------------------------------
#----退出按钮----       
    def OnButtonexitButton(self, event): #退出按钮
        '''退出红球过滤选号面板'''
        #关闭窗口
        self.Close()

        event.Skip()

#-------------------------------------------------------------------------------
#----选号面板----
    def OnRadioButtonallyesRadiobutton(self, event): #全选按钮
        '''选择全部的号码，并注满号码池'''
        #值均设为True，即选中状态 #这部分代码应该有优化的空间，Ctrl键都磨没了
        self.checkBox01.SetValue(True)
        self.checkBox02.SetValue(True)
        self.checkBox03.SetValue(True)
        self.checkBox04.SetValue(True)
        self.checkBox05.SetValue(True)
        self.checkBox06.SetValue(True)
        self.checkBox07.SetValue(True)
        self.checkBox08.SetValue(True)
        self.checkBox09.SetValue(True)
        self.checkBox10.SetValue(True)
        self.checkBox11.SetValue(True)
        self.checkBox12.SetValue(True)
        self.checkBox13.SetValue(True)
        self.checkBox14.SetValue(True)
        self.checkBox15.SetValue(True)
        self.checkBox16.SetValue(True)
        self.checkBox17.SetValue(True)
        self.checkBox18.SetValue(True)
        self.checkBox19.SetValue(True)
        self.checkBox20.SetValue(True)
        self.checkBox21.SetValue(True)
        self.checkBox22.SetValue(True)
        self.checkBox23.SetValue(True)
        self.checkBox24.SetValue(True)
        self.checkBox25.SetValue(True)
        self.checkBox26.SetValue(True)
        self.checkBox27.SetValue(True)
        self.checkBox28.SetValue(True)
        self.checkBox29.SetValue(True)
        self.checkBox30.SetValue(True)
        self.checkBox31.SetValue(True)
        self.checkBox32.SetValue(True)
        self.checkBox33.SetValue(True)
        #注满号码池
        global num_pool
        num_pool = [] #先清空一下，避免号码池中已经有了一些号码
        for i in range(1, 33+1):
            num_pool.append(i)
        #显示选择了多少个球
        msg[1] = '%.2d'%(len(num_pool))
        self.Refresh()
        
        event.Skip()

    def OnRadioButtonallnoRadiobutton(self, event): #全不选按钮
        '''不选择号码并清空号码池'''
        #值均设为False，即反选状态 
        self.checkBox01.SetValue(False)
        self.checkBox02.SetValue(False)
        self.checkBox03.SetValue(False)
        self.checkBox04.SetValue(False)
        self.checkBox05.SetValue(False)
        self.checkBox06.SetValue(False)
        self.checkBox07.SetValue(False)
        self.checkBox08.SetValue(False)
        self.checkBox09.SetValue(False)
        self.checkBox10.SetValue(False)
        self.checkBox11.SetValue(False)        
        self.checkBox12.SetValue(False)
        self.checkBox13.SetValue(False)
        self.checkBox14.SetValue(False)
        self.checkBox15.SetValue(False)
        self.checkBox16.SetValue(False)
        self.checkBox17.SetValue(False)
        self.checkBox18.SetValue(False)
        self.checkBox19.SetValue(False)
        self.checkBox20.SetValue(False)
        self.checkBox21.SetValue(False)
        self.checkBox22.SetValue(False)
        self.checkBox23.SetValue(False)
        self.checkBox24.SetValue(False)
        self.checkBox25.SetValue(False)
        self.checkBox26.SetValue(False)
        self.checkBox27.SetValue(False)
        self.checkBox28.SetValue(False)
        self.checkBox29.SetValue(False)
        self.checkBox30.SetValue(False)
        self.checkBox31.SetValue(False)
        self.checkBox32.SetValue(False)
        self.checkBox33.SetValue(False)
        #清空号码池  
        global num_pool
        num_pool = []
        #显示选择了多少个球
        msg[1] = '%.2d'%(len(num_pool))
        self.Refresh()
        
        event.Skip()

    def OnCheckBox01Checkbox(self, event): #01
        '''将1添加到号码池中，或从号码池中删除'''
        global num_pool
        if 1 in num_pool: #看看在不在
            num_pool.remove(1) #删除     
        else:
            num_pool.append(1) #添加

        #号码池个数显示更新
        msg[1] = '%.2d'%(len(num_pool))
        self.Refresh()
        
        event.Skip()
        
    def OnCheckBox02Checkbox(self, event): #02
        '''将2添加到号码池中，或从号码池中删除'''
        global num_pool
        if 2 in num_pool:
            num_pool.remove(2)      
        else:
            num_pool.append(2)

        #号码池个数显示更新
        msg[1] = '%.2d'%(len(num_pool))
        self.Refresh()
        
        event.Skip()
        
    def OnCheckBox03Checkbox(self, event):#03
        '''将3添加到号码池中，或从号码池中删除'''
        global num_pool
        if 3 in num_pool:
            num_pool.remove(3)      
        else:
            num_pool.append(3)

        #号码池个数显示更新
        msg[1] = '%.2d'%(len(num_pool))
        self.Refresh()
        
        event.Skip()

    def OnCheckBox04Checkbox(self, event):#04
        '''将4添加到号码池中，或从号码池中删除'''
        global num_pool
        if 4 in num_pool:
            num_pool.remove(4)      
        else:
            num_pool.append(4)

        #号码池个数显示更新
        msg[1] = '%.2d'%(len(num_pool))
        self.Refresh()
        
        event.Skip()

    def OnCheckBox05Checkbox(self, event):#05
        '''将5添加到号码池中，或从号码池中删除'''
        global num_pool
        if 5 in num_pool:
            num_pool.remove(5)      
        else:
            num_pool.append(5)

        #号码池个数显示更新
        msg[1] = '%.2d'%(len(num_pool))
        self.Refresh()
         
        event.Skip()

    def OnCheckBox06Checkbox(self, event):#06
        '''将6添加到号码池中，或从号码池中删除'''
        global num_pool
        if 6 in num_pool:
            num_pool.remove(6)      
        else:
            num_pool.append(6)

        #号码池个数显示更新
        msg[1] = '%.2d'%(len(num_pool))
        self.Refresh()
        
        event.Skip()
        
    def OnCheckBox07Checkbox(self, event):#07
        '''将7添加到号码池中，或从号码池中删除'''
        global num_pool
        if 7 in num_pool:
            num_pool.remove(7)      
        else:
            num_pool.append(7)

        #号码池个数显示更新
        msg[1] = '%.2d'%(len(num_pool))
        self.Refresh()
         
        event.Skip()
        
    def OnCheckBox08Checkbox(self, event):#08
        '''将8添加到号码池中，或从号码池中删除'''
        global num_pool
        if 8 in num_pool:
            num_pool.remove(8)      
        else:
            num_pool.append(8)

        #号码池个数显示更新
        msg[1] = '%.2d'%(len(num_pool))
        self.Refresh()
        
        event.Skip()
        
    def OnCheckBox09Checkbox(self, event):#09
        '''将9添加到号码池中，或从号码池中删除'''
        global num_pool
        if 9 in num_pool:
            num_pool.remove(9)      
        else:
            num_pool.append(9)

        #号码池个数显示更新
        msg[1] = '%.2d'%(len(num_pool))
        self.Refresh()
         
        event.Skip()

    def OnCheckBox10Checkbox(self, event):#10
        '''将10添加到号码池中，或从号码池中删除'''
        global num_pool
        if 10 in num_pool:
            num_pool.remove(10)      
        else:
            num_pool.append(10)

        #号码池个数显示更新
        msg[1] = '%.2d'%(len(num_pool))
        self.Refresh()
        
        event.Skip()

    def OnCheckBox11Checkbox(self, event):#11
        '''将11添加到号码池中，或从号码池中删除'''
        global num_pool
        if 11 in num_pool:
            num_pool.remove(11)      
        else:
            num_pool.append(11)

        #号码池个数显示更新
        msg[1] = '%.2d'%(len(num_pool))
        self.Refresh()
        
        event.Skip()

    def OnCheckBox12Checkbox(self, event):#12
        '''将12添加到号码池中，或从号码池中删除'''
        global num_pool
        if 12 in num_pool:
            num_pool.remove(12)      
        else:
            num_pool.append(12)

        #号码池个数显示更新
        msg[1] = '%.2d'%(len(num_pool))
        self.Refresh()
        
        event.Skip()

    def OnCheckBox13Checkbox(self, event):#13
        '''将13添加到号码池中，或从号码池中删除'''
        global num_pool
        if 13 in num_pool:
            num_pool.remove(13)      
        else:
            num_pool.append(13)

        #号码池个数显示更新
        msg[1] = '%.2d'%(len(num_pool))
        self.Refresh()
        
        event.Skip()

    def OnCheckBox14Checkbox(self, event):#14
        '''将14添加到号码池中，或从号码池中删除'''
        global num_pool
        if 14 in num_pool:
            num_pool.remove(14)      
        else:
            num_pool.append(14)

        #号码池个数显示更新
        msg[1] = '%.2d'%(len(num_pool))
        self.Refresh()
        
        event.Skip()

    def OnCheckBox15Checkbox(self, event):#15
        '''将15添加到号码池中，或从号码池中删除'''
        global num_pool
        if 15 in num_pool:
            num_pool.remove(15)      
        else:
            num_pool.append(15)

        #号码池个数显示更新
        msg[1] = '%.2d'%(len(num_pool))
        self.Refresh()
        
        event.Skip()

    def OnCheckBox16Checkbox(self, event):#16
        '''将16添加到号码池中，或从号码池中删除'''
        global num_pool
        if 16 in num_pool:
            num_pool.remove(16)      
        else:
            num_pool.append(16)

        #号码池个数显示更新
        msg[1] = '%.2d'%(len(num_pool))
        self.Refresh()
        
        event.Skip()
        
    def OnCheckBox17Checkbox(self, event):#17
        '''将17添加到号码池中，或从号码池中删除'''
        global num_pool
        if 17 in num_pool:
            num_pool.remove(17)      
        else:
            num_pool.append(17)

        #号码池个数显示更新
        msg[1] = '%.2d'%(len(num_pool))
        self.Refresh()
        
        event.Skip()

    def OnCheckBox18Checkbox(self, event):#18
        '''将18添加到号码池中，或从号码池中删除'''
        global num_pool
        if 18 in num_pool:
            num_pool.remove(18)      
        else:
            num_pool.append(18)

        #号码池个数显示更新
        msg[1] = '%.2d'%(len(num_pool))
        self.Refresh()
        
        event.Skip()

    def OnCheckBox19Checkbox(self, event):#19
        '''将19添加到号码池中，或从号码池中删除'''
        global num_pool
        if 19 in num_pool:
            num_pool.remove(19)      
        else:
            num_pool.append(19)

        #号码池个数显示更新
        msg[1] = '%.2d'%(len(num_pool))
        self.Refresh()
        
        event.Skip()

    def OnCheckBox20Checkbox(self, event):#20
        '''将20添加到号码池中，或从号码池中删除'''
        global num_pool
        if 20 in num_pool:
            num_pool.remove(20)      
        else:
            num_pool.append(20)

        #号码池个数显示更新
        msg[1] = '%.2d'%(len(num_pool))
        self.Refresh()
        
        event.Skip()

    def OnCheckBox21Checkbox(self, event):#21
        '''将21添加到号码池中，或从号码池中删除'''
        global num_pool
        if 21 in num_pool:
            num_pool.remove(21)      
        else:
            num_pool.append(21)

        #号码池个数显示更新
        msg[1] = '%.2d'%(len(num_pool))
        self.Refresh()
        
        event.Skip()

    def OnCheckBox22Checkbox(self, event):#22
        '''将22添加到号码池中，或从号码池中删除'''
        global num_pool
        if 22 in num_pool:
            num_pool.remove(22)      
        else:
            num_pool.append(22)

        #号码池个数显示更新
        msg[1] = '%.2d'%(len(num_pool))
        self.Refresh()
        
        event.Skip()

    def OnCheckBox23Checkbox(self, event):#23
        '''将23添加到号码池中，或从号码池中删除'''
        global num_pool
        if 23 in num_pool:
            num_pool.remove(23)      
        else:
            num_pool.append(23)

        #号码池个数显示更新
        msg[1] = '%.2d'%(len(num_pool))
        self.Refresh()
        
        event.Skip()

    def OnCheckBox24Checkbox(self, event):#24
        '''将24添加到号码池中，或从号码池中删除'''
        global num_pool
        if 24 in num_pool:
            num_pool.remove(24)      
        else:
            num_pool.append(24)

        #号码池个数显示更新
        msg[1] = '%.2d'%(len(num_pool))
        self.Refresh()
        
        event.Skip()

    def OnCheckBox25Checkbox(self, event):#25
        '''将25添加到号码池中，或从号码池中删除'''
        global num_pool
        if 25 in num_pool:
            num_pool.remove(25)      
        else:
            num_pool.append(25)

        #号码池个数显示更新
        msg[1] = '%.2d'%(len(num_pool))
        self.Refresh()
        
        event.Skip()

    def OnCheckBox26Checkbox(self, event):#26
        '''将26添加到号码池中，或从号码池中删除'''
        global num_pool
        if 26 in num_pool:
            num_pool.remove(26)      
        else:
            num_pool.append(26)

        #号码池个数显示更新
        msg[1] = '%.2d'%(len(num_pool))
        self.Refresh()
        
        event.Skip()

    def OnCheckBox27Checkbox(self, event):#27
        '''将27添加到号码池中，或从号码池中删除'''
        global num_pool
        if 27 in num_pool:
            num_pool.remove(27)      
        else:
            num_pool.append(27)

        #号码池个数显示更新
        msg[1] = '%.2d'%(len(num_pool))
        self.Refresh()
        
        event.Skip()

    def OnCheckBox28Checkbox(self, event):#28
        '''将28添加到号码池中，或从号码池中删除'''
        global num_pool
        if 28 in num_pool:
            num_pool.remove(28)      
        else:
            num_pool.append(28)

        #号码池个数显示更新
        msg[1] = '%.2d'%(len(num_pool))
        self.Refresh()
        
        event.Skip()

    def OnCheckBox29Checkbox(self, event):#29
        '''将29添加到号码池中，或从号码池中删除'''
        global num_pool
        if 29 in num_pool:
            num_pool.remove(29)      
        else:
            num_pool.append(29)

        #号码池个数显示更新
        msg[1] = '%.2d'%(len(num_pool))
        self.Refresh()
        
        event.Skip()

    def OnCheckBox30Checkbox(self, event):#30
        '''将30添加到号码池中，或从号码池中删除'''
        global num_pool
        if 30 in num_pool:
            num_pool.remove(30)      
        else:
            num_pool.append(30)

        #号码池个数显示更新
        msg[1] = '%.2d'%(len(num_pool))
        self.Refresh()
        
        event.Skip()

    def OnCheckBox31Checkbox(self, event):#31
        '''将31添加到号码池中，或从号码池中删除'''
        global num_pool
        if 31 in num_pool:
            num_pool.remove(31)      
        else:
            num_pool.append(31)

        #号码池个数显示更新
        msg[1] = '%.2d'%(len(num_pool))
        self.Refresh()
        
        event.Skip()

    def OnCheckBox32Checkbox(self, event):#32
        '''将32添加到号码池中，或从号码池中删除'''
        global num_pool
        if 32 in num_pool:
            num_pool.remove(32)      
        else:
            num_pool.append(32)

        #号码池个数显示更新
        msg[1] = '%.2d'%(len(num_pool))
        self.Refresh()
        
        event.Skip()
    def OnCheckBox33Checkbox(self, event):#33
        '''将33添加到号码池中，或从号码池中删除'''
        global num_pool
        if 33 in num_pool:
            num_pool.remove(33)      
        else:
            num_pool.append(33)

        #号码池个数显示更新
        msg[1] = '%.2d'%(len(num_pool))
        self.Refresh()
        
        event.Skip()
       
#-------------------------------------------------------------------------------
#----绘图----

    def OnPanel1Paint(self, event):
        dc = wx.PaintDC(self.panel1)
        #self.panel1.DoPrepareDC(dc)
        #画面清空       
        dc.Clear()
        #文字设定
        global msg
        msg = ['','','']
        msg[0] = '开始红球过滤，选择号码后点击“生成初始数据”按钮'
        msg[1] = '%.2d'%(len(num_pool)) #显示号码池中的号码个数
        msg[2] = '小提示：蓝色的号码为上期出现的号码，右上角紫色号码表示已选号码个数'
        #文字格式
        dc.SetFont(wx.Font(10, wx.NORMAL, wx.NORMAL, wx.NORMAL))
        #文字颜色
        dc.SetTextForeground('BLUE')
        #文字位置
        dc.DrawText(msg[0].decode('utf-8'), 5, 5)
        #文字颜色
        dc.SetTextForeground('MEDIUM ORCHID')        
        dc.DrawText(msg[1], 450, 5)
        #小提示
        dc.SetFont(wx.Font(8, wx.NORMAL, wx.NORMAL, wx.NORMAL))
        dc.SetTextForeground('BROWN')
        dc.DrawText(msg[2].decode('utf-8'), 30, 400)
