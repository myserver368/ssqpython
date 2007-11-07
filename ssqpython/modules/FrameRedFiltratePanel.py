#Boa:Frame:FrameRedFiltratePanel
# -*- coding: cp936 -*-
# otherrrr@gmail.com
# �������ѡ�����

import wx
import os
import time

from DataFileIO import readDataFileToArray
from FilterFileIO import readFilterFileToArray
from PredictFileIO import writePredictData
from BetFileIO import readBetFileToArray
from DataCompute import redOrderCoumpute, dataParaCompute, percentCompute, dataFiltrate

import FrameRedFiltrate

data_array = []  #���ݣ������ʽ��
data_para_array = [] #���ݵ���ز���

redOrder = [] #������밴�ų�������ɴ�С����
redTimes = [] #�����Ӧ���Ŵ���

num_pool = [] #�����

filter_array = [] #���˲���
percent_array = [] #���������İٷֱ�
data_f = [] #���˺����ɵ�����
msg = [] #��ʾ��Ϣ #�����ʵ���Ըĳ�dict

checkBox_list = [] #����ѡ��ť��

def create(parent, choice_num):
    return FrameRedFiltratePanel(parent, choice_num)

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

    def __init__(self, parent, choice_num):
        self._init_ctrls(parent)
        #��������ʾ
        print 'FrameRedFiltratePanel����'
        print '��ѡ��ĺ���',choice_num #��ѡ����
        
        #����λ��
        self.Center()
             
        #��ȡ��������
        global data_array, redOrder, redTimes, bet_array, \
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
        redOrder, redTimes = redOrderCoumpute(data_array)
        #�������������ᵼ�½������Щ�ٶۣ���ÿ��Զ���̴���
        #���㿪�����ݶ�Ӧ�Ĳ�����24���Ӧ����������
        data_para_array = dataParaCompute(data_array, redOrder, bet_array)
        #����ٷֱ�
        percent_array = percentCompute(filter_array, data_para_array)
            
        #����һ�ڳ��ֵĺ����Ϊ��ɫ
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
                         self.checkBox32,self.checkBox32,self.checkBox33
                         ]
        for i in range(1, 6+1):
            checkBox_list[int(data_array[0][i])-1].SetForegroundColour('BLUE')

        #����ѡ��ĺ�����ʾΪ��ѡ״̬
        for i in range(0, len(choice_num)/3):
            checkBox_list[int(choice_num[i*3:i*3+2])-1].SetValue(True)
        
        #����������
        global num_pool
        num_pool = []
        #����ѡ��ĺ����������
        for i in range(0, len(choice_num)/3):
            num_pool.append(int(choice_num[i*3:i*3+2]))
                         
        #���Ҫ��unicode�汾��wxPython�в鿴���֣���Ҫ����unicode���������£�
        #print unicode(filter_array[0][1], 'mbcs')

#-------------------------------------------------------------------------------
#----�������ɰ�ť----

    def OnButtondatabuildButton(self, event): #��ʼ�������ɰ�ť
        '''���ɳ�ʼ���ݣ���ѡ��ȫ������Ϊ1107568�飩'''
        #��Щ�����ڳ�ʼ����ʱ���п��ܱ��Ĺ�
        global num_pool, data_para_array, percent_array
        #��������ԭʼ����
        data_f = []
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

            #�򿪹�����岢�����ݴ����ȥ!!
            ALL_datas = [data_array, redOrder, redTimes, bet_array,
                         data_para_array, filter_array, percent_array,
                         data_f, num_pool]
            _FrameRedFiltrate = FrameRedFiltrate.create(None, ALL_datas)
            _FrameRedFiltrate.Show() 
        
            #�ر�����
            self.Close()  
            
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
#----���ذ�ť----  
    def OnButtonloadButton(self, event): #���ذ�ť
        '''���������ɵ�����'''
        
        #ʹ���ļ��򿪿�
        print '�ļ�ѡ�������'

        #��������ԭʼ����
        data_f = []
            
        #��ʾ�ļ�ѡ���
        dlg = wx.FileDialog(
            self, message="ѡ����Ҫ���ص��ļ�",
            defaultDir=os.getcwd(), 
            defaultFile="",
            #wildcard="", #ͨ��������������ļ����ͣ�
            style=wx.OPEN  | wx.CHANGE_DIR
            #style=wx.OPEN | wx.MULTIPLE | wx.CHANGE_DIR #��Ҫ��ѡ
            )
        
        if dlg.ShowModal()==wx.ID_OK:         
            #��ȡѡ���ļ��е�����
            f = open(dlg.GetPaths()[0], 'r') 
            s = f.readlines()
            f.close()
            #���ݸ�ʽת��
            ##��ʵת����ʱ��Ӧ���ж�һ�������Ƿ�Ϸ�������...
            a = []
            for st in s:
                a.append([int(st[0:2]),int(st[3:5]),int(st[6:8]),\
                          int(st[9:11]),int(st[12:14]),int(st[15:17])])
            #���ݼ���
            for at in a:
                data_f.append(at)
            #��ʾһ��
            print '������%d������������'%len(a)

        #�ر�    
        dlg.Destroy()

        if len(data_f)!=0:
            #�ر�����
            self.Close()
            #�򿪹�����岢�����ݴ����ȥ!!
            ALL_datas = [data_array, redOrder, redTimes, bet_array,
                         data_para_array, filter_array, percent_array,
                         data_f, num_pool]
            _FrameRedFiltrate = FrameRedFiltrate.create(None, ALL_datas)
            _FrameRedFiltrate.Show()              
            
        event.Skip()

#-------------------------------------------------------------------------------
#----����������밴ť----        
    def OnButtoninputButton(self, event): #����������밴ť
        '''һ���������'''
        dlg = wx.TextEntryDialog(
                self, '����֮�����ÿո�ָ�������֤�����Ϊ2λ',
                '������һ�����', 'Python')
        #Ĭ��ֵ
        dlg.SetValue("01 02 03 04 05 06")

        if dlg.ShowModal() == wx.ID_OK:
            #print dlg.GetValue()
            #����������
            global num_pool
            num_pool = []
            #����ѡ��ĺ����������
            for i in range(0, (len(dlg.GetValue())+1)/3):
                num_pool.append(int(dlg.GetValue()[i*3:i*3+2]))
            #��ʾѡ���˶��ٸ���
            msg[1] = '%.2d'%(len(num_pool))
            self.Refresh()
            ##Ӧ���Ƚ����к���״̬��Ϊδѡ��Ҳ����������Σ�
            #����ѡ��ĺ�����ʾΪ��ѡ״̬
            for i in range(0, (len(dlg.GetValue())+1)/3):
                checkBox_list[int(dlg.GetValue()[i*3:i*3+2])-1].SetValue(True)
            
        dlg.Destroy()
        
        event.Skip()

#-------------------------------------------------------------------------------
#----һ�����˰�ť----        
    def OnButtononestepButton(self, event): #һ�����˰�ť
        '''һ���Թ���'''
        global data_f, num_pool,filter_array
        if len(num_pool)>=6:
            continue_f = True #�Ƿ�������й����жϷ�
            if len(num_pool)>20:
                
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
                step = 0
                for i in range(0, len(filter_array)):
                    #+1
                    step = step + 1
                    #��Ϊ���ǡ�
                    filter_array[step-1][2] = '��' + filter_array[step-1][2][2:]
                    #����
                    data_f = dataFiltrate(data_array, data_f, step, filter_array, redOrder, bet_array)
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

#-------------------------------------------------------------------------------
#----�˳���ť----       
    def OnButtonexitButton(self, event): #�˳���ť
        '''�˳��������ѡ�����'''
        #�رմ���
        self.Close()

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
        msg = ['','']
        msg[0] = '��ʼ������ˣ�ѡ�������������ɳ�ʼ���ݡ���ť'
        msg[1] = '%.2d'%(len(num_pool)) #��ʾ������еĺ������
        #���ָ�ʽ
        dc.SetFont(wx.Font(10, wx.NORMAL, wx.NORMAL, wx.NORMAL))
        #������ɫ
        dc.SetTextForeground('BLUE')
        #����λ��
        dc.DrawText(msg[0], 5, 5)
        dc.DrawText(msg[1], 450, 5)
