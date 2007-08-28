#Boa:Frame:FrameRedFiltrate
# -*- coding: cp936 -*-
# otherrrr@gmail.com
# ����������

import wx
import os
import time

from DataFileIO import readDataFileToArray
from FilterFileIO import readFilterFileToArray
from PredictFileIO import writePredictData
from BetFileIO import readBetFileToArray
from DataCompute import redOrderCoumpute, dataParaCompute, percentCompute, dataFiltrate

data_array = []  #���ݣ������ʽ��
data_para_array = [] #���ݵ���ز���

redOrder = [] #������밴�ų�������ɴ�С����
redTimes = [] #�����Ӧ���Ŵ���
redOrder100 = [] 
redTimes100 = []
redOrder50 = [] 
redTimes50 = [] 

num_pool = [] #�����

filter_array = [] #���˲���
percent_array = [] #���������İٷֱ�
data_f = [] #���˺����ɵ�����
step = 0 #���˲���
msg = [] #��ʾ��Ϣ #�����ʵ���Ըĳ�dict

term = 20 #������������ͼ��ʾ��������Ĭ����ʾ���20������

def create(parent):
    return FrameRedFiltrate(parent)

[wxID_FRAMEREDFILTRATE, wxID_FRAMEREDFILTRATEBUTTONDATABUILD, 
 wxID_FRAMEREDFILTRATEBUTTONEXIT, wxID_FRAMEREDFILTRATEBUTTONLASTSTEP, 
 wxID_FRAMEREDFILTRATEBUTTONLOWERMINUS, wxID_FRAMEREDFILTRATEBUTTONLOWERPLUS, 
 wxID_FRAMEREDFILTRATEBUTTONNEXTSTEP, wxID_FRAMEREDFILTRATEBUTTONONESTEP, 
 wxID_FRAMEREDFILTRATEBUTTONSAVE, wxID_FRAMEREDFILTRATEBUTTONUPPERMINUS, 
 wxID_FRAMEREDFILTRATEBUTTONUPPERPLUS, wxID_FRAMEREDFILTRATEBUTTONUSE, 
 wxID_FRAMEREDFILTRATECHECKBOX01, wxID_FRAMEREDFILTRATECHECKBOX02, 
 wxID_FRAMEREDFILTRATECHECKBOX03, wxID_FRAMEREDFILTRATECHECKBOX04, 
 wxID_FRAMEREDFILTRATECHECKBOX05, wxID_FRAMEREDFILTRATECHECKBOX06, 
 wxID_FRAMEREDFILTRATECHECKBOX07, wxID_FRAMEREDFILTRATECHECKBOX08, 
 wxID_FRAMEREDFILTRATECHECKBOX09, wxID_FRAMEREDFILTRATECHECKBOX10, 
 wxID_FRAMEREDFILTRATECHECKBOX11, wxID_FRAMEREDFILTRATECHECKBOX12, 
 wxID_FRAMEREDFILTRATECHECKBOX13, wxID_FRAMEREDFILTRATECHECKBOX14, 
 wxID_FRAMEREDFILTRATECHECKBOX15, wxID_FRAMEREDFILTRATECHECKBOX16, 
 wxID_FRAMEREDFILTRATECHECKBOX17, wxID_FRAMEREDFILTRATECHECKBOX18, 
 wxID_FRAMEREDFILTRATECHECKBOX19, wxID_FRAMEREDFILTRATECHECKBOX20, 
 wxID_FRAMEREDFILTRATECHECKBOX21, wxID_FRAMEREDFILTRATECHECKBOX22, 
 wxID_FRAMEREDFILTRATECHECKBOX23, wxID_FRAMEREDFILTRATECHECKBOX24, 
 wxID_FRAMEREDFILTRATECHECKBOX25, wxID_FRAMEREDFILTRATECHECKBOX26, 
 wxID_FRAMEREDFILTRATECHECKBOX27, wxID_FRAMEREDFILTRATECHECKBOX28, 
 wxID_FRAMEREDFILTRATECHECKBOX29, wxID_FRAMEREDFILTRATECHECKBOX30, 
 wxID_FRAMEREDFILTRATECHECKBOX31, wxID_FRAMEREDFILTRATECHECKBOX32, 
 wxID_FRAMEREDFILTRATECHECKBOX33, wxID_FRAMEREDFILTRATEPANEL1, 
 wxID_FRAMEREDFILTRATEPANEL2, wxID_FRAMEREDFILTRATEPANEL3, 
 wxID_FRAMEREDFILTRATERADIOBUTTON10T, wxID_FRAMEREDFILTRATERADIOBUTTON20T, 
 wxID_FRAMEREDFILTRATERADIOBUTTON40T, wxID_FRAMEREDFILTRATERADIOBUTTONALLNO, 
 wxID_FRAMEREDFILTRATERADIOBUTTONALLYES, wxID_FRAMEREDFILTRATETEXTCTRLDATAF, 
] = [wx.NewId() for _init_ctrls in range(54)]

class FrameRedFiltrate(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAMEREDFILTRATE,
              name=u'FrameAbnormalFiltrate', parent=prnt, pos=wx.Point(388,
              232), size=wx.Size(491, 482), style=wx.DEFAULT_FRAME_STYLE,
              title=u'\u7ea2\u7403\u8fc7\u6ee4')
        self.SetIcon(wx.Icon(u'pic/red.ico',wx.BITMAP_TYPE_ICO))
        self.SetClientSize(wx.Size(483, 455))

        self.panel1 = wx.Panel(id=wxID_FRAMEREDFILTRATEPANEL1, name='panel1',
              parent=self, pos=wx.Point(0, 0), size=wx.Size(483, 455),
              style=wx.TAB_TRAVERSAL)
        self.panel1.Bind(wx.EVT_PAINT, self.OnPanel1Paint)

        self.buttonexit = wx.Button(id=wxID_FRAMEREDFILTRATEBUTTONEXIT,
              label=u'\u9000\u51fa', name=u'buttonexit', parent=self.panel1,
              pos=wx.Point(20, 420), size=wx.Size(60, 24), style=0)
        self.buttonexit.Bind(wx.EVT_BUTTON, self.OnButtonexitButton,
              id=wxID_FRAMEREDFILTRATEBUTTONEXIT)

        self.buttondatabuild = wx.Button(id=wxID_FRAMEREDFILTRATEBUTTONDATABUILD,
              label=u'\u751f\u6210\u521d\u59cb\u6570\u636e',
              name=u'buttondatabuild', parent=self.panel1, pos=wx.Point(96, 32),
              size=wx.Size(90, 24), style=0)
        self.buttondatabuild.SetForegroundColour(wx.Colour(255, 0, 0))
        self.buttondatabuild.Bind(wx.EVT_BUTTON, self.OnButtondatabuildButton,
              id=wxID_FRAMEREDFILTRATEBUTTONDATABUILD)

        self.buttonnextstep = wx.Button(id=wxID_FRAMEREDFILTRATEBUTTONNEXTSTEP,
              label=u'\u4e0b\u4e00\u6b65', name=u'buttonnextstep',
              parent=self.panel1, pos=wx.Point(380, 420), size=wx.Size(75, 23),
              style=0)
        self.buttonnextstep.Bind(wx.EVT_BUTTON, self.OnButtonnextstepButton,
              id=wxID_FRAMEREDFILTRATEBUTTONNEXTSTEP)

        self.buttonlaststep = wx.Button(id=wxID_FRAMEREDFILTRATEBUTTONLASTSTEP,
              label=u'\u4e0a\u4e00\u6b65', name=u'buttonlaststep',
              parent=self.panel1, pos=wx.Point(280, 420), size=wx.Size(75, 24),
              style=0)
        self.buttonlaststep.Bind(wx.EVT_BUTTON, self.OnButtonlaststepButton,
              id=wxID_FRAMEREDFILTRATEBUTTONLASTSTEP)

        self.buttonuse = wx.Button(id=wxID_FRAMEREDFILTRATEBUTTONUSE,
              label=u'\u4f7f\u7528\u6b64\u6761\u4ef6', name=u'buttonuse',
              parent=self.panel1, pos=wx.Point(312, 80), size=wx.Size(90, 24),
              style=0)
        self.buttonuse.SetForegroundColour(wx.Colour(255, 0, 0))
        self.buttonuse.Bind(wx.EVT_BUTTON, self.OnButtonuseButton,
              id=wxID_FRAMEREDFILTRATEBUTTONUSE)

        self.buttonsave = wx.Button(id=wxID_FRAMEREDFILTRATEBUTTONSAVE,
              label=u'\u4fdd\u5b58\u8fc7\u6ee4\u540e\u6570\u636e',
              name=u'buttonsave', parent=self.panel1, pos=wx.Point(280, 32),
              size=wx.Size(104, 24), style=0)
        self.buttonsave.SetForegroundColour(wx.Colour(255, 0, 0))
        self.buttonsave.Bind(wx.EVT_BUTTON, self.OnButtonsaveButton,
              id=wxID_FRAMEREDFILTRATEBUTTONSAVE)

        self.buttonlowerminus = wx.Button(id=wxID_FRAMEREDFILTRATEBUTTONLOWERMINUS,
              label=u'\u4e0b\u9650\uff0d', name=u'buttonlowerminus',
              parent=self.panel1, pos=wx.Point(256, 50), size=wx.Size(48, 24),
              style=0)
        self.buttonlowerminus.Bind(wx.EVT_BUTTON, self.OnButtonlowerminusButton,
              id=wxID_FRAMEREDFILTRATEBUTTONLOWERMINUS)

        self.buttonlowerplus = wx.Button(id=wxID_FRAMEREDFILTRATEBUTTONLOWERPLUS,
              label=u'\u4e0b\u9650\uff0b', name=u'buttonlowerplus',
              parent=self.panel1, pos=wx.Point(312, 50), size=wx.Size(48, 24),
              style=0)
        self.buttonlowerplus.Bind(wx.EVT_BUTTON, self.OnButtonlowerplusButton,
              id=wxID_FRAMEREDFILTRATEBUTTONLOWERPLUS)

        self.buttonupperplus = wx.Button(id=wxID_FRAMEREDFILTRATEBUTTONUPPERPLUS,
              label=u'\u4e0a\u9650\uff0b', name=u'buttonupperplus',
              parent=self.panel1, pos=wx.Point(424, 50), size=wx.Size(48, 24),
              style=0)
        self.buttonupperplus.Bind(wx.EVT_BUTTON, self.OnButtonupperplusButton,
              id=wxID_FRAMEREDFILTRATEBUTTONUPPERPLUS)

        self.buttonupperminus = wx.Button(id=wxID_FRAMEREDFILTRATEBUTTONUPPERMINUS,
              label=u'\u4e0a\u9650\uff0d', name=u'buttonupperminus',
              parent=self.panel1, pos=wx.Point(368, 50), size=wx.Size(48, 24),
              style=0)
        self.buttonupperminus.Bind(wx.EVT_BUTTON, self.OnButtonupperminusButton,
              id=wxID_FRAMEREDFILTRATEBUTTONUPPERMINUS)

        self.panel2 = wx.Panel(id=wxID_FRAMEREDFILTRATEPANEL2, name='panel2',
              parent=self.panel1, pos=wx.Point(20, 100), size=wx.Size(440, 240),
              style=wx.STATIC_BORDER | wx.TAB_TRAVERSAL)
        self.panel2.SetBackgroundColour(wx.Colour(226, 219, 207))

        self.radioButtonallyes = wx.RadioButton(id=wxID_FRAMEREDFILTRATERADIOBUTTONALLYES,
              label=u'\u5168\u9009', name=u'radioButtonallyes',
              parent=self.panel2, pos=wx.Point(130, 30), size=wx.Size(48, 14),
              style=0)
        self.radioButtonallyes.SetValue(False)
        self.radioButtonallyes.Bind(wx.EVT_RADIOBUTTON,
              self.OnRadioButtonallyesRadiobutton,
              id=wxID_FRAMEREDFILTRATERADIOBUTTONALLYES)

        self.radioButtonallno = wx.RadioButton(id=wxID_FRAMEREDFILTRATERADIOBUTTONALLNO,
              label=u'\u5168\u4e0d\u9009', name=u'radioButtonallno',
              parent=self.panel2, pos=wx.Point(270, 30), size=wx.Size(56, 14),
              style=0)
        self.radioButtonallno.SetValue(True)
        self.radioButtonallno.Bind(wx.EVT_RADIOBUTTON,
              self.OnRadioButtonallnoRadiobutton,
              id=wxID_FRAMEREDFILTRATERADIOBUTTONALLNO)

        self.checkBox01 = wx.CheckBox(id=wxID_FRAMEREDFILTRATECHECKBOX01,
              label=u'01', name=u'checkBox01', parent=self.panel2,
              pos=wx.Point(80, 60), size=wx.Size(40, 14), style=0)
        self.checkBox01.SetValue(False)
        self.checkBox01.Bind(wx.EVT_CHECKBOX, self.OnCheckBox01Checkbox,
              id=wxID_FRAMEREDFILTRATECHECKBOX01)

        self.checkBox02 = wx.CheckBox(id=wxID_FRAMEREDFILTRATECHECKBOX02,
              label=u'02', name=u'checkBox02', parent=self.panel2,
              pos=wx.Point(140, 60), size=wx.Size(40, 14), style=0)
        self.checkBox02.SetValue(False)
        self.checkBox02.Bind(wx.EVT_CHECKBOX, self.OnCheckBox02Checkbox,
              id=wxID_FRAMEREDFILTRATECHECKBOX02)

        self.checkBox03 = wx.CheckBox(id=wxID_FRAMEREDFILTRATECHECKBOX03,
              label=u'03', name=u'checkBox03', parent=self.panel2,
              pos=wx.Point(200, 60), size=wx.Size(40, 14), style=0)
        self.checkBox03.SetValue(False)
        self.checkBox03.Bind(wx.EVT_CHECKBOX, self.OnCheckBox03Checkbox,
              id=wxID_FRAMEREDFILTRATECHECKBOX03)

        self.checkBox04 = wx.CheckBox(id=wxID_FRAMEREDFILTRATECHECKBOX04,
              label=u'04', name=u'checkBox04', parent=self.panel2,
              pos=wx.Point(260, 60), size=wx.Size(40, 14), style=0)
        self.checkBox04.SetValue(False)
        self.checkBox04.Bind(wx.EVT_CHECKBOX, self.OnCheckBox04Checkbox,
              id=wxID_FRAMEREDFILTRATECHECKBOX04)

        self.checkBox05 = wx.CheckBox(id=wxID_FRAMEREDFILTRATECHECKBOX05,
              label=u'05', name=u'checkBox05', parent=self.panel2,
              pos=wx.Point(320, 60), size=wx.Size(40, 14), style=0)
        self.checkBox05.SetValue(False)
        self.checkBox05.Bind(wx.EVT_CHECKBOX, self.OnCheckBox05Checkbox,
              id=wxID_FRAMEREDFILTRATECHECKBOX05)

        self.checkBox06 = wx.CheckBox(id=wxID_FRAMEREDFILTRATECHECKBOX06,
              label=u'06', name=u'checkBox06', parent=self.panel2,
              pos=wx.Point(50, 90), size=wx.Size(40, 14), style=0)
        self.checkBox06.SetValue(False)
        self.checkBox06.Bind(wx.EVT_CHECKBOX, self.OnCheckBox06Checkbox,
              id=wxID_FRAMEREDFILTRATECHECKBOX06)

        self.checkBox07 = wx.CheckBox(id=wxID_FRAMEREDFILTRATECHECKBOX07,
              label=u'07', name=u'checkBox07', parent=self.panel2,
              pos=wx.Point(110, 90), size=wx.Size(40, 14), style=0)
        self.checkBox07.SetValue(False)
        self.checkBox07.Bind(wx.EVT_CHECKBOX, self.OnCheckBox07Checkbox,
              id=wxID_FRAMEREDFILTRATECHECKBOX07)

        self.checkBox08 = wx.CheckBox(id=wxID_FRAMEREDFILTRATECHECKBOX08,
              label=u'08', name=u'checkBox08', parent=self.panel2,
              pos=wx.Point(170, 90), size=wx.Size(40, 14), style=0)
        self.checkBox08.SetValue(False)
        self.checkBox08.Bind(wx.EVT_CHECKBOX, self.OnCheckBox08Checkbox,
              id=wxID_FRAMEREDFILTRATECHECKBOX08)

        self.checkBox09 = wx.CheckBox(id=wxID_FRAMEREDFILTRATECHECKBOX09,
              label=u'09', name=u'checkBox09', parent=self.panel2,
              pos=wx.Point(230, 90), size=wx.Size(40, 14), style=0)
        self.checkBox09.SetValue(False)
        self.checkBox09.Bind(wx.EVT_CHECKBOX, self.OnCheckBox09Checkbox,
              id=wxID_FRAMEREDFILTRATECHECKBOX09)

        self.checkBox10 = wx.CheckBox(id=wxID_FRAMEREDFILTRATECHECKBOX10,
              label=u'10', name=u'checkBox10', parent=self.panel2,
              pos=wx.Point(290, 90), size=wx.Size(40, 14), style=0)
        self.checkBox10.SetValue(False)
        self.checkBox10.Bind(wx.EVT_CHECKBOX, self.OnCheckBox10Checkbox,
              id=wxID_FRAMEREDFILTRATECHECKBOX10)

        self.checkBox11 = wx.CheckBox(id=wxID_FRAMEREDFILTRATECHECKBOX11,
              label=u'11', name=u'checkBox11', parent=self.panel2,
              pos=wx.Point(350, 90), size=wx.Size(40, 14), style=0)
        self.checkBox11.SetValue(False)
        self.checkBox11.Bind(wx.EVT_CHECKBOX, self.OnCheckBox11Checkbox,
              id=wxID_FRAMEREDFILTRATECHECKBOX11)

        self.checkBox12 = wx.CheckBox(id=wxID_FRAMEREDFILTRATECHECKBOX12,
              label=u'12', name=u'checkBox12', parent=self.panel2,
              pos=wx.Point(80, 120), size=wx.Size(40, 14), style=0)
        self.checkBox12.SetValue(False)
        self.checkBox12.Bind(wx.EVT_CHECKBOX, self.OnCheckBox12Checkbox,
              id=wxID_FRAMEREDFILTRATECHECKBOX12)

        self.checkBox13 = wx.CheckBox(id=wxID_FRAMEREDFILTRATECHECKBOX13,
              label=u'13', name=u'checkBox13', parent=self.panel2,
              pos=wx.Point(140, 120), size=wx.Size(40, 14), style=0)
        self.checkBox13.SetValue(False)
        self.checkBox13.Bind(wx.EVT_CHECKBOX, self.OnCheckBox13Checkbox,
              id=wxID_FRAMEREDFILTRATECHECKBOX13)

        self.checkBox14 = wx.CheckBox(id=wxID_FRAMEREDFILTRATECHECKBOX14,
              label=u'14', name=u'checkBox14', parent=self.panel2,
              pos=wx.Point(200, 120), size=wx.Size(40, 14), style=0)
        self.checkBox14.SetValue(False)
        self.checkBox14.Bind(wx.EVT_CHECKBOX, self.OnCheckBox14Checkbox,
              id=wxID_FRAMEREDFILTRATECHECKBOX14)

        self.checkBox15 = wx.CheckBox(id=wxID_FRAMEREDFILTRATECHECKBOX15,
              label=u'15', name=u'checkBox15', parent=self.panel2,
              pos=wx.Point(260, 120), size=wx.Size(40, 14), style=0)
        self.checkBox15.SetValue(False)
        self.checkBox15.Bind(wx.EVT_CHECKBOX, self.OnCheckBox15Checkbox,
              id=wxID_FRAMEREDFILTRATECHECKBOX15)

        self.checkBox16 = wx.CheckBox(id=wxID_FRAMEREDFILTRATECHECKBOX16,
              label=u'16', name=u'checkBox16', parent=self.panel2,
              pos=wx.Point(320, 120), size=wx.Size(40, 14), style=0)
        self.checkBox16.SetValue(False)
        self.checkBox16.Bind(wx.EVT_CHECKBOX, self.OnCheckBox16Checkbox,
              id=wxID_FRAMEREDFILTRATECHECKBOX16)

        self.checkBox17 = wx.CheckBox(id=wxID_FRAMEREDFILTRATECHECKBOX17,
              label=u'17', name=u'checkBox17', parent=self.panel2,
              pos=wx.Point(50, 150), size=wx.Size(40, 14), style=0)
        self.checkBox17.SetValue(False)
        self.checkBox17.Bind(wx.EVT_CHECKBOX, self.OnCheckBox17Checkbox,
              id=wxID_FRAMEREDFILTRATECHECKBOX17)

        self.checkBox18 = wx.CheckBox(id=wxID_FRAMEREDFILTRATECHECKBOX18,
              label=u'18', name=u'checkBox18', parent=self.panel2,
              pos=wx.Point(110, 150), size=wx.Size(40, 14), style=0)
        self.checkBox18.SetValue(False)
        self.checkBox18.Bind(wx.EVT_CHECKBOX, self.OnCheckBox18Checkbox,
              id=wxID_FRAMEREDFILTRATECHECKBOX18)

        self.checkBox19 = wx.CheckBox(id=wxID_FRAMEREDFILTRATECHECKBOX19,
              label=u'19', name=u'checkBox19', parent=self.panel2,
              pos=wx.Point(170, 150), size=wx.Size(40, 14), style=0)
        self.checkBox19.SetValue(False)
        self.checkBox19.Bind(wx.EVT_CHECKBOX, self.OnCheckBox19Checkbox,
              id=wxID_FRAMEREDFILTRATECHECKBOX19)

        self.checkBox20 = wx.CheckBox(id=wxID_FRAMEREDFILTRATECHECKBOX20,
              label=u'20', name=u'checkBox20', parent=self.panel2,
              pos=wx.Point(230, 150), size=wx.Size(40, 14), style=0)
        self.checkBox20.SetValue(False)
        self.checkBox20.Bind(wx.EVT_CHECKBOX, self.OnCheckBox20Checkbox,
              id=wxID_FRAMEREDFILTRATECHECKBOX20)

        self.checkBox21 = wx.CheckBox(id=wxID_FRAMEREDFILTRATECHECKBOX21,
              label=u'21', name=u'checkBox21', parent=self.panel2,
              pos=wx.Point(290, 150), size=wx.Size(40, 14), style=0)
        self.checkBox21.SetValue(False)
        self.checkBox21.Bind(wx.EVT_CHECKBOX, self.OnCheckBox21Checkbox,
              id=wxID_FRAMEREDFILTRATECHECKBOX21)

        self.checkBox22 = wx.CheckBox(id=wxID_FRAMEREDFILTRATECHECKBOX22,
              label=u'22', name=u'checkBox22', parent=self.panel2,
              pos=wx.Point(350, 150), size=wx.Size(40, 14), style=0)
        self.checkBox22.SetValue(False)
        self.checkBox22.Bind(wx.EVT_CHECKBOX, self.OnCheckBox22Checkbox,
              id=wxID_FRAMEREDFILTRATECHECKBOX22)

        self.checkBox23 = wx.CheckBox(id=wxID_FRAMEREDFILTRATECHECKBOX23,
              label=u'23', name=u'checkBox23', parent=self.panel2,
              pos=wx.Point(80, 180), size=wx.Size(40, 14), style=0)
        self.checkBox23.SetValue(False)
        self.checkBox23.Bind(wx.EVT_CHECKBOX, self.OnCheckBox23Checkbox,
              id=wxID_FRAMEREDFILTRATECHECKBOX23)

        self.checkBox24 = wx.CheckBox(id=wxID_FRAMEREDFILTRATECHECKBOX24,
              label=u'24', name=u'checkBox24', parent=self.panel2,
              pos=wx.Point(140, 180), size=wx.Size(40, 14), style=0)
        self.checkBox24.SetValue(False)
        self.checkBox24.Bind(wx.EVT_CHECKBOX, self.OnCheckBox24Checkbox,
              id=wxID_FRAMEREDFILTRATECHECKBOX24)

        self.checkBox25 = wx.CheckBox(id=wxID_FRAMEREDFILTRATECHECKBOX25,
              label=u'25', name=u'checkBox25', parent=self.panel2,
              pos=wx.Point(200, 180), size=wx.Size(40, 14), style=0)
        self.checkBox25.SetValue(False)
        self.checkBox25.Bind(wx.EVT_CHECKBOX, self.OnCheckBox25Checkbox,
              id=wxID_FRAMEREDFILTRATECHECKBOX25)

        self.checkBox26 = wx.CheckBox(id=wxID_FRAMEREDFILTRATECHECKBOX26,
              label=u'26', name=u'checkBox26', parent=self.panel2,
              pos=wx.Point(260, 180), size=wx.Size(40, 14), style=0)
        self.checkBox26.SetValue(False)
        self.checkBox26.Bind(wx.EVT_CHECKBOX, self.OnCheckBox26Checkbox,
              id=wxID_FRAMEREDFILTRATECHECKBOX26)

        self.checkBox27 = wx.CheckBox(id=wxID_FRAMEREDFILTRATECHECKBOX27,
              label=u'27', name=u'checkBox27', parent=self.panel2,
              pos=wx.Point(320, 180), size=wx.Size(40, 14), style=0)
        self.checkBox27.SetValue(False)
        self.checkBox27.Bind(wx.EVT_CHECKBOX, self.OnCheckBox27Checkbox,
              id=wxID_FRAMEREDFILTRATECHECKBOX27)

        self.checkBox28 = wx.CheckBox(id=wxID_FRAMEREDFILTRATECHECKBOX28,
              label=u'28', name=u'checkBox28', parent=self.panel2,
              pos=wx.Point(50, 210), size=wx.Size(40, 14), style=0)
        self.checkBox28.SetValue(False)
        self.checkBox28.Bind(wx.EVT_CHECKBOX, self.OnCheckBox28Checkbox,
              id=wxID_FRAMEREDFILTRATECHECKBOX28)

        self.checkBox29 = wx.CheckBox(id=wxID_FRAMEREDFILTRATECHECKBOX29,
              label=u'29', name=u'checkBox29', parent=self.panel2,
              pos=wx.Point(110, 210), size=wx.Size(40, 14), style=0)
        self.checkBox29.SetValue(False)
        self.checkBox29.Bind(wx.EVT_CHECKBOX, self.OnCheckBox29Checkbox,
              id=wxID_FRAMEREDFILTRATECHECKBOX29)

        self.checkBox30 = wx.CheckBox(id=wxID_FRAMEREDFILTRATECHECKBOX30,
              label=u'30', name=u'checkBox30', parent=self.panel2,
              pos=wx.Point(170, 210), size=wx.Size(40, 14), style=0)
        self.checkBox30.SetValue(False)
        self.checkBox30.Bind(wx.EVT_CHECKBOX, self.OnCheckBox30Checkbox,
              id=wxID_FRAMEREDFILTRATECHECKBOX30)

        self.checkBox31 = wx.CheckBox(id=wxID_FRAMEREDFILTRATECHECKBOX31,
              label=u'31', name=u'checkBox31', parent=self.panel2,
              pos=wx.Point(230, 210), size=wx.Size(40, 14), style=0)
        self.checkBox31.SetValue(False)
        self.checkBox31.Bind(wx.EVT_CHECKBOX, self.OnCheckBox31Checkbox,
              id=wxID_FRAMEREDFILTRATECHECKBOX31)

        self.checkBox32 = wx.CheckBox(id=wxID_FRAMEREDFILTRATECHECKBOX32,
              label=u'32', name=u'checkBox32', parent=self.panel2,
              pos=wx.Point(290, 210), size=wx.Size(40, 14), style=0)
        self.checkBox32.SetValue(False)
        self.checkBox32.Bind(wx.EVT_CHECKBOX, self.OnCheckBox32Checkbox,
              id=wxID_FRAMEREDFILTRATECHECKBOX32)

        self.checkBox33 = wx.CheckBox(id=wxID_FRAMEREDFILTRATECHECKBOX33,
              label=u'33', name=u'checkBox33', parent=self.panel2,
              pos=wx.Point(350, 210), size=wx.Size(40, 14), style=0)
        self.checkBox33.SetValue(False)
        self.checkBox33.Bind(wx.EVT_CHECKBOX, self.OnCheckBox33Checkbox,
              id=wxID_FRAMEREDFILTRATECHECKBOX33)

        self.panel3 = wx.Panel(id=wxID_FRAMEREDFILTRATEPANEL3, name='panel3',
              parent=self.panel1, pos=wx.Point(16, 112), size=wx.Size(448, 296),
              style=wx.SUNKEN_BORDER | wx.TAB_TRAVERSAL)
        self.panel3.SetBackgroundColour(wx.Colour(237, 236, 233))
        self.panel3.Bind(wx.EVT_PAINT, self.OnPanel3Paint)

        self.radioButton10t = wx.RadioButton(id=wxID_FRAMEREDFILTRATERADIOBUTTON10T,
              label=u'10\u671f', name=u'radioButton10t', parent=self.panel3,
              pos=wx.Point(230, 10), size=wx.Size(54, 14), style=0)
        self.radioButton10t.SetValue(False)
        self.radioButton10t.Bind(wx.EVT_RADIOBUTTON,
              self.OnRadioButton10tRadiobutton,
              id=wxID_FRAMEREDFILTRATERADIOBUTTON10T)

        self.radioButton20t = wx.RadioButton(id=wxID_FRAMEREDFILTRATERADIOBUTTON20T,
              label=u'20\u671f', name=u'radioButton20t', parent=self.panel3,
              pos=wx.Point(290, 10), size=wx.Size(54, 14), style=0)
        self.radioButton20t.SetValue(True)
        self.radioButton20t.Bind(wx.EVT_RADIOBUTTON,
              self.OnRadioButton20tRadiobutton,
              id=wxID_FRAMEREDFILTRATERADIOBUTTON20T)

        self.radioButton40t = wx.RadioButton(id=wxID_FRAMEREDFILTRATERADIOBUTTON40T,
              label=u'40\u671f', name=u'radioButton40t', parent=self.panel3,
              pos=wx.Point(350, 10), size=wx.Size(54, 14), style=0)
        self.radioButton40t.SetValue(False)
        self.radioButton40t.Bind(wx.EVT_RADIOBUTTON,
              self.OnRadioButton40tRadiobutton,
              id=wxID_FRAMEREDFILTRATERADIOBUTTON40T)

        self.textCtrldataf = wx.TextCtrl(id=wxID_FRAMEREDFILTRATETEXTCTRLDATAF,
              name=u'textCtrldataf', parent=self.panel1, pos=wx.Point(16, 112),
              size=wx.Size(448, 296), style=wx.TE_MULTILINE,
              value=u'\u663e\u793a\u8fc7\u6ee4\u540e\u6570\u636e')

        self.buttononestep = wx.Button(id=wxID_FRAMEREDFILTRATEBUTTONONESTEP,
              label=u'\u4e00\u6b65\u8fc7\u6ee4', name=u'buttononestep',
              parent=self.panel1, pos=wx.Point(242, 32), size=wx.Size(75, 24),
              style=0)
        self.buttononestep.SetForegroundColour(wx.Colour(128, 0, 255))
        self.buttononestep.Bind(wx.EVT_BUTTON, self.OnButtononestepButton,
              id=wxID_FRAMEREDFILTRATEBUTTONONESTEP)

    def __init__(self, parent):
        self._init_ctrls(parent)
       
        #����λ��
        self.Center()
             
        #��ȡ��������
        global data_array, redOrder, redOrder100, redTimes, redTimes100, \
               redOrder50, redTimes50, bet_array, \
               data_para_array, filter_array, percent_array
        
        #if len(data_array)==0: #�����Ϳ������¶�ȡ����������
        #��ȡ����ʱ��Щ�ӳ٣���ʾһ������
        image = wx.Image("pic/splash.jpg", wx.BITMAP_TYPE_ANY)
        bmp = image.ConvertToBitmap()
        wx.SplashScreen(bmp, wx.SPLASH_CENTRE_ON_SCREEN | wx.SPLASH_TIMEOUT, 1800, None, -1)
        wx.Yield() 
        
        #��ȡ��������
        data_array = readDataFileToArray()
        #��ȡ�̶�Ͷע
        bet_array = readBetFileToArray()
        #��ȡ��������
        filter_array = readFilterFileToArray()
        #�������������������
        redOrder, redTimes, redOrder100, redTimes100, redOrder50, redTimes50 = redOrderCoumpute(data_array)
        #�������������ᵼ�½������Щ�ٶۣ���ÿ��Զ���̴���
        #���㿪�����ݶ�Ӧ�Ĳ�����24���Ӧ����������
        data_para_array = dataParaCompute(data_array, redOrder, redOrder100, redOrder50, bet_array)
        #����ٷֱ�
        percent_array = percentCompute(filter_array, data_para_array)
            
        #����һ�ڳ��ֵĺ����Ϊ��ɫ
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
                         self.checkBox32,self.checkBox32,self.checkBox33
                         ]
        for i in range(1, 6+1):
            checkBox_list[int(data_array[0][i])-1].SetForegroundColour('BLUE')


        #self.checkBox02.  
            
        #��ť��ʾ�����أ����ư�ť��ʾ�������Ĳ�̫���룬̫���ң�
        #Ĭ�Ͻ�step��0�ǲ��Ǿͼ򵥶���
        global step
        step = 0
        #����������
        global num_pool, data_f
        num_pool = []
        data_f = []
        if step==0:
            self.buttondatabuild.Show()
            self.buttononestep.Show()
            self.buttonnextstep.Show(False)
            self.buttonlaststep.Show(False)
            self.buttonuse.Show(False)
            self.buttonsave.Show(False)
            self.buttonlowerminus.Show(False)
            self.buttonlowerplus.Show(False)
            self.buttonupperminus.Show(False)
            self.buttonupperplus.Show(False)
            self.panel3.Show(False) #����ͼ��岻��ʾ
            self.textCtrldataf.Show(False) #Ԥ�����ݽ������ʾ
        '''
        if step==1:
            self.buttonnextstep.Show()
            self.buttonlaststep.Show(False)
            self.buttondatabuild.Show(False)
            self.buttononestep.Show(False)
            self.buttonsave.Show(False)    
            if '��' in filter_array[step-1][2]:
                self.buttonuse.Show()
                self.buttonlowerminus.Show()
                self.buttonlowerplus.Show()
                self.buttonupperminus.Show()
                self.buttonupperplus.Show()                  
            else:
                self.buttonuse.Show(False)
                self.buttonlowerminus.Show(False)
                self.buttonlowerplus.Show(False)
                self.buttonupperplus.Show(False)
                self.buttonupperminus.Show(False)                
            self.panel2.Show(False) #ѡ����岻��ʾ 
            self.panel3.Show() #����ͼ�����ʾ
            self.textCtrldataf.Show(False) #Ԥ�����ݽ������ʾ
        if step>1 and step<=len(filter_array) and len(filter_array)!=0:
            self.buttonnextstep.Show()
            self.buttonlaststep.Show()           
            self.buttondatabuild.Show(False)
            self.buttononestep.Show(False)
            self.buttonsave.Show(False)
            if '��' in filter_array[step-1][2]:
                self.buttonuse.Show()
                self.buttonlowerminus.Show()
                self.buttonlowerplus.Show()
                self.buttonupperminus.Show()
                self.buttonupperplus.Show()                  
            else:
                self.buttonuse.Show(False)
                self.buttonlowerminus.Show(False)
                self.buttonlowerplus.Show(False)
                self.buttonupperplus.Show(False)
                self.buttonupperminus.Show(False)
            self.panel2.Show(False) #ѡ����岻��ʾ
            self.textCtrldataf.Show(False) #Ԥ�����ݽ������ʾ
        if step>len(filter_array) and len(filter_array)!=0:
            self.buttonlaststep.Show()
            self.buttonsave.Show()
            self.buttonuse.Show(False)             
            self.buttonnextstep.Show(False)
            self.buttondatabuild.Show(False)
            self.buttononestep.Show(False)
            self.buttonlowerminus.Show(False)
            self.buttonlowerplus.Show(False)
            self.buttonupperminus.Show(False)
            self.buttonupperplus.Show(False)             
            self.panel2.Show(False) #ѡ����岻��ʾ
            self.panel3.Show(False) #����ͼ��岻��ʾ
            self.textCtrldataf.SetFont(wx.Font(10, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, ""))
            self.textCtrldataf.Show() #Ԥ�����ݽ����ʾ
            #����ʾ�����д������
            self.textCtrldataf.Clear()
            show_txt = '���˺��������£�\n'
            for i in range(0, len(data_f)):
                show_txt = show_txt + '%.2d %.2d %.2d %.2d %.2d %.2d\n'\
                           %(data_f[i][0],data_f[i][1],data_f[i][2],data_f[i][3],data_f[i][4],data_f[i][5])
            self.textCtrldataf.AppendText(show_txt)
        '''                 
        #���Ҫ��unicode�汾��wxPython�в鿴���֣���Ҫ����unicode���������£�
        #print unicode(filter_array[0][1], 'mbcs')



#-------------------------------------------------------------------------------
#----�������ɰ�ť----

    def OnButtondatabuildButton(self, event): #��ʼ�������ɰ�ť
        '''���ɳ�ʼ���ݣ���ѡ��ȫ������Ϊ1107568�飩'''
        global data_f, step, num_pool, data_para_array, percent_array
        #�жϺ�����Ƿ���ڵ���6������
        if len(num_pool)>=6:           
            #��������е����ְ��մ�С�����˳������
            for i in range(len(num_pool)-1, 0, -1):
                for j in range(0, i):
                    if num_pool[j]>num_pool[j+1]:
                        tmp = num_pool[j]
                        num_pool[j] = num_pool[j+1]
                        num_pool[j+1] = tmp
            #������
            dlg = wx.ProgressDialog("��ʼ���������С���",
                            "���Ժ�",
                            maximum = 1107568,
                            parent = self,
                            style = wx.PD_APP_MODAL
                            | wx.PD_ELAPSED_TIME
                            | wx.PD_REMAINING_TIME
                            )
            #1107568����������
            #�������������ַ���������ʱ�䶼��ֻ࣬���㷨��ͬ����
            #֮�����õ�1�֣�����Ϊ�������Ժ�����ȥ��ĳ����
            #��1��:��Ҳ���Կ�����һ�ֱ�����
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
            #��2��:
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
            #�������ر�
            dlg.Destroy()                    
            #0+1=1
            step = step + 1
            #��ť��ʾ������
            self.buttondatabuild.Show(False)
            self.buttononestep.Show(False)
            self.buttonnextstep.Show()
            self.buttonlowerminus.Show()
            self.buttonlowerplus.Show()
            self.buttonupperminus.Show()
            self.buttonupperplus.Show()         
            if '��' in filter_array[step-1][2]:
                self.buttonuse.Show()
            else:
                self.buttonuse.Show(False) 
            #ѡ����岻��ʾ
            self.panel2.Show(False) 
            #����ͼ�����ʾ
            self.panel3.Show() 
            #ˢ��
            self.Refresh()
            
            #��������ѡ��������
            filter_name = [] #���й������������б�
            for i in range(0, len(filter_array)):
                filter_name.append(filter_array[i][1])
            self.comboBox1 = wx.ComboBox(choices=filter_name,
                  id=-1, name='comboBox1',
                  parent=self.panel1, pos=wx.Point(344, 17), size=wx.Size(110, 22),
                  style=0, value=u'\u9009\u62e9\u8fc7\u6ee4\u6761\u4ef6')
            #��
            self.comboBox1.Bind(wx.EVT_TEXT, self.OnComboBox1Text, id=-1)            

        #������еĺ���С��6��
        else:
            #������ʾ��
            dlg = wx.MessageDialog(self, 'ѡ�еĺ�������6����', 
                                   '������ѡ�����',
                                   wx.OK | wx.ICON_INFORMATION
                                   )
            dlg.ShowModal()
            dlg.Destroy()   
            
        event.Skip()
        
#-------------------------------------------------------------------------------
#----ѡ�����----
    def OnRadioButtonallyesRadiobutton(self, event): #ȫѡ��ť
        '''ѡ��ȫ���ĺ��룬��ע�������'''
        #ֵ����ΪTrue����ѡ��״̬ #�ⲿ�ִ���Ӧ�����Ż��Ŀռ䣬Ctrl����ĥû��
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
        #ע�������
        global num_pool
        num_pool = [] #�����һ�£������������Ѿ�����һЩ����
        for i in range(1, 33+1):
            num_pool.append(i)
        #��ʾѡ���˶��ٸ���
        msg[1] = '%.2d'%(len(num_pool))
        self.Refresh()
        
        event.Skip()

    def OnRadioButtonallnoRadiobutton(self, event): #ȫ��ѡ��ť
        '''��ѡ����벢��պ����'''
        #ֵ����ΪFalse������ѡ״̬ 
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
        #��պ����  
        global num_pool
        num_pool = []
        #��ʾѡ���˶��ٸ���
        msg[1] = '%.2d'%(len(num_pool))
        self.Refresh()
        
        event.Skip()

    def OnCheckBox01Checkbox(self, event): #01
        '''��1��ӵ�������У���Ӻ������ɾ��'''
        global num_pool
        if 1 in num_pool: #�����ڲ���
            num_pool.remove(1) #ɾ��     
        else:
            num_pool.append(1) #���

        #����ظ�����ʾ����
        msg[1] = '%.2d'%(len(num_pool))
        self.Refresh()
        
        event.Skip()
        
    def OnCheckBox02Checkbox(self, event): #02
        '''��2��ӵ�������У���Ӻ������ɾ��'''
        global num_pool
        if 2 in num_pool:
            num_pool.remove(2)      
        else:
            num_pool.append(2)

        #����ظ�����ʾ����
        msg[1] = '%.2d'%(len(num_pool))
        self.Refresh()
        
        event.Skip()
        
    def OnCheckBox03Checkbox(self, event):#03
        '''��3��ӵ�������У���Ӻ������ɾ��'''
        global num_pool
        if 3 in num_pool:
            num_pool.remove(3)      
        else:
            num_pool.append(3)

        #����ظ�����ʾ����
        msg[1] = '%.2d'%(len(num_pool))
        self.Refresh()
        
        event.Skip()

    def OnCheckBox04Checkbox(self, event):#04
        '''��4��ӵ�������У���Ӻ������ɾ��'''
        global num_pool
        if 4 in num_pool:
            num_pool.remove(4)      
        else:
            num_pool.append(4)

        #����ظ�����ʾ����
        msg[1] = '%.2d'%(len(num_pool))
        self.Refresh()
        
        event.Skip()

    def OnCheckBox05Checkbox(self, event):#05
        '''��5��ӵ�������У���Ӻ������ɾ��'''
        global num_pool
        if 5 in num_pool:
            num_pool.remove(5)      
        else:
            num_pool.append(5)

        #����ظ�����ʾ����
        msg[1] = '%.2d'%(len(num_pool))
        self.Refresh()
         
        event.Skip()

    def OnCheckBox06Checkbox(self, event):#06
        '''��6��ӵ�������У���Ӻ������ɾ��'''
        global num_pool
        if 6 in num_pool:
            num_pool.remove(6)      
        else:
            num_pool.append(6)

        #����ظ�����ʾ����
        msg[1] = '%.2d'%(len(num_pool))
        self.Refresh()
        
        event.Skip()
        
    def OnCheckBox07Checkbox(self, event):#07
        '''��7��ӵ�������У���Ӻ������ɾ��'''
        global num_pool
        if 7 in num_pool:
            num_pool.remove(7)      
        else:
            num_pool.append(7)

        #����ظ�����ʾ����
        msg[1] = '%.2d'%(len(num_pool))
        self.Refresh()
         
        event.Skip()
        
    def OnCheckBox08Checkbox(self, event):#08
        '''��8��ӵ�������У���Ӻ������ɾ��'''
        global num_pool
        if 8 in num_pool:
            num_pool.remove(8)      
        else:
            num_pool.append(8)

        #����ظ�����ʾ����
        msg[1] = '%.2d'%(len(num_pool))
        self.Refresh()
        
        event.Skip()
        
    def OnCheckBox09Checkbox(self, event):#09
        '''��9��ӵ�������У���Ӻ������ɾ��'''
        global num_pool
        if 9 in num_pool:
            num_pool.remove(9)      
        else:
            num_pool.append(9)

        #����ظ�����ʾ����
        msg[1] = '%.2d'%(len(num_pool))
        self.Refresh()
         
        event.Skip()

    def OnCheckBox10Checkbox(self, event):#10
        '''��10��ӵ�������У���Ӻ������ɾ��'''
        global num_pool
        if 10 in num_pool:
            num_pool.remove(10)      
        else:
            num_pool.append(10)

        #����ظ�����ʾ����
        msg[1] = '%.2d'%(len(num_pool))
        self.Refresh()
        
        event.Skip()

    def OnCheckBox11Checkbox(self, event):#11
        '''��11��ӵ�������У���Ӻ������ɾ��'''
        global num_pool
        if 11 in num_pool:
            num_pool.remove(11)      
        else:
            num_pool.append(11)

        #����ظ�����ʾ����
        msg[1] = '%.2d'%(len(num_pool))
        self.Refresh()
        
        event.Skip()

    def OnCheckBox12Checkbox(self, event):#12
        '''��12��ӵ�������У���Ӻ������ɾ��'''
        global num_pool
        if 12 in num_pool:
            num_pool.remove(12)      
        else:
            num_pool.append(12)

        #����ظ�����ʾ����
        msg[1] = '%.2d'%(len(num_pool))
        self.Refresh()
        
        event.Skip()

    def OnCheckBox13Checkbox(self, event):#13
        '''��13��ӵ�������У���Ӻ������ɾ��'''
        global num_pool
        if 13 in num_pool:
            num_pool.remove(13)      
        else:
            num_pool.append(13)

        #����ظ�����ʾ����
        msg[1] = '%.2d'%(len(num_pool))
        self.Refresh()
        
        event.Skip()

    def OnCheckBox14Checkbox(self, event):#14
        '''��14��ӵ�������У���Ӻ������ɾ��'''
        global num_pool
        if 14 in num_pool:
            num_pool.remove(14)      
        else:
            num_pool.append(14)

        #����ظ�����ʾ����
        msg[1] = '%.2d'%(len(num_pool))
        self.Refresh()
        
        event.Skip()

    def OnCheckBox15Checkbox(self, event):#15
        '''��15��ӵ�������У���Ӻ������ɾ��'''
        global num_pool
        if 15 in num_pool:
            num_pool.remove(15)      
        else:
            num_pool.append(15)

        #����ظ�����ʾ����
        msg[1] = '%.2d'%(len(num_pool))
        self.Refresh()
        
        event.Skip()

    def OnCheckBox16Checkbox(self, event):#16
        '''��16��ӵ�������У���Ӻ������ɾ��'''
        global num_pool
        if 16 in num_pool:
            num_pool.remove(16)      
        else:
            num_pool.append(16)

        #����ظ�����ʾ����
        msg[1] = '%.2d'%(len(num_pool))
        self.Refresh()
        
        event.Skip()
        
    def OnCheckBox17Checkbox(self, event):#17
        '''��17��ӵ�������У���Ӻ������ɾ��'''
        global num_pool
        if 17 in num_pool:
            num_pool.remove(17)      
        else:
            num_pool.append(17)

        #����ظ�����ʾ����
        msg[1] = '%.2d'%(len(num_pool))
        self.Refresh()
        
        event.Skip()

    def OnCheckBox18Checkbox(self, event):#18
        '''��18��ӵ�������У���Ӻ������ɾ��'''
        global num_pool
        if 18 in num_pool:
            num_pool.remove(18)      
        else:
            num_pool.append(18)

        #����ظ�����ʾ����
        msg[1] = '%.2d'%(len(num_pool))
        self.Refresh()
        
        event.Skip()

    def OnCheckBox19Checkbox(self, event):#19
        '''��19��ӵ�������У���Ӻ������ɾ��'''
        global num_pool
        if 19 in num_pool:
            num_pool.remove(19)      
        else:
            num_pool.append(19)

        #����ظ�����ʾ����
        msg[1] = '%.2d'%(len(num_pool))
        self.Refresh()
        
        event.Skip()

    def OnCheckBox20Checkbox(self, event):#20
        '''��20��ӵ�������У���Ӻ������ɾ��'''
        global num_pool
        if 20 in num_pool:
            num_pool.remove(20)      
        else:
            num_pool.append(20)

        #����ظ�����ʾ����
        msg[1] = '%.2d'%(len(num_pool))
        self.Refresh()
        
        event.Skip()

    def OnCheckBox21Checkbox(self, event):#21
        '''��21��ӵ�������У���Ӻ������ɾ��'''
        global num_pool
        if 21 in num_pool:
            num_pool.remove(21)      
        else:
            num_pool.append(21)

        #����ظ�����ʾ����
        msg[1] = '%.2d'%(len(num_pool))
        self.Refresh()
        
        event.Skip()

    def OnCheckBox22Checkbox(self, event):#22
        '''��22��ӵ�������У���Ӻ������ɾ��'''
        global num_pool
        if 22 in num_pool:
            num_pool.remove(22)      
        else:
            num_pool.append(22)

        #����ظ�����ʾ����
        msg[1] = '%.2d'%(len(num_pool))
        self.Refresh()
        
        event.Skip()

    def OnCheckBox23Checkbox(self, event):#23
        '''��23��ӵ�������У���Ӻ������ɾ��'''
        global num_pool
        if 23 in num_pool:
            num_pool.remove(23)      
        else:
            num_pool.append(23)

        #����ظ�����ʾ����
        msg[1] = '%.2d'%(len(num_pool))
        self.Refresh()
        
        event.Skip()

    def OnCheckBox24Checkbox(self, event):#24
        '''��24��ӵ�������У���Ӻ������ɾ��'''
        global num_pool
        if 24 in num_pool:
            num_pool.remove(24)      
        else:
            num_pool.append(24)

        #����ظ�����ʾ����
        msg[1] = '%.2d'%(len(num_pool))
        self.Refresh()
        
        event.Skip()

    def OnCheckBox25Checkbox(self, event):#25
        '''��25��ӵ�������У���Ӻ������ɾ��'''
        global num_pool
        if 25 in num_pool:
            num_pool.remove(25)      
        else:
            num_pool.append(25)

        #����ظ�����ʾ����
        msg[1] = '%.2d'%(len(num_pool))
        self.Refresh()
        
        event.Skip()

    def OnCheckBox26Checkbox(self, event):#26
        '''��26��ӵ�������У���Ӻ������ɾ��'''
        global num_pool
        if 26 in num_pool:
            num_pool.remove(26)      
        else:
            num_pool.append(26)

        #����ظ�����ʾ����
        msg[1] = '%.2d'%(len(num_pool))
        self.Refresh()
        
        event.Skip()

    def OnCheckBox27Checkbox(self, event):#27
        '''��27��ӵ�������У���Ӻ������ɾ��'''
        global num_pool
        if 27 in num_pool:
            num_pool.remove(27)      
        else:
            num_pool.append(27)

        #����ظ�����ʾ����
        msg[1] = '%.2d'%(len(num_pool))
        self.Refresh()
        
        event.Skip()

    def OnCheckBox28Checkbox(self, event):#28
        '''��28��ӵ�������У���Ӻ������ɾ��'''
        global num_pool
        if 28 in num_pool:
            num_pool.remove(28)      
        else:
            num_pool.append(28)

        #����ظ�����ʾ����
        msg[1] = '%.2d'%(len(num_pool))
        self.Refresh()
        
        event.Skip()

    def OnCheckBox29Checkbox(self, event):#29
        '''��29��ӵ�������У���Ӻ������ɾ��'''
        global num_pool
        if 29 in num_pool:
            num_pool.remove(29)      
        else:
            num_pool.append(29)

        #����ظ�����ʾ����
        msg[1] = '%.2d'%(len(num_pool))
        self.Refresh()
        
        event.Skip()

    def OnCheckBox30Checkbox(self, event):#30
        '''��30��ӵ�������У���Ӻ������ɾ��'''
        global num_pool
        if 30 in num_pool:
            num_pool.remove(30)      
        else:
            num_pool.append(30)

        #����ظ�����ʾ����
        msg[1] = '%.2d'%(len(num_pool))
        self.Refresh()
        
        event.Skip()

    def OnCheckBox31Checkbox(self, event):#31
        '''��31��ӵ�������У���Ӻ������ɾ��'''
        global num_pool
        if 31 in num_pool:
            num_pool.remove(31)      
        else:
            num_pool.append(31)

        #����ظ�����ʾ����
        msg[1] = '%.2d'%(len(num_pool))
        self.Refresh()
        
        event.Skip()

    def OnCheckBox32Checkbox(self, event):#32
        '''��32��ӵ�������У���Ӻ������ɾ��'''
        global num_pool
        if 32 in num_pool:
            num_pool.remove(32)      
        else:
            num_pool.append(32)

        #����ظ�����ʾ����
        msg[1] = '%.2d'%(len(num_pool))
        self.Refresh()
        
        event.Skip()
    def OnCheckBox33Checkbox(self, event):#33
        '''��33��ӵ�������У���Ӻ������ɾ��'''
        global num_pool
        if 33 in num_pool:
            num_pool.remove(33)      
        else:
            num_pool.append(33)

        #����ظ�����ʾ����
        msg[1] = '%.2d'%(len(num_pool))
        self.Refresh()
        
        event.Skip()

#-------------------------------------------------------------------------------
#----��ͼ----

    def OnPanel1Paint(self, event):
        dc = wx.PaintDC(self.panel1)
        #self.panel1.DoPrepareDC(dc)
        #�������       
        dc.Clear()
        #�����趨
        global msg
        if step==0:
            msg = ['','']
            msg[0] = '��ʼ������ˣ�ѡ�������������ɳ�ʼ���ݡ���ť'
            msg[1] = '%.2d'%(len(num_pool)) #��ʾ������еĺ������
        if step>0 and step<=len(filter_array):
            msg = ['','','','','','','','','']
            msg[0] = '��ǰΪ��%.2d/%d����%s'%(step, len(filter_array), filter_array[step-1][1])
            msg[1] = '��%s��'%(filter_array[step-1][4])
            msg[2] = '��ǰ����Ϊ%d�����˱�Ϊ%.4f'%(len(data_f), len(data_f)*100.0/1107568)+'%'
            msg[3] = '��ǰ���÷�ΧΪ����%d, %d��'%(int(filter_array[step-1][3].split("-")[0]),int(filter_array[step-1][3].split("-")[1]))
            msg[4] = '�ѿ��������еķ��ϳ̶�Ϊ%s'%(percent_array[step-1])+'%'
            msg[5] = '�Ƿ�ʹ�ô˹���������' 
            if '��' in filter_array[step-1][2]:
                msg[6] = '��'
            else :
                msg[6] = '��'        
        if step>len(filter_array):
            msg = ['','','']
            msg[0] = '������ϣ�'
            msg[1] = '��ǰ����Ϊ%d�����˱�Ϊ%.4f'%(len(data_f), len(data_f)*100.0/1107568)+'%'
            msg[2] = '����������������������˺����ݡ���ť'
        #��������
        dc.SetFont(wx.Font(10, wx.NORMAL, wx.NORMAL, wx.NORMAL))
        if len(msg)==2: #��1��
            dc.SetTextForeground('BLUE')
            #dc.SetFont(wx.Font(10, wx.NORMAL, wx.NORMAL, wx.NORMAL))
            dc.DrawText(msg[0], 5, 5)
            dc.DrawText(msg[1], 450, 5)
        elif len(msg)==3: #���1��
            dc.SetTextForeground('BLUE')
            #dc.SetFont(wx.Font(10, wx.NORMAL, wx.NORMAL, wx.NORMAL))            
            for i in range(0, 3):
                dc.DrawText(msg[i], 5, 5+i*16)
        else : #�м䲽
            dc.SetTextForeground('BLUE')
            #dc.SetFont(wx.Font(10, wx.NORMAL, wx.NORMAL, wx.NORMAL))            
            for i in range(0, 6):
                dc.DrawText(msg[i], 5, 5+i*16)
            if msg[6]=='��': #��ɫ�ġ���
                dc.SetTextForeground('RED')
                dc.DrawText(msg[6], 5+150, 5+5*16)
            if msg[6]=='��': #��ɫ�ġ��ǡ�
                dc.SetTextForeground('#009900')
                dc.DrawText(msg[6], 5+150, 5+5*16)
        
        event.Skip()
        
#-------------------------------------------------------------------------------
#----���水ť----
    def OnButtonnextstepButton(self, event): #��һ����ť
        '''������һ������'''
        global step 
        #+1
        if step<=len(filter_array):   
            step = step + 1  
        if step<=len(filter_array): 
            if '��' in filter_array[step-1][2]:
                self.buttonuse.Show()
                self.buttonlowerminus.Show()
                self.buttonlowerplus.Show()
                self.buttonupperminus.Show()
                self.buttonupperplus.Show()                   
            else:
                self.buttonuse.Show(False) 
                self.buttonlowerminus.Show(False)
                self.buttonlowerplus.Show(False)
                self.buttonupperminus.Show(False)
                self.buttonupperplus.Show(False)    
        #��ʾ����һ������ť
        if step>1:
            self.buttonlaststep.Show()
        #���ء���һ������ť�����Ǳ���
        if step>len(filter_array):
            self.buttonsave.Show()
            self.buttonnextstep.Show(False)
            self.buttonuse.Show(False) 
            self.buttonlowerminus.Show(False)
            self.buttonlowerplus.Show(False)
            self.buttonupperminus.Show(False)
            self.buttonupperplus.Show(False)
            self.panel3.Show(False) #����ͼ��岻��ʾ
            self.comboBox1.Show(False) #����ѡ������������ʾ
            self.textCtrldataf.SetFont(wx.Font(10, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "")) #����һ�£����ܴ�ͷ��ʼ��ʾ
            self.textCtrldataf.Show() #Ԥ�����ݽ����ʾ
            #����ʾ�����д������
            self.textCtrldataf.Clear()
            '''
            self.textCtrldataf.AppendText('���˺��������£�\n')
            for i in range(0, len(data_f)):
                self.textCtrldataf.AppendText('%.2d %.2d %.2d %.2d %.2d %.2d\n'\
                                              %(data_f[i][0],data_f[i][1],data_f[i][2],data_f[i][3],data_f[i][4],data_f[i][5]))
            '''
            #�Ƚ��ı��������һ������ӵ���ʾ�ؼ��л�Ƚ�ʡʱ�䣬�Ƚ�û���ӳٵĸо�
            #���ע�����࣬���沿��û����ʾ��������Ϊtextctrlֻ����ʾ64KB������
            #���Ըĳ�richtext������ֻ����windows����
            if len(data_f)>200:
                show_txt = '���˺��������£��������ʾ200�飩\n'                
                for i in range(0, 200): #ֻ��ʾ200��
                    show_txt = show_txt + '%.2d %.2d %.2d %.2d %.2d %.2d\n'\
                               %(data_f[i][0],data_f[i][1],data_f[i][2],data_f[i][3],data_f[i][4],data_f[i][5])
            else:
                show_txt = '���˺��������£�\n'  
                for i in range(0, len(data_f)):
                    show_txt = show_txt + '%.2d %.2d %.2d %.2d %.2d %.2d\n'\
                               %(data_f[i][0],data_f[i][1],data_f[i][2],data_f[i][3],data_f[i][4],data_f[i][5])
            self.textCtrldataf.AppendText(show_txt)
            self.textCtrldataf.SetInsertionPoint(0)
        #ˢ��
        self.Refresh() 
                    
        event.Skip()

    def OnButtonlaststepButton(self, event): #��һ����ť
        '''������һ������'''
        global step
        #-1
        if step>1:
            step = step - 1  
            if '��' in filter_array[step-1][2]:
                self.buttonuse.Show()
                self.buttonlowerminus.Show()
                self.buttonlowerplus.Show()
                self.buttonupperminus.Show()
                self.buttonupperplus.Show()                    
            else:
                self.buttonuse.Show(False) 
                self.buttonlowerminus.Show(False)
                self.buttonlowerplus.Show(False)
                self.buttonupperminus.Show(False)
                self.buttonupperplus.Show(False)                   
        #��ʾ����һ������ť
        if step<=len(filter_array):
            self.buttonnextstep.Show()
            self.panel3.Show() #����ͼ�����ʾ
            self.comboBox1.Show() #����ѡ����������ʾ
            self.buttonsave.Show(False)  
            self.textCtrldataf.Show(False) #Ԥ�����ݽ������ʾ
        #���ء���һ������ť�����Ǳ���
        if step==1:
            self.buttonlaststep.Show(False)
        #ˢ��
        self.Refresh() 
        
        event.Skip()
        
    def OnButtonexitButton(self, event): #�˳���ť
        '''�˳�����������'''
        #�رմ���
        self.Close()

        event.Skip()
        
#-------------------------------------------------------------------------------
#----�����������ư�ť----
    def OnButtonuseButton(self, event): #ʹ�ô�������ť
        '''ȷ��ʹ�ø��������ˣ������񡱸�Ϊ���ǡ���
           Ӧ����Ӧ���������ݽ��й��ˣ�ˢ����ʾ������
        '''       
        #��Ϊ���ǡ�
        global filter_array, data_f
        filter_array[step-1][2] = '��' + filter_array[step-1][2][2:]
        #����
        data_f = dataFiltrate(data_array, data_f, step, filter_array, redOrder, redOrder100, redOrder50, bet_array)
        #���ذ�ť������
        self.buttonuse.Show(False) 
        #���ؿɵ�����Χ��ť 
        self.buttonlowerminus.Show(False)
        self.buttonlowerplus.Show(False)
        self.buttonupperplus.Show(False)
        self.buttonupperminus.Show(False)
        #ˢ��
        self.Refresh() 
        
        event.Skip()
        
    def OnButtonlowerminusButton(self, event): #��Χ�е�����ֵ��С
        '''����Χ�е�����ֵ��1����ˢ����ʾ����'''
        global filter_array, percent_array
        #���޼�1
        tmp = int(filter_array[step-1][3].split('-')[0])
        if tmp!=0 and tmp<1000:
            tmp = int(filter_array[step-1][3].split('-')[0]) - 1 
        #���¹�������
        #ע�⣺��Ϊsplit֮��õ�����str������������Ҫint����������ת����
        #      ������ʱ��10�����9,�����ָ���str��ʱ�������1λ
        #      Ҳ�п���9�ӵ�10��str����1λ
        #      ���������д�µ��ļ�ʱ(****_��������.txt)Ҫ���´�����һ����
        filter_array[step-1][3] = '%d'%(tmp) + '-' + filter_array[step-1][3].split('-')[1]\
                                             + '-' + filter_array[step-1][3].split('-')[2]
        #���¼���ٷֱ�
        percent_array = percentCompute(filter_array, data_para_array)
        #ˢ��
        self.Refresh() 
        
        event.Skip()

    def OnButtonlowerplusButton(self, event): #��Χ�е�����ֵ����
        '''����Χ�е�����ֵ��1����ˢ����ʾ����'''
        global filter_array, percent_array
        #���޼�1
        tmp = int(filter_array[step-1][3].split('-')[0])
        if tmp<int(filter_array[step-1][3].split('-')[1]):
            tmp = int(filter_array[step-1][3].split('-')[0]) + 1 
        #���¹�������
        filter_array[step-1][3] = '%d'%(tmp) + '-' + filter_array[step-1][3].split('-')[1]\
                                             + '-' + filter_array[step-1][3].split('-')[2]     
        #���¼���ٷֱ�
        percent_array = percentCompute(filter_array, data_para_array)
        #ˢ��
        self.Refresh() 
        
        event.Skip()
        
    def OnButtonupperminusButton(self, event): #��Χ�е�����ֵ��С
        '''����Χ�е�����ֵ��1����ˢ����ʾ����'''
        global filter_array, percent_array
        #���޼�1
        tmp = int(filter_array[step-1][3].split('-')[1])
        if tmp>int(filter_array[step-1][3].split('-')[0]):
            tmp = int(filter_array[step-1][3].split('-')[1]) - 1            
        #���¹�������
        filter_array[step-1][3] = filter_array[step-1][3].split('-')[0] + '-' + '%d'%(tmp)\
                                             + '-' + filter_array[step-1][3].split('-')[2]                
        #���¼���ٷֱ�
        percent_array = percentCompute(filter_array, data_para_array)
        #ˢ��
        self.Refresh() 
        
        event.Skip()
        
    def OnButtonupperplusButton(self, event): #��Χ�е�����ֵ����
        '''����Χ�е�����ֵ��1����ˢ����ʾ����'''
        global filter_array, percent_array
        #���޼�1
        tmp = int(filter_array[step-1][3].split('-')[1])
        if tmp<999:
            tmp = int(filter_array[step-1][3].split('-')[1]) + 1           
        #���¹�������
        filter_array[step-1][3] = filter_array[step-1][3].split('-')[0] + '-' + '%d'%(tmp)\
                                             + '-' + filter_array[step-1][3].split('-')[2]           
        #���¼���ٷֱ�
        percent_array = percentCompute(filter_array, data_para_array)
        #ˢ��
        self.Refresh() 
        
        event.Skip()
        
    def OnButtonsaveButton(self, event): #���水ť
        '''������˺����ݼ�Ӧ�õ��Ĺ�������''' 
        
        #д����
        writePredictData(data_array, data_f, filter_array, num_pool)
        #����Ӧ�ļ���
        os.startfile('%s'%(int(data_array[0][0])+1))
        #�رմ���
        #����һֱ��ʾ�űȽϺ�һ�㣬��˵�أ�
        self.Close() 
        
        event.Skip()

#-------------------------------------------------------------------------------
#----������������ͼ��ʾ----
    def OnPanel3Paint(self, event): #��������ͼ
        dc = wx.PaintDC(self.panel3)     
        dc.Clear()
        
        #���Ƴ�ȥ����Ŀո�
        name_no_blank = filter_array[step-1][1].split(' ')[0]
        #���10�ڵ�
        if term==10:
            #����
            dc.SetTextForeground('FIREBRICK') #�ͻ�שɫ  
            dc.DrawText('%s����ͼ�����10�ڣ�'%name_no_blank, 10, 10)
            #��������
            dc.SetPen(wx.Pen('BLUE', 1))
            dc.DrawLine(20,30,20,280) #����
            dc.DrawLine(10,270,420,270) #����
            dc.DrawLine(20,30,15,35) #���ߵļ�ͷ
            dc.DrawLine(20,30,25,35)
            dc.DrawLine(420,270,415,265) #���ߵļ�ͷ
            dc.DrawLine(420,270,415,275)
            #�õ����10�ڵ�ֵ���б�
            value_10 = []
            for i in range(0, 10):
                value_10.append(data_para_array[i][name_no_blank])
            #���ƽ��ֵ
            value_a = 0.0
            for i in range(0, 10):
                value_a = value_a + value_10[i]
            value_a = value_a*1.0/10
            #���ֵ��ƽ��ֵ��4
            value_max = int(value_a*4)
            #��10��������
            dc.SetPen(wx.Pen('MEDIUM VIOLET RED', 1)) #������߿���ɫ
            dc.SetBrush(wx.Brush('#FFD5D5', wx.SOLID)) #�����ڲ������ɫ
            for i in range(0, 10):
                #��������Ϊ�����ϽǺ����ꡢ���Ͻ������ꡢ����
                dc.DrawRectangle(40+i*36, 270-240*value_10[9-i]/value_max, 20, 240*value_10[9-i]/value_max)
            #�ڳ����ζ��ˣ���ע��������
            dc.SetTextForeground('ORANGE RED') 
            for i in range(0, 10):
                dc.DrawText('%s'%value_10[9-i], 40+i*36, (270-240*value_10[9-i]/value_max)-15)
            #���������·���ע���������
            dc.SetTextForeground('ORCHID')
            dc.SetFont(wx.Font(7, wx.SWISS, wx.NORMAL, wx.NORMAL))  
            for i in range(0, 10):
                dc.DrawRotatedText('%s'%data_array[9-i][0], 40+i*36-8, 275, 15) #��ת����
            #����10�ھ�ֵ��
            dc.SetPen(wx.Pen('DARK OLIVE GREEN', 1, wx.DOT_DASH))
            dc.DrawLine(20,270-240*value_a/value_max,420,270-240*value_a/value_max)
            #��10�ھ�ֵ���ϱ�ע���������
            dc.SetTextForeground('DARK OLIVE GREEN')
            dc.SetFont(wx.Font(8, wx.NORMAL, wx.NORMAL, wx.NORMAL))
            dc.DrawText('10�ھ�ֵ%s'%value_a, 360, 270-240*value_a/value_max-15)
        #���20�ڵ�
        if term==20:
            #����
            dc.SetTextForeground('FIREBRICK') #�ͻ�שɫ  
            dc.DrawText('%s����ͼ�����20�ڣ�'%name_no_blank, 10, 10)
            #��������
            dc.SetPen(wx.Pen('BLUE', 1))
            dc.DrawLine(20,30,20,280) #����
            dc.DrawLine(10,270,420,270) #����
            dc.DrawLine(20,30,15,35) #���ߵļ�ͷ
            dc.DrawLine(20,30,25,35)
            dc.DrawLine(420,270,415,265) #���ߵļ�ͷ
            dc.DrawLine(420,270,415,275)
            #�õ����20�ڵ�ֵ���б�
            value_20 = []
            for i in range(0, 20):
                value_20.append(data_para_array[i][name_no_blank])
            #���ƽ��ֵ
            value_a = 0.0
            for i in range(0, 20):
                value_a = value_a + value_20[i]
            value_a = value_a*1.0/20
            #���ֵ��ƽ��ֵ��4
            value_max = int(value_a*4) #��int����Ϊfloat�ᵼ�³����εײ���ʱ�޷��Ӵ���x��
            #��20��������
            dc.SetPen(wx.Pen('MEDIUM VIOLET RED', 1)) #������߿���ɫ
            dc.SetBrush(wx.Brush('#FFD5D5', wx.SOLID )) #�����ڲ������ɫ
            for i in range(0, 20):
            #��������Ϊ�����ϽǺ����ꡢ���Ͻ������ꡢ����
                dc.DrawRectangle(30+i*18, 270-240*value_20[19-i]/value_max, 10, 240*value_20[19-i]/value_max)
            #�ڳ����ζ��ˣ���ע��������
            dc.SetTextForeground('ORANGE RED') 
            for i in range(0, 20):
                dc.DrawText('%s'%value_20[19-i], 30+i*18, (270-240*value_20[19-i]/value_max)-15)
            #���������·���ע���������
            dc.SetTextForeground('ORCHID')
            dc.SetFont(wx.Font(7, wx.SWISS, wx.NORMAL, wx.NORMAL))  
            for i in range(3, 20, 4): #��4����ʾ��Ҫ��̫����
                dc.DrawText('%s'%data_array[19-i][0], 30+i*18-4, 275)
            #����20�ھ�ֵ��
            dc.SetPen(wx.Pen('DARK OLIVE GREEN', 1, wx.DOT_DASH))
            dc.DrawLine(20,270-240*value_a/value_max,420,270-240*value_a/value_max)
            #��20�ھ�ֵ���ϱ�ע���������
            dc.SetTextForeground('DARK OLIVE GREEN')
            dc.SetFont(wx.Font(8, wx.NORMAL, wx.NORMAL, wx.NORMAL))
            dc.DrawText('20�ھ�ֵ%s'%value_a, 360, 270-240*value_a/value_max-15)
        #���40�ڵ�
        if term==40:
            #����
            dc.SetTextForeground('FIREBRICK') #�ͻ�שɫ  
            dc.DrawText('%s����ͼ�����40�ڣ�'%name_no_blank, 10, 10)
            #��������
            dc.SetPen(wx.Pen('BLUE', 1))
            dc.DrawLine(20,30,20,280) #����
            dc.DrawLine(10,270,420,270) #����
            dc.DrawLine(20,30,15,35) #���ߵļ�ͷ
            dc.DrawLine(20,30,25,35)
            dc.DrawLine(420,270,415,265) #���ߵļ�ͷ
            dc.DrawLine(420,270,415,275)
            #�õ����40�ڵ�ֵ���б�
            value_40 = []
            for i in range(0, 40):
                value_40.append(data_para_array[i][name_no_blank])
            #���ƽ��ֵ
            value_a = 0.0
            for i in range(0, 40):
                value_a = value_a + value_40[i]
            value_a = value_a*1.0/40
            #���ֵ��ƽ��ֵ��4
            value_max = int(value_a*4) #��int����Ϊfloat�ᵼ�³����εײ���ʱ�޷��Ӵ���x��
            #��40��������
            dc.SetPen(wx.Pen('MEDIUM VIOLET RED', 1)) #������߿���ɫ
            dc.SetBrush(wx.Brush('#FFD5D5', wx.SOLID )) #�����ڲ������ɫ
            for i in range(0, 40):
            #��������Ϊ�����ϽǺ����ꡢ���Ͻ������ꡢ����
                dc.DrawRectangle(30+i*9, 270-240*value_40[39-i]/value_max, 5, 240*value_40[39-i]/value_max)
            #�ڳ����ζ��ˣ���ע��������
            dc.SetTextForeground('ORANGE RED') 
            for i in range(0, 40):
                dc.DrawText('%s'%value_40[39-i], 30+i*9, (270-240*value_40[39-i]/value_max)-15)
            #���������·���ע���������
            dc.SetTextForeground('ORCHID')
            dc.SetFont(wx.Font(7, wx.SWISS, wx.NORMAL, wx.NORMAL))  
            for i in range(3, 40, 8): #��8����ʾ��Ҫ��̫����
                dc.DrawText('%s'%data_array[19-i][0], 30+i*18-4, 275)
            #����40�ھ�ֵ��
            dc.SetPen(wx.Pen('DARK OLIVE GREEN', 1, wx.DOT_DASH))
            dc.DrawLine(20,270-240*value_a/value_max,420,270-240*value_a/value_max)
            #��40�ھ�ֵ���ϱ�ע���������
            dc.SetTextForeground('DARK OLIVE GREEN')
            dc.SetFont(wx.Font(8, wx.NORMAL, wx.NORMAL, wx.NORMAL))
            dc.DrawText('40�ھ�ֵ%s'%value_a, 360, 270-240*value_a/value_max-15)
        
        event.Skip()

    def OnRadioButton10tRadiobutton(self, event): #��ʾ10������ͼ
        global term
        term = 10
        self.Refresh() #ˢ�£����������ļ�������
        event.Skip()

    def OnRadioButton20tRadiobutton(self, event): #��ʾ20������ͼ
        global term
        term = 20    
        self.Refresh() #ˢ��
        event.Skip()
        
    def OnRadioButton40tRadiobutton(self, event): #��ʾ40������ͼ
        global term
        term = 40    
        self.Refresh() #ˢ��
        event.Skip()
        

    def OnButtononestepButton(self, event): #һ�����˰�ť
        '''һ���Թ���'''
        global data_f, step, num_pool,filter_array
        if len(num_pool)>=6:
            continue_f = True #�Ƿ�������й����жϷ�
            if len(num_pool)>12:
                
                dlg = wx.MessageDialog(self, 'ѡ�����϶�ʱ������ʱ���Ƚϳ�', 
                                       'ȷ��Ҫһ�����ˣ�',
                                       wx.YES_NO | wx.NO_DEFAULT | wx.ICON_INFORMATION
                                       )
                result = dlg.ShowModal()
                dlg.Destroy()
                if result==wx.ID_YES: #ȷ����Ҫһ������
                    continue_f = True
                if result==wx.ID_NO: #������һ������
                    continue_f = False
            #if continue_f==True:
            if continue_f:
                #��ʼʱ��
                start_time = int(time.time())           
                #--������               
                dlg = wx.ProgressDialog("�����С���",
                                "�����ĵȴ���",
                                maximum = len(filter_array) + 1 + 1,
                                parent = self,
                                style = wx.PD_APP_MODAL
                                )
                #�رյ�ǰ���ڣ����������壩 #������رմ��ڣ���Ϊstep�ı仯������������Ҳ����ű仯
                self.Close()                  
                #--��������е����ְ��մ�С�����˳������
                for i in range(len(num_pool)-1, 0, -1):
                    for j in range(0, i):
                        if num_pool[j]>num_pool[j+1]:
                            num_pool[j], num_pool[j+1] = num_pool[j+1], num_pool[j]
                #--������Ҫ�����˵���������
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
                dlg.Update(1)
                #��ʾԭʼע��
                #print len(data_f)
                #--��ʼ����
                for i in range(0, len(filter_array)):
                    #+1
                    step = step + 1
                    #��Ϊ���ǡ�
                    filter_array[step-1][2] = '��' + filter_array[step-1][2][2:]
                    #����
                    data_f = dataFiltrate(data_array, data_f, step, filter_array, redOrder, redOrder100, redOrder50, bet_array)
                    #���½�����
                    dlg.Update(step+1)
                    #��ʾ���˺��ע��
                    #print len(data_f)
                    #����̨������ڽ��еĲ���
                    if step==1:
                        print '%.2d time=%d num=%d'%(step,int(time.time())-start_time,len(data_f))
                        last_time = int(time.time())
                    else:
                        print '%.2d time=%d num=%d'%(step,int(time.time())-last_time,len(data_f))
                        last_time = int(time.time())                    
                #--�������ر�
                dlg.Destroy()
                #��ֹʱ��
                stop_time = int(time.time())
                #д����
                writePredictData(data_array, data_f, filter_array, num_pool)              
                #��ʾ���ɵ�ע����ѯ���Ƿ�򿪶�Ӧ�ļ���
                tip_text = '������%dע������%d��'%(len(data_f),stop_time-start_time)
                dlg_f = wx.MessageDialog(self, tip_text, 
                                        '�򿪶�Ӧ�ļ��У�',
                                        wx.YES_NO | wx.YES_DEFAULT | wx.ICON_INFORMATION
                                        )
                open_folder = dlg_f.ShowModal()
                dlg_f.Destroy()
                if open_folder==wx.ID_YES:
                    #����Ӧ�ļ���
                    os.startfile('%s'%(int(data_array[0][0])+1))
                else:
                    pass            
        else:
            #������ʾ��
            dlg = wx.MessageDialog(self, 'ѡ�еĺ�������6����', 
                                   '������ѡ�����',
                                   wx.OK | wx.ICON_INFORMATION
                                   )
            dlg.ShowModal()
            dlg.Destroy()              
        event.Skip()

    def OnComboBox1Text(self, event):
        #�ж���ѡ�����ĸ���������������ת���Ǹ�����������ʾ�����������ݺͲ�����
        #ע�⣡event.GetString()�õ���ʵ���ϲ���string����unicode
        global step
        for i in range(0, len(filter_array)):
            if event.GetString().encode('cp936') in filter_array[i][1]:
                step = i+1
                self.Refresh()
                break

        event.Skip()
