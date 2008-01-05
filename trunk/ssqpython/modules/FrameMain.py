#! usr/bin/python
# -*- coding:utf-8 -*-
#Boa:Frame:FrameMain
# otherrrr@gmail.com
# 主面板

import wx
import wx.stc
import wx.lib.scrolledpanel
import wx.lib.dialogs
from wx.lib.wordwrap import wordwrap

from DataFileIO import readDataFileToString, readDataFileToArray, writeStringToDataFile
from BetFileIO import readBetFileToArray
from DataCompute import dataParaCompute, redOrderCoumpute
from FileIO import DataParaFileRead, DataParaFileWrite, XmlWrite

import FrameRedFiltratePanel
import FrameReport
import FrameBlue
import FrameDownload
import FrameRedShrink
import FrameOptional
import FrameReplace
import FrameSafe
import FrameCompare

import os
import random
import time
import locale

_max_height = 0   #滚动窗口高度(int)
data_string = ''  #数据(str)
data_array = []   #数据(list)
choice_num = ''   #选择的号码(str)

bet_array = [] #固定投注号码(list)
data_para_array = [] #数据的相关参数(list(dic))
redOrder = [] #红球号码按着出球次数由大到小排列(list)
redTimes = [] #红球对应出号次数(list)

def create(parent):
    return FrameMain(parent)

[wxID_FRAMEMAIN, wxID_FRAMEMAINNOTEBOOK1, wxID_FRAMEMAINPANEL1, 
 wxID_FRAMEMAINSCROLLEDWINDOW1, wxID_FRAMEMAINSTATUSBAR1, 
 wxID_FRAMEMAINTEXTCTRL1, 
] = [wx.NewId() for _init_ctrls in range(6)]

[wxID_FRAMEMAINMENUDATAITEMSADD, wxID_FRAMEMAINMENUDATAITEMSDEL, 
 wxID_FRAMEMAINMENUDATAITEMSDOWNLOAD, wxID_FRAMEMAINMENUDATAITEMSEXIT, 
] = [wx.NewId() for _init_coll_menuData_Items in range(4)]

[wxID_FRAMEMAINMENUFILTRATEITEMSCOMPARE, wxID_FRAMEMAINMENUFILTRATEITEMSFBLUE, 
 wxID_FRAMEMAINMENUFILTRATEITEMSFRED, wxID_FRAMEMAINMENUFILTRATEITEMSOPTIONAL, 
 wxID_FRAMEMAINMENUFILTRATEITEMSREPLACE, wxID_FRAMEMAINMENUFILTRATEITEMSSAFE, 
 wxID_FRAMEMAINMENUFILTRATEITEMSSRED, 
] = [wx.NewId() for _init_coll_menuFiltrate_Items in range(7)]

[wxID_FRAMEMAINMENUCHECKITEMSCCOMPLEX, wxID_FRAMEMAINMENUCHECKITEMSCFIXED, 
 wxID_FRAMEMAINMENUCHECKITEMSCPREDICT, wxID_FRAMEMAINMENUCHECKITEMSCSELF, 
] = [wx.NewId() for _init_coll_menuCheck_Items in range(4)]

[wxID_FRAMEMAINMENUHELPITEMSABOUT, wxID_FRAMEMAINMENUHELPITEMSFAQ, 
] = [wx.NewId() for _init_coll_menuHelp_Items in range(2)]

[wxID_FRAMEMAINMENUFILTRATEREDITEMSREDBASIC, 
 wxID_FRAMEMAINMENUFILTRATEREDITEMSREDMEDIA, 
] = [wx.NewId() for _init_coll_menuFiltrateRed_Items in range(2)]

[wxID_FRAMEMAINMENURANDOMITEMSDR, wxID_FRAMEMAINMENURANDOMITEMSER, 
 wxID_FRAMEMAINMENURANDOMITEMSFR, wxID_FRAMEMAINMENURANDOMITEMSSR, 
] = [wx.NewId() for _init_coll_menuRandom_Items in range(4)]

class FrameMain(wx.Frame):
    def _init_coll_menuCheck_Items(self, parent):
        # generated method, don't edit

        parent.Append(help=u'\u56fa\u5b9a\u6295\u6ce8\u5bf9\u5956',
              id=wxID_FRAMEMAINMENUCHECKITEMSCFIXED, kind=wx.ITEM_NORMAL,
              text=u'\u56fa\u5b9a\u6295\u6ce8\u5bf9\u5956(&F)\tF9')
        parent.Append(help=u'\u9884\u6d4b\u6570\u636e\u5bf9\u5956',
              id=wxID_FRAMEMAINMENUCHECKITEMSCPREDICT, kind=wx.ITEM_NORMAL,
              text=u'\u9884\u6d4b\u6570\u636e\u5bf9\u5956(&P)\tF11')
        parent.Append(help=u'\u590d\u5f0f\u6295\u6ce8\u5151\u5956',
              id=wxID_FRAMEMAINMENUCHECKITEMSCCOMPLEX, kind=wx.ITEM_NORMAL,
              text=u'\u590d\u5f0f\u6295\u6ce8\u5151\u5956(&J)\tCtrl+J')
        parent.Append(help=u'\u81ea\u9009\u6570\u636e\u5151\u5956',
              id=wxID_FRAMEMAINMENUCHECKITEMSCSELF, kind=wx.ITEM_NORMAL,
              text=u'\u81ea\u9009\u6570\u636e\u5151\u5956(&K)\tCtrl+K')
        self.Bind(wx.EVT_MENU, self.OnMenuCheckItemscfixedMenu,
              id=wxID_FRAMEMAINMENUCHECKITEMSCFIXED)
        self.Bind(wx.EVT_MENU, self.OnMenuCheckItemscpredictMenu,
              id=wxID_FRAMEMAINMENUCHECKITEMSCPREDICT)
        self.Bind(wx.EVT_MENU, self.OnMenuCheckItemscselfMenu,
              id=wxID_FRAMEMAINMENUCHECKITEMSCSELF)
        self.Bind(wx.EVT_MENU, self.OnMenuCheckItemsccomplexMenu,
              id=wxID_FRAMEMAINMENUCHECKITEMSCCOMPLEX)

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
        parent.Append(help=u'\u9000\u51fa\u7a0b\u5e8f',
              id=wxID_FRAMEMAINMENUDATAITEMSEXIT, kind=wx.ITEM_NORMAL,
              text=u'\u9000\u51fa\u7a0b\u5e8f(&X)\tCtrl+Q')
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
        parent.Append(help=u'\u7a33\u80c6\u7f29\u6c34',
              id=wxID_FRAMEMAINMENUFILTRATEITEMSSAFE, kind=wx.ITEM_NORMAL,
              text=u'\u7a33\u80c6\u7f29\u6c34(&D)\tCtrl+U')
        parent.Append(help=u'\u81ea\u9009\u8fc7\u6ee4',
              id=wxID_FRAMEMAINMENUFILTRATEITEMSOPTIONAL, kind=wx.ITEM_NORMAL,
              text=u'\u81ea\u9009\u8fc7\u6ee4(&O)\tCtrl+O')
        parent.Append(help=u'\u6761\u4ef6\u66ff\u6362',
              id=wxID_FRAMEMAINMENUFILTRATEITEMSREPLACE, kind=wx.ITEM_NORMAL,
              text=u'\u6761\u4ef6\u66ff\u6362(&C)\tCtrl+T')
        parent.Append(help=u'\u67e5\u770b\u88ab\u6ee4\u6570\u636e',
              id=wxID_FRAMEMAINMENUFILTRATEITEMSCOMPARE, kind=wx.ITEM_NORMAL,
              text=u'\u67e5\u770b\u88ab\u6ee4\u6570\u636e(&G)\tCtrl+G')
        self.Bind(wx.EVT_MENU, self.OnMenuFiltrateItemsfredMenu,
              id=wxID_FRAMEMAINMENUFILTRATEITEMSFRED)
        self.Bind(wx.EVT_MENU, self.OnMenuFiltrateItemsfblueMenu,
              id=wxID_FRAMEMAINMENUFILTRATEITEMSFBLUE)
        self.Bind(wx.EVT_MENU, self.OnMenuFiltrateItemssredMenu,
              id=wxID_FRAMEMAINMENUFILTRATEITEMSSRED)
        self.Bind(wx.EVT_MENU, self.OnMenuFiltrateItemsoptionalMenu,
              id=wxID_FRAMEMAINMENUFILTRATEITEMSOPTIONAL)
        self.Bind(wx.EVT_MENU, self.OnMenuFiltrateItemsreplaceMenu,
              id=wxID_FRAMEMAINMENUFILTRATEITEMSREPLACE)
        self.Bind(wx.EVT_MENU, self.OnMenuFiltrateItemssafeMenu,
              id=wxID_FRAMEMAINMENUFILTRATEITEMSSAFE)
        self.Bind(wx.EVT_MENU, self.OnMenuFiltrateItemscompareMenu,
              id=wxID_FRAMEMAINMENUFILTRATEITEMSCOMPARE)

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
        parent.Append(help=u'\u81ea\u9009\u673a\u9009',
              id=wxID_FRAMEMAINMENURANDOMITEMSER, kind=wx.ITEM_NORMAL,
              text=u'\u81ea\u9009\u673a\u9009(&E)\tCtrl+C')
        self.Bind(wx.EVT_MENU, self.OnMenuRandomItemsdrMenu,
              id=wxID_FRAMEMAINMENURANDOMITEMSDR)
        self.Bind(wx.EVT_MENU, self.OnMenuRandomItemsfrMenu,
              id=wxID_FRAMEMAINMENURANDOMITEMSFR)
        self.Bind(wx.EVT_MENU, self.OnMenuRandomItemssrMenu,
              id=wxID_FRAMEMAINMENURANDOMITEMSSR)
        self.Bind(wx.EVT_MENU, self.OnMenuRandomItemserMenu,
              id=wxID_FRAMEMAINMENURANDOMITEMSER)

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

        parent.AddPage(imageId=-1, page=self.textCtrl1, select=False,
              text=u'\u6570\u636e\u6587\u672c')
        parent.AddPage(imageId=-1, page=self.scrolledWindow1, select=False,
              text=u'\u5206\u5e03\u56fe')
        parent.AddPage(imageId=-1, page=self.panel1, select=True, text=u'Flash')

    def _init_sizers(self):
        # generated method, don't edit
        self.boxSizer1 = wx.BoxSizer(orient=wx.VERTICAL)

        self.panel1.SetSizer(self.boxSizer1)

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
              style=wx.DEFAULT_FRAME_STYLE, title=u'\u53cc\u8272\u87d2 1.0.6')
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

        self.panel1 = wx.Panel(id=wxID_FRAMEMAINPANEL1, name='panel1',
              parent=self.notebook1, pos=wx.Point(0, 0), size=wx.Size(604, 322),
              style=wx.TAB_TRAVERSAL)

        self._init_coll_notebook1_Pages(self.notebook1)

        self._init_sizers()

    def __init__(self, parent):
        self._init_ctrls(parent)
        t1 = time.time()
        #命令行提示
        print (u'FrameMain启动').encode(locale.getdefaultlocale()[1])
        #启动时显示画面
        image = wx.Image("pic/splash.jpg", wx.BITMAP_TYPE_ANY)
        bmp = image.ConvertToBitmap()
        wx.SplashScreen(bmp, wx.SPLASH_CENTRE_ON_SCREEN | wx.SPLASH_TIMEOUT, 800, None, -1)
        wx.Yield()         
        global data_string
        #文本显示
        data_string = readDataFileToString()
        self.textCtrl1.SetFont(wx.Font(12, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "")) 
        self.textCtrl1.Clear()
        self.textCtrl1.AppendText(data_string)
        self.textCtrl1.SetInsertionPoint(0)
        #图表显示
        global _max_height, data_array 
        data_array = readDataFileToArray()
        #_max_height = 15.4*len(data_array) - 190 #显示所有的（问题是拖动时有一些迟钝）
        _max_height = 15.4*100 - 190 #只显示最近100期的
        self.scrolledWindow1.SetScrollbars(1, 1, 890, _max_height, 0, _max_height) #定位于数据最下方
        #读取固定投注
        global bet_array
        bet_array = readBetFileToArray()
        #计算出球次数并排列球号
        global redOrder, redTimes
        redOrder, redTimes = redOrderCoumpute(data_array)
        #生成参数并读取参数
        global data_para_array
        ##1、首先判断“全部参数”是否存在
        if os.path.exists(u"data/全部参数.txt"):
            print (u'“全部参数.txt”已存在').encode(locale.getdefaultlocale()[1])
            ##2、再判断是否为最新一期
            f = open(u'data/全部参数.txt', 'r')
            ts = f.read(7)
            f.close()
            if ts==data_array[0][0]:
                #直接读取文件
                print (u'“全部参数.txt”为最新').encode(locale.getdefaultlocale()[1])
                data_para_array = DataParaFileRead(u"data/全部参数.txt")
            else:
                #添加参数
                print (u'“全部参数.txt”不是最新(%s->%s)'%(data_array[0][0],ts)).encode(locale.getdefaultlocale()[1])
                #计算开奖数据对应的参数
                data_para_array = dataParaCompute(data_array, redOrder, bet_array)
                #写入文件
                DataParaFileWrite(data_para_array, data_array)
        else:
            print (u'未找到“全部参数.txt”，正在生成……').encode(locale.getdefaultlocale()[1])
            #计算开奖数据对应的参数（与过滤条件项数相同）
            data_para_array = dataParaCompute(data_array, redOrder, bet_array)
            #写入文件
            DataParaFileWrite(data_para_array, data_array)

        #Flash显示
        if wx.Platform == '__WXMSW__': #必须是Windows平台
            #创建Flash显示会调用到的xml[耗时0.015s]
            XmlWrite(u"data/近期数据.xml",data_array,data_para_array,redOrder,redTimes)            
            from wx.lib.flashwin import FlashWindow
            #创建一个Flash窗口
            self.panel1.flash = FlashWindow(self.panel1, style=wx.SUNKEN_BORDER)
            #屏蔽Flash的右键
            self.panel1.flash.menu = False
            #self.panel1.flash.LoadMovie(0, 'file://' + os.path.abspath('pic/flash.swf'))
            #像上面这样加file就不行
            self.panel1.flash.LoadMovie(0, os.path.abspath(u'pic/flash.swf'))
            #添加sizer
            self.boxSizer1.Add(self.panel1.flash, proportion=1, flag=wx.EXPAND)
            #强迫sizer重新定位及刷新大小
            self.boxSizer1.SetDimension(0, 0, 604, 322) 
            #调用Flash的FSCommand
            from wx.lib.flashwin import EVT_FSCommand
            #将Flash ocx的消息事件绑定到getFlashVars函数上
            self.Bind(EVT_FSCommand, self.getFlashVars)
        else: #__WXGTK__(linux ubuntu 7.10)
            #根据google analytics的分析(20071010)
            #98%的访问者是windows用户
            #97%的访问者使用Flash
            #92%的访问者来自中国
	    self.notebook1.ChangeSelection(0) #将首选项改为文本数据显示
            wx.StaticText(self.panel1, -1, u"对不起，您的系统不支持Flash！", pos=(20, 34))
        #设置焦点（主要是为了捕捉键盘输入）
        self.SetFocus()
        #显示启动所需时间
        t2 = time.time()
        print (u'本次启动耗时%.2f秒'%(t2-t1)).encode(locale.getdefaultlocale()[1])
        #正常0.765s更新数据2.765s
        #测试
        
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
        global data_string, data_array

        #打开下载面板
        _FrameDownload = FrameDownload.create(None)
        _FrameDownload.Show()
        #重新读取数据
        data_string = readDataFileToString() 
        data_array = readDataFileToArray()
        #刷新“数据文本”中的显示  
        self.textCtrl1.Clear() 
        self.textCtrl1.AppendText(data_string)
        self.textCtrl1.ShowPosition(0)
        if wx.Platform == '__WXMSW__':
            #重新创建Flash显示会调用到的xml
            XmlWrite(u"data/近期数据.xml",data_array,data_para_array,redOrder,redTimes)
            #刷新Flash
            self.panel1.flash.GotoFrame(1) #跳到第1帧
            self.panel1.flash.Play() #播放
        #设置焦点
        #self.SetFocus()
        #打开这个窗口就跑到主界面后面去了，估计原因是因为上面更新了textCtrl1
        
        event.Skip()
        
    def OnMenuDataItemsaddMenu(self, event):
        '''添加数据'''
        global data_string, data_array
        
        dlg = wx.TextEntryDialog(
                self, u'  请输入新的数据，注意保持格式！',
                u'添加数据')

        #dlg.SetValue("2007001 01,02,03,04,05,06+07")
        dlg.SetValue("%s 01,02,03,04,05,06+07"%str(int(data_array[0][0])+1))

        if dlg.ShowModal() == wx.ID_OK:
            writeStringToDataFile(dlg.GetValue()+'\n'+data_string)
            #显示一下
            print (u'添加了一组数据').encode(locale.getdefaultlocale()[1])
            #重新读取数据
            data_string = readDataFileToString() 
            data_array = readDataFileToArray() 
            #刷新数据
            self.textCtrl1.Clear() 
            self.textCtrl1.AppendText(data_string.decode('utf-8'))            
            self.textCtrl1.ShowPosition(0)
            if wx.Platform == '__WXMSW__':            
                #重新创建Flash显示会调用到的xml
                XmlWrite(u"data/近期数据.xml",data_array,data_para_array,redOrder,redTimes)
                #刷新Flash
                self.panel1.flash.GotoFrame(1) #跳到第1帧
                self.panel1.flash.Play() #播放            
        dlg.Destroy()

        #设置焦点
        self.SetFocus()
        
        event.Skip()
        
    def OnMenuDataItemsdelMenu(self, event):
        '''删除数据'''
        global data_string, data_array
        
        dlg = wx.MessageDialog(self, u'  最近一期数据会被删除！\n%s\n'%str(data_string.split('\n')[0]), 
                               u'删除数据',
                               wx.OK | wx.CANCEL | wx.ICON_INFORMATION
                               )
        
        if dlg.ShowModal() == wx.ID_OK:
            #显示一下
            print (u'删除了一组数据').encode(locale.getdefaultlocale()[1])
            #win 28 #linux 有时会是 29
            writeStringToDataFile(data_string[len(data_string.split('\n')[0])+1:])
            #重新读取数据
            data_string = readDataFileToString() 
            data_array = readDataFileToArray() 
            #刷新数据
            self.textCtrl1.Clear() 
            self.textCtrl1.AppendText(data_string)
            #self.textCtrl1.ShowPosition(0) #win
            self.textCtrl1.SetInsertionPoint(0) #linux
            if wx.Platform == '__WXMSW__':            
                #重新创建Flash显示会调用到的xml
                XmlWrite(u"data/近期数据.xml",data_array,data_para_array,redOrder,redTimes)
                #刷新Flash
                self.panel1.flash.GotoFrame(1) #跳到第1帧
                self.panel1.flash.Play() #播放
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
   
    def OnMenuFiltrateItemsfredMenu(self, event): #红球过滤选好面板
        '''红球过滤功能选号面板'''
        _FrameRedFiltratePanel = FrameRedFiltratePanel.create(None, choice_num, data_array, bet_array, data_para_array, redOrder, redTimes)
        _FrameRedFiltratePanel.Show() 
                
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
            dlg = wx.MessageDialog(self, u'未找到对应文件夹，请先生成过滤数据！',
                                   u'提示',
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

    def OnMenuFiltrateItemssafeMenu(self, event): #稳胆缩水
        '''稳胆缩水功能'''

        #数据最新一期的期号
        date = int(data_array[0][0])
        #判断是否存在预测数据，即判断文件夹是否存在
        if '%s'%(date+1) in os.listdir(os.curdir):
            #若有则可以打开稳胆缩水面板
            _FrameSafe = FrameSafe.create(None)
            _FrameSafe.Show()
        else :
            #若没有，则提示需要先过滤数据
            dlg = wx.MessageDialog(self, u'未找到对应文件夹，请先生成过滤数据！',
                                   u'提示',
                                   wx.OK | wx.ICON_INFORMATION
                                   )
            dlg.ShowModal()
            dlg.Destroy()
            
        event.Skip()
        
    def OnMenuFiltrateItemsoptionalMenu(self, event): #自选过滤
        '''自选过滤功能'''
        _FrameOptional = FrameOptional.create(None)
        _FrameOptional.Show()
        
        event.Skip()
        
    def OnMenuFiltrateItemsreplaceMenu(self, event): #条件替换
        '''过滤条件替换功能'''
        _FrameReplace = FrameReplace.create(None)
        _FrameReplace.Show()

        event.Skip()

    def OnMenuFiltrateItemscompareMenu(self, event): #查看被滤数据
        '''查看被滤数据功能'''
        _FrameCompare = FrameCompare.create(None)
        _FrameCompare.Show()
        
        event.Skip()
        
#-------------------------------------------------------------------------------
#----机选----
    def OnMenuRandomItemsdrMenu(self, event):
        '''直接机选'''
        while True: 
            num = []
            for i in range(0, 6): #得到随机数
                num.append('%.2d'%(random.randint(1,33)))
            big = True
            for i in range(0, 5): #判断是不是一个比一个大
                if num[i]>=num[i+1]:
                    big = False
                    break
            #简单的判断，否则会出一些很不合理的值，比如01 02 03 04 05 06+BB
            option = True
            if int(num[0])>19: #1.一号位在1－19之间
                option = False
            if int(num[1])>24: #2.二号位在2－24之间
                option = False
            if int(num[2])>28: #3.三号位在3－28之间
                option = False
            if int(num[3])<5 or int(num[3])>31: #4.四号位在5－31之间
                option = False
            if int(num[4])<7: #5.五号位在7－32之间
                option = False
            if int(num[5])<11: #6.六号位在11－33之间
                option = False
            #机选篮球
            if big==True and option==True:
                num.append('%.2d'%(random.randint(1,16))) 
                break

        str_num = '%s %s %s %s %s %s+%s'%(num[0],num[1],num[2],num[3],num[4],num[5],num[6])
        print str_num #命令行显示一下
        dlg = wx.MessageDialog(self, '%s'%(str_num), 
                               u'直接机选号码如下：',
                               wx.OK | wx.ICON_INFORMATION
                               )
        dlg.ShowModal()
        dlg.Destroy()

        #设置焦点
        self.SetFocus()        
        
        event.Skip()

    def OnMenuRandomItemsfrMenu(self, event):
        '''过滤机选'''
        #数据最新一期的期号
        date = int(data_array[0][0])
        #打开过滤数据
        try:
            #文件读取
            f = open(u'%d/%d预测数据.txt'%(date+1,date+1), 'r')
            s = f.readlines()                     
            f.close()
            #号码显示
            num_t = random.randint(0,len(s)-1) #随机数
            print s[num_t].split('\n')[0], num_t #命令行显示一下
            dlg = wx.MessageDialog(self, '%s'%s[num_t], 
                                   u'过滤机选号码如下：（红）',
                                   wx.OK | wx.ICON_INFORMATION
                                   )
            dlg.ShowModal()
            dlg.Destroy()
            #设置焦点
            self.SetFocus()              
        except:
            #错误提示
            dlg = wx.MessageDialog(self, u'未找到对应文件或对应文件为空\n(%s目录下%s预测数据.txt)'%(date+1,date+1),  
                                   u'错误！',
                                   wx.OK | wx.ICON_INFORMATION
                                   )
            dlg.ShowModal()
            dlg.Destroy()
            #设置焦点
            self.SetFocus()
            
        event.Skip()

    def OnMenuRandomItemssrMenu(self, event):
        '''缩水机选'''
        #数据最新一期的期号
        date = int(data_array[0][0])

        #打开缩水数据
        try:
            f = open(u'%s/%s缩水数据.txt'%(date+1,date+1), 'r')
            s = f.readlines()                     
            f.close()
            #号码显示
            num_t = random.randint(0,len(s)-1) #随机数
            print s[num_t].split('\n')[0], num_t #命令行显示一下                 
            dlg = wx.MessageDialog(self, '%s'%s[num_t], 
                                   u'缩水机选号码如下：（红）',
                                   wx.OK | wx.ICON_INFORMATION
                                   )
            dlg.ShowModal()
            dlg.Destroy()
            #设置焦点
            self.SetFocus()             
        except:
            #错误提示
            dlg = wx.MessageDialog(self, u'未找到对应文件或对应文件为空\n(%s目录下%s缩水数据.txt)'%(date+1,date+1),  
                                   u'错误！',
                                   wx.OK | wx.ICON_INFORMATION
                                   )
            dlg.ShowModal()
            dlg.Destroy()
            #设置焦点
            self.SetFocus()              
        
        event.Skip()
        
    def OnMenuRandomItemserMenu(self, event):
        '''自选机选'''
        #数据最新一期的期号
        date = int(data_array[0][0])

        #打开缩水数据
        try:
            f = open(u'%s/%s自选数据.txt'%(date+1,date+1), 'r')
            s = f.readlines()                     
            f.close()
            #号码显示
            num_t = random.randint(0,len(s)-1) #随机数
            print s[num_t].split('\n')[0], num_t #命令行显示一下                 
            dlg = wx.MessageDialog(self, '%s'%s[num_t], 
                                   u'自选机选号码如下：（红）',
                                   wx.OK | wx.ICON_INFORMATION
                                   )
            dlg.ShowModal()
            dlg.Destroy()
            #设置焦点
            self.SetFocus()             
        except:
            #错误提示
            dlg = wx.MessageDialog(self, u'未找到对应文件或对应文件为空\n(%s目录下%s自选数据.txt)'%(date+1,date+1), 
                                   u'错误！',
                                   wx.OK | wx.ICON_INFORMATION
                                   )
            dlg.ShowModal()
            dlg.Destroy()
            #设置焦点
            self.SetFocus()             
        
        event.Skip()

        
#-------------------------------------------------------------------------------
#----对奖----
        
    def OnMenuCheckItemscfixedMenu(self, event): #固定投注对奖
        '''读取固定投注文件并对奖'''
        #因已在主程序启动时读取，故不需要再次读取
        #bet_array = readBetFileToArray()
        
        msg = u'' #中奖信息
        msg = msg + u'固定投注中共有%d注！\n'%(len(bet_array))
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
                money = u'未中奖'
            elif (r_nums<=2 and b_nums==1): #6等
                money = u'5元'
            elif (r_nums==4 and b_nums==0) or (r_nums==3 and b_nums==1): #5等
                money = u'10元'
            elif (r_nums==5 and b_nums==0) or (r_nums==4 and b_nums==1): #4等
                money = u'200元'
            elif (r_nums==5 and b_nums==1): #3等
                money = u'3000元'
            elif (r_nums==6 and b_nums==0): #2等
                money = u'二等奖'
            elif (r_nums==6 and b_nums==1): #1等
                money = u'一等奖'

            msg = msg+ u'第%d注：%d+%d=%s\n'%(i+1,r_nums,b_nums,money)
        
        dlg = wx.MessageDialog(self, msg, 
                               u'%s期固定投注对奖'%(data_array[0][0]),
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
        
    def OnMenuCheckItemsccomplexMenu(self, event): #复式投注兑奖
        '''复式投注兑奖功能'''
        #投注号码
        bet_nums = ''
        #红球号码
        red_nums = []
        #篮球号码
        blue_nums = []
        #所有可能的注数
        bets_array = []
        #号码输入
        dlg = wx.TextEntryDialog(
                self, u'  请注意同色号码之间为逗号，红蓝号码之间为加号！',
                u'输入复式投注号码')

        dlg.SetValue("01,02,03,04,05,06,07,08,09,10+01,02")
        #得到号码
        if dlg.ShowModal() == wx.ID_OK:
            bet_nums = dlg.GetValue()
            #print type(dlg.GetValue()) #unicode
        dlg.Destroy()
        #保证不小于01,02,03,04,05,06+07
        if len(bet_nums)>=20:
            #得到数组
            red_nums = bet_nums.split("+")[0].split(",")
            blue_nums = bet_nums.split("+")[1].split(",")
            #把数组里的空数据丢掉（这个有可能是用户多输入逗号所造成的）
            #（未完成）
            #生成所有可能的注数
            for bt in blue_nums:
                pos1 = 0
                for t1 in red_nums[pos1:-5]:
                    pos2 = pos1 + 1
                    for t2 in red_nums[pos2:-4]:
                        pos3 = pos2 + 1
                        for t3 in red_nums[pos3:-3]:
                            pos4 = pos3 + 1
                            for t4 in red_nums[pos4:-2]:
                                pos5 = pos4 + 1
                                for t5 in red_nums[pos5:-1]:
                                    pos6 = pos5 + 1
                                    for t6 in red_nums[pos6:]:
                                        bets_array.append([t1,t2,t3,t4,t5,t6,bt])
                                    pos5 = pos5 + 1
                                pos4 = pos4 + 1
                            pos3 = pos3 + 1
                        pos2 = pos2 + 1
                    pos1 = pos1 + 1
            #兑奖
            ##中奖信息
            msg = '' 
            ##中奖金额
            money = 0
            ##是否提示（一二三等奖）
            tip = False
            ##判断
            for i in range(0, len(bets_array)):
                ##判断红球
                r_nums = 0 
                for j in range(0, 6):
                    if bets_array[i][j] in data_array[0][1:7]: #前6个
                        r_nums = r_nums + 1
                ##判断蓝球
                b_nums = 0 
                if bets_array[i][6]==data_array[0][7]:
                    b_nums = 1
                ##判断中奖金额
                if (r_nums<=3 and b_nums==0): #无
                    pass
                elif (r_nums<=2 and b_nums==1): #6等
                    money = money + 5
                elif (r_nums==4 and b_nums==0) or (r_nums==3 and b_nums==1): #5等
                    money = money + 10
                elif (r_nums==5 and b_nums==0) or (r_nums==4 and b_nums==1): #4等
                    money = money + 200
                elif (r_nums==5 and b_nums==1): #3等
                    money = money + 3000
                    tip = True
                elif (r_nums==6 and b_nums==0): #2等
                    money = money + 100000
                    tip = True
                elif (r_nums==6 and b_nums==1): #1等
                    money = money + 500000
                    tip = True
            #文字
            if tip==False:
                msg = u'中奖金额为%d元！'%money
            if tip==True:
                msg = u'中奖金额为%d元！\n（不准确！！）'%money
            #弹出兑奖结果窗口
            dlg = wx.MessageDialog(self, msg, 
                                   u'%s期复式投注对奖'%(data_array[0][0]),
                                   wx.OK | wx.ICON_INFORMATION
                                   )
            dlg.ShowModal()
            dlg.Destroy()       
            #注意12等奖
        
        event.Skip()
                
    def OnMenuCheckItemscselfMenu(self, event): #自选数据兑奖
        '''选择任意数据进行兑奖'''
        #数据最新一期的期号
        date = int(data_array[0][0])
        #显示文件选择框
        dlg = wx.FileDialog(
            self, message=u"选择需要兑奖的文件",
            defaultDir=os.getcwd(), 
            defaultFile="",
            style=wx.OPEN
            )   
        #点击“打开”按钮
        if dlg.ShowModal()==wx.ID_OK:         
            #读取选择文件中的数据
            f = open(dlg.GetPaths()[0], 'r') 
            s = f.readlines()
            f.close()
            #数据转换
            bets_array = []
            for i in range(0, len(s)):
                if len(s)>2:
                    bets_array.append([s[i][0:2],s[i][3:5],s[i][6:8],s[i][9:11],
                                      s[i][12:14],s[i][15:17],s[i][18:20]])
            #兑奖
            msg = u'' #中奖信息
            msg = msg + u'文件共有%d注！\n'%(len(s))
            for i in range(0, len(bets_array)):
                r_nums = 0 #红球
                for j in range(0, 6):
                    if bets_array[i][j] in data_array[0][1:7]: #前6个
                        r_nums = r_nums + 1
                b_nums = 0 #蓝球
                if bets_array[i][6]==data_array[0][7]:
                    b_nums = 1
                money = u'' #金额
                if (r_nums<=3 and b_nums==0): #无
                    money = u'未中奖'
                elif (r_nums<=2 and b_nums==1): #6等
                    money = u'5元'
                elif (r_nums==4 and b_nums==0) or (r_nums==3 and b_nums==1): #5等
                    money = u'10元'
                elif (r_nums==5 and b_nums==0) or (r_nums==4 and b_nums==1): #4等
                    money = u'200元'
                elif (r_nums==5 and b_nums==1): #3等
                    money = u'3000元'
                elif (r_nums==6 and b_nums==0): #2等
                    money = u'二等奖'
                elif (r_nums==6 and b_nums==1): #1等
                    money = u'一等奖'

                msg = msg+ u'第%d注：%d+%d=%s\n'%(i+1,r_nums,b_nums,money)
            
            dlg = wx.MessageDialog(self, msg, 
                                   u'%s期对奖结构'%(data_array[0][0]),
                                   wx.OK | wx.ICON_INFORMATION
                                   )
            dlg.ShowModal()
            dlg.Destroy()             
        #关闭    
        dlg.Destroy()
  
        
        #打开文件
        event.Skip()
        
#-------------------------------------------------------------------------------
#----帮助----

    def OnMenuHelpItemsfaqMenu(self, event): #使用说明
        '''读取并显示说明文档文件'''
        f = open(u"data/说明文档.txt", "r")
        msg = f.read().decode('utf-8')
        f.close()

        dlg = wx.lib.dialogs.ScrolledMessageDialog(self, msg, u"使用说明")
        dlg.ShowModal()
                
        event.Skip()

    def OnMenuHelpItemsaboutMenu(self, event): #关于
        '''提示软件基本信息'''
        info = wx.AboutDialogInfo()
        info.Name = u"双色蟒"
        info.Version = u"1.0.6"
        info.Description = wordwrap(
            u"双色蟒彩票分析软件，用于双色球彩票数据分析、对奖及投注过滤。 "
            u"\n\n祝您中奖 :)",
            350, wx.ClientDC(self))
        info.WebSite = (u"http://code.google.com/p/ssqpython/",      
                        u"双色蟒主页")
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

        #因为在菜单后面标注有快捷键，所以会自动捕捉，而且会自动运行对应的函数
        
##        #F1就显示帮助
##        if keycode==wx.WXK_F1:
##            self.OnMenuHelpItemsfaqMenu(event)
##            
##        #F2就下载数据
##        if keycode==wx.WXK_F2:
##            self.OnMenuDataItemsdownloadMenu(event)
##        #F3就添加数据
##        if keycode==wx.WXK_F3:
##            self.OnMenuDataItemsaddMenu(event)
##        #F4就删除数据（20070911取消，和Alt+F4冲突）
##        #Ctrl+D就删除数据
##        if keycode==4: #键值4
##            self.OnMenuDataItemsdelMenu(event)
##        
##        #F5就红球过滤
##        if keycode==wx.WXK_F5:
##            self.OnMenuFiltrateItemsfredMenu(event)
##        #F6就红球缩水
##        if keycode==wx.WXK_F6:
##            self.OnMenuFiltrateItemssredMenu(event)
##        #F7就篮球推荐
##        if keycode==wx.WXK_F7:
##            self.OnMenuFiltrateItemsfblueMenu(event)
##        #Ctrl+O就自选过滤
##        if keycode==15:
##            self.OnMenuFiltrateItemsoptionalMenu(event)
##        #Ctrl+T就条件替换
##        if keycode==20:
##            self.OnMenuFiltrateItemsreplaceMenu(event)
##            
##        #F8就直接机选
##        if keycode==wx.WXK_F8:
##            self.OnMenuRandomItemsdrMenu(event)            
##        #Ctrl+A就过滤机选
##        if keycode==1: #键值1
##            self.OnMenuRandomItemsfrMenu(event)            
##        #Ctrl+B就缩水机选 
##        if keycode==2: #键值2
##            self.OnMenuRandomItemssrMenu(event)
##        #Ctrl+C就自选机选 
##        if keycode==3: #键值3
##            self.OnMenuRandomItemserMenu(event)
##            
##        #F9就固定投注兑奖
##        if keycode==wx.WXK_F9:
##            self.OnMenuCheckItemscfixedMenu(event)
##        #F11就预测数据兑奖
##        if keycode==wx.WXK_F11:
##            self.OnMenuCheckItemscpredictMenu(event)
##        #Ctrl+K就自选数据兑奖
##        if keycode==11: #键值11
##            self.OnMenuCheckItemscselfMenu(event)
##            
##        #F12就显示关于
##        if keycode==wx.WXK_F12:
##            self.OnMenuHelpItemsaboutMenu(event)
##            
##        #Ctrl+Q就退出
##        if keycode==17: #键值17
##            self.OnMenuDataItemsexitMenu(event)

        #Ctrl+S就提示心水号码（复活节彩蛋，呵呵）
        if keycode==19:
            self.EasterEggs(event)
        
        event.Skip()

#-------------------------------------------------------------------------------
#----Flash FSCommand传递值过来----
    def getFlashVars(self, evt):
        #print '选择的号码为',evt.args #即FSCommand中的第二个值
        #if len(evt.args)!=0: #判断是否为空
        global choice_num #全局变量
        choice_num = str(evt.args)
        self.OnMenuFiltrateItemsfredMenu(evt) #打开选号面板
        #我现在不会从Python传值到Flash里面

#-------------------------------------------------------------------------------
#----心水号码----
    def EasterEggs(self, event):
        '''心水号码'''
        '''此功能开发完成后可整体移植到Flash中'''
        '''横向跳号X/纵向跳号Y'''
        '''X向最多11，Y向最多9'''        
        #1.0 荐号
        ##1.1.类型1:1&5-2&4==3--XY--还需要在看看...
        ##1.2.类型2:2-1&3==2----N---
        #2.0 杀号
        ##2.1.类型1:2-2-2!=2----Y---
        ##2.2.类型2:1-2-3!=4----XY--
        ##2.3.类型3:3-2-1!=0----XY--
        ##2.4.类型4:1-2-2!=2----N---
        ##2.5.类型5:3-2-2!=2----N---
        ##2.6.类型6:3-3-2!=2----N---
        ##2.7.类型7:1-1-2!=2----N---
        ##2.8.类型8:2-3-2!=2----N---
        ##2.9.类型9:2-1-2!=2----N---
        ##2.10类型10:1-2&3!=3---N---
        ##2.11类型11:3-2&1!=1---N---

        #统计荐号----
        good_nums = []
        ##1.1（1&5-2&4==3）
        for y in range(0, 4): #纵向上跳号
            for x in range(0, 3): #横向上跳号            
                for i in range(1, 33+1): #反向考虑：从每一个可能出位来考虑（正向则是从每一个已出号码来考虑）
                    num1 = i-2*(2**x)
                    if num1<1:
                        num1 = num1+33
                    num2 = i-1*(2**x)
                    if num2<1:
                        num2 = num2+33
                    num3 = i+1*(2**x)
                    if num3>33:
                        num3 = num3-33
                    num4 = i+2*(2**x)
                    if num4>33:
                        num4 = num4-33
                    if '%.2d'%num2 in data_array[0+1*y][1:7] and \
                       '%.2d'%num3 in data_array[0+1*y][1:7] and \
                       '%.2d'%num1 in data_array[1+2*y][1:7] and \
                       '%.2d'%num4 in data_array[1+2*y][1:7]:
                        good_nums.append('%.2d'%i)
                        print '1.1 num=%d x=%d y=%d'%(i,x,y)
        ##1.2（2-1&3==2）
        for i in range(1, 33+1):
            num1 = i
            num2 = i-1
            if num2<1:
                num2 = num2+33
            num3 = i+1
            if num3>33:
                num3 = num3-33
            if '%.2d'%num1 in data_array[1][1:7] and \
               '%.2d'%num2 in data_array[0][1:7] and \
               '%.2d'%num3 in data_array[0][1:7]:
                good_nums.append('%.2d'%i)
                print '1.2 num=%d x=%d y=%d'%(i,x,y)
        #统计杀号----
        bad_nums = []
        ##2.1（2-2-2!=2）
        for y in range(0, 3): #纵向上跳号
            for i in range(1, 33+1):
                num1 = i
                num2 = i         
                num3 = i         
                if '%.2d'%num1 in data_array[2+3*y][1:7] and \
                   '%.2d'%num2 in data_array[1+2*y][1:7] and \
                   '%.2d'%num3 in data_array[0+1*y][1:7]:
                    bad_nums.append('%.2d'%i)
                    print '2.1 num=%d x=%d y=%d'%(i,x,y)
        ##2.2（1-2-3!=4）
        for y in range(0, 3): #纵向上跳号
            for x in range(0, 3): #横向上跳号
                for i in range(1, 33+1):
                    num1 = i-3*(2**x)
                    if num1<1:
                        num1 = num1+33
                    num2 = i-2*(2**x)
                    if num2<1:
                        num2 = num2+33            
                    num3 = i-1*(2**x)
                    if num3<1:
                        num3 = num3+33            
                    if '%.2d'%num1 in data_array[2+3*y][1:7] and \
                       '%.2d'%num2 in data_array[1+2*y][1:7] and \
                       '%.2d'%num3 in data_array[0+1*y][1:7]:
                        bad_nums.append('%.2d'%i)
                        print '2.2 num=%d x=%d y=%d'%(i,x,y)
        ##2.3（3-2-1!=0）
        for y in range(0, 3): #纵向上跳号
            for x in range(0, 3): #横向上跳号
                for i in range(1, 33+1):
                    num1 = i+3*(2**x)
                    if num1>33:
                        num1 = num1-33
                    num2 = i+2*(2**x)
                    if num2>33:
                        num2 = num2-33            
                    num3 = i+1*(2**x)
                    if num3>33:
                        num3 = num3-33            
                    if '%.2d'%num1 in data_array[2+3*y][1:7] and \
                       '%.2d'%num2 in data_array[1+2*y][1:7] and \
                       '%.2d'%num3 in data_array[0+1*y][1:7]:
                        bad_nums.append('%.2d'%i)
                        print '2.3 num=%d x=%d y=%d'%(i,x,y)
        ##2.4（1-2-2!=2）
        for i in range(1, 33+1):
            num1 = i-1
            if num1<1:
                num1 = num1+33
            num2 = i
            num3 = i
            if '%.2d'%num1 in data_array[2][1:7] and \
               '%.2d'%num2 in data_array[1][1:7] and \
               '%.2d'%num3 in data_array[0][1:7]:
                bad_nums.append('%.2d'%i)
                print '2.4 num=%d x=%d y=%d'%(i,x,y)
        ##2.5（3-2-2!=2）
        for i in range(1, 33+1):
            num1 = i+1
            if num1>33:
                num1 = num1-33
            num2 = i
            num3 = i
            if '%.2d'%num1 in data_array[2][1:7] and \
               '%.2d'%num2 in data_array[1][1:7] and \
               '%.2d'%num3 in data_array[0][1:7]:
                bad_nums.append('%.2d'%i)
                print '2.5 num=%d x=%d y=%d'%(i,x,y)
        ##2.6（3-3-2!=2）
        for i in range(1, 33+1):
            num1 = i+1
            if num1>33:
                num1 = num1-33
            num2 = i+1
            if num2>33:
                num2 = num2-33
            num3 = i
            if '%.2d'%num1 in data_array[2][1:7] and \
               '%.2d'%num2 in data_array[1][1:7] and \
               '%.2d'%num3 in data_array[0][1:7]:
                bad_nums.append('%.2d'%i)
                print '2.6 num=%d x=%d y=%d'%(i,x,y)
        ##2.7（1-1-2!=2）
        for i in range(1, 33+1):
            num1 = i-1
            if num1<1:
                num1 = num1+33
            num2 = i-1
            if num2<1:
                num2 = num2+33
            num3 = i
            if '%.2d'%num1 in data_array[2][1:7] and \
               '%.2d'%num2 in data_array[1][1:7] and \
               '%.2d'%num3 in data_array[0][1:7]:
                bad_nums.append('%.2d'%i)
                print '2.7 num=%d x=%d y=%d'%(i,x,y)
        ##2.8（2-3-2!=2）
        for i in range(1, 33+1):
            num1 = i
            num2 = i+1
            if num2>33:
                num2 = num2-33
            num3 = i
            if '%.2d'%num1 in data_array[2][1:7] and \
               '%.2d'%num2 in data_array[1][1:7] and \
               '%.2d'%num3 in data_array[0][1:7]:
                bad_nums.append('%.2d'%i)
                print '2.8 num=%d x=%d y=%d'%(i,x,y)
        ##2.9（2-1-2!=2）
        for i in range(1, 33+1):
            num1 = i
            num2 = i-1
            if num2<1:
                num2 = num2+33
            num3 = i
            if '%.2d'%num1 in data_array[2][1:7] and \
               '%.2d'%num2 in data_array[1][1:7] and \
               '%.2d'%num3 in data_array[0][1:7]:
                bad_nums.append('%.2d'%i)
                print '2.9 num=%d x=%d y=%d'%(i,x,y)
        ##2.10（1-2&3!=3）
        for i in range(1, 33+1):
            num1 = i-2
            if num1<1:
                num1 = num1+33
            num2 = i-1
            if num2<1:
                num2 = num2+33
            num3 = i
            if '%.2d'%num1 in data_array[1][1:7] and \
               '%.2d'%num2 in data_array[0][1:7] and \
               '%.2d'%num3 in data_array[0][1:7]:
                bad_nums.append('%.2d'%i)
                print '2.10 num=%d x=%d y=%d'%(i,x,y)
        ##2.11（3-2&1!=1）
        for i in range(1, 33+1):
            num1 = i+2
            if num1>33:
                num1 = num1-33
            num2 = i+1
            if num2>33:
                num2 = num2-33
            num3 = i
            if '%.2d'%num1 in data_array[1][1:7] and \
               '%.2d'%num2 in data_array[0][1:7] and \
               '%.2d'%num3 in data_array[0][1:7]:
                bad_nums.append('%.2d'%i)    
                print '2.11 num=%d x=%d y=%d'%(i,x,y)
        #去除重复情况
        good_news = []
        if len(good_nums)>1:
            for i in range(0, len(good_nums)):
                if good_nums[i] not in good_nums[i+1:]:
                    good_news.append(good_nums[i])
        else:
            good_news = good_nums
        bad_news = []
        if len(bad_nums)>1:
            for i in range(0, len(bad_nums)):
                if bad_nums[i] not in bad_nums[i+1:]:
                    bad_news.append(bad_nums[i])
        else:
            bad_news = bad_nums
        #按大小号排序
        if len(bad_news)>1:
            for j in range(0, len(bad_news)-1): #这个次数对不对？？
                for i in range(0, len(bad_news)-1):
                    if bad_news[i]>bad_news[i+1]:
                        (bad_news[i],bad_news[i+1]) = (bad_news[i+1],bad_news[i])
                        #上面这种替换方法好吗？
                        #比 a=b, b=c, c=a 快吗？
        if len(good_news)>1:
            for j in range(0, len(good_news)-1): 
                for i in range(0, len(good_news)-1):
                    if good_news[i]>good_news[i+1]:
                        (good_news[i],good_news[i+1]) = (good_news[i+1],good_news[i])
        #若出现某个号码同时在good和bad中出现
        s3 = u''
        if len(good_news)!=0:
            for t in good_news:
                if t in bad_news:
                    s3 = s3 + u'～%s重复了～\n'%t
        #判断有无号码存在，若存在则合并成字符串
        if len(good_news)==0:
            s1 = u'无'
        else:
            s1 = u' '.join(good_news)
        if len(bad_news)==0:
            s2 = u'无'
        else:
            s2 = u' '.join(bad_news)         
        #弹出对话框
        dlg = wx.MessageDialog(self,
                               u'本期建议选择号码：%s\n本期建议删除号码：%s\n%s'%(s1,s2,s3), 
                               u'心水号码（未通过ISO9001测试！）',
                               wx.OK 
                               )
        dlg.ShowModal()
        dlg.Destroy()

        #设置焦点（不然的话，焦点就跑到“数据文本”上面了）
        self.SetFocus()
        
        event.Skip()

