#! usr/bin/python
# -*- coding:utf-8 -*-
#Boa:Frame:FrameRedFiltrate
# otherrrr@gmail.com
# 红球过滤面板

import wx
import wx.lib.ticker
import os
import time
import locale

from DataFileIO import readDataFileToArray
from FilterFileIO import readFilterFileToArray
from PredictFileIO import writePredictData
from BetFileIO import readBetFileToArray
from DataCompute import redOrderCoumpute, dataParaCompute, percentCompute, dataFiltrate

data_array = []  #数据（数组格式）
data_para_array = [] #数据的相关参数

redOrder = [] #红球号码按着出球次数由大到小排列
redTimes = [] #红球对应出号次数

num_pool = [] #号码池

filter_array = [] #过滤参数
percent_array = [] #过滤条件的百分比
data_f = [] #过滤后生成的数据
step = 0 #过滤步骤
msg = [] #显示信息 #这个其实可以改成dict

term = 20 #过滤条件走势图显示的期数，默认显示最近20期走势

#20071123添加“删除组数显示”功能
nums_before = [0, False]#过滤之前的组数/是否显示

#20071126添加
data_f_origin = []#过滤前的数据

#20071225添加
data_f_down = []#被过滤的数据

def create(parent, ALL_datas):
    return FrameRedFiltrate(parent, ALL_datas)

[wxID_FRAMEREDFILTRATE, wxID_FRAMEREDFILTRATEBUTTONEXIT, 
 wxID_FRAMEREDFILTRATEBUTTONLASTSTEP, wxID_FRAMEREDFILTRATEBUTTONLOWERMINUS, 
 wxID_FRAMEREDFILTRATEBUTTONLOWERPLUS, wxID_FRAMEREDFILTRATEBUTTONNEXTSTEP, 
 wxID_FRAMEREDFILTRATEBUTTONSAVE, wxID_FRAMEREDFILTRATEBUTTONSAVEOTHER, 
 wxID_FRAMEREDFILTRATEBUTTONUPPERMINUS, wxID_FRAMEREDFILTRATEBUTTONUPPERPLUS, 
 wxID_FRAMEREDFILTRATEBUTTONUSE, wxID_FRAMEREDFILTRATEPANEL1, 
 wxID_FRAMEREDFILTRATEPANEL3, wxID_FRAMEREDFILTRATERADIOBUTTON10T, 
 wxID_FRAMEREDFILTRATERADIOBUTTON20T, wxID_FRAMEREDFILTRATERADIOBUTTON40T, 
 wxID_FRAMEREDFILTRATETEXTCTRLDATAF, wxID_FRAMEREDFILTRATETICKER1, 
] = [wx.NewId() for _init_ctrls in range(18)]

class FrameRedFiltrate(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAMEREDFILTRATE,
              name=u'FrameAbnormalFiltrate', parent=prnt, pos=wx.Point(388,
              232), size=wx.Size(491, 482), style=wx.DEFAULT_FRAME_STYLE,
              title=u'\u7ea2\u7403\u8fc7\u6ee4')
        self.SetIcon(wx.Icon(u'pic/red.ico',wx.BITMAP_TYPE_ICO))
        self.SetClientSize(wx.Size(483, 455))
        self.Bind(wx.EVT_CLOSE, self.OnFrameRedFiltrateClose)

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

        self.buttonsaveother = wx.Button(id=wxID_FRAMEREDFILTRATEBUTTONSAVEOTHER,
              label=u'\u88ab\u8fc7\u6ee4\u6389\u7684\u6570\u636e',
              name=u'buttonsaveother', parent=self.panel1, pos=wx.Point(304,
              80), size=wx.Size(104, 24), style=0)
        self.buttonsaveother.SetForegroundColour(wx.Colour(0, 128, 128))
        self.buttonsaveother.Bind(wx.EVT_BUTTON, self.OnButtonsaveotherButton,
              id=wxID_FRAMEREDFILTRATEBUTTONSAVEOTHER)

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

        self.ticker1 = wx.lib.ticker.Ticker(direction='rtl',
              id=wxID_FRAMEREDFILTRATETICKER1, name='ticker1',
              parent=self.panel1, pos=wx.Point(105, 423), size=wx.Size(160, 20),
              start=True, style=0, text=u'\u663e\u793a\u6570\u636e')
        self.ticker1.SetToolTipString(u'\u663e\u793a\u5f53\u524d\u6570\u636e')

    def __init__(self, parent, ALL_datas):
        self._init_ctrls(parent)
        #命令行提示
        print (u'FrameRedFiltrate启动').encode(locale.getdefaultlocale()[1])
        #数据定义
        global data_array, redOrder, redTimes, bet_array, data_f,\
               data_para_array, filter_array, percent_array, num_pool
        #数据传入
        [data_array, redOrder, redTimes, bet_array,
         data_para_array, filter_array, percent_array,
         data_f, num_pool] = ALL_datas
        #备份一下data_f作为初始数据，这样就可以减去过滤后的数据，从而得到被过滤数据
        global data_f_origin
        data_f_origin = data_f
        #调整位置
        self.Center()          
        #默认将step归1
        global step
        step = 1
        #按钮及控件的显示和隐藏    
        self.buttonnextstep.Show()
        self.buttonlaststep.Show(False)
        self.buttonsave.Show(False)
        self.buttonsaveother.Show(False)
        if u'否      '==filter_array[step-1][2]:
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
        self.panel3.Show() #走势图面板显示
        self.textCtrldataf.Show(False) #预测数据结果不显示
        #创建条件选择下拉条
        filter_name = [] #所有过滤条件名称列表
        for i in range(0, len(filter_array)):
            filter_name.append(filter_array[i][1].decode('utf-8')) #linux
        self.comboBox1 = wx.ComboBox(choices=filter_name,
              id=-1, name='comboBox1',
              parent=self.panel1, pos=wx.Point(344, 10), size=wx.Size(110, 22),
              style=0, value=u'\u9009\u62e9\u8fc7\u6ee4\u6761\u4ef6')
        #绑定
        self.comboBox1.Bind(wx.EVT_TEXT, self.OnComboBox1Text, id=-1)  
        #测试
        self.UpdateRollingText()
        #如果要在unicode版本的wxPython中查看汉字，就要进行unicode操作，如下：
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
        if step==0: #此项已无用
            msg = ['','']
            msg[0] = u'开始红球过滤，选择号码后点击“生成初始数据”按钮'
            msg[1] = '%.2d'%(len(num_pool)) #显示号码池中的号码个数
        if step>0 and step<=len(filter_array):
            msg = ['','','','','','','']
            msg[0] = u'当前为第%.2d/%d步：%s'%(step, len(filter_array), filter_array[step-1][1].decode('utf-8'))
            msg[1] = u'（%s）'%(filter_array[step-1][4].decode('utf-8'))
            if u'是      '==filter_array[step-1][2] and nums_before[1]==True:
                msg[2] = u'当前组数为%d，过滤比为%.4f'%(len(data_f), len(data_f)*100.0/1107568)+'%'+u'，本步过滤掉%d组'%(nums_before[0]-len(data_f))
            else:
                msg[2] = u'当前组数为%d，过滤比为%.4f'%(len(data_f), len(data_f)*100.0/1107568)+'%'
            msg[3] = u'当前设置范围为：【%d, %d】'%(int(filter_array[step-1][3].split("-")[0]),int(filter_array[step-1][3].split("-")[1]))
            msg[4] = u'已开奖数据中的符合程度为%s'%(percent_array[step-1])+'%'
            msg[5] = u'是否使用此过滤条件：' 
            if u'是      '==filter_array[step-1][2]:
                msg[6] = u'是'
            else :
                msg[6] = u'否'        
        if step>len(filter_array):
            msg = ['','','']
            msg[0] = u'过滤完毕！'
            msg[1] = u'当前组数为%d，过滤比为%.4f'%(len(data_f), len(data_f)*100.0/1107568)+'%'
            msg[2] = u'若保存数据请点击“保存过滤后数据”按钮'
        #绘制文字
        dc.SetFont(wx.Font(10, wx.NORMAL, wx.NORMAL, wx.NORMAL))
        if len(msg)==2: #第1步
            dc.SetTextForeground('BLUE')
            #dc.SetFont(wx.Font(10, wx.NORMAL, wx.NORMAL, wx.NORMAL))
            dc.DrawText(msg[0], 5, 5)
            dc.DrawText(msg[1], 450, 5)
        elif len(msg)==3: #最后1步
            dc.SetTextForeground('BLUE')
            #dc.SetFont(wx.Font(10, wx.NORMAL, wx.NORMAL, wx.NORMAL))            
            for i in range(0, 3):
                dc.DrawText(msg[i], 5, 5+i*16)
        else : #中间步
            dc.SetTextForeground('BLUE')
            #dc.SetFont(wx.Font(10, wx.NORMAL, wx.NORMAL, wx.NORMAL))            
            for i in range(0, 6):
                dc.DrawText(msg[i], 5, 5+i*16)
            if msg[6]==u'否': #红色的“否”
                dc.SetTextForeground('RED')
                dc.DrawText(msg[6], 5+150, 5+5*16)
            if msg[6]==u'是': #绿色的“是”
                dc.SetTextForeground('#009900')
                dc.DrawText(msg[6], 5+150, 5+5*16)

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
            if u'否      '==filter_array[step-1][2]:
                self.buttonuse.Show()
                self.buttonsaveother.Show(False)
                self.buttonlowerminus.Show()
                self.buttonlowerplus.Show()
                self.buttonupperminus.Show()
                self.buttonupperplus.Show()
            else:
                self.buttonuse.Show(False)
                self.buttonsaveother.Show(False)
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
            self.buttonsaveother.Show(False)
            self.buttonnextstep.Show(False)
            self.buttonuse.Show(False) 
            self.buttonlowerminus.Show(False)
            self.buttonlowerplus.Show(False)
            self.buttonupperminus.Show(False)
            self.buttonupperplus.Show(False)
            self.panel3.Show(False) #走势图面板不显示
            self.comboBox1.Show(False) #条件选择下拉条不显示
            self.textCtrldataf.SetFont(wx.Font(10, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "")) #设置一下，就能从头开始显示
            self.textCtrldataf.Show() #预测数据结果显示
            #在显示面板中写入数据
            self.textCtrldataf.Clear()
            '''
            self.textCtrldataf.AppendText('过滤后数据如下：\n')
            for i in range(0, len(data_f)):
                self.textCtrldataf.AppendText('%.2d %.2d %.2d %.2d %.2d %.2d\n'\
                                              %(data_f[i][0],data_f[i][1],data_f[i][2],data_f[i][3],data_f[i][4],data_f[i][5]))
            '''
            #先将文本处理好再一次性添加到显示控件中会比较省时间，比较没有延迟的感觉
            #如果注数过多，后面部分没有显示出来，因为textctrl只能显示64KB的文字
            #可以改成richtext，但是只能在windows下用
            if len(data_f)>200:
                show_txt = u'过滤后数据如下：（最多显示200组）\n'                
                for i in range(0, 200): #只显示200组
                    show_txt = show_txt + u'%.2d %.2d %.2d %.2d %.2d %.2d\n'\
                               %(data_f[i][0],data_f[i][1],data_f[i][2],data_f[i][3],data_f[i][4],data_f[i][5])
            else:
                show_txt = u'过滤后数据如下：\n'  
                for i in range(0, len(data_f)):
                    show_txt = show_txt + u'%.2d %.2d %.2d %.2d %.2d %.2d\n'\
                               %(data_f[i][0],data_f[i][1],data_f[i][2],data_f[i][3],data_f[i][4],data_f[i][5])
            self.textCtrldataf.AppendText(show_txt)
            self.textCtrldataf.SetInsertionPoint(0)
        #不显示过滤掉的组数
        global nums_before
        nums_before[1] = False            
        #刷新
        self.Refresh() 
                    
        event.Skip()

    def OnButtonlaststepButton(self, event): #上一步按钮
        '''返回上一步过滤'''
        global step
        #-1
        if step>1:
            step = step - 1  
            if u'否      '==filter_array[step-1][2]:
                self.buttonuse.Show()
                self.buttonlowerminus.Show()
                self.buttonsaveother.Show(False)                
                self.buttonlowerplus.Show()
                self.buttonupperminus.Show()
                self.buttonupperplus.Show()
            else:
                self.buttonuse.Show(False)
                self.buttonsaveother.Show(False)
                self.buttonlowerminus.Show(False)
                self.buttonlowerplus.Show(False)
                self.buttonupperminus.Show(False)
                self.buttonupperplus.Show(False)                   
        #显示“下一步”按钮
        if step<=len(filter_array):
            self.buttonnextstep.Show()
            self.panel3.Show() #走势图面板显示
            self.comboBox1.Show() #条件选择下拉条显示
            self.buttonsave.Show(False)
            self.buttonsaveother.Show(False)
            self.textCtrldataf.Show(False) #预测数据结果不显示
        #隐藏“上一步”按钮（就是本身）
        if step==1:
            self.buttonlaststep.Show(False)
        #不显示过滤掉的组数
        global nums_before
        nums_before[1] = False
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
        global filter_array, data_f, nums_before
        #改为“是”
        #filter_array[step-1][2] = '是' + filter_array[step-1][2][2:]
	filter_array[step-1][2] = u'是      ' #utf-8 20071203
        #保留过滤前组数，并显示（当按上一步、下一步之后就再不显示了）
        nums_before[0] = len(data_f)
        nums_before[1] = True
        #更新被过滤前数据
        global data_f_origin
        data_f_origin = data_f        
        #过滤（20071225修改）
##        data_f = dataFiltrate(data_array, data_f, step,
##                              filter_array, redOrder, bet_array)
        global data_f_down
        data_f, data_f_down = dataFiltrate(data_array, data_f, step,
                                           filter_array, redOrder, bet_array)
        #隐藏按钮（本身）
        self.buttonuse.Show(False) 
        #隐藏可调整范围按钮 
        self.buttonlowerminus.Show(False)
        self.buttonlowerplus.Show(False)
        self.buttonupperplus.Show(False)
        self.buttonupperminus.Show(False)
        #显示保存被过滤掉的数据按钮
        self.buttonsaveother.Show(True)
        #刷新
        self.Refresh() 
        #更新滚动显示
        self.UpdateRollingText()
        
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
        writePredictData(data_array, data_f, filter_array, num_pool)
        #打开相应文件夹
        #os.startfile('%s'%(int(data_array[0][0])+1))
        #关闭窗口
        #还是一直显示着比较好一点，你说呢？
        #self.Close() 
        
        #20071126修改保存后的显示方式
        #弹出提示框
        dlg = wx.MessageDialog(self, u'过滤后数据及过滤条件已保存到%d目录下'\
        %(int(data_array[0][0])+1), 
                               u'提示：',
                               wx.OK | wx.ICON_INFORMATION
                               )
        dlg.ShowModal()
        dlg.Destroy()         
        
        event.Skip()

    def OnButtonsaveotherButton(self, event): #保存被过滤掉的数据
        '''保存被过滤掉的数据'''
        #求得被过滤掉的数据
##        #方法3
##        #还是很慢
##        data_f_rest = []
##        data_f_rest = [i for i in data_f_origin if i not in data_f]
##        #方法1
##        #想简单点，但是出现list objects are unhashable错误
##        data_f_test = list(set(data_f_origin)-set(data_f))
##        #方法2
##        #当组数特别多的时候，很慢！！
##        for dt in data_f_origin:
##            if dt not in data_f:
##                data_f_rest.append(dt)
        #显示文件选择框
        dlg = wx.FileDialog(
            self, message=u"保存被过滤掉的数据",
            defaultFile="",
            style=wx.SAVE
            )
        #设置保存的默认文件名
        dlg.SetFilename(u'被滤数据.txt')
        #点击“打开”按钮
        if dlg.ShowModal()==wx.ID_OK:
            #写入数据
	    if wx.Platform == '__WXMSW__':
                if '.txt' in dlg.GetPath().encode('mbcs'): #20071225
                    f = open(dlg.GetPath().encode('mbcs'), 'w')
                else:
                    f = open(dlg.GetPath().encode('mbcs')+'.txt', 'w')
	    else:
		f = open(dlg.GetPath(), 'w')
            for i in range(0, len(data_f_down)):
                f.write('%.2d %.2d %.2d %.2d %.2d %.2d\n'\
                        %(data_f_down[i][0],data_f_down[i][1],data_f_down[i][2],\
                          data_f_down[i][3],data_f_down[i][4],data_f_down[i][5]))
            f.close()
            #本身不显示
            self.buttonsaveother.Show(False)
            
        #关闭    
        dlg.Destroy()
        
        event.Skip()
#-------------------------------------------------------------------------------
#----过滤条件走势图显示----
    def OnPanel3Paint(self, event): #绘制走势图
        dc = wx.PaintDC(self.panel3)     
        dc.Clear()
        
        #名称除去后面的空格
        name_no_blank = filter_array[step-1][1].split(' ')[0].decode('utf-8') 
        #最近10期的
        if term==10:
            #标题
            dc.SetTextForeground('FIREBRICK') #耐火砖色  
            dc.DrawText(u'%s走势图（最近10期）'%name_no_blank, 10, 10)
            #画坐标线
            dc.SetPen(wx.Pen('BLUE', 1))
            dc.DrawLine(20,30,20,280) #竖线
            dc.DrawLine(10,270,420,270) #横线
            dc.DrawLine(20,30,15,35) #竖线的箭头
            dc.DrawLine(20,30,25,35)
            dc.DrawLine(420,270,415,265) #横线的箭头
            dc.DrawLine(420,270,415,275)
            #得到最近10期的值的列表
            value_10 = []
            for i in range(0, 10):
                value_10.append(data_para_array[i][name_no_blank.encode('utf-8')])
            #算出平均值
            value_a = 0.0
            for i in range(0, 10):
                value_a = value_a + value_10[i]
            value_a = value_a*1.0/10
            #最大值＝平均值×4
            value_max = int(value_a*4)
            #画10个长方形
            dc.SetPen(wx.Pen('MEDIUM VIOLET RED', 1)) #设置外边框颜色
            dc.SetBrush(wx.Brush('#FFD5D5', wx.SOLID)) #设置内部填充颜色
            for i in range(0, 10):
                #参数依次为：左上角横坐标、左上角纵坐标、宽、高
                dc.DrawRectangle(40+i*36, 270-240*value_10[9-i]/value_max, 20, 240*value_10[9-i]/value_max)
            #在长方形顶端，标注具体数字
            dc.SetTextForeground('ORANGE RED') 
            for i in range(0, 10):
                dc.DrawText('%s'%value_10[9-i], 40+i*36, (270-240*value_10[9-i]/value_max)-15)
            #在坐标轴下方标注具体的期数
            dc.SetTextForeground('ORCHID')
            dc.SetFont(wx.Font(7, wx.SWISS, wx.NORMAL, wx.NORMAL))  
            for i in range(0, 10):
                dc.DrawRotatedText('%s'%data_array[9-i][0], 40+i*36-8, 275, 15) #旋转文字
            #画出10期均值线
            dc.SetPen(wx.Pen('DARK OLIVE GREEN', 1, wx.DOT_DASH))
            dc.DrawLine(20,270-240*value_a/value_max,420,270-240*value_a/value_max)
            #在10期均值线上标注具体的数字
            dc.SetTextForeground('DARK OLIVE GREEN')
            dc.SetFont(wx.Font(8, wx.NORMAL, wx.NORMAL, wx.NORMAL))
            dc.DrawText(u'10期均值%s'%value_a, 360, 270-240*value_a/value_max-15)
        #最近20期的
        if term==20:
            #标题
            dc.SetTextForeground('FIREBRICK') #耐火砖色  
            dc.DrawText(u'%s走势图（最近20期）'%name_no_blank, 10, 10)
            #画坐标线
            dc.SetPen(wx.Pen('BLUE', 1))
            dc.DrawLine(20,30,20,280) #竖线
            dc.DrawLine(10,270,420,270) #横线
            dc.DrawLine(20,30,15,35) #竖线的箭头
            dc.DrawLine(20,30,25,35)
            dc.DrawLine(420,270,415,265) #横线的箭头
            dc.DrawLine(420,270,415,275)
            #得到最近20期的值的列表
            value_20 = []
            for i in range(0, 20):
                value_20.append(data_para_array[i][name_no_blank.encode('utf-8')])
            #算出平均值
            value_a = 0.0
            for i in range(0, 20):
                value_a = value_a + value_20[i]
            value_a = value_a*1.0/20
            #最大值＝平均值×4
            value_max = int(value_a*4) #加int是因为float会导致长方形底部有时无法接触到x轴
            #画20个长方形
            dc.SetPen(wx.Pen('MEDIUM VIOLET RED', 1)) #设置外边框颜色
            dc.SetBrush(wx.Brush('#FFD5D5', wx.SOLID )) #设置内部填充颜色
            for i in range(0, 20):
            #参数依次为：左上角横坐标、左上角纵坐标、宽、高
                dc.DrawRectangle(30+i*18, 270-240*value_20[19-i]/value_max, 10, 240*value_20[19-i]/value_max)
            #在长方形顶端，标注具体数字
            dc.SetTextForeground('ORANGE RED') 
            for i in range(0, 20):
                dc.DrawText('%s'%value_20[19-i], 30+i*18, (270-240*value_20[19-i]/value_max)-15)
            #在坐标轴下方标注具体的期数
            dc.SetTextForeground('ORCHID')
            dc.SetFont(wx.Font(7, wx.SWISS, wx.NORMAL, wx.NORMAL))  
            for i in range(3, 20, 4): #隔4期显示，要不太挤了
                dc.DrawText('%s'%data_array[19-i][0], 30+i*18-4, 275)
            #画出20期均值线
            dc.SetPen(wx.Pen('DARK OLIVE GREEN', 1, wx.DOT_DASH))
            dc.DrawLine(20,270-240*value_a/value_max,420,270-240*value_a/value_max)
            #在20期均值线上标注具体的数字
            dc.SetTextForeground('DARK OLIVE GREEN')
            dc.SetFont(wx.Font(8, wx.NORMAL, wx.NORMAL, wx.NORMAL))
            dc.DrawText(u'20期均值%s'%value_a, 360, 270-240*value_a/value_max-15)
        #最近40期的
        if term==40:
            #标题
            dc.SetTextForeground('FIREBRICK') #耐火砖色  
            dc.DrawText(u'%s走势图（最近40期）'%name_no_blank, 10, 10)
            #画坐标线
            dc.SetPen(wx.Pen('BLUE', 1))
            dc.DrawLine(20,30,20,280) #竖线
            dc.DrawLine(10,270,420,270) #横线
            dc.DrawLine(20,30,15,35) #竖线的箭头
            dc.DrawLine(20,30,25,35)
            dc.DrawLine(420,270,415,265) #横线的箭头
            dc.DrawLine(420,270,415,275)
            #得到最近40期的值的列表
            value_40 = []
            for i in range(0, 40):
                value_40.append(data_para_array[i][name_no_blank.encode('utf-8')])
            #算出平均值
            value_a = 0.0
            for i in range(0, 40):
                value_a = value_a + value_40[i]
            value_a = value_a*1.0/40
            #最大值＝平均值×4
            value_max = int(value_a*4) #加int是因为float会导致长方形底部有时无法接触到x轴
            #画40个长方形
            dc.SetPen(wx.Pen('MEDIUM VIOLET RED', 1)) #设置外边框颜色
            dc.SetBrush(wx.Brush('#FFD5D5', wx.SOLID )) #设置内部填充颜色
            for i in range(0, 40):
            #参数依次为：左上角横坐标、左上角纵坐标、宽、高
                dc.DrawRectangle(30+i*9, 270-240*value_40[39-i]/value_max, 5, 240*value_40[39-i]/value_max)
            #在长方形顶端，标注具体数字
            dc.SetTextForeground('ORANGE RED') 
            for i in range(0, 40):
                dc.DrawText('%s'%value_40[39-i], 30+i*9, (270-240*value_40[39-i]/value_max)-15)
            #在坐标轴下方标注具体的期数
            dc.SetTextForeground('ORCHID')
            dc.SetFont(wx.Font(7, wx.SWISS, wx.NORMAL, wx.NORMAL))  
            for i in range(3, 40, 8): #隔8期显示，要不太挤了
                dc.DrawText('%s'%data_array[19-i][0], 30+i*18-4, 275)
            #画出40期均值线
            dc.SetPen(wx.Pen('DARK OLIVE GREEN', 1, wx.DOT_DASH))
            dc.DrawLine(20,270-240*value_a/value_max,420,270-240*value_a/value_max)
            #在40期均值线上标注具体的数字
            dc.SetTextForeground('DARK OLIVE GREEN')
            dc.SetFont(wx.Font(8, wx.NORMAL, wx.NORMAL, wx.NORMAL))
            dc.DrawText(u'40期均值%s'%value_a, 360, 270-240*value_a/value_max-15)
        
        event.Skip()

    def OnRadioButton10tRadiobutton(self, event): #显示10期走势图
        global term
        term = 10
        self.Refresh() #刷新，这样就所改即所得了
        event.Skip()

    def OnRadioButton20tRadiobutton(self, event): #显示20期走势图
        global term
        term = 20    
        self.Refresh() #刷新
        event.Skip()
        
    def OnRadioButton40tRadiobutton(self, event): #显示40期走势图
        global term
        term = 40    
        self.Refresh() #刷新
        event.Skip()
        
    def OnComboBox1Text(self, event):
        #判断是选择了哪个过滤条件，并跳转到那个条件（即显示该条件的数据和参数）
        #注意！event.GetString()得到的实际上不是string而是unicode
        global step
        for i in range(0, len(filter_array)):
            if event.GetString().encode('utf-8') in filter_array[i][1]:
                step = i+1
                self.Refresh()
                break
        #还要控制一下按钮的显示（20071108）
        if step==1: #上一步/下一步按钮
            self.buttonnextstep.Show()
            self.buttonlaststep.Show(False)
        else:
            self.buttonnextstep.Show()
            self.buttonlaststep.Show()              
        if u'否      '==filter_array[step-1][2]: #条件使用/范围调整按钮
            self.buttonuse.Show()
            self.buttonlowerminus.Show()
            self.buttonlowerplus.Show()
            self.buttonupperminus.Show()
            self.buttonupperplus.Show()
            self.buttonsaveother.Show(False) #20080107
        else:
            self.buttonuse.Show(False)
            self.buttonsaveother.Show(False)
            self.buttonlowerminus.Show(False)
            self.buttonlowerplus.Show(False)
            self.buttonupperplus.Show(False)
            self.buttonupperminus.Show(False)
        #不显示过滤掉的组数
        global nums_before
        nums_before[1] = False
        
        event.Skip()

    def UpdateRollingText(self):
        #更新滚动文字显示
        s_tmp = ''
        if len(data_f)>100: #应该包括所有的，但是太慢了
            for i in range(0, 100): 
                a_tmp = data_f[i]
                s_tmp = s_tmp +'%.2d %.2d %.2d %.2d %.2d %.2d          '\
                                %(a_tmp[0],a_tmp[1],a_tmp[2],a_tmp[3],a_tmp[4],a_tmp[5])
        else:
            for i in range(0, len(data_f)): 
                a_tmp = data_f[i]
                s_tmp = s_tmp +'%.2d %.2d %.2d %.2d %.2d %.2d          '\
                                %(a_tmp[0],a_tmp[1],a_tmp[2],a_tmp[3],a_tmp[4],a_tmp[5])
        self.ticker1.SetText(s_tmp)

    def OnFrameRedFiltrateClose(self, event):
        #关闭窗口时要做的事（比如关掉进程等等）
        
        event.Skip()

