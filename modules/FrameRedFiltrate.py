# -*- coding: cp936 -*-
# otherrrr@gmail.com
# 红球过滤面板

import wx
import os

from modules.DataFileIO import readDataFileToArray
from modules.FilterFileIO import readFilterFileToArray
from modules.PredictFileIO import writePredictData
from modules.DataCompute import redOrderCoumput, dataParaCompute,\
                                percentCompute, dataFiltrate

data_array = []  #数据（数组格式）
data_para_array = [] #数据的相关参数

redOrder = [] #红球号码按着出球次数由大到小排列
redTimes = [] #红球对应出号次数

num_pool = [] #号码池

filter_array = [] #过滤参数
percent_array = [] #过滤条件的百分比
data_f = [] #过滤后生成的数据
step = 0 #过滤步骤
msg = ['第几步－－过滤条件名称','说明','当前剩余组数','过滤条件范围','百分比','是否已启用'] #显示信息 #这个其实可以改成dict

def create(parent):
    return FrameRedFiltrate(parent)

[wxID_FRAMEREDFILTRATE, wxID_FRAMEREDFILTRATEBUTTONDATABUILD, 
 wxID_FRAMEREDFILTRATEBUTTONEXIT, wxID_FRAMEREDFILTRATEBUTTONLASTSTEP, 
 wxID_FRAMEREDFILTRATEBUTTONLOWERMINUS, wxID_FRAMEREDFILTRATEBUTTONLOWERPLUS, 
 wxID_FRAMEREDFILTRATEBUTTONNEXTSTEP, wxID_FRAMEREDFILTRATEBUTTONSAVE, 
 wxID_FRAMEREDFILTRATEBUTTONUPPERMINUS, wxID_FRAMEREDFILTRATEBUTTONUPPERPLUS, 
 wxID_FRAMEREDFILTRATEBUTTONUSE, wxID_FRAMEREDFILTRATECHECKBOX01, 
 wxID_FRAMEREDFILTRATECHECKBOX02, wxID_FRAMEREDFILTRATECHECKBOX03, 
 wxID_FRAMEREDFILTRATECHECKBOX04, wxID_FRAMEREDFILTRATECHECKBOX05, 
 wxID_FRAMEREDFILTRATECHECKBOX06, wxID_FRAMEREDFILTRATECHECKBOX07, 
 wxID_FRAMEREDFILTRATECHECKBOX08, wxID_FRAMEREDFILTRATECHECKBOX09, 
 wxID_FRAMEREDFILTRATECHECKBOX10, wxID_FRAMEREDFILTRATECHECKBOX11, 
 wxID_FRAMEREDFILTRATECHECKBOX12, wxID_FRAMEREDFILTRATECHECKBOX13, 
 wxID_FRAMEREDFILTRATECHECKBOX14, wxID_FRAMEREDFILTRATECHECKBOX15, 
 wxID_FRAMEREDFILTRATECHECKBOX16, wxID_FRAMEREDFILTRATECHECKBOX17, 
 wxID_FRAMEREDFILTRATECHECKBOX18, wxID_FRAMEREDFILTRATECHECKBOX19, 
 wxID_FRAMEREDFILTRATECHECKBOX20, wxID_FRAMEREDFILTRATECHECKBOX21, 
 wxID_FRAMEREDFILTRATECHECKBOX22, wxID_FRAMEREDFILTRATECHECKBOX23, 
 wxID_FRAMEREDFILTRATECHECKBOX24, wxID_FRAMEREDFILTRATECHECKBOX25, 
 wxID_FRAMEREDFILTRATECHECKBOX26, wxID_FRAMEREDFILTRATECHECKBOX27, 
 wxID_FRAMEREDFILTRATECHECKBOX28, wxID_FRAMEREDFILTRATECHECKBOX29, 
 wxID_FRAMEREDFILTRATECHECKBOX30, wxID_FRAMEREDFILTRATECHECKBOX31, 
 wxID_FRAMEREDFILTRATECHECKBOX32, wxID_FRAMEREDFILTRATECHECKBOX33, 
 wxID_FRAMEREDFILTRATEPANEL1, wxID_FRAMEREDFILTRATEPANEL2, 
 wxID_FRAMEREDFILTRATERADIOBUTTONALLNO, 
 wxID_FRAMEREDFILTRATERADIOBUTTONALLYES, 
] = [wx.NewId() for _init_ctrls in range(48)]

class FrameRedFiltrate(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAMEREDFILTRATE,
              name=u'FrameAbnormalFiltrate', parent=prnt, pos=wx.Point(388,
              232), size=wx.Size(491, 482), style=wx.DEFAULT_FRAME_STYLE,
              title=u'\u7ea2\u7403\u8fc7\u6ee4')
        self.SetIcon(wx.Icon(u'pic/red.ico',
              wx.BITMAP_TYPE_ICO))
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

        self.radioButtonallyes = wx.RadioButton(id=wxID_FRAMEREDFILTRATERADIOBUTTONALLYES,
              label=u'\u5168\u9009', name=u'radioButtonallyes',
              parent=self.panel2, pos=wx.Point(80, 30), size=wx.Size(48, 14),
              style=0)
        self.radioButtonallyes.SetValue(False)
        self.radioButtonallyes.Bind(wx.EVT_RADIOBUTTON,
              self.OnRadioButtonallyesRadiobutton,
              id=wxID_FRAMEREDFILTRATERADIOBUTTONALLYES)

        self.radioButtonallno = wx.RadioButton(id=wxID_FRAMEREDFILTRATERADIOBUTTONALLNO,
              label=u'\u5168\u4e0d\u9009', name=u'radioButtonallno',
              parent=self.panel2, pos=wx.Point(240, 30), size=wx.Size(56, 14),
              style=0)
        self.radioButtonallno.SetValue(True)
        self.radioButtonallno.Bind(wx.EVT_RADIOBUTTON,
              self.OnRadioButtonallnoRadiobutton,
              id=wxID_FRAMEREDFILTRATERADIOBUTTONALLNO)

        self.checkBox01 = wx.CheckBox(id=wxID_FRAMEREDFILTRATECHECKBOX01,
              label=u'01', name=u'checkBox01', parent=self.panel2,
              pos=wx.Point(60, 60), size=wx.Size(40, 14), style=0)
        self.checkBox01.SetValue(False)
        self.checkBox01.Bind(wx.EVT_CHECKBOX, self.OnCheckBox01Checkbox,
              id=wxID_FRAMEREDFILTRATECHECKBOX01)

        self.checkBox02 = wx.CheckBox(id=wxID_FRAMEREDFILTRATECHECKBOX02,
              label=u'02', name=u'checkBox02', parent=self.panel2,
              pos=wx.Point(120, 60), size=wx.Size(40, 14), style=0)
        self.checkBox02.SetValue(False)
        self.checkBox02.Bind(wx.EVT_CHECKBOX, self.OnCheckBox02Checkbox,
              id=wxID_FRAMEREDFILTRATECHECKBOX02)

        self.checkBox03 = wx.CheckBox(id=wxID_FRAMEREDFILTRATECHECKBOX03,
              label=u'03', name=u'checkBox03', parent=self.panel2,
              pos=wx.Point(180, 60), size=wx.Size(40, 14), style=0)
        self.checkBox03.SetValue(False)
        self.checkBox03.Bind(wx.EVT_CHECKBOX, self.OnCheckBox03Checkbox,
              id=wxID_FRAMEREDFILTRATECHECKBOX03)

        self.checkBox04 = wx.CheckBox(id=wxID_FRAMEREDFILTRATECHECKBOX04,
              label=u'04', name=u'checkBox04', parent=self.panel2,
              pos=wx.Point(240, 60), size=wx.Size(40, 14), style=0)
        self.checkBox04.SetValue(False)
        self.checkBox04.Bind(wx.EVT_CHECKBOX, self.OnCheckBox04Checkbox,
              id=wxID_FRAMEREDFILTRATECHECKBOX04)

        self.checkBox05 = wx.CheckBox(id=wxID_FRAMEREDFILTRATECHECKBOX05,
              label=u'05', name=u'checkBox05', parent=self.panel2,
              pos=wx.Point(300, 60), size=wx.Size(40, 14), style=0)
        self.checkBox05.SetValue(False)
        self.checkBox05.Bind(wx.EVT_CHECKBOX, self.OnCheckBox05Checkbox,
              id=wxID_FRAMEREDFILTRATECHECKBOX05)

        self.checkBox06 = wx.CheckBox(id=wxID_FRAMEREDFILTRATECHECKBOX06,
              label=u'06', name=u'checkBox06', parent=self.panel2,
              pos=wx.Point(30, 90), size=wx.Size(40, 14), style=0)
        self.checkBox06.SetValue(False)
        self.checkBox06.Bind(wx.EVT_CHECKBOX, self.OnCheckBox06Checkbox,
              id=wxID_FRAMEREDFILTRATECHECKBOX06)

        self.checkBox07 = wx.CheckBox(id=wxID_FRAMEREDFILTRATECHECKBOX07,
              label=u'07', name=u'checkBox07', parent=self.panel2,
              pos=wx.Point(90, 90), size=wx.Size(40, 14), style=0)
        self.checkBox07.SetValue(False)
        self.checkBox07.Bind(wx.EVT_CHECKBOX, self.OnCheckBox07Checkbox,
              id=wxID_FRAMEREDFILTRATECHECKBOX07)

        self.checkBox08 = wx.CheckBox(id=wxID_FRAMEREDFILTRATECHECKBOX08,
              label=u'08', name=u'checkBox08', parent=self.panel2,
              pos=wx.Point(150, 90), size=wx.Size(40, 14), style=0)
        self.checkBox08.SetValue(False)
        self.checkBox08.Bind(wx.EVT_CHECKBOX, self.OnCheckBox08Checkbox,
              id=wxID_FRAMEREDFILTRATECHECKBOX08)

        self.checkBox09 = wx.CheckBox(id=wxID_FRAMEREDFILTRATECHECKBOX09,
              label=u'09', name=u'checkBox09', parent=self.panel2,
              pos=wx.Point(210, 90), size=wx.Size(40, 14), style=0)
        self.checkBox09.SetValue(False)
        self.checkBox09.Bind(wx.EVT_CHECKBOX, self.OnCheckBox09Checkbox,
              id=wxID_FRAMEREDFILTRATECHECKBOX09)

        self.checkBox10 = wx.CheckBox(id=wxID_FRAMEREDFILTRATECHECKBOX10,
              label=u'10', name=u'checkBox10', parent=self.panel2,
              pos=wx.Point(270, 90), size=wx.Size(40, 14), style=0)
        self.checkBox10.SetValue(False)
        self.checkBox10.Bind(wx.EVT_CHECKBOX, self.OnCheckBox10Checkbox,
              id=wxID_FRAMEREDFILTRATECHECKBOX10)

        self.checkBox11 = wx.CheckBox(id=wxID_FRAMEREDFILTRATECHECKBOX11,
              label=u'11', name=u'checkBox11', parent=self.panel2,
              pos=wx.Point(330, 90), size=wx.Size(40, 14), style=0)
        self.checkBox11.SetValue(False)
        self.checkBox11.Bind(wx.EVT_CHECKBOX, self.OnCheckBox11Checkbox,
              id=wxID_FRAMEREDFILTRATECHECKBOX11)

        self.checkBox12 = wx.CheckBox(id=wxID_FRAMEREDFILTRATECHECKBOX12,
              label=u'12', name=u'checkBox12', parent=self.panel2,
              pos=wx.Point(60, 120), size=wx.Size(40, 14), style=0)
        self.checkBox12.SetValue(False)
        self.checkBox12.Bind(wx.EVT_CHECKBOX, self.OnCheckBox12Checkbox,
              id=wxID_FRAMEREDFILTRATECHECKBOX12)

        self.checkBox13 = wx.CheckBox(id=wxID_FRAMEREDFILTRATECHECKBOX13,
              label=u'13', name=u'checkBox13', parent=self.panel2,
              pos=wx.Point(120, 120), size=wx.Size(40, 14), style=0)
        self.checkBox13.SetValue(False)
        self.checkBox13.Bind(wx.EVT_CHECKBOX, self.OnCheckBox13Checkbox,
              id=wxID_FRAMEREDFILTRATECHECKBOX13)

        self.checkBox14 = wx.CheckBox(id=wxID_FRAMEREDFILTRATECHECKBOX14,
              label=u'14', name=u'checkBox14', parent=self.panel2,
              pos=wx.Point(180, 120), size=wx.Size(40, 14), style=0)
        self.checkBox14.SetValue(False)
        self.checkBox14.Bind(wx.EVT_CHECKBOX, self.OnCheckBox14Checkbox,
              id=wxID_FRAMEREDFILTRATECHECKBOX14)

        self.checkBox15 = wx.CheckBox(id=wxID_FRAMEREDFILTRATECHECKBOX15,
              label=u'15', name=u'checkBox15', parent=self.panel2,
              pos=wx.Point(240, 120), size=wx.Size(40, 14), style=0)
        self.checkBox15.SetValue(False)
        self.checkBox15.Bind(wx.EVT_CHECKBOX, self.OnCheckBox15Checkbox,
              id=wxID_FRAMEREDFILTRATECHECKBOX15)

        self.checkBox16 = wx.CheckBox(id=wxID_FRAMEREDFILTRATECHECKBOX16,
              label=u'16', name=u'checkBox16', parent=self.panel2,
              pos=wx.Point(300, 120), size=wx.Size(40, 14), style=0)
        self.checkBox16.SetValue(False)
        self.checkBox16.Bind(wx.EVT_CHECKBOX, self.OnCheckBox16Checkbox,
              id=wxID_FRAMEREDFILTRATECHECKBOX16)

        self.checkBox17 = wx.CheckBox(id=wxID_FRAMEREDFILTRATECHECKBOX17,
              label=u'17', name=u'checkBox17', parent=self.panel2,
              pos=wx.Point(30, 150), size=wx.Size(40, 14), style=0)
        self.checkBox17.SetValue(False)
        self.checkBox17.Bind(wx.EVT_CHECKBOX, self.OnCheckBox17Checkbox,
              id=wxID_FRAMEREDFILTRATECHECKBOX17)

        self.checkBox18 = wx.CheckBox(id=wxID_FRAMEREDFILTRATECHECKBOX18,
              label=u'18', name=u'checkBox18', parent=self.panel2,
              pos=wx.Point(90, 150), size=wx.Size(40, 14), style=0)
        self.checkBox18.SetValue(False)
        self.checkBox18.Bind(wx.EVT_CHECKBOX, self.OnCheckBox18Checkbox,
              id=wxID_FRAMEREDFILTRATECHECKBOX18)

        self.checkBox19 = wx.CheckBox(id=wxID_FRAMEREDFILTRATECHECKBOX19,
              label=u'19', name=u'checkBox19', parent=self.panel2,
              pos=wx.Point(150, 150), size=wx.Size(40, 14), style=0)
        self.checkBox19.SetValue(False)
        self.checkBox19.Bind(wx.EVT_CHECKBOX, self.OnCheckBox19Checkbox,
              id=wxID_FRAMEREDFILTRATECHECKBOX19)

        self.checkBox20 = wx.CheckBox(id=wxID_FRAMEREDFILTRATECHECKBOX20,
              label=u'20', name=u'checkBox20', parent=self.panel2,
              pos=wx.Point(210, 150), size=wx.Size(40, 14), style=0)
        self.checkBox20.SetValue(False)
        self.checkBox20.Bind(wx.EVT_CHECKBOX, self.OnCheckBox20Checkbox,
              id=wxID_FRAMEREDFILTRATECHECKBOX20)

        self.checkBox21 = wx.CheckBox(id=wxID_FRAMEREDFILTRATECHECKBOX21,
              label=u'21', name=u'checkBox21', parent=self.panel2,
              pos=wx.Point(270, 150), size=wx.Size(40, 14), style=0)
        self.checkBox21.SetValue(False)
        self.checkBox21.Bind(wx.EVT_CHECKBOX, self.OnCheckBox21Checkbox,
              id=wxID_FRAMEREDFILTRATECHECKBOX21)

        self.checkBox22 = wx.CheckBox(id=wxID_FRAMEREDFILTRATECHECKBOX22,
              label=u'22', name=u'checkBox22', parent=self.panel2,
              pos=wx.Point(330, 150), size=wx.Size(40, 14), style=0)
        self.checkBox22.SetValue(False)
        self.checkBox22.Bind(wx.EVT_CHECKBOX, self.OnCheckBox22Checkbox,
              id=wxID_FRAMEREDFILTRATECHECKBOX22)

        self.checkBox23 = wx.CheckBox(id=wxID_FRAMEREDFILTRATECHECKBOX23,
              label=u'23', name=u'checkBox23', parent=self.panel2,
              pos=wx.Point(60, 180), size=wx.Size(40, 14), style=0)
        self.checkBox23.SetValue(False)
        self.checkBox23.Bind(wx.EVT_CHECKBOX, self.OnCheckBox23Checkbox,
              id=wxID_FRAMEREDFILTRATECHECKBOX23)

        self.checkBox24 = wx.CheckBox(id=wxID_FRAMEREDFILTRATECHECKBOX24,
              label=u'24', name=u'checkBox24', parent=self.panel2,
              pos=wx.Point(120, 180), size=wx.Size(40, 14), style=0)
        self.checkBox24.SetValue(False)
        self.checkBox24.Bind(wx.EVT_CHECKBOX, self.OnCheckBox24Checkbox,
              id=wxID_FRAMEREDFILTRATECHECKBOX24)

        self.checkBox25 = wx.CheckBox(id=wxID_FRAMEREDFILTRATECHECKBOX25,
              label=u'25', name=u'checkBox25', parent=self.panel2,
              pos=wx.Point(180, 180), size=wx.Size(40, 14), style=0)
        self.checkBox25.SetValue(False)
        self.checkBox25.Bind(wx.EVT_CHECKBOX, self.OnCheckBox25Checkbox,
              id=wxID_FRAMEREDFILTRATECHECKBOX25)

        self.checkBox26 = wx.CheckBox(id=wxID_FRAMEREDFILTRATECHECKBOX26,
              label=u'26', name=u'checkBox26', parent=self.panel2,
              pos=wx.Point(240, 180), size=wx.Size(40, 14), style=0)
        self.checkBox26.SetValue(False)
        self.checkBox26.Bind(wx.EVT_CHECKBOX, self.OnCheckBox26Checkbox,
              id=wxID_FRAMEREDFILTRATECHECKBOX26)

        self.checkBox27 = wx.CheckBox(id=wxID_FRAMEREDFILTRATECHECKBOX27,
              label=u'27', name=u'checkBox27', parent=self.panel2,
              pos=wx.Point(300, 180), size=wx.Size(40, 14), style=0)
        self.checkBox27.SetValue(False)
        self.checkBox27.Bind(wx.EVT_CHECKBOX, self.OnCheckBox27Checkbox,
              id=wxID_FRAMEREDFILTRATECHECKBOX27)

        self.checkBox28 = wx.CheckBox(id=wxID_FRAMEREDFILTRATECHECKBOX28,
              label=u'28', name=u'checkBox28', parent=self.panel2,
              pos=wx.Point(30, 210), size=wx.Size(40, 14), style=0)
        self.checkBox28.SetValue(False)
        self.checkBox28.Bind(wx.EVT_CHECKBOX, self.OnCheckBox28Checkbox,
              id=wxID_FRAMEREDFILTRATECHECKBOX28)

        self.checkBox29 = wx.CheckBox(id=wxID_FRAMEREDFILTRATECHECKBOX29,
              label=u'29', name=u'checkBox29', parent=self.panel2,
              pos=wx.Point(90, 210), size=wx.Size(40, 14), style=0)
        self.checkBox29.SetValue(False)
        self.checkBox29.Bind(wx.EVT_CHECKBOX, self.OnCheckBox29Checkbox,
              id=wxID_FRAMEREDFILTRATECHECKBOX29)

        self.checkBox30 = wx.CheckBox(id=wxID_FRAMEREDFILTRATECHECKBOX30,
              label=u'30', name=u'checkBox30', parent=self.panel2,
              pos=wx.Point(150, 210), size=wx.Size(40, 14), style=0)
        self.checkBox30.SetValue(False)
        self.checkBox30.Bind(wx.EVT_CHECKBOX, self.OnCheckBox30Checkbox,
              id=wxID_FRAMEREDFILTRATECHECKBOX30)

        self.checkBox31 = wx.CheckBox(id=wxID_FRAMEREDFILTRATECHECKBOX31,
              label=u'31', name=u'checkBox31', parent=self.panel2,
              pos=wx.Point(210, 210), size=wx.Size(40, 14), style=0)
        self.checkBox31.SetValue(False)
        self.checkBox31.Bind(wx.EVT_CHECKBOX, self.OnCheckBox31Checkbox,
              id=wxID_FRAMEREDFILTRATECHECKBOX31)

        self.checkBox32 = wx.CheckBox(id=wxID_FRAMEREDFILTRATECHECKBOX32,
              label=u'32', name=u'checkBox32', parent=self.panel2,
              pos=wx.Point(270, 210), size=wx.Size(40, 14), style=0)
        self.checkBox32.SetValue(False)
        self.checkBox32.Bind(wx.EVT_CHECKBOX, self.OnCheckBox32Checkbox,
              id=wxID_FRAMEREDFILTRATECHECKBOX32)

        self.checkBox33 = wx.CheckBox(id=wxID_FRAMEREDFILTRATECHECKBOX33,
              label=u'33', name=u'checkBox33', parent=self.panel2,
              pos=wx.Point(330, 210), size=wx.Size(40, 14), style=0)
        self.checkBox33.SetValue(False)
        self.checkBox33.Bind(wx.EVT_CHECKBOX, self.OnCheckBox33Checkbox,
              id=wxID_FRAMEREDFILTRATECHECKBOX33)

    def __init__(self, parent):
        self._init_ctrls(parent)

        #调整位置
        self.Center()
        #读取开奖数据
        global data_array, redOrder, redTimes, \
               data_para_array, filter_array, percent_array
        if len(data_array)==0:
            data_array = readDataFileToArray()
            #计算出球次数并排列球号
            redOrder, redTimes = redOrderCoumput(data_array)
            #计算开奖数据对应的参数（24项－对应过滤条件）
            data_para_array = dataParaCompute(data_array, redOrder)
            #读取过滤条件
            filter_array = readFilterFileToArray()
            #计算百分比
            percent_array = percentCompute(filter_array, data_para_array)
        #按钮显示和隐藏（控制按钮显示部分做的不太理想，太混乱）
        if step==0:
            self.buttondatabuild.Show()
            self.buttonnextstep.Show(False)
            self.buttonlaststep.Show(False)
            self.buttonuse.Show(False)
            self.buttonsave.Show(False)
            self.buttonlowerminus.Show(False)
            self.buttonlowerplus.Show(False)
            self.buttonupperminus.Show(False)
            self.buttonupperplus.Show(False)
        if step==1:
            self.buttonnextstep.Show()
            self.buttonlaststep.Show(False)
            self.buttondatabuild.Show(False)
            self.buttonsave.Show(False)    
            if '否' in filter_array[step-1][2]:
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
            self.panel2.Show(False) #选号面板不显示 
        if step>1 and step<=len(filter_array) and len(filter_array)!=0:
            self.buttonnextstep.Show()
            self.buttonlaststep.Show()           
            self.buttondatabuild.Show(False)
            self.buttonsave.Show(False)
            if '否' in filter_array[step-1][2]:
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
            self.panel2.Show(False) #选号面板不显示
        if step>len(filter_array) and len(filter_array)!=0:
            self.buttonlaststep.Show()
            self.buttonsave.Show()
            self.buttonuse.Show(False)             
            self.buttonnextstep.Show(False)
            self.buttondatabuild.Show(False)
            self.buttonlowerminus.Show(False)
            self.buttonlowerplus.Show(False)
            self.buttonupperminus.Show(False)
            self.buttonupperplus.Show(False)             
            self.panel2.Show(False) #选号面板不显示
            
        #如果要在unicode版本中的wxPython中查看汉字，就要进行unicode操作，如下：
        #print unicode(filter_array[0][1], 'mbcs')    

#-------------------------------------------------------------------------------
#----绘图----

    def OnPanel1Paint(self, event):
        dc = wx.PaintDC(self.panel1)
        #self.panel1.DoPrepareDC(dc)
        #画面清空       
        dc.Clear()
        #文字设定
        global msg
        if step==0:
            msg = ['','','','','','']
            msg[0] = '开始红球过滤，选择号码然后点击“生成初始数据”按钮'
        if step>0 and step<=len(filter_array):
            msg = ['','','','','','']
            msg[0] = '当前为第%.2d/%d步：%s'%(step, len(filter_array), filter_array[step-1][1])
            msg[1] = '（%s）'%(filter_array[step-1][4])
            msg[2] = '当前组数为%d，过滤比为%.4f'%(len(data_f), len(data_f)*100.0/1107568)+'%'
            msg[3] = '当前设置范围为：【%d, %d】'%(int(filter_array[step-1][3].split("-")[0]),int(filter_array[step-1][3].split("-")[1]))
            msg[4] = '已开奖数据中的符合程度为%s'%(percent_array[step-1])+'%'                
            if '是' in filter_array[step-1][2]:
                msg[5] = '是否使用此过滤条件：是'
            else :
                msg[5] = '是否使用此过滤条件：否'            
        if step>len(filter_array):
            msg = ['','','','','','']
            msg[0] = '过滤完毕！'
            msg[1] = '当前组数为%d，过滤比为%.4f'%(len(data_f), len(data_f)*100.0/1107568)+'%'
            msg[2] = '若保存数据请点击“保存过滤后数据”按钮'
        #绘制文字
        dc.SetTextForeground('BLUE')
        dc.SetFont(wx.Font(10, wx.NORMAL, wx.NORMAL, wx.NORMAL))
        for i in range(0, len(msg)):
            dc.DrawText(msg[i], 5, 5+i*16)
        #绘制图形
        
        event.Skip()

#-------------------------------------------------------------------------------
#----数据生成按钮----

    def OnButtondatabuildButton(self, event): #初始数据生成按钮
        '''生成初始数据（若选择全部红球即为1107568组）'''
        global data_f, step, num_pool
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
            dlg = wx.ProgressDialog("初始数据生成中……",
                            "请稍候！",
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
                                    #为了测试便捷之用
                                    #if len(data_f)>10:
                                     #   break
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
            #0+1=1
            step = step + 1
            #按钮显示和隐藏
            self.buttondatabuild.Show(False)
            self.buttonnextstep.Show()
            self.buttonlowerminus.Show()
            self.buttonlowerplus.Show()
            self.buttonupperminus.Show()
            self.buttonupperplus.Show()         
            if '否' in filter_array[step-1][2]:
                self.buttonuse.Show()
            else:
                self.buttonuse.Show(False) 
            #选号面板不显示
            self.panel2.Show(False) 
            #刷新
            self.Refresh()
        #号码池中的号码小于6个
        else:
            #弹出提示框
            dlg = wx.MessageDialog(self, '选中的号码少于6个！', 
                                   'Sorry',
                                   wx.OK | wx.ICON_INFORMATION
                                   )
            dlg.ShowModal()
            dlg.Destroy()   
            
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
        for i in range(1, 33+1):
            num_pool.append(i)
            
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
        
        event.Skip()

    def OnCheckBox01Checkbox(self, event): #01
        '''将1添加到号码池中，或从号码池中删除'''
        global num_pool
        if 1 in num_pool: #看看在不在
            num_pool.remove(1) #删除     
        else:
            num_pool.append(1) #添加
            
        event.Skip()
        
    def OnCheckBox02Checkbox(self, event): #02
        '''将2添加到号码池中，或从号码池中删除'''
        global num_pool
        if 2 in num_pool:
            num_pool.remove(2)      
        else:
            num_pool.append(2)
            
        event.Skip()
        
    def OnCheckBox03Checkbox(self, event):#03
        '''将3添加到号码池中，或从号码池中删除'''
        global num_pool
        if 3 in num_pool:
            num_pool.remove(3)      
        else:
            num_pool.append(3)
            
        event.Skip()

    def OnCheckBox04Checkbox(self, event):#04
        '''将4添加到号码池中，或从号码池中删除'''
        global num_pool
        if 4 in num_pool:
            num_pool.remove(4)      
        else:
            num_pool.append(4)
            
        event.Skip()

    def OnCheckBox05Checkbox(self, event):#05
        '''将5添加到号码池中，或从号码池中删除'''
        global num_pool
        if 5 in num_pool:
            num_pool.remove(5)      
        else:
            num_pool.append(5)
            
        event.Skip()

    def OnCheckBox06Checkbox(self, event):#06
        '''将6添加到号码池中，或从号码池中删除'''
        global num_pool
        if 6 in num_pool:
            num_pool.remove(6)      
        else:
            num_pool.append(6)
            
        event.Skip()
        
    def OnCheckBox07Checkbox(self, event):#07
        '''将7添加到号码池中，或从号码池中删除'''
        global num_pool
        if 7 in num_pool:
            num_pool.remove(7)      
        else:
            num_pool.append(7)
            
        event.Skip()
        
    def OnCheckBox08Checkbox(self, event):#08
        '''将8添加到号码池中，或从号码池中删除'''
        global num_pool
        if 8 in num_pool:
            num_pool.remove(8)      
        else:
            num_pool.append(8)
            
        event.Skip()
        
    def OnCheckBox09Checkbox(self, event):#09
        '''将9添加到号码池中，或从号码池中删除'''
        global num_pool
        if 9 in num_pool:
            num_pool.remove(9)      
        else:
            num_pool.append(9)
            
        event.Skip()

    def OnCheckBox10Checkbox(self, event):#10
        '''将10添加到号码池中，或从号码池中删除'''
        global num_pool
        if 10 in num_pool:
            num_pool.remove(10)      
        else:
            num_pool.append(10)
            
        event.Skip()

    def OnCheckBox11Checkbox(self, event):#11
        '''将11添加到号码池中，或从号码池中删除'''
        global num_pool
        if 11 in num_pool:
            num_pool.remove(11)      
        else:
            num_pool.append(11)
            
        event.Skip()

    def OnCheckBox12Checkbox(self, event):#12
        '''将12添加到号码池中，或从号码池中删除'''
        global num_pool
        if 12 in num_pool:
            num_pool.remove(12)      
        else:
            num_pool.append(12)
            
        event.Skip()

    def OnCheckBox13Checkbox(self, event):#13
        '''将13添加到号码池中，或从号码池中删除'''
        global num_pool
        if 13 in num_pool:
            num_pool.remove(13)      
        else:
            num_pool.append(13)
            
        event.Skip()

    def OnCheckBox14Checkbox(self, event):#14
        '''将14添加到号码池中，或从号码池中删除'''
        global num_pool
        if 14 in num_pool:
            num_pool.remove(14)      
        else:
            num_pool.append(14)
            
        event.Skip()

    def OnCheckBox15Checkbox(self, event):#15
        '''将15添加到号码池中，或从号码池中删除'''
        global num_pool
        if 15 in num_pool:
            num_pool.remove(15)      
        else:
            num_pool.append(15)
            
        event.Skip()

    def OnCheckBox16Checkbox(self, event):#16
        '''将16添加到号码池中，或从号码池中删除'''
        global num_pool
        if 16 in num_pool:
            num_pool.remove(16)      
        else:
            num_pool.append(16)
            
        event.Skip()
        
    def OnCheckBox17Checkbox(self, event):#17
        '''将17添加到号码池中，或从号码池中删除'''
        global num_pool
        if 17 in num_pool:
            num_pool.remove(17)      
        else:
            num_pool.append(17)
            
        event.Skip()

    def OnCheckBox18Checkbox(self, event):#18
        '''将18添加到号码池中，或从号码池中删除'''
        global num_pool
        if 18 in num_pool:
            num_pool.remove(18)      
        else:
            num_pool.append(18)
            
        event.Skip()

    def OnCheckBox19Checkbox(self, event):#19
        '''将19添加到号码池中，或从号码池中删除'''
        global num_pool
        if 19 in num_pool:
            num_pool.remove(19)      
        else:
            num_pool.append(19)
            
        event.Skip()

    def OnCheckBox20Checkbox(self, event):#20
        '''将20添加到号码池中，或从号码池中删除'''
        global num_pool
        if 20 in num_pool:
            num_pool.remove(20)      
        else:
            num_pool.append(20)
            
        event.Skip()

    def OnCheckBox21Checkbox(self, event):#21
        '''将21添加到号码池中，或从号码池中删除'''
        global num_pool
        if 21 in num_pool:
            num_pool.remove(21)      
        else:
            num_pool.append(21)
            
        event.Skip()

    def OnCheckBox22Checkbox(self, event):#22
        '''将22添加到号码池中，或从号码池中删除'''
        global num_pool
        if 22 in num_pool:
            num_pool.remove(22)      
        else:
            num_pool.append(22)
            
        event.Skip()

    def OnCheckBox23Checkbox(self, event):#23
        '''将23添加到号码池中，或从号码池中删除'''
        global num_pool
        if 23 in num_pool:
            num_pool.remove(23)      
        else:
            num_pool.append(23)
            
        event.Skip()

    def OnCheckBox24Checkbox(self, event):#24
        '''将24添加到号码池中，或从号码池中删除'''
        global num_pool
        if 24 in num_pool:
            num_pool.remove(24)      
        else:
            num_pool.append(24)
            
        event.Skip()

    def OnCheckBox25Checkbox(self, event):#25
        '''将25添加到号码池中，或从号码池中删除'''
        global num_pool
        if 25 in num_pool:
            num_pool.remove(25)      
        else:
            num_pool.append(25)
            
        event.Skip()

    def OnCheckBox26Checkbox(self, event):#26
        '''将26添加到号码池中，或从号码池中删除'''
        global num_pool
        if 26 in num_pool:
            num_pool.remove(26)      
        else:
            num_pool.append(26)
            
        event.Skip()

    def OnCheckBox27Checkbox(self, event):#27
        '''将27添加到号码池中，或从号码池中删除'''
        global num_pool
        if 27 in num_pool:
            num_pool.remove(27)      
        else:
            num_pool.append(27)
            
        event.Skip()

    def OnCheckBox28Checkbox(self, event):#28
        '''将28添加到号码池中，或从号码池中删除'''
        global num_pool
        if 28 in num_pool:
            num_pool.remove(28)      
        else:
            num_pool.append(28)
            
        event.Skip()

    def OnCheckBox29Checkbox(self, event):#29
        '''将29添加到号码池中，或从号码池中删除'''
        global num_pool
        if 29 in num_pool:
            num_pool.remove(29)      
        else:
            num_pool.append(29)
            
        event.Skip()

    def OnCheckBox30Checkbox(self, event):#30
        '''将30添加到号码池中，或从号码池中删除'''
        global num_pool
        if 30 in num_pool:
            num_pool.remove(30)      
        else:
            num_pool.append(30)
            
        event.Skip()

    def OnCheckBox31Checkbox(self, event):#31
        '''将31添加到号码池中，或从号码池中删除'''
        global num_pool
        if 31 in num_pool:
            num_pool.remove(31)      
        else:
            num_pool.append(31)
            
        event.Skip()

    def OnCheckBox32Checkbox(self, event):#32
        '''将32添加到号码池中，或从号码池中删除'''
        global num_pool
        if 32 in num_pool:
            num_pool.remove(32)      
        else:
            num_pool.append(32)
            
        event.Skip()
    def OnCheckBox33Checkbox(self, event):#33
        '''将33添加到号码池中，或从号码池中删除'''
        global num_pool
        if 33 in num_pool:
            num_pool.remove(33)      
        else:
            num_pool.append(33)
            
        event.Skip()

        
#-------------------------------------------------------------------------------
#----常规按钮----
    def OnButtonnextstepButton(self, event): #下一步按钮
        '''进行下一步过滤'''
        global step 
        #+1
        if step<=len(filter_array):   
            step = step + 1  
        if step<=len(filter_array): 
            if '否' in filter_array[step-1][2]:
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
        #显示“上一步”按钮
        if step>1:
            self.buttonlaststep.Show()
        #隐藏“下一步”按钮（就是本身）
        if step>len(filter_array):
            self.buttonsave.Show()
            self.buttonnextstep.Show(False)
            self.buttonuse.Show(False) 
            self.buttonlowerminus.Show(False)
            self.buttonlowerplus.Show(False)
            self.buttonupperminus.Show(False)
            self.buttonupperplus.Show(False)              
        #刷新
        self.Refresh() 
                    
        event.Skip()

    def OnButtonlaststepButton(self, event): #上一步按钮
        '''返回上一步过滤'''
        global step
        #-1
        if step>1:
            step = step - 1  
            if '否' in filter_array[step-1][2]:
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
        #显示“下一步”按钮
        if step<=len(filter_array):
            self.buttonnextstep.Show()             
            self.buttonsave.Show(False)       
        #隐藏“上一步”按钮（就是本身）
        if step==1:
            self.buttonlaststep.Show(False)
        #刷新
        self.Refresh() 
        
        event.Skip()
        
    def OnButtonexitButton(self, event): #退出按钮
        '''退出红球过滤面板'''
        #关闭窗口
        self.Close()

        event.Skip()
        
#-------------------------------------------------------------------------------
#----过滤条件控制按钮----
    def OnButtonuseButton(self, event): #使用此条件按钮
        '''确定使用该条件过滤，将“否”改为“是”，
           应用相应条件对数据进行过滤，刷新显示的数据
        '''
        #改为“是”
        global filter_array, data_f
        filter_array[step-1][2] = '是' + filter_array[step-1][2][2:]
        #过滤
        data_f = dataFiltrate(data_array, data_f, step, filter_array, redOrder)
        #隐藏按钮（本身）
        self.buttonuse.Show(False) 
        #隐藏可调整范围按钮 
        self.buttonlowerminus.Show(False)
        self.buttonlowerplus.Show(False)
        self.buttonupperplus.Show(False)
        self.buttonupperminus.Show(False)
        #刷新
        self.Refresh() 
        
        event.Skip()
        
    def OnButtonlowerminusButton(self, event): #范围中的下限值减小
        '''将范围中的下限值减1，并刷新显示数据'''
        global filter_array, percent_array
        #下限减1
        tmp = int(filter_array[step-1][3].split('-')[0])
        if tmp!=0 and tmp<1000:
            tmp = int(filter_array[step-1][3].split('-')[0]) - 1 
        #更新过滤条件
        #注意：因为split之后得到的是str，但是我们需要int，所以我们转换了
        #      但是有时候10会减到9,这样恢复成str的时候就少了1位
        #      也有可能9加到10，str增加1位
        #      因此我们在写新的文件时(****_过滤条件.txt)要重新处理这一部分
        filter_array[step-1][3] = '%d'%(tmp) + '-' + filter_array[step-1][3].split('-')[1]\
                                             + '-' + filter_array[step-1][3].split('-')[2]
        #重新计算百分比
        percent_array = percentCompute(filter_array, data_para_array)
        #刷新
        self.Refresh() 
        
        event.Skip()

    def OnButtonlowerplusButton(self, event): #范围中的下限值增大
        '''将范围中的下限值加1，并刷新显示数据'''
        global filter_array, percent_array
        #下限加1
        tmp = int(filter_array[step-1][3].split('-')[0])
        if tmp<int(filter_array[step-1][3].split('-')[1]):
            tmp = int(filter_array[step-1][3].split('-')[0]) + 1 
        #更新过滤条件
        filter_array[step-1][3] = '%d'%(tmp) + '-' + filter_array[step-1][3].split('-')[1]\
                                             + '-' + filter_array[step-1][3].split('-')[2]     
        #重新计算百分比
        percent_array = percentCompute(filter_array, data_para_array)
        #刷新
        self.Refresh() 
        
        event.Skip()
        
    def OnButtonupperminusButton(self, event): #范围中的上限值减小
        '''将范围中的上限值减1，并刷新显示数据'''
        global filter_array, percent_array
        #上限减1
        tmp = int(filter_array[step-1][3].split('-')[1])
        if tmp>int(filter_array[step-1][3].split('-')[0]):
            tmp = int(filter_array[step-1][3].split('-')[1]) - 1            
        #更新过滤条件
        filter_array[step-1][3] = filter_array[step-1][3].split('-')[0] + '-' + '%d'%(tmp)\
                                             + '-' + filter_array[step-1][3].split('-')[2]                
        #重新计算百分比
        percent_array = percentCompute(filter_array, data_para_array)
        #刷新
        self.Refresh() 
        
        event.Skip()
        
    def OnButtonupperplusButton(self, event): #范围中的上限值增大
        '''将范围中的上限值加1，并刷新显示数据'''
        global filter_array, percent_array
        #上限加1
        tmp = int(filter_array[step-1][3].split('-')[1])
        if tmp<999:
            tmp = int(filter_array[step-1][3].split('-')[1]) + 1           
        #更新过滤条件
        filter_array[step-1][3] = filter_array[step-1][3].split('-')[0] + '-' + '%d'%(tmp)\
                                             + '-' + filter_array[step-1][3].split('-')[2]           
        #重新计算百分比
        percent_array = percentCompute(filter_array, data_para_array)
        #刷新
        self.Refresh() 
        
        event.Skip()
        
    def OnButtonsaveButton(self, event): #保存按钮
        '''保存过滤后数据及应用到的过滤条件''' 
        
        #写数据
        writePredictData(data_array, data_f, filter_array)
        #打开相应文件夹
        os.startfile('%s'%(int(data_array[0][0])+1))
        #关闭窗口
        self.Close()
        
        event.Skip()

