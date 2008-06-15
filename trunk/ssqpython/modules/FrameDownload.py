#! usr/bin/python
# -*- coding:utf-8 -*-
#Boa:Frame:FrameDownload
# otherrrr@gmail.com
# 数据下载面板

import wx
import locale

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
        #命令行提示
        print (u'FrameDownload启动').encode(locale.getdefaultlocale()[1])
        
        #下载数据时有可能延迟，显示一个画面
        image = wx.Image("pic/splash.jpg", wx.BITMAP_TYPE_ANY)
        bmp = image.ConvertToBitmap()
        wx.SplashScreen(bmp, wx.SPLASH_CENTRE_ON_SCREEN | wx.SPLASH_TIMEOUT, 1800, None, -1)
        wx.Yield()    
        #清空显示区
        self.textCtrl1.Clear()
        #访问网址(500wan & bwlc) 2008.06.12
        url = ['http://north.500wan.com/Info/ssq/datachart/history.aspx',\
               'http://www.bwlc.gov.cn/search/aspsuangse_ss.asp?']
        #导入包
        import urllib2
        #默认不需要代理
        using_proxy = False        
        #侦测网络是否存在Proxy
        try:
            f = urllib2.urlopen('http://www.baidu.com/')
            f.close()
        except Exception,ex: #得到异常类型
            #print ex 
            if str(ex)=='HTTP Error 407: Proxy authorization required':
                #需要代理验证
                using_proxy = True
        #判断访问网络是否出错
        net_access = True
        # 下载到的网页内容
        data_web = ''
        # 使用的网址
        url_used = ''
##        url_used = url[0]
        #不需要代理
        if using_proxy==False:        
            self.textCtrl1.AppendText(u'访问网络中……（未使用代理服务）\n')
            try:
                for url_t in url:
                    f = urllib2.urlopen(url_t)
                    data_web = f.read() #得到网页
                    f.close()
                    if len(data_web)>10000:
                        url_used = url_t
                        break
            except Exception,ex:
                self.textCtrl1.AppendText(u'出错了！\n')
                self.textCtrl1.AppendText(str(ex)+'\n')
                net_access = False
        #需要代理
        if using_proxy==True:
            self.textCtrl1.AppendText(u'访问网络中……（使用代理服务）\n')            
            #访问“代理设置.ini”得到参数
            f = open(u'data/代理设置.ini', 'r')
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
                for url_t in url:
                    response = opener.open(url)
                    data_web = response.read() #得到网页
                    if len(data_web)>10000:
                        url_used = url_t
                        break                    
            except Exception,ex:
                self.textCtrl1.AppendText(u'出错了！\n')                
                self.textCtrl1.AppendText(str(ex)+'\n')
                net_access = False                
##        #若要查看具体错误，可使用备份功能
##        #备份得到的网页
##        f = open('backup.htm', 'w')
##        f.write(data_web)
##        f.close()
##        #打开备份的网页
##        f = open('backup.htm', 'r')
##        data_web = f.read()
##        f.close()
        #查找出网络上的最近的数据
        if net_access==True:
            # 30组数据列表
            datas_array = []
            # 首先将得到的数据按照不同的网站处理好
            if '500wan' in url_used: # 500wan
                pos = 0
                for i in range(0, 30):
                    pos = data_web.find('<tr class="t_tr', pos+1, len(data_web))
                    t = ''
                    t = t + '20' + str(data_web[pos+22:pos+22+5])
                    for j in range(0, 7):
                        arg = '' #间隔
                        if j==0:
                            arg = ' '
                        elif j>0 and j<6:
                            arg = ','
                        else:
                            arg = '+'
                        t = t + arg + data_web[pos+53+28*j:pos+53+2+28*j]
                    datas_array.append(t+'\n')
            if 'bwlc' in url_used: # bwlc
                pos = 0
                for i in range(0, 30):
                    pos = data_web.find('num_ss_suangse.asp?qitime=', pos+2, len(data_web))
                    t = ''
                    t = t + ''.join(data_web[pos+26:pos+34].split('-')) + ' '
                    for j in range(0, 6):
                        if j==5:
                            t = t + data_web[pos+620+97*j:pos+620+2+97*j] + '+'
                        else:
                            t = t + data_web[pos+620+97*j:pos+620+2+97*j] + ','
                    t = t + data_web[pos+1241:pos+1241+2]
                    datas_array.append(t+'\n')
            # 显示网络最后更新的数据
            self.textCtrl1.AppendText(u'网络数据最后更新：\n'+datas_array[0]) #最后更新的数据
            #查看本地数据
            data_string = readDataFileToString()
            self.textCtrl1.AppendText(u'本地数据最后更新：\n'+data_string[:28]+'\n')
            if int(data_string[:7])==int(datas_array[0][:7]):
                self.textCtrl1.AppendText(u'本地数据和网络数据已同步，无须更新！\n')
            if int(data_string[:7]) > int(datas_array[0][:7]):
                self.textCtrl1.AppendText(u'本地数据比网络数据还要新，无须更新！\n')
            if int(data_string[:7]) < int(datas_array[0][:7]):
                self.textCtrl1.AppendText(u'网络数据比本地数据要新，正在更新！\n')
                #确定需要更新多少组数据
                group_num = int(datas_array[0][:7]) - int(data_string[:7])
                self.textCtrl1.AppendText(u'需要更新%d组数据\n'%group_num)
                #确定需要更新的数据
                new_data = ''
                for i in range(0, group_num):
                    new_data = new_data + datas_array[i]
                self.textCtrl1.AppendText(new_data)
                #更新数据
                writeStringToDataFile(new_data+data_string)
                self.textCtrl1.AppendText(u'数据已更新，可以关闭此窗口！\n')
        else:
            self.textCtrl1.AppendText(u'无法更新数据！\n请重新尝试，或联系otherrrr@gmail.com\n')       


