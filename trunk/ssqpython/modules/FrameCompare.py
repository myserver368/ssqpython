#! usr/bin/python
# -*- coding:utf-8 -*-
#Boa:Frame:FrameCompare
# otherrrr@gmail.com
# 查看被滤数据面板

import wx
import os
import locale

def create(parent, date):
    return FrameCompare(parent, date)

class FrameCompare(wx.Frame):
    def __init__(self, parent, date):

        wx.Frame.__init__(self, parent, name='FrameCompare',
                          title=u"查看过滤数据", pos=wx.DefaultPosition,
                          size=(568, 330),
                          style=wx.SYSTEM_MENU | wx.CAPTION \
                          |  wx.CLOSE_BOX | wx.CLIP_CHILDREN)
        self.SetIcon(wx.Icon(u'pic/red.ico',wx.BITMAP_TYPE_ICO))
        #命令行提示
        print (u'FrameCompare启动').encode(locale.getdefaultlocale()[1])

        # Create a Panel
        panel = wx.Panel(self, -1)

        # Data definition
        self.fileList = []
        self.panels = []
        self.flash = []
        # Get all datas(embedded '被滤数据')
        if '%d'%(date+1) in os.listdir(os.curdir):
            for ts in os.listdir('%d'%(date+1)):
                if (u'被滤数据').encode(locale.getdefaultlocale()[1]) in ts:
                    self.fileList.append(ts)

        if len(self.fileList)==0:
            wx.StaticText(panel, -1, u"对不起，未在%d目录下发现被滤数据！\n或者不存在%d目录！"%(date+1,date+1), \
                          pos=(20, 34))
        elif wx.Platform!='__WXMSW__':
            wx.StaticText(panel, -1, u"对不起，您的系统不支持Flash控件！\n该功能只在Windows下可用。", \
                          pos=(20, 34))
        else:
            from wx.lib.flashwin import FlashWindow

            # Create an ImageList
            imagelist = wx.ImageList(32,32)        
            # Get a pic 
            bmp = wx.ArtProvider.GetBitmap(wx.ART_NORMAL_FILE, wx.ART_OTHER, (32,32))
            # Add image to ImageList
            imagelist.Add(bmp)       
            # Create a Listbook
            listBook = wx.Listbook(panel, -1, style=wx.BK_DEFAULT)                             
            # Listbook's imagelist assign
            listBook.AssignImageList(imagelist)
            # Circle create pages
            for i in range(0, len(self.fileList)):
                # Create a Panel, and add to panels[]
                self.panels.append(wx.Panel(listBook, -1))
                # Read file
                f = open('%d/%s'%(date+1,self.fileList[i]), 'r')
                s = f.read()
                f.close()
                # Flash
                self.flash.append(FlashWindow(self.panels[i], style=wx.SUNKEN_BORDER))
                self.flash[i].LoadMovie(0, os.path.abspath(u'pic/flashC.swf'))
                self.boxSizer1 = wx.BoxSizer(orient=wx.VERTICAL)
                self.boxSizer1.Add(self.flash[i], proportion=1, flag=wx.EXPAND)
                self.boxSizer1.SetDimension(0, 0, 538, 340) 
                self.panels[i].SetSizer(self.boxSizer1)
                self.flash[i].SetVariable("fdata_max", len(s)/18)
                self.flash[i].SetVariable("fdata_str", s)
                # Add page to listbook
                listBook.AddPage(self.panels[i], self.fileList[i], imageId=0)       
            # Sizer
            sizer = wx.BoxSizer()
            sizer.Add(listBook, 1, wx.EXPAND)
            panel.SetSizer(sizer)
        # Test


