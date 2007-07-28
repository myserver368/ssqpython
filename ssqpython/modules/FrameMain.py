#Boa:Frame:FrameMain
# -*- coding: cp936 -*-
# otherrrr@gmail.com
# �����

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

_max_height = 0   #�������ڸ߶�
data_string = ''  #���ݣ��ַ�����ʽ��
data_array = []   #���ݣ������ʽ��

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
        parent.Append(help=u'\u84dd\u7403\u53f7\u7801\u63a8\u8350',
              id=wxID_FRAMEMAINMENUFILTRATEITEMSFBLUE, kind=wx.ITEM_NORMAL,
              text=u'\u84dd\u7403\u63a8\u8350')
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
        
        #����ʱ��ʾ����
        image = wx.Image("pic/splash.jpg", wx.BITMAP_TYPE_ANY)
        bmp = image.ConvertToBitmap()
        wx.SplashScreen(bmp, wx.SPLASH_CENTRE_ON_SCREEN | wx.SPLASH_TIMEOUT, 1500, None, -1)
        wx.Yield()         
        
        global _max_height, data_array, data_string

        #�ı���ʾ
        data_string = readDataFileToString()
        self.textCtrl1.SetFont(wx.Font(12, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "")) 
        self.textCtrl1.Clear()
        self.textCtrl1.AppendText(data_string)

        #ͼ����ʾ  
        data_array = readDataFileToArray()
        #_max_height = 15.4*len(data_array) - 190 #��ʾ���еģ��������϶�ʱ��һЩ�ٶۣ�
        _max_height = 15.4*100 - 190 #ֻ��ʾ���100�ڵ�
        self.scrolledWindow1.SetScrollbars(1, 1, 890, _max_height, 0, _max_height) #��λ���������·�
        
#-------------------------------------------------------------------------------
#----��ͼ----

    def OnScrolledWindow1Paint(self, event):
        '''���Ʒֲ�ͼ'''           
        dc = wx.PaintDC(self.scrolledWindow1)
        self.scrolledWindow1.DoPrepareDC(dc)       
        dc.Clear()

        #�ָ��߷�����ǰ�滭�����⵲ס��������
        dc.SetPen(wx.Pen("#B3B3B3", 1)) #�ָ���
        for i in range(1, 34-1):
            dc.DrawLine(i*16+47, 5, i*16+47, _max_height-20)
        for i in range(0, 100-1):
            dc.DrawLine(49, _max_height-(i*15+39), 840, _max_height-(i*15+39))
        for i in range(1, 16+1):
            dc.DrawLine(i*16+563, 5, i*16+563, _max_height-20)
            
        dc.SetTextForeground('RED') #��ɫ���
        dc.SetFont(wx.Font(10, wx.NORMAL, wx.NORMAL, wx.NORMAL))    
        for i in range(1, 33+1):
            dc.DrawText('%.2d'%i, i*16+34, _max_height-25)
            
        dc.SetTextForeground('#009900') #�ںţ���ɫ��
        for i in range(0, 100):
            dc.DrawText(str(data_array[i][0]), 0, _max_height-(i*15+39)) #���
            dc.DrawText(str(data_array[i][0]), 840, _max_height-(i*15+39)) #�Ҳ�
        
        dc.SetPen(wx.Pen("RED", 1)) #��ɫ��ֲ�ͼ  
        dc.SetBrush(wx.Brush(wx.RED, wx.SOLID))
        for i in range(0, 100):
            for j in range(1, 6+1):
                for k in range(1, 33+1): 
                    if int(data_array[i][j])==k:
                        dc.DrawRectangle(k*16+35, _max_height-(i*15+35), 10, 10) 
        
        dc.SetPen(wx.Pen("#777777", 1)) #�������� ��ɫ 1����
        for i in range(0, 100-1):
            dc.DrawLine((int(data_array[i][1]))*16+40, _max_height-(i*15+30), (int(data_array[i+1][1]))*16+40, _max_height-((i+1)*15+30))
        
        dc.SetPen(wx.Pen("#990099", 1)) #�������� ��ɫ 2����
        for i in range(0, 100-1):
            dc.DrawLine((int(data_array[i][2]))*16+40, _max_height-(i*15+30), (int(data_array[i+1][2]))*16+40, _max_height-((i+1)*15+30))
        
        dc.SetPen(wx.Pen("#CC9900", 1)) #�������� ��ɫ 3����
        for i in range(0, 100-1):
            dc.DrawLine((int(data_array[i][3]))*16+40, _max_height-(i*15+30), (int(data_array[i+1][3]))*16+40, _max_height-((i+1)*15+30))

        dc.SetPen(wx.Pen("STEEL BLUE", 1)) #�������� ��ɫ 4����
        for i in range(0, 100-1):
            dc.DrawLine((int(data_array[i][4]))*16+40, _max_height-(i*15+30), (int(data_array[i+1][4]))*16+40, _max_height-((i+1)*15+30))
                
        dc.SetPen(wx.Pen("#6699FF", 1)) #�������� ��ɫ 5����
        for i in range(0, 100-1):
            dc.DrawLine((int(data_array[i][5]))*16+40, _max_height-(i*15+30), (int(data_array[i+1][5]))*16+40, _max_height-((i+1)*15+30))
                
        dc.SetPen(wx.Pen("LIME GREEN", 1)) #�������� ��ɫ 6����
        for i in range(0, 100-1):
            dc.DrawLine((int(data_array[i][6]))*16+40, _max_height-(i*15+30), (int(data_array[i+1][6]))*16+40, _max_height-((i+1)*15+30))  
                      
        dc.SetPen(wx.Pen("BLUE", 1)) #��ɫ��ֲ�ͼ  
        dc.SetBrush(wx.Brush(wx.BLUE, wx.SOLID))
        for i in range(0, 100):
            for j in range(1, 16+1):
                if int(data_array[i][7])==j:
                    dc.DrawRectangle(j*16+567, _max_height-(i*15+35), 10, 10)    
                         
        dc.SetPen(wx.Pen("CADET BLUE", 1)) #�������� ��ɫ ����
        for i in range(0, 100-1):
            dc.DrawLine((int(data_array[i][7]))*16+572, _max_height-(i*15+30), (int(data_array[i+1][7]))*16+572, _max_height-((i+1)*15+30)) 
            
        dc.SetTextForeground('BLUE') #��ɫ���
        dc.SetFont(wx.Font(10, wx.NORMAL, wx.NORMAL, wx.NORMAL))    
        for i in range(1, 16+1):
            dc.DrawText('%.2d'%i, i*16+565, _max_height-25)            
            
        event.Skip()
        
#-------------------------------------------------------------------------------
#----����----

    def OnMenuDataItemsaddMenu(self, event):
        '''��������'''
        global data_string, data_array
        
        dlg = wx.TextEntryDialog(
                self, '  �������µ����ݣ�ע�Ᵽ�ָ�ʽ��',
                '��������')

        dlg.SetValue("2007001 01,02,03,04,05,06+07")

        if dlg.ShowModal() == wx.ID_OK:
            writeStringToDataFile(dlg.GetValue()+'\n'+data_string)
            
            data_string = readDataFileToString() #���¶�ȡ����
            data_array = readDataFileToArray() 
        
            self.textCtrl1.Clear() #ˢ������
            self.textCtrl1.AppendText(data_string)
            self.textCtrl1.ShowPosition(0)
            
        dlg.Destroy()
                
        event.Skip()
        
    def OnMenuDataItemsdelMenu(self, event):
        '''ɾ������'''
        global data_string, data_array
        
        dlg = wx.MessageDialog(self, '  ���һ�����ݻᱻɾ����\n%s\n'%str(data_string.split('\n')[0]), 
                               'ɾ������',
                               wx.OK | wx.CANCEL | wx.ICON_INFORMATION
                               )
        
        if dlg.ShowModal() == wx.ID_OK:
            writeStringToDataFile(data_string[29:]) #ÿһ�ڵ�����Ϊ28�ֽ�

            data_string = readDataFileToString() #���¶�ȡ����
            data_array = readDataFileToArray() 
        
            self.textCtrl1.Clear() #ˢ������
            self.textCtrl1.AppendText(data_string)
            self.textCtrl1.ShowPosition(0)            
        
        dlg.Destroy()             
        
        event.Skip()
        
    def OnMenuDataItemsexitMenu(self, event):
        '''�˳�'''
        self.Close()
        
        event.Skip()

#-------------------------------------------------------------------------------
#----����----
   
    def OnMenuFiltrateItemsfredMenu(self, event): #�������
        '''������˹���'''
        _FrameRedFiltrate = FrameRedFiltrate.create(None)
        _FrameRedFiltrate.Show() 
                
        event.Skip()  

    def OnMenuFiltrateItemsfblueMenu(self, event): #�����Ƽ�
        '''�����Ƽ�����'''
        _FrameBlue = FrameBlue.create(None)
        _FrameBlue.Show() 
        
        event.Skip()

#-------------------------------------------------------------------------------
#----�Խ�----
        
    def OnMenuCheckItemscpredictMenu(self, event): #Ԥ�����ݶԽ�
        '''��ȡԤ�������ļ����Խ�'''
        #��ȡ����ʱ��Щ�ӳ٣���ʾһ������
        image = wx.Image("pic/splash.jpg", wx.BITMAP_TYPE_ANY)
        bmp = image.ConvertToBitmap()
        wx.SplashScreen(bmp, wx.SPLASH_CENTRE_ON_SCREEN | wx.SPLASH_TIMEOUT, 1200, None, -1)
        wx.Yield()
        
        _FrameReport = FrameReport.create(None)
        _FrameReport.Show()
            
        event.Skip()

    def OnMenuCheckItemscfixedMenu(self, event): #�̶�Ͷע�Խ�
        '''��ȡ�̶�Ͷע�ļ����Խ�'''       
        bet_array = readBetFileToArray()
        
        msg = '' #�н���Ϣ
        msg = msg + '�̶�Ͷע�й���%dע��\n'%(len(bet_array))
        for i in range(0, len(bet_array)):
            r_nums = 0 #����
            for j in range(0, 6):
                if bet_array[i][j] in data_array[0][1:7]: #ǰ6��
                    r_nums = r_nums + 1
            
            b_nums = 0 #����
            if bet_array[i][6]==data_array[0][7]:
                b_nums = 1
                
            money = '' #���
            if (r_nums<=3 and b_nums==0): #��
                money = 'δ�н�'
            elif (r_nums<=2 and b_nums==1): #6��
                money = '5Ԫ'
            elif (r_nums==4 and b_nums==0) or (r_nums==3 and b_nums==1): #5��
                money = '10Ԫ'
            elif (r_nums==5 and b_nums==0) or (r_nums==4 and b_nums==1): #4��
                money = '200Ԫ'
            elif (r_nums==5 and b_nums==1): #3��
                money = '3000Ԫ'
            elif (r_nums==6 and b_nums==0): #2��
                money = '���Ƚ�'
            elif (r_nums==6 and b_nums==1): #1��
                money = 'һ�Ƚ�'

            msg = msg+ '��%dע��%d+%d=%s\n'%(i+1,r_nums,b_nums,money)
        
        dlg = wx.MessageDialog(self, msg, 
                               '%s�ڹ̶�Ͷע�Խ�'%(data_array[0][0]),
                               wx.OK | wx.ICON_INFORMATION
                               )
        dlg.ShowModal()
        dlg.Destroy()   
                
        event.Skip()

#-------------------------------------------------------------------------------
#----����----

    def OnMenuHelpItemsfaqMenu(self, event): #ʹ��˵��
        '''��ȡ����ʾ˵���ĵ��ļ�'''
        f = open("˵���ĵ�.txt", "r")
        msg = f.read()
        f.close()

        dlg = wx.lib.dialogs.ScrolledMessageDialog(self, msg, "ʹ��˵��")
        dlg.ShowModal()
                
        event.Skip()

    def OnMenuHelpItemsaboutMenu(self, event): #����
        '''��ʾ����������Ϣ'''
        info = wx.AboutDialogInfo()
        info.Name = "˫ɫ��"
        info.Version = "0.9.7"
        info.Description = wordwrap(
            u"˫ɫ����Ʊ��������������˫ɫ���Ʊ���ݷ������Խ���Ͷע���ˡ� "
            u"\n\nף���н� :)",
            350, wx.ClientDC(self))
        info.WebSite = ("http://code.google.com/p/ssqpython/",      
                        "˫ɫ����ҳ")
        info.Developers = [ "otherrrr@gmail.com" ]
        
        wx.AboutBox(info)
        
        event.Skip()        