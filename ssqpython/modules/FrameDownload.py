#Boa:Frame:FrameDownload
# -*- coding: cp936 -*-
# otherrrr@gmail.com
# �����������

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
        #�����Ļ
        self.textCtrl1.Clear()
        #������ַ���ҵ�blog��
        url = 'http://hi.baidu.com/otherrrr/blog/item/30172834dfbf8c3a5bb5f500.html'
        self.textCtrl1.AppendText('������ַ��http://hi.baidu.com/otherrrr/\n')
        #�����
        import urllib2
        #��������Ƿ����Proxy
        try:
            f = urllib2.urlopen(url)
            f.close()
        except Exception,ex: #�õ��쳣����
            #print ex 
            if str(ex)=='HTTP Error 407: Proxy authorization required':
                #��Ҫ������֤
                using_proxy = True
            else:
                using_proxy = False
        #Ĭ�ϲ���Ҫ����
        using_proxy = False
        #�жϷ��������Ƿ����
        net_access = True
        #����Ҫ����
        if using_proxy==False:        
            self.textCtrl1.AppendText('���������С�����δʹ�ô������\n')
            try:
                f = urllib2.urlopen(url)
                data_web = f.read() #�õ���ҳ
                f.close()
            except Exception,ex:
                self.textCtrl1.AppendText('�����ˣ�\n')
                self.textCtrl1.AppendText(str(ex)+'\n')
                net_access = False
        #��Ҫ����
        if using_proxy==True:
            self.textCtrl1.AppendText('���������С�����ʹ�ô������\n')            
            #���ʡ���������.ini���õ�����
            f = open('��������.ini', 'r')
            s = f.readlines()
            f.close()
            server = s[1].split(':')[1][:-1] #������
            port = s[3].split(':')[1][:-1] #�˿�
            username = s[5].split(':')[1][:-1] #�˻���
            password = s[7].split(':')[1][:-1] #����
            protocol = s[9].split(':')[1][:-1] #Э��
            #���ô���
            proxy_handler = urllib2.ProxyHandler({protocol:protocol+'://'+username+':'+password+'@'+server+':'+port})
            opener = urllib2.build_opener(proxy_handler)
            try:
                response = opener.open(url)
                data_web = response.read() #�õ���ҳ
            except Exception,ex:
                self.textCtrl1.AppendText('�����ˣ�\n')                
                self.textCtrl1.AppendText(str(ex)+'\n')
                net_access = False                
        #��Ҫ�鿴������󣬿�ʹ�ñ��ݹ���
        '''
        #���ݵõ�����ҳ
        f = open('backup.htm', 'w')
        f.write(data_web)
        f.close()
        #�򿪱��ݵ���ҳ
        f = open('backup.htm', 'r')
        data_web = f.read()
        f.close()
        '''
        #���ҳ������ϵ����������
        if net_access==True and len(data_web)>10000:
            #>10000����Ϊ��������С��33484����������С��2699(2007.08.28�������)
            pos = data_web.find('<div class="cnt">', 0, len(data_web)) #�õ�λ��
            #pos = s.index('<div class="cnt">') #��һ�ֵõ�λ�õķ���
            self.textCtrl1.AppendText('�������������£�\n'+str(data_web[pos+17:pos+17+28])+'\n') #�����µ�����
            #�鿴��������
            data_string = readDataFileToString()
            self.textCtrl1.AppendText('�������������£�\n'+data_string[:28]+'\n')
            if int(data_web[pos+17:pos+17+7])==int(data_string[:7]):
                self.textCtrl1.AppendText('�������ݺ�����������ͬ����������£�\n')
            if int(data_web[pos+17:pos+17+7])<int(data_string[:7]):
                self.textCtrl1.AppendText('�������ݱ��������ݻ�Ҫ�£�������£�\n')
            if int(data_web[pos+17:pos+17+7])>int(data_string[:7]):
                self.textCtrl1.AppendText('�������ݱȱ�������Ҫ�£����ڸ��£�\n')
                #ȷ����Ҫ���¶���������
                group_num = int(data_web[pos+17:pos+17+7]) - int(data_string[:7])
                self.textCtrl1.AppendText('��Ҫ����%d������\n'%group_num)
                #ȷ����Ҫ���µ�����
                new_data = ''
                for i in range(0, group_num):
                    new_data = new_data + (data_web[pos+i*33+17:pos+i*33+17+28]+'\n')
                self.textCtrl1.AppendText(new_data)
                #��������
                writeStringToDataFile(new_data+data_string)
                self.textCtrl1.AppendText('�����Ѹ��£����Թرմ˴��ڣ�\n')
        else:
            self.textCtrl1.AppendText('�޷��������ݣ�\n�����³��ԣ�����ϵotherrrr@gmail.com\n')       


