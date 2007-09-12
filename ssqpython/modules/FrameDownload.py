#Boa:Frame:FrameDownload
# -*- coding: cp936 -*-
# otherrrr@gmail.com
# 数据下载面板

import wx

from DataFileIO import readDataFileToString, writeStringToDataFile
        
def create(parent):
    return FrameDownload(parent)

[wxID_FRAMEDOWNLOAD, wxID_FRAMEDOWNLOADTEXTCTRL1, 
] = [wx.NewId() for _init_ctrls in range(2)]

class FrameDownload(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAMEDOWNLOAD, name=u'FrameDownload',
              parent=prnt, pos=wx.Point(293, 237), size=wx.Size(421, 318),
              style=wx.DEFAULT_FRAME_STYLE, title=u'\u6570\u636e\u4e0b\u8f7d')
        self.SetClientSize(wx.Size(413, 291))
        self.SetIcon(wx.Icon(u'pic/logo.ico',wx.BITMAP_TYPE_ICO))

        self.textCtrl1 = wx.TextCtrl(id=wxID_FRAMEDOWNLOADTEXTCTRL1,
              name='textCtrl1', parent=self, pos=wx.Point(0, 0),
              size=wx.Size(413, 291), style=wx.TE_MULTILINE,
              value=u'\u663e\u793a\u7a97\u53e3')

    def __init__(self, parent):
        self._init_ctrls(parent)
        #下载数据时有可能延迟，显示一个画面
        image = wx.Image("pic/splash.jpg", wx.BITMAP_TYPE_ANY)
        bmp = image.ConvertToBitmap()
        wx.SplashScreen(bmp, wx.SPLASH_CENTRE_ON_SCREEN | wx.SPLASH_TIMEOUT, 1800, None, -1)
        wx.Yield()         
        #清空显示区
        self.textCtrl1.Clear()
        #访问网址（我的blog）
        url = 'http://hi.baidu.com/otherrrr/blog/item/30172834dfbf8c3a5bb5f500.html'
        self.textCtrl1.AppendText('访问网址：http://hi.baidu.com/otherrrr/\n')
        #导入包
        import urllib2
        #默认不需要代理
        using_proxy = False        
        #侦测网络是否存在Proxy
        try:
            f = urllib2.urlopen(url)
            f.close()
        except Exception,ex: #得到异常类型
            #print ex 
            if str(ex)=='HTTP Error 407: Proxy authorization required':
                #需要代理验证
                using_proxy = True
            else:
                using_proxy = False
        #判断访问网络是否出错
        net_access = True
        #不需要代理
        if using_proxy==False:        
            self.textCtrl1.AppendText('访问网络中……（未使用代理服务）\n')
            try:
                f = urllib2.urlopen(url)
                data_web = f.read() #得到网页
                f.close()
            except Exception,ex:
                self.textCtrl1.AppendText('出错了！\n')
                self.textCtrl1.AppendText(str(ex)+'\n')
                net_access = False
        #需要代理
        if using_proxy==True:
            self.textCtrl1.AppendText('访问网络中……（使用代理服务）\n')            
            #访问“代理设置.ini”得到参数
            f = open('代理设置.ini', 'r')
            s = f.readlines()
            f.close()
            server = s[1].split(':')[1][:-1] #服务器
            port = s[3].split(':')[1][:-1] #端口
            username = s[5].split(':')[1][:-1] #账户名
            password = s[7].split(':')[1][:-1] #密码
            protocol = s[9].split(':')[1][:-1] #协议
            #设置代理
            proxy_handler = urllib2.ProxyHandler({protocol:protocol+'://'+username+':'+password+'@'+server+':'+port})
            opener = urllib2.build_opener(proxy_handler)
            try:
                response = opener.open(url)
                data_web = response.read() #得到网页
            except Exception,ex:
                self.textCtrl1.AppendText('出错了！\n')                
                self.textCtrl1.AppendText(str(ex)+'\n')
                net_access = False                
        #若要查看具体错误，可使用备份功能
        '''
        #备份得到的网页
        f = open('backup.htm', 'w')
        f.write(data_web)
        f.close()
        #打开备份的网页
        f = open('backup.htm', 'r')
        data_web = f.read()
        f.close()
        '''
        #查找出网络上的最近的数据
        if net_access==True and len(data_web)>10000:
            #>10000是因为：正常大小是33484，非正常大小是2699(2007.08.28测得数据)
            pos = data_web.find('<div class="cnt">', 0, len(data_web)) #得到位置
            #pos = s.index('<div class="cnt">') #另一种得到位置的方法
            self.textCtrl1.AppendText('网络数据最后更新：\n'+str(data_web[pos+17:pos+17+28])+'\n') #最后更新的数据
            #查看本地数据
            data_string = readDataFileToString()
            self.textCtrl1.AppendText('本地数据最后更新：\n'+data_string[:28]+'\n')
            if int(data_web[pos+17:pos+17+7])==int(data_string[:7]):
                self.textCtrl1.AppendText('本地数据和网络数据已同步，无须更新！\n')
            if int(data_web[pos+17:pos+17+7])<int(data_string[:7]):
                self.textCtrl1.AppendText('本地数据比网络数据还要新，无须更新！\n')
            if int(data_web[pos+17:pos+17+7])>int(data_string[:7]):
                self.textCtrl1.AppendText('网络数据比本地数据要新，正在更新！\n')
                #确定需要更新多少组数据
                group_num = int(data_web[pos+17:pos+17+7]) - int(data_string[:7])
                self.textCtrl1.AppendText('需要更新%d组数据\n'%group_num)
                #确定需要更新的数据
                new_data = ''
                for i in range(0, group_num):
                    new_data = new_data + (data_web[pos+i*33+17:pos+i*33+17+28]+'\n')
                self.textCtrl1.AppendText(new_data)
                #更新数据
                writeStringToDataFile(new_data+data_string)
                self.textCtrl1.AppendText('数据已更新，可以关闭此窗口！\n')
        else:
            self.textCtrl1.AppendText('无法更新数据！\n请重新尝试，或联系otherrrr@gmail.com\n')       


