#Boa:Frame:FrameMain
# -*- coding: cp936 -*-
# otherrrr@gmail.com
# 主面板

import wx
import wx.stc
import wx.lib.scrolledpanel
import wx.lib.dialogs
from wx.lib.wordwrap import wordwrap

from DataFileIO import readDataFileToString, readDataFileToArray, writeStringToDataFile
from BetFileIO import readBetFileToArray

import FrameRedFiltrate
import FrameReport
import FrameBlue
import FrameDownload
import FrameRedShrink

import os
import random

_max_height = 0   #滚动窗口高度
data_string = ''  #数据（字符串格式）
data_array = []   #数据（数组格式）

def create(parent):
    return FrameMain(parent)

[wxID_FRAMEMAIN, wxID_FRAMEMAINNOTEBOOK1, wxID_FRAMEMAINSCROLLEDWINDOW1, 
 wxID_FRAMEMAINSTATUSBAR1, wxID_FRAMEMAINTEXTCTRL1, 
] = [wx.NewId() for _init_ctrls in range(5)]

[wxID_FRAMEMAINMENUDATAITEMSADD, wxID_FRAMEMAINMENUDATAITEMSDEL, 
 wxID_FRAMEMAINMENUDATAITEMSDOWNLOAD, wxID_FRAMEMAINMENUDATAITEMSEXIT, 
] = [wx.NewId() for _init_coll_menuData_Items in range(4)]

[wxID_FRAMEMAINMENUFILTRATEITEMSFBLUE, wxID_FRAMEMAINMENUFILTRATEITEMSFRED, 
 wxID_FRAMEMAINMENUFILTRATEITEMSSRED, 
] = [wx.NewId() for _init_coll_menuFiltrate_Items in range(3)]

[wxID_FRAMEMAINMENUCHECKITEMSCFIXED, wxID_FRAMEMAINMENUCHECKITEMSCPREDICT, 
] = [wx.NewId() for _init_coll_menuCheck_Items in range(2)]

[wxID_FRAMEMAINMENUHELPITEMSABOUT, wxID_FRAMEMAINMENUHELPITEMSFAQ, 
] = [wx.NewId() for _init_coll_menuHelp_Items in range(2)]

[wxID_FRAMEMAINMENUFILTRATEREDITEMSREDBASIC, 
 wxID_FRAMEMAINMENUFILTRATEREDITEMSREDMEDIA, 
] = [wx.NewId() for _init_coll_menuFiltrateRed_Items in range(2)]

[wxID_FRAMEMAINMENURANDOMITEMSDR, wxID_FRAMEMAINMENURANDOMITEMSFR, 
 wxID_FRAMEMAINMENURANDOMITEMSSR, 
] = [wx.NewId() for _init_coll_menuRandom_Items in range(3)]

class FrameMain(wx.Frame):
    def _init_coll_menuCheck_Items(self, parent):
        # generated method, don't edit

        parent.Append(help=u'\u56fa\u5b9a\u6295\u6ce8\u5bf9\u5956',
              id=wxID_FRAMEMAINMENUCHECKITEMSCFIXED, kind=wx.ITEM_NORMAL,
              text=u'\u56fa\u5b9a\u6295\u6ce8\u5bf9\u5956(&F)\tF9')
        parent.Append(help=u'\u9884\u6d4b\u6570\u636e\u5bf9\u5956',
              id=wxID_FRAMEMAINMENUCHECKITEMSCPREDICT, kind=wx.ITEM_NORMAL,
              text=u'\u9884\u6d4b\u6570\u636e\u5bf9\u5956(&P)\tF11')
        self.Bind(wx.EVT_MENU, self.OnMenuCheckItemscfixedMenu,
              id=wxID_FRAMEMAINMENUCHECKITEMSCFIXED)
        self.Bind(wx.EVT_MENU, self.OnMenuCheckItemscpredictMenu,
              id=wxID_FRAMEMAINMENUCHECKITEMSCPREDICT)

    def _init_coll_menuBar1_Menus(self, parent):
        # generated method, don't edit

        parent.Append(menu=self.menuData, title=u'\u6570\u636e(&D)')
        parent.Append(menu=self.menuFiltrate, title=u'\u8fc7\u6ee4(&F)')
        parent.Append(menu=self.menuRandom, title=u'\u673a\u9009(&R)')
        parent.Append(menu=self.menuCheck, title=u'\u5bf9\u5956(&C)')
        parent.Append(menu=self.menuHelp, title=u'\u5e2e\u52a9(&H)')

    def _init_coll_menuData_Items(self, parent):
        # generated method, don't edit

        parent.Append(help=u'\u4e0b\u8f7d\u6570\u636e',
              id=wxID_FRAMEMAINMENUDATAITEMSDOWNLOAD, kind=wx.ITEM_NORMAL,
              text=u'\u4e0b\u8f7d\u6570\u636e(&D)\tF2')
        parent.Append(help=u'\u6dfb\u52a0\u6570\u636e',
              id=wxID_FRAMEMAINMENUDATAITEMSADD, kind=wx.ITEM_NORMAL,
              text=u'\u6dfb\u52a0\u6570\u636e(&A)\tF3')
        parent.Append(help=u'\u5220\u9664\u6570\u636e',
              id=wxID_FRAMEMAINMENUDATAITEMSDEL, kind=wx.ITEM_NORMAL,
              text=u'\u5220\u9664\u6570\u636e(&E)\tCtrl+D')
        parent.Append(help=u'\u9000\u51fa', id=wxID_FRAMEMAINMENUDATAITEMSEXIT,
              kind=wx.ITEM_NORMAL, text=u'\u9000\u51fa(&X)\tCtrl+Q')
        self.Bind(wx.EVT_MENU, self.OnMenuDataItemsdownloadMenu,
              id=wxID_FRAMEMAINMENUDATAITEMSDOWNLOAD)
        self.Bind(wx.EVT_MENU, self.OnMenuDataItemsaddMenu,
              id=wxID_FRAMEMAINMENUDATAITEMSADD)
        self.Bind(wx.EVT_MENU, self.OnMenuDataItemsdelMenu,
              id=wxID_FRAMEMAINMENUDATAITEMSDEL)
        self.Bind(wx.EVT_MENU, self.OnMenuDataItemsexitMenu,
              id=wxID_FRAMEMAINMENUDATAITEMSEXIT)

    def _init_coll_menuFiltrate_Items(self, parent):
        # generated method, don't edit

        parent.Append(help=u'\u7ea2\u7403\u8fc7\u6ee4',
              id=wxID_FRAMEMAINMENUFILTRATEITEMSFRED, kind=wx.ITEM_NORMAL,
              text=u'\u7ea2\u7403\u8fc7\u6ee4(&F)\tF5')
        parent.Append(help=u'\u7ea2\u7403\u7f29\u6c34',
              id=wxID_FRAMEMAINMENUFILTRATEITEMSSRED, kind=wx.ITEM_NORMAL,
              text=u'\u7ea2\u7403\u7f29\u6c34(&S)\tF6')
        parent.Append(help=u'\u84dd\u7403\u63a8\u8350',
              id=wxID_FRAMEMAINMENUFILTRATEITEMSFBLUE, kind=wx.ITEM_NORMAL,
              text=u'\u84dd\u7403\u63a8\u8350(&B)\tF7')
        self.Bind(wx.EVT_MENU, self.OnMenuFiltrateItemsfredMenu,
              id=wxID_FRAMEMAINMENUFILTRATEITEMSFRED)
        self.Bind(wx.EVT_MENU, self.OnMenuFiltrateItemsfblueMenu,
              id=wxID_FRAMEMAINMENUFILTRATEITEMSFBLUE)
        self.Bind(wx.EVT_MENU, self.OnMenuFiltrateItemssredMenu,
              id=wxID_FRAMEMAINMENUFILTRATEITEMSSRED)

    def _init_coll_menuRandom_Items(self, parent):
        # generated method, don't edit

        parent.Append(help=u'\u76f4\u63a5\u673a\u9009',
              id=wxID_FRAMEMAINMENURANDOMITEMSDR, kind=wx.ITEM_NORMAL,
              text=u'\u76f4\u63a5\u673a\u9009(&D)\tF8')
        parent.Append(help=u'\u8fc7\u6ee4\u540e\u6570\u636e\u673a\u9009',
              id=wxID_FRAMEMAINMENURANDOMITEMSFR, kind=wx.ITEM_NORMAL,
              text=u'\u8fc7\u6ee4\u673a\u9009(&F)\tCtrl+A')
        parent.Append(help=u'\u7f29\u6c34\u540e\u6570\u636e\u673a\u9009',
              id=wxID_FRAMEMAINMENURANDOMITEMSSR, kind=wx.ITEM_NORMAL,
              text=u'\u7f29\u6c34\u673a\u9009(&S)\tCtrl+B')
        self.Bind(wx.EVT_MENU, self.OnMenuRandomItemsdrMenu,
              id=wxID_FRAMEMAINMENURANDOMITEMSDR)
        self.Bind(wx.EVT_MENU, self.OnMenuRandomItemsfrMenu,
              id=wxID_FRAMEMAINMENURANDOMITEMSFR)
        self.Bind(wx.EVT_MENU, self.OnMenuRandomItemssrMenu,
              id=wxID_FRAMEMAINMENURANDOMITEMSSR)

    def _init_coll_menuHelp_Items(self, parent):
        # generated method, don't edit

        parent.Append(help=u'\u8bf4\u660e', id=wxID_FRAMEMAINMENUHELPITEMSFAQ,
              kind=wx.ITEM_NORMAL, text=u'\u8bf4\u660e(&R)\tF1')
        parent.Append(help=u'\u5173\u4e8e', id=wxID_FRAMEMAINMENUHELPITEMSABOUT,
              kind=wx.ITEM_NORMAL, text=u'\u5173\u4e8e(&A)\tF12')
        self.Bind(wx.EVT_MENU, self.OnMenuHelpItemsaboutMenu,
              id=wxID_FRAMEMAINMENUHELPITEMSABOUT)
        self.Bind(wx.EVT_MENU, self.OnMenuHelpItemsfaqMenu,
              id=wxID_FRAMEMAINMENUHELPITEMSFAQ)

    def _init_coll_notebook1_Pages(self, parent):
        # generated method, don't edit

        parent.AddPage(imageId=-1, page=self.textCtrl1, select=True,
              text=u'\u6570\u636e\u6587\u672c')
        parent.AddPage(imageId=-1, page=self.scrolledWindow1, select=False,
              text=u'\u5206\u5e03\u56fe')

    def _init_utils(self):
        # generated method, don't edit
        self.menuBar1 = wx.MenuBar()

        self.menuData = wx.Menu(title='')

        self.menuFiltrate = wx.Menu(title='')

        self.menuRandom = wx.Menu(title='')

        self.menuCheck = wx.Menu(title='')

        self.menuHelp = wx.Menu(title='')

        self._init_coll_menuBar1_Menus(self.menuBar1)
        self._init_coll_menuData_Items(self.menuData)
        self._init_coll_menuFiltrate_Items(self.menuFiltrate)
        self._init_coll_menuRandom_Items(self.menuRandom)
        self._init_coll_menuCheck_Items(self.menuCheck)
        self._init_coll_menuHelp_Items(self.menuHelp)

    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAMEMAIN, name='', parent=prnt,
              pos=wx.Point(280, 120), size=wx.Size(620, 415),
              style=wx.DEFAULT_FRAME_STYLE, title=u'\u53cc\u8272\u87d2')
        self._init_utils()
        self.SetClientSize(wx.Size(612, 388))
        self.SetMenuBar(self.menuBar1)
        self.SetIcon(wx.Icon(u'pic/logo.ico',wx.BITMAP_TYPE_ICO))
        self.Bind(wx.EVT_CHAR, self.OnFrameMainChar)

        self.statusBar1 = wx.StatusBar(id=wxID_FRAMEMAINSTATUSBAR1,
              name='statusBar1', parent=self, style=0)
        self.statusBar1.SetStatusText(u'\u53cc\u8272\u87d2')
        self.SetStatusBar(self.statusBar1)

        self.notebook1 = wx.Notebook(id=wxID_FRAMEMAINNOTEBOOK1,
              name='notebook1', parent=self, pos=wx.Point(0, 0),
              size=wx.Size(612, 349), style=0)

        self.textCtrl1 = wx.TextCtrl(id=wxID_FRAMEMAINTEXTCTRL1,
              name='textCtrl1', parent=self.notebook1, pos=wx.Point(0, 0),
              size=wx.Size(604, 322), style=wx.TE_MULTILINE,
              value=u'\u7efc\u5408\u6570\u636e\u6587\u672c\u663e\u793a')

        self.scrolledWindow1 = wx.ScrolledWindow(id=wxID_FRAMEMAINSCROLLEDWINDOW1,
              name='scrolledWindow1', parent=self.notebook1, pos=wx.Point(0, 0),
              size=wx.Size(604, 322),
              style=wx.SUNKEN_BORDER | wx.HSCROLL | wx.VSCROLL)
        self.scrolledWindow1.Bind(wx.EVT_PAINT, self.OnScrolledWindow1Paint)

        self._init_coll_notebook1_Pages(self.notebook1)

    def __init__(self, parent):
        self._init_ctrls(parent)
        
        #启动时显示画面
        image = wx.Image("pic/splash.jpg", wx.BITMAP_TYPE_ANY)
        bmp = image.ConvertToBitmap()
        wx.SplashScreen(bmp, wx.SPLASH_CENTRE_ON_SCREEN | wx.SPLASH_TIMEOUT, 1500, None, -1)
        wx.Yield()         
        
        global _max_height, data_array, data_string

        #文本显示
        data_string = readDataFileToString()
        self.textCtrl1.SetFont(wx.Font(12, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "")) 
        self.textCtrl1.Clear()
        self.textCtrl1.AppendText(data_string)

        #图表显示  
        data_array = readDataFileToArray()
        #_max_height = 15.4*len(data_array) - 190 #显示所有的（问题是拖动时有一些迟钝）
        _max_height = 15.4*100 - 190 #只显示最近100期的
        self.scrolledWindow1.SetScrollbars(1, 1, 890, _max_height, 0, _max_height) #定位于数据最下方

        #设置焦点（主要是为了捕捉键盘输入）
        self.SetFocus()
        
#-------------------------------------------------------------------------------
#----绘图----

    def OnScrolledWindow1Paint(self, event):
        '''绘制分布图'''           
        dc = wx.PaintDC(self.scrolledWindow1)
        self.scrolledWindow1.DoPrepareDC(dc)       
        dc.Clear()

        #分隔线放在最前面画，以免挡住其他的线
        dc.SetPen(wx.Pen("#B3B3B3", 1)) #分隔线
        for i in range(1, 34-1):
            dc.DrawLine(i*16+47, 5, i*16+47, _max_height-20)
        for i in range(0, 100-1):
            dc.DrawLine(49, _max_height-(i*15+39), 840, _max_height-(i*15+39))
        for i in range(1, 16+1):
            dc.DrawLine(i*16+563, 5, i*16+563, _max_height-20)
            
        dc.SetTextForeground('RED') #红色球号
        dc.SetFont(wx.Font(10, wx.NORMAL, wx.NORMAL, wx.NORMAL))    
        for i in range(1, 33+1):
            dc.DrawText('%.2d'%i, i*16+34, _max_height-25)
            
        dc.SetTextForeground('#009900') #期号（绿色）
        for i in range(0, 100):
            dc.DrawText(str(data_array[i][0]), 0, _max_height-(i*15+39)) #左侧
            dc.DrawText(str(data_array[i][0]), 840, _max_height-(i*15+39)) #右侧
        
        dc.SetPen(wx.Pen("RED", 1)) #红色球分布图  
        dc.SetBrush(wx.Brush(wx.RED, wx.SOLID))
        for i in range(0, 100):
            for j in range(1, 6+1):
                for k in range(1, 33+1): 
                    if int(data_array[i][j])==k:
                        dc.DrawRectangle(k*16+35, _max_height-(i*15+35), 10, 10) 
        
        dc.SetPen(wx.Pen("#777777", 1)) #画走势线 灰色 1号球
        for i in range(0, 100-1):
            dc.DrawLine((int(data_array[i][1]))*16+40, _max_height-(i*15+30), (int(data_array[i+1][1]))*16+40, _max_height-((i+1)*15+30))
        
        dc.SetPen(wx.Pen("#990099", 1)) #画走势线 紫色 2号球
        for i in range(0, 100-1):
            dc.DrawLine((int(data_array[i][2]))*16+40, _max_height-(i*15+30), (int(data_array[i+1][2]))*16+40, _max_height-((i+1)*15+30))
        
        dc.SetPen(wx.Pen("#CC9900", 1)) #画走势线 棕色 3号球
        for i in range(0, 100-1):
            dc.DrawLine((int(data_array[i][3]))*16+40, _max_height-(i*15+30), (int(data_array[i+1][3]))*16+40, _max_height-((i+1)*15+30))

        dc.SetPen(wx.Pen("STEEL BLUE", 1)) #画走势线 蓝色 4号球
        for i in range(0, 100-1):
            dc.DrawLine((int(data_array[i][4]))*16+40, _max_height-(i*15+30), (int(data_array[i+1][4]))*16+40, _max_height-((i+1)*15+30))
                
        dc.SetPen(wx.Pen("#6699FF", 1)) #画走势线 青色 5号球
        for i in range(0, 100-1):
            dc.DrawLine((int(data_array[i][5]))*16+40, _max_height-(i*15+30), (int(data_array[i+1][5]))*16+40, _max_height-((i+1)*15+30))
                
        dc.SetPen(wx.Pen("LIME GREEN", 1)) #画走势线 绿色 6号球
        for i in range(0, 100-1):
            dc.DrawLine((int(data_array[i][6]))*16+40, _max_height-(i*15+30), (int(data_array[i+1][6]))*16+40, _max_height-((i+1)*15+30))  
                      
        dc.SetPen(wx.Pen("BLUE", 1)) #蓝色球分布图  
        dc.SetBrush(wx.Brush(wx.BLUE, wx.SOLID))
        for i in range(0, 100):
            for j in range(1, 16+1):
                if int(data_array[i][7])==j:
                    dc.DrawRectangle(j*16+567, _max_height-(i*15+35), 10, 10)    
                         
        dc.SetPen(wx.Pen("CADET BLUE", 1)) #画走势线 蓝色 蓝球
        for i in range(0, 100-1):
            dc.DrawLine((int(data_array[i][7]))*16+572, _max_height-(i*15+30), (int(data_array[i+1][7]))*16+572, _max_height-((i+1)*15+30)) 
            
        dc.SetTextForeground('BLUE') #蓝色球号
        dc.SetFont(wx.Font(10, wx.NORMAL, wx.NORMAL, wx.NORMAL))    
        for i in range(1, 16+1):
            dc.DrawText('%.2d'%i, i*16+565, _max_height-25)            
            
        event.Skip()
        
#-------------------------------------------------------------------------------
#----数据----
    def OnMenuDataItemsdownloadMenu(self, event):
        '''下载数据'''   
        _FrameDownload = FrameDownload.create(None)
        _FrameDownload.Show()

        data_string = readDataFileToString() #重新读取数据
        data_array = readDataFileToArray()
            
        self.textCtrl1.Clear() #刷新数据
        self.textCtrl1.AppendText(data_string)
        self.textCtrl1.ShowPosition(0) 

        #设置焦点
        #self.SetFocus()
        
        event.Skip()
        
    def OnMenuDataItemsaddMenu(self, event):
        '''添加数据'''
        global data_string, data_array
        
        dlg = wx.TextEntryDialog(
                self, '  请输入新的数据，注意保持格式！',
                '添加数据')

        dlg.SetValue("2007001 01,02,03,04,05,06+07")

        if dlg.ShowModal() == wx.ID_OK:
            writeStringToDataFile(dlg.GetValue()+'\n'+data_string)
            
            data_string = readDataFileToString() #重新读取数据
            data_array = readDataFileToArray() 
        
            self.textCtrl1.Clear() #刷新数据
            self.textCtrl1.AppendText(data_string)
            self.textCtrl1.ShowPosition(0)
            
        dlg.Destroy()

        #设置焦点
        self.SetFocus()
        
        event.Skip()
        
    def OnMenuDataItemsdelMenu(self, event):
        '''删除数据'''
        global data_string, data_array
        
        dlg = wx.MessageDialog(self, '  最近一期数据会被删除！\n%s\n'%str(data_string.split('\n')[0]), 
                               '删除数据',
                               wx.OK | wx.CANCEL | wx.ICON_INFORMATION
                               )
        
        if dlg.ShowModal() == wx.ID_OK:
            writeStringToDataFile(data_string[29:]) #每一期的数据为28字节

            data_string = readDataFileToString() #重新读取数据
            data_array = readDataFileToArray() 
        
            self.textCtrl1.Clear() #刷新数据
            self.textCtrl1.AppendText(data_string)
            self.textCtrl1.ShowPosition(0)            
        
        dlg.Destroy()             

        #设置焦点
        self.SetFocus()
        
        event.Skip()
        
    def OnMenuDataItemsexitMenu(self, event):
        '''退出'''
        self.Close()
        
        event.Skip()

#-------------------------------------------------------------------------------
#----过滤----
   
    def OnMenuFiltrateItemsfredMenu(self, event): #红球过滤
        '''红球过滤功能'''
        _FrameRedFiltrate = FrameRedFiltrate.create(None)
        _FrameRedFiltrate.Show() 
                
        event.Skip()  

    def OnMenuFiltrateItemssredMenu(self, event):
        '''红球缩水功能'''
        #数据最新一期的期号
        date = int(data_array[0][0])
        #判断是否存在预测数据，即判断文件夹是否存在
        if '%s'%(date+1) in os.listdir(os.curdir):
            #若有则可以打开红球缩水面板
            _FrameRedShrink = FrameRedShrink.create(None)
            _FrameRedShrink.Show() 
        else :
            #若没有，则提示需要先过滤数据
            dlg = wx.MessageDialog(self, '未找到对应文件夹，请先生成过滤数据！',
                                   '提示',
                                   wx.OK | wx.ICON_INFORMATION
                                   )
            dlg.ShowModal()
            dlg.Destroy()
            
        event.Skip()
        
    def OnMenuFiltrateItemsfblueMenu(self, event): #蓝球推荐
        '''蓝球推荐功能'''
        _FrameBlue = FrameBlue.create(None)
        _FrameBlue.Show() 
        
        event.Skip()

#-------------------------------------------------------------------------------
#----机选----
    def OnMenuRandomItemsdrMenu(self, event):
        '''直接机选'''
        while True: #不做任何判断
            num = []
            for i in range(0, 6): #得到随机数
                num.append('%.2d'%(random.randint(1,33)))
            big = True
            for i in range(0, 5): #判断是不是一个比一个大
                if num[i]>=num[i+1]:
                    big = False
                    break
            if big==True:
                num.append('%.2d'%(random.randint(1,16))) #机选篮球
                break

        str_num = '%s %s %s %s %s %s+%s'%(num[0],num[1],num[2],num[3],num[4],num[5],num[6])
        dlg = wx.MessageDialog(self, '%s'%(str_num), 
                               '直接机选号码如下：',
                               wx.OK | wx.ICON_INFORMATION
                               )
        dlg.ShowModal()
        dlg.Destroy()
        
        event.Skip()

    def OnMenuRandomItemsfrMenu(self, event):
        '''过滤机选'''
        #数据最新一期的期号
        date = int(data_array[0][0])

        #打开过滤数据
        try:
            #文件读取
            f = open('%s/%s预测数据.txt'%(date+1,date+1), 'r')
            s = f.readlines()                     
            f.close()
            #号码显示
            dlg = wx.MessageDialog(self, '%s'%s[random.randint(0,len(s)-1)], 
                                   '过滤机选号码如下：（红）',
                                   wx.OK | wx.ICON_INFORMATION
                                   )
            dlg.ShowModal()
            dlg.Destroy()            
        except:
            #错误提示
            dlg = wx.MessageDialog(self, '未找到对应文件', 
                                   '错误！',
                                   wx.OK | wx.ICON_INFORMATION
                                   )
            dlg.ShowModal()
            dlg.Destroy()
            
        event.Skip()

    def OnMenuRandomItemssrMenu(self, event):
        '''缩水机选'''
        #数据最新一期的期号
        date = int(data_array[0][0])

        #打开缩水数据
        try:
            f = open('%s/%s缩水数据.txt'%(date+1,date+1), 'r')
            s = f.readlines()                     
            f.close()
            #号码显示
            dlg = wx.MessageDialog(self, '%s'%s[random.randint(0,len(s)-1)], 
                                   '缩水机选号码如下：（红）',
                                   wx.OK | wx.ICON_INFORMATION
                                   )
            dlg.ShowModal()
            dlg.Destroy()   
        except:
            #错误提示
            dlg = wx.MessageDialog(self, '未找到对应文件', 
                                   '错误！',
                                   wx.OK | wx.ICON_INFORMATION
                                   )
            dlg.ShowModal()
            dlg.Destroy()
        
        event.Skip()
        
#-------------------------------------------------------------------------------
#----对奖----
        
    def OnMenuCheckItemscfixedMenu(self, event): #固定投注对奖
        '''读取固定投注文件并对奖'''       
        bet_array = readBetFileToArray()
        
        msg = '' #中奖信息
        msg = msg + '固定投注中共有%d注！\n'%(len(bet_array))
        for i in range(0, len(bet_array)):
            r_nums = 0 #红球
            for j in range(0, 6):
                if bet_array[i][j] in data_array[0][1:7]: #前6个
                    r_nums = r_nums + 1
            
            b_nums = 0 #蓝球
            if bet_array[i][6]==data_array[0][7]:
                b_nums = 1
                
            money = '' #金额
            if (r_nums<=3 and b_nums==0): #无
                money = '未中奖'
            elif (r_nums<=2 and b_nums==1): #6等
                money = '5元'
            elif (r_nums==4 and b_nums==0) or (r_nums==3 and b_nums==1): #5等
                money = '10元'
            elif (r_nums==5 and b_nums==0) or (r_nums==4 and b_nums==1): #4等
                money = '200元'
            elif (r_nums==5 and b_nums==1): #3等
                money = '3000元'
            elif (r_nums==6 and b_nums==0): #2等
                money = '二等奖'
            elif (r_nums==6 and b_nums==1): #1等
                money = '一等奖'

            msg = msg+ '第%d注：%d+%d=%s\n'%(i+1,r_nums,b_nums,money)
        
        dlg = wx.MessageDialog(self, msg, 
                               '%s期固定投注对奖'%(data_array[0][0]),
                               wx.OK | wx.ICON_INFORMATION
                               )
        dlg.ShowModal()
        dlg.Destroy()   
             
        #设置焦点
        self.SetFocus()
                        
        event.Skip()

    def OnMenuCheckItemscpredictMenu(self, event): #预测数据对奖
        '''读取预测数据文件并对奖'''
        #读取数据时有些延迟，显示一个画面
        image = wx.Image("pic/splash.jpg", wx.BITMAP_TYPE_ANY)
        bmp = image.ConvertToBitmap()
        wx.SplashScreen(bmp, wx.SPLASH_CENTRE_ON_SCREEN | wx.SPLASH_TIMEOUT, 1200, None, -1)
        wx.Yield()
        
        _FrameReport = FrameReport.create(None)
        _FrameReport.Show()

        event.Skip()
        
#-------------------------------------------------------------------------------
#----帮助----

    def OnMenuHelpItemsfaqMenu(self, event): #使用说明
        '''读取并显示说明文档文件'''
        f = open("说明文档.txt", "r")
        msg = f.read()
        f.close()

        dlg = wx.lib.dialogs.ScrolledMessageDialog(self, msg, "使用说明")
        dlg.ShowModal()
                
        event.Skip()

    def OnMenuHelpItemsaboutMenu(self, event): #关于
        '''提示软件基本信息'''
        info = wx.AboutDialogInfo()
        info.Name = "双色蟒"
        info.Version = "0.9.9"
        info.Description = wordwrap(
            u"双色蟒彩票分析软件，用于双色球彩票数据分析、对奖及投注过滤。 "
            u"\n\n祝您中奖 :)",
            350, wx.ClientDC(self))
        info.WebSite = ("http://code.google.com/p/ssqpython/",      
                        "双色蟒主页")
        info.Developers = [ "otherrrr@gmail.com" ]
        
        wx.AboutBox(info)
        
        event.Skip()        

#-------------------------------------------------------------------------------
#----快捷键----

    def OnFrameMainChar(self, event):
        '''快捷键'''
        #得到键值
        keycode = event.GetKeyCode()
        #print keycode
        
        #F1就显示帮助
        if keycode==wx.WXK_F1:
            self.OnMenuHelpItemsfaqMenu(event)
            
        #F2就下载数据
        if keycode==wx.WXK_F2:
            self.OnMenuDataItemsdownloadMenu(event)
        #F3就添加数据
        if keycode==wx.WXK_F3:
            self.OnMenuDataItemsaddMenu(event)
        #F4就删除数据（20070911取消，和Alt+F4冲突）
        #Ctrl+D就删除数据
        if keycode==4: #键值4
            self.OnMenuDataItemsdelMenu(event)
        
        #F5就红球过滤
        if keycode==wx.WXK_F5:
            self.OnMenuFiltrateItemsfredMenu(event)
        #F6就红球缩水
        if keycode==wx.WXK_F6:
            self.OnMenuFiltrateItemssredMenu(event)
        #F7就篮球推荐
        if keycode==wx.WXK_F7:
            self.OnMenuFiltrateItemsfblueMenu(event)

        #F8就直接机选
        if keycode==wx.WXK_F8:
            self.OnMenuRandomItemsdrMenu(event)            
        #Ctrl+A就过滤机选 
        if keycode==1: #键值1
            self.OnMenuRandomItemsfrMenu(event)            
        #Ctrl+B就缩水机选 
        if keycode==2: #键值2
            self.OnMenuRandomItemssrMenu(event)
            
        #F9就固定投注兑奖
        if keycode==wx.WXK_F9:
            self.OnMenuCheckItemscfixedMenu(event)
        #F11就预测数据兑奖
        if keycode==wx.WXK_F11:
            self.OnMenuCheckItemscpredictMenu(event)
            
        #F12就显示关于
        if keycode==wx.WXK_F12:
            self.OnMenuHelpItemsaboutMenu(event)
            
        #Ctrl+Q就退出（Ctrl+W也退出）
        if keycode==17 or keycode==23: #键值17 和 23
            self.OnMenuDataItemsexitMenu(event)
            
        event.Skip()
        
