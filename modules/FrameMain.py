# -*- coding: cp936 -*-
# otherrrr@gmail.com
# 主面板

import wx
import wx.stc
import wx.lib.scrolledpanel
import wx.lib.dialogs
from wx.lib.wordwrap import wordwrap

from modules.DataFileIO import readDataFileToString, readDataFileToArray, writeStringToDataFile
from modules.BetFileIO import readBetFileToArray

import FrameRedFiltrate
import FrameReport

_max_height = 0   #滚动窗口高度
data_string = ''  #数据（字符串格式）
data_array = []   #数据（数组格式）

def create(parent):
    return FrameMain(parent)

[wxID_FRAMEMAIN, wxID_FRAMEMAINNOTEBOOK1, wxID_FRAMEMAINSCROLLEDWINDOW1, 
 wxID_FRAMEMAINSTATUSBAR1, wxID_FRAMEMAINTEXTCTRL1, 
] = [wx.NewId() for _init_ctrls in range(5)]

[wxID_FRAMEMAINMENUDATAITEMSADD, wxID_FRAMEMAINMENUDATAITEMSDEL, 
 wxID_FRAMEMAINMENUDATAITEMSEXIT, 
] = [wx.NewId() for _init_coll_menuData_Items in range(3)]

[wxID_FRAMEMAINMENUFILTRATEITEMSFBLUE, wxID_FRAMEMAINMENUFILTRATEITEMSFRED, 
] = [wx.NewId() for _init_coll_menuFiltrate_Items in range(2)]

[wxID_FRAMEMAINMENUCHECKITEMSCFIXED, wxID_FRAMEMAINMENUCHECKITEMSCPREDICT, 
] = [wx.NewId() for _init_coll_menuCheck_Items in range(2)]

[wxID_FRAMEMAINMENUHELPITEMSABOUT, wxID_FRAMEMAINMENUHELPITEMSFAQ, 
] = [wx.NewId() for _init_coll_menuHelp_Items in range(2)]

[wxID_FRAMEMAINMENUFILTRATEREDITEMSREDBASIC, 
 wxID_FRAMEMAINMENUFILTRATEREDITEMSREDMEDIA, 
] = [wx.NewId() for _init_coll_menuFiltrateRed_Items in range(2)]

class FrameMain(wx.Frame):
    def _init_coll_menuCheck_Items(self, parent):
        # generated method, don't edit

        parent.Append(help=u'\u56fa\u5b9a\u6295\u6ce8\u5bf9\u5956',
              id=wxID_FRAMEMAINMENUCHECKITEMSCFIXED, kind=wx.ITEM_NORMAL,
              text=u'\u56fa\u5b9a\u6295\u6ce8\u5bf9\u5956')
        parent.Append(help=u'\u9884\u6d4b\u6570\u636e\u5bf9\u5956',
              id=wxID_FRAMEMAINMENUCHECKITEMSCPREDICT, kind=wx.ITEM_NORMAL,
              text=u'\u9884\u6d4b\u6570\u636e\u5bf9\u5956')
        self.Bind(wx.EVT_MENU, self.OnMenuCheckItemscfixedMenu,
              id=wxID_FRAMEMAINMENUCHECKITEMSCFIXED)
        self.Bind(wx.EVT_MENU, self.OnMenuCheckItemscpredictMenu,
              id=wxID_FRAMEMAINMENUCHECKITEMSCPREDICT)

    def _init_coll_menuBar1_Menus(self, parent):
        # generated method, don't edit

        parent.Append(menu=self.menuData, title=u'\u6570\u636e')
        parent.Append(menu=self.menuFiltrate, title=u'\u8fc7\u6ee4')
        parent.Append(menu=self.menuCheck, title=u'\u5bf9\u5956')
        parent.Append(menu=self.menuHelp, title=u'\u5e2e\u52a9')

    def _init_coll_menuHelp_Items(self, parent):
        # generated method, don't edit

        parent.Append(help=u'\u4f7f\u7528\u8bf4\u660e',
              id=wxID_FRAMEMAINMENUHELPITEMSFAQ, kind=wx.ITEM_NORMAL,
              text=u'\u4f7f\u7528\u8bf4\u660e')
        parent.Append(help=u'\u5173\u4e8e', id=wxID_FRAMEMAINMENUHELPITEMSABOUT,
              kind=wx.ITEM_NORMAL, text=u'\u5173\u4e8e')
        self.Bind(wx.EVT_MENU, self.OnMenuHelpItemsaboutMenu,
              id=wxID_FRAMEMAINMENUHELPITEMSABOUT)
        self.Bind(wx.EVT_MENU, self.OnMenuHelpItemsfaqMenu,
              id=wxID_FRAMEMAINMENUHELPITEMSFAQ)

    def _init_coll_menuData_Items(self, parent):
        # generated method, don't edit

        parent.Append(help=u'\u6dfb\u52a0\u6570\u636e',
              id=wxID_FRAMEMAINMENUDATAITEMSADD, kind=wx.ITEM_NORMAL,
              text=u'\u6dfb\u52a0\u6570\u636e')
        parent.Append(help=u'\u5220\u9664\u6570\u636e',
              id=wxID_FRAMEMAINMENUDATAITEMSDEL, kind=wx.ITEM_NORMAL,
              text=u'\u5220\u9664\u6570\u636e')
        parent.Append(help=u'\u9000\u51fa', id=wxID_FRAMEMAINMENUDATAITEMSEXIT,
              kind=wx.ITEM_NORMAL, text=u'\u9000\u51fa')
        self.Bind(wx.EVT_MENU, self.OnMenuDataItemsexitMenu,
              id=wxID_FRAMEMAINMENUDATAITEMSEXIT)
        self.Bind(wx.EVT_MENU, self.OnMenuDataItemsaddMenu,
              id=wxID_FRAMEMAINMENUDATAITEMSADD)
        self.Bind(wx.EVT_MENU, self.OnMenuDataItemsdelMenu,
              id=wxID_FRAMEMAINMENUDATAITEMSDEL)

    def _init_coll_menuFiltrate_Items(self, parent):
        # generated method, don't edit

        parent.Append(help=u'\u7ea2\u7403\u8fc7\u6ee4',
              id=wxID_FRAMEMAINMENUFILTRATEITEMSFRED, kind=wx.ITEM_NORMAL,
              text=u'\u7ea2\u7403\u8fc7\u6ee4')
        parent.Append(help=u'\u84dd\u7403\u8fc7\u6ee4',
              id=wxID_FRAMEMAINMENUFILTRATEITEMSFBLUE, kind=wx.ITEM_NORMAL,
              text=u'\u84dd\u7403\u8fc7\u6ee4')
        self.Bind(wx.EVT_MENU, self.OnMenuFiltrateItemsfredMenu,
              id=wxID_FRAMEMAINMENUFILTRATEITEMSFRED)
        self.Bind(wx.EVT_MENU, self.OnMenuFiltrateItemsfblueMenu,
              id=wxID_FRAMEMAINMENUFILTRATEITEMSFBLUE)

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

        self.menuCheck = wx.Menu(title='')

        self.menuHelp = wx.Menu(title='')

        self._init_coll_menuBar1_Menus(self.menuBar1)
        self._init_coll_menuData_Items(self.menuData)
        self._init_coll_menuFiltrate_Items(self.menuFiltrate)
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
        self.SetIcon(wx.Icon(u'pic/logo.ico',
              wx.BITMAP_TYPE_ICO))

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
        
        global _max_height, data_array, data_string

        #文本显示
        data_string = readDataFileToString()
        self.textCtrl1.SetFont(wx.Font(12, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "")) 
        self.textCtrl1.Clear()
        self.textCtrl1.AppendText(data_string)

        #图表显示  
        data_array = readDataFileToArray()
        _max_height = 15.4*len(data_array) - 190
        self.scrolledWindow1.SetScrollbars(1, 1, 890, _max_height, 0, _max_height) #定位于数据最下方
        
#-------------------------------------------------------------------------------
#----绘图----

    def OnScrolledWindow1Paint(self, event):
        '''绘制分布图'''           
        dc = wx.PaintDC(self.scrolledWindow1)
        self.scrolledWindow1.DoPrepareDC(dc)       
        dc.Clear()
            
        dc.SetTextForeground('RED') #红色球号
        dc.SetFont(wx.Font(10, wx.NORMAL, wx.NORMAL, wx.NORMAL))    
        for i in range(1, 33+1):
            dc.DrawText('%.2d'%i, i*16+34, _max_height-25)
            
        dc.SetTextForeground('#009900') #期号（绿色）
        for i in range(0, len(data_array)):
            dc.DrawText(str(data_array[i][0]), 0, _max_height-(i*15+39)) #左侧
            dc.DrawText(str(data_array[i][0]), 840, _max_height-(i*15+39)) #右侧
        
        dc.SetPen(wx.Pen("RED", 1)) #红色球分布图  
        dc.SetBrush(wx.Brush(wx.RED, wx.SOLID))
        for i in range(0, len(data_array)):
            for j in range(1, 6+1):
                for k in range(1, 33+1): 
                    if int(data_array[i][j])==k:
                        dc.DrawRectangle(k*16+35, _max_height-(i*15+35), 10, 10) 
        
        dc.SetPen(wx.Pen("DARK OLIVE", 1)) #画走势线 灰色 1号球
        for i in range(0, len(data_array)-1):
            dc.DrawLine((int(data_array[i][1]))*16+40, _max_height-(i*15+30), (int(data_array[i+1][1]))*16+40, _max_height-((i+1)*15+30))
        
        dc.SetPen(wx.Pen("ORCHID", 1)) #画走势线 紫色 2号球
        for i in range(0, len(data_array)-1):
            dc.DrawLine((int(data_array[i][2]))*16+40, _max_height-(i*15+30), (int(data_array[i+1][2]))*16+40, _max_height-((i+1)*15+30))
        
        dc.SetPen(wx.Pen("BROWN", 1)) #画走势线 棕色 3号球
        for i in range(0, len(data_array)-1):
            dc.DrawLine((int(data_array[i][3]))*16+40, _max_height-(i*15+30), (int(data_array[i+1][3]))*16+40, _max_height-((i+1)*15+30))

        dc.SetPen(wx.Pen("TAN", 1)) #画走势线 茶色 4号球
        for i in range(0, len(data_array)-1):
            dc.DrawLine((int(data_array[i][4]))*16+40, _max_height-(i*15+30), (int(data_array[i+1][4]))*16+40, _max_height-((i+1)*15+30))
                
        dc.SetPen(wx.Pen("STEEL BLUE", 1)) #画走势线 蓝色 5号球
        for i in range(0, len(data_array)-1):
            dc.DrawLine((int(data_array[i][5]))*16+40, _max_height-(i*15+30), (int(data_array[i+1][5]))*16+40, _max_height-((i+1)*15+30))
                
        dc.SetPen(wx.Pen("LIME GREEN", 1)) #画走势线 绿色 6号球
        for i in range(0, len(data_array)-1):
            dc.DrawLine((int(data_array[i][6]))*16+40, _max_height-(i*15+30), (int(data_array[i+1][6]))*16+40, _max_height-((i+1)*15+30))  
                      
        dc.SetPen(wx.Pen("BLUE", 1)) #蓝色球分布图  
        dc.SetBrush(wx.Brush(wx.BLUE, wx.SOLID))
        for i in range(0, len(data_array)):
            for j in range(1, 16+1):
                if int(data_array[i][7])==j:
                    dc.DrawRectangle(j*16+567, _max_height-(i*15+35), 10, 10)    
                         
        dc.SetPen(wx.Pen("CADET BLUE", 1)) #画走势线 蓝色 蓝球
        for i in range(0, len(data_array)-1):
            dc.DrawLine((int(data_array[i][7]))*16+572, _max_height-(i*15+30), (int(data_array[i+1][7]))*16+572, _max_height-((i+1)*15+30)) 
                               
        dc.SetPen(wx.Pen("#B3B3B3", 1)) #分隔线
        for i in range(1, 34-1):
            dc.DrawLine(i*16+47, 5, i*16+47, _max_height-20)
        for i in range(0, len(data_array)-1):
            dc.DrawLine(49, _max_height-(i*15+39), 840, _max_height-(i*15+39))
        for i in range(1, 16+1):
            dc.DrawLine(i*16+563, 5, i*16+563, _max_height-20)     
            
        dc.SetTextForeground('BLUE') #蓝色球号
        dc.SetFont(wx.Font(10, wx.NORMAL, wx.NORMAL, wx.NORMAL))    
        for i in range(1, 16+1):
            dc.DrawText('%.2d'%i, i*16+565, _max_height-25)            
            
        event.Skip()
        
#-------------------------------------------------------------------------------
#----数据----

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

    def OnMenuFiltrateItemsfblueMenu(self, event): #蓝球过滤
        '''蓝球过滤功能'''
        dlg = wx.MessageDialog(self, '该功能尚未完善！', 
                               'Sorry',
                               wx.OK | wx.ICON_INFORMATION
                               )
        dlg.ShowModal()
        dlg.Destroy()  
                
        event.Skip()

#-------------------------------------------------------------------------------
#----对奖----
        
    def OnMenuCheckItemscpredictMenu(self, event): #预测数据对奖
        '''读取预测数据文件并对奖'''
        _FrameReport = FrameReport.create(None)
        _FrameReport.Show()
            
        event.Skip()

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
        info.Version = "0.9.2"
        info.Description = wordwrap(
            u"双色蟒彩票分析软件，用于双色球彩票数据分析、对奖及过滤投注。 "
            u"\n\n祝您中奖 :)",
            350, wx.ClientDC(self))
        info.WebSite = ("http://code.google.com/p/ssqpython/",      
                        "双色蟒主页")
        info.Developers = [ "otherrrr@gmail.com" ]
        
        wx.AboutBox(info)
        
        event.Skip()        
