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

num_pool = [] #�����

filter_array = [] #���˲���
percent_array = [] #���������İٷֱ�
data_f = [] #���˺����ɵ�����
step = 0 #���˲���
msg = [] #��ʾ��Ϣ #�����ʵ���Ըĳ�dict

term = 20 #������������ͼ��ʾ��������Ĭ����ʾ���20������

def create(parent, ALL_datas):
    return FrameRedFiltrate(parent, ALL_datas)

[wxID_FRAMEREDFILTRATE, wxID_FRAMEREDFILTRATEBUTTONEXIT, 
 wxID_FRAMEREDFILTRATEBUTTONLASTSTEP, wxID_FRAMEREDFILTRATEBUTTONLOWERMINUS, 
 wxID_FRAMEREDFILTRATEBUTTONLOWERPLUS, wxID_FRAMEREDFILTRATEBUTTONNEXTSTEP, 
 wxID_FRAMEREDFILTRATEBUTTONSAVE, wxID_FRAMEREDFILTRATEBUTTONUPPERMINUS, 
 wxID_FRAMEREDFILTRATEBUTTONUPPERPLUS, wxID_FRAMEREDFILTRATEBUTTONUSE, 
 wxID_FRAMEREDFILTRATEPANEL1, wxID_FRAMEREDFILTRATEPANEL3, 
 wxID_FRAMEREDFILTRATERADIOBUTTON10T, wxID_FRAMEREDFILTRATERADIOBUTTON20T, 
 wxID_FRAMEREDFILTRATERADIOBUTTON40T, wxID_FRAMEREDFILTRATETEXTCTRLDATAF, 
] = [wx.NewId() for _init_ctrls in range(16)]

class FrameRedFiltrate(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAMEREDFILTRATE,
              name=u'FrameAbnormalFiltrate', parent=prnt, pos=wx.Point(388,
              232), size=wx.Size(491, 489), style=wx.DEFAULT_FRAME_STYLE,
              title=u'\u7ea2\u7403\u8fc7\u6ee4')
        self.SetIcon(wx.Icon(u'pic/red.ico',wx.BITMAP_TYPE_ICO))
        self.SetClientSize(wx.Size(483, 455))

        self.panel1 = wx.Panel(id=wxID_FRAMEREDFILTRATEPANEL1, name='panel1',
              parent=self, pos=wx.Point(0, 0), size=wx.Size(483, 455),
              style=wx.TAB_TRAVERSAL)
        self.panel1.Bind(wx.EVT_PAINT, self.OnPanel1Paint)

        self.buttonexit = wx.Button(id=wxID_FRAMEREDFILTRATEBUTTONEXIT,
              label=u'\u9000\u51fa(&X)', name=u'buttonexit', parent=self.panel1,
              pos=wx.Point(20, 420), size=wx.Size(60, 24), style=0)
        self.buttonexit.Bind(wx.EVT_BUTTON, self.OnButtonexitButton,
              id=wxID_FRAMEREDFILTRATEBUTTONEXIT)

        self.buttonnextstep = wx.Button(id=wxID_FRAMEREDFILTRATEBUTTONNEXTSTEP,
              label=u'\u4e0b\u4e00\u6b65(&N)', name=u'buttonnextstep',
              parent=self.panel1, pos=wx.Point(380, 420), size=wx.Size(75, 23),
              style=0)
        self.buttonnextstep.Bind(wx.EVT_BUTTON, self.OnButtonnextstepButton,
              id=wxID_FRAMEREDFILTRATEBUTTONNEXTSTEP)

        self.buttonlaststep = wx.Button(id=wxID_FRAMEREDFILTRATEBUTTONLASTSTEP,
              label=u'\u4e0a\u4e00\u6b65(&L)', name=u'buttonlaststep',
              parent=self.panel1, pos=wx.Point(280, 420), size=wx.Size(75, 24),
              style=0)
        self.buttonlaststep.Bind(wx.EVT_BUTTON, self.OnButtonlaststepButton,
              id=wxID_FRAMEREDFILTRATEBUTTONLASTSTEP)

        self.buttonuse = wx.Button(id=wxID_FRAMEREDFILTRATEBUTTONUSE,
              label=u'\u4f7f\u7528\u6b64\u6761\u4ef6(&U)', name=u'buttonuse',
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

    def __init__(self, parent, ALL_datas):
        self._init_ctrls(parent)
        #��������ʾ
        print 'FrameRedFiltrate����'
        #���ݶ���
        global data_array, redOrder, redTimes, bet_array, data_f,\
               data_para_array, filter_array, percent_array, num_pool
        #���ݴ���
        [data_array, redOrder, redTimes, bet_array,
         data_para_array, filter_array, percent_array,
         data_f, num_pool] = ALL_datas
        #����λ��
        self.Center()        
        
        #Ĭ�Ͻ�step��1
        global step
        step = 1
        #��ť���ؼ�����ʾ������    
        self.buttonnextstep.Show()
        self.buttonlaststep.Show(False)
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
        self.panel3.Show() #����ͼ�����ʾ
        self.textCtrldataf.Show(False) #Ԥ�����ݽ������ʾ

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
        #���Ҫ��unicode�汾��wxPython�в鿴���֣���Ҫ����unicode���������£�
        #print unicode(filter_array[0][1], 'mbcs')
        
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
        data_f = dataFiltrate(data_array, data_f, step, filter_array, redOrder, bet_array)
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
