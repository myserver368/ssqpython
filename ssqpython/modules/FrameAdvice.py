#Boa:Frame:FrameAdvice
# -*- coding: cp936 -*-
# otherrrr@gmail.com
# �����Ƽ����

import wx

from DataFileIO import readDataFileToArray
from DataCompute import blueCoumpute, blueAdvice

def create(parent):
    return FrameAdvice(parent)

[wxID_FRAMEADVICE, wxID_FRAMEADVICETEXTCTRL1, 
] = [wx.NewId() for _init_ctrls in range(2)]

class FrameAdvice(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAMEADVICE, name=u'FrameAdvice',
              parent=prnt, pos=wx.Point(325, 260), size=wx.Size(436, 322),
              style=wx.DEFAULT_FRAME_STYLE,
              title=u'\u7bee\u7403\u63a8\u8350\u53f7\u7801')
        self.SetClientSize(wx.Size(428, 295))
        self.SetIcon(wx.Icon(u'pic/blue.ico',
              wx.BITMAP_TYPE_ICO))

        self.textCtrl1 = wx.TextCtrl(id=wxID_FRAMEADVICETEXTCTRL1,
              name='textCtrl1', parent=self, pos=wx.Point(0, 0),
              size=wx.Size(428, 295), style=wx.TE_MULTILINE,
              value=u'\u63a8\u8350\u53f7\u7801\u53ca\u7406\u7531')

    def __init__(self, parent):
        self._init_ctrls(parent)
        #��������ʾ
        print 'FrameAdvice����'
        
        data_array = readDataFileToArray() #��ȡ��������
        blue_times, blue_step, blue_drop = blueCoumpute(data_array) #��ȡ����������
        blueDatas, adviceDatas, blue_hot, blue_cold = blueAdvice(data_array, blue_times) #��ȡ�������
        
        self.textCtrl1.Clear() #�����Ļ
        self.textCtrl1.SetFont(wx.Font(10, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "")) #��������
        
        last_text = '' #ǰ�ڷ���
        last_text = last_text + '���5�ڿ��������������ݣ�\n'
        for i in range(4, -1, -1):
            last_text = last_text + '%s %s %s %s %s '%(data_array[i][0],data_array[i][7],\
                                                        blueDatas[i]['��ż'],blueDatas[i]['����'],blueDatas[i]['��С'])
            if blueDatas[i]['��������ͬ']=='ͬ':
                last_text = last_text + '��������ͬ '
            else:
                last_text = last_text + '�����ڲ�ͬ '
            if blueDatas[i]['11��������']=='��':
                last_text = last_text + '11������\n'
            else:
                last_text = last_text + '11������\n'

        self.textCtrl1.AppendText(last_text+'\n')#��ʾ���ڷ���
        
        now_text = '' #���ڷ���
        #��ż�Է���------------------------------------------------------------------
        now_text = now_text + '��ż�Է�����\n'
        #-
        if blueDatas[0]['��ż']=='��': #��һ��Ϊ��
            ToOdd = adviceDatas['������']*100.0/(adviceDatas['������']+adviceDatas['����ż']) #������
            ToEven = adviceDatas['����ż']*100.0/(adviceDatas['������']+adviceDatas['����ż']) #����ż
            now_text = now_text + '�������������ĸ���Ϊ��%.2f'%(ToOdd) + '%\n'
            now_text = now_text + '��������ż���ĸ���Ϊ��%.2f'%(ToEven) + '%\n'            
        if blueDatas[0]['��ż']=='ż': #��һ��Ϊż
            ToOdd = adviceDatas['ż����']*100.0/(adviceDatas['ż����']+adviceDatas['ż��ż'])
            ToEven = adviceDatas['ż��ż']*100.0/(adviceDatas['ż����']+adviceDatas['ż��ż'])          
            now_text = now_text + 'ż�����������ĸ���Ϊ��%.2f'%(ToOdd) + '%\n'
            now_text = now_text + 'ż������ż���ĸ���Ϊ��%.2f'%(ToEven) + '%\n'
        #--   
        if blueDatas[0]['��ż']=='��' and blueDatas[1]['��ż']=='��': #��һ��Ϊ�棬����һ��Ϊ��
            ToToOdd = adviceDatas['����������']*100.0/(adviceDatas['����������']+adviceDatas['��������ż']) #��������
            ToToEven = adviceDatas['��������ż']*100.0/(adviceDatas['����������']+adviceDatas['��������ż']) #������ż
            now_text = now_text + '���������������������ĸ���Ϊ��%.2f'%(ToToOdd) + '%\n'
            now_text = now_text + '����������������ż���ĸ���Ϊ��%.2f'%(ToToEven) + '%\n'
        if blueDatas[0]['��ż']=='��' and blueDatas[1]['��ż']=='ż': #��һ��Ϊ�棬����һ��Ϊż
            ToToOdd = adviceDatas['ż��������']*100.0/(adviceDatas['ż��������']+adviceDatas['ż������ż'])
            ToToEven = adviceDatas['ż������ż']*100.0/(adviceDatas['ż��������']+adviceDatas['ż������ż'])
            now_text = now_text + 'ż�������������������ĸ���Ϊ��%.2f'%(ToToOdd) + '%\n'
            now_text = now_text + 'ż��������������ż���ĸ���Ϊ��%.2f'%(ToToEven) + '%\n'             
        if blueDatas[0]['��ż']=='ż' and blueDatas[1]['��ż']=='��': #��һ��Ϊż������һ��Ϊ��
            ToToOdd = adviceDatas['����ż����']*100.0/(adviceDatas['����ż����']+adviceDatas['����ż��ż'])
            ToToEven = adviceDatas['����ż��ż']*100.0/(adviceDatas['����ż����']+adviceDatas['����ż��ż'])
            now_text = now_text + '��������ż�����������ĸ���Ϊ��%.2f'%(ToToOdd) + '%\n'
            now_text = now_text + '��������ż������ż���ĸ���Ϊ��%.2f'%(ToToEven) + '%\n'            
        if blueDatas[0]['��ż']=='ż' and blueDatas[1]['��ż']=='ż': #��һ��Ϊż������һ��Ϊż
            ToToOdd = adviceDatas['ż��ż����']*100.0/(adviceDatas['ż��ż����']+adviceDatas['ż��ż��ż'])
            ToToEven = adviceDatas['ż��ż��ż']*100.0/(adviceDatas['ż��ż����']+adviceDatas['ż��ż��ż'])           
            now_text = now_text + 'ż������ż�����������ĸ���Ϊ��%.2f'%(ToToOdd) + '%\n'
            now_text = now_text + 'ż������ż������ż���ĸ���Ϊ��%.2f'%(ToToEven) + '%\n'         
        #�����Է���------------------------------------------------------------------
        now_text = now_text + '\n�����Է�����\n'
        #-
        if blueDatas[0]['����']=='��': #��һ��Ϊ��
            ToCold = adviceDatas['������']*100.0/(adviceDatas['������']+adviceDatas['������'])
            ToHot = adviceDatas['������']*100.0/(adviceDatas['������']+adviceDatas['������'])
            now_text = now_text + '�Ⱥ�������ŵĸ���Ϊ��%.2f'%(ToCold) + '%\n'
            now_text = now_text + '�Ⱥ������Ⱥŵĸ���Ϊ��%.2f'%(ToHot) + '%\n'
        if blueDatas[0]['����']=='��': #��һ��Ϊ��
            ToCold = adviceDatas['������']*100.0/(adviceDatas['������']+adviceDatas['������'])
            ToHot = adviceDatas['������']*100.0/(adviceDatas['������']+adviceDatas['������'])
            now_text = now_text + '���������ŵĸ���Ϊ��%.2f'%(ToCold) + '%\n'
            now_text = now_text + '��������Ⱥŵĸ���Ϊ��%.2f'%(ToHot) + '%\n'
        #--
        if blueDatas[0]['����']=='��' and blueDatas[1]['����']=='��': #��һ��Ϊ�ȣ�����һ��Ϊ��
            ToToCold = adviceDatas['����������']*100.0/(adviceDatas['����������']+adviceDatas['����������'])
            ToToHot = adviceDatas['����������']*100.0/(adviceDatas['����������']+adviceDatas['����������'])
            now_text = now_text + '�Ⱥ������Ⱥ�������ŵĸ���Ϊ��%.2f'%(ToToCold) + '%\n'
            now_text = now_text + '�Ⱥ������Ⱥ������Ⱥŵĸ���Ϊ��%.2f'%(ToToHot) + '%\n'
        if blueDatas[0]['����']=='��' and blueDatas[1]['����']=='��': #��һ��Ϊ�ȣ�����һ��Ϊ��
            ToToCold = adviceDatas['����������']*100.0/(adviceDatas['����������']+adviceDatas['����������'])
            ToToHot = adviceDatas['����������']*100.0/(adviceDatas['����������']+adviceDatas['����������'])
            now_text = now_text + '�Ⱥ������Ⱥ�������ŵĸ���Ϊ��%.2f'%(ToToCold) + '%\n'
            now_text = now_text + '�Ⱥ������Ⱥ������Ⱥŵĸ���Ϊ��%.2f'%(ToToHot) + '%\n'
        if blueDatas[0]['����']=='��' and blueDatas[1]['����']=='��': #��һ��Ϊ�䣬����һ��Ϊ��
            ToToCold = adviceDatas['����������']*100.0/(adviceDatas['����������']+adviceDatas['����������'])
            ToToHot = adviceDatas['����������']*100.0/(adviceDatas['����������']+adviceDatas['����������'])
            now_text = now_text + '�Ⱥ��������������ŵĸ���Ϊ��%.2f'%(ToToCold) + '%\n'
            now_text = now_text + '�Ⱥ�������������Ⱥŵĸ���Ϊ��%.2f'%(ToToHot) + '%\n'
        if blueDatas[0]['����']=='��' and blueDatas[1]['����']=='��': #��һ��Ϊ�䣬����һ��Ϊ��
            ToToCold = adviceDatas['����������']*100.0/(adviceDatas['����������']+adviceDatas['����������'])
            ToToHot = adviceDatas['����������']*100.0/(adviceDatas['����������']+adviceDatas['����������'])
            now_text = now_text + '����������������ŵĸ���Ϊ��%.2f'%(ToToCold) + '%\n'
            now_text = now_text + '���������������Ⱥŵĸ���Ϊ��%.2f'%(ToToHot) + '%\n'
        #��С�Է���------------------------------------------------------------------
        now_text = now_text + '\n��С�Է�����\n'
        #-
        if blueDatas[0]['��С']=='��': #��һ��Ϊ��
            ToSmall = adviceDatas['����С']*100.0/(adviceDatas['����С']+adviceDatas['������'])
            ToBig = adviceDatas['������']*100.0/(adviceDatas['����С']+adviceDatas['������'])
            now_text = now_text + '�������С�ŵĸ���Ϊ��%.2f'%(ToSmall) + '%\n'
            now_text = now_text + '������Ŵ�ŵĸ���Ϊ��%.2f'%(ToBig) + '%\n'
        if blueDatas[0]['��С']=='С': #��һ��ΪС
            ToSmall = adviceDatas['С��С']*100.0/(adviceDatas['С��С']+adviceDatas['С����'])
            ToBig = adviceDatas['С����']*100.0/(adviceDatas['С��С']+adviceDatas['С����'])
            now_text = now_text + 'С������С�ŵĸ���Ϊ��%.2f'%(ToSmall) + '%\n'
            now_text = now_text + 'С�����Ŵ�ŵĸ���Ϊ��%.2f'%(ToBig) + '%\n'
        #--
        if blueDatas[0]['��С']=='��' and blueDatas[1]['��С']=='��': #��һ��Ϊ������һ��Ϊ��
            ToToSmall = adviceDatas['��������С']*100.0/(adviceDatas['��������С']+adviceDatas['����������'])
            ToToBig = adviceDatas['����������']*100.0/(adviceDatas['��������С']+adviceDatas['����������'])
            now_text = now_text + '������Ŵ������С�ŵĸ���Ϊ��%.2f'%(ToToSmall) + '%\n'
            now_text = now_text + '������Ŵ�����Ŵ�ŵĸ���Ϊ��%.2f'%(ToToBig) + '%\n'
        if blueDatas[0]['��С']=='��' and blueDatas[1]['��С']=='С': #��һ��Ϊ������һ��ΪС
            ToToSmall = adviceDatas['С������С']*100.0/(adviceDatas['С������С']+adviceDatas['С��������'])
            ToToBig = adviceDatas['С��������']*100.0/(adviceDatas['С������С']+adviceDatas['С��������'])
            now_text = now_text + '������Ŵ������С�ŵĸ���Ϊ��%.2f'%(ToToSmall) + '%\n'
            now_text = now_text + '������Ŵ�����Ŵ�ŵĸ���Ϊ��%.2f'%(ToToBig) + '%\n'
        if blueDatas[0]['��С']=='С' and blueDatas[1]['��С']=='��': #��һ��ΪС������һ��Ϊ��
            ToToSmall = adviceDatas['����С��С']*100.0/(adviceDatas['����С��С']+adviceDatas['����С����'])
            ToToBig = adviceDatas['����С����']*100.0/(adviceDatas['����С��С']+adviceDatas['����С����'])
            now_text = now_text + '�������С������С�ŵĸ���Ϊ��%.2f'%(ToToSmall) + '%\n'
            now_text = now_text + '�������С�����Ŵ�ŵĸ���Ϊ��%.2f'%(ToToBig) + '%\n'
        if blueDatas[0]['��С']=='С' and blueDatas[1]['��С']=='С': #��һ��ΪС������һ��ΪС
            ToToSmall = adviceDatas['С��С��С']*100.0/(adviceDatas['С��С��С']+adviceDatas['С��С����'])
            ToToBig = adviceDatas['С��С����']*100.0/(adviceDatas['С��С��С']+adviceDatas['С��С����'])
            now_text = now_text + 'С������С������С�ŵĸ���Ϊ��%.2f'%(ToToSmall) + '%\n'
            now_text = now_text + 'С������С�����Ŵ�ŵĸ���Ϊ��%.2f'%(ToToBig) + '%\n'
        #��ͬ�Է���------------------------------------------------------------------
        now_text = now_text + '\n��ͬ�Է�����\n'
        #-
        if blueDatas[0]['��������ͬ']=='ͬ': #��һ��Ϊͬ
            ToDiff = adviceDatas['ͬ����']*100.0/(adviceDatas['ͬ����']+adviceDatas['ͬ��ͬ'])
            ToSame = adviceDatas['ͬ��ͬ']*100.0/(adviceDatas['ͬ����']+adviceDatas['ͬ��ͬ'])
            now_text = now_text + '��ͬ���Ų�ͬ�ĸ���Ϊ��%.2f'%(ToSame) + '%\n'
            now_text = now_text + '��ͬ������ͬ�ĸ���Ϊ��%.2f'%(ToDiff) + '%\n'
        if blueDatas[0]['��������ͬ']=='��': #��һ��Ϊ��
            ToDiff = adviceDatas['������']*100.0/(adviceDatas['������']+adviceDatas['����ͬ'])
            ToSame = adviceDatas['����ͬ']*100.0/(adviceDatas['������']+adviceDatas['����ͬ'])
            now_text = now_text + '��ͬ���Ų�ͬ�ĸ���Ϊ��%.2f'%(ToSame) + '%\n'
            now_text = now_text + '��ͬ������ͬ�ĸ���Ϊ��%.2f'%(ToDiff) + '%\n'
        #--
        if blueDatas[0]['��������ͬ']=='ͬ' and blueDatas[1]['��������ͬ']=='ͬ': #��һ��Ϊͬ������һ��Ϊͬ
            ToToDiff = adviceDatas['ͬ��ͬ����']*100.0/(adviceDatas['ͬ��ͬ����']+adviceDatas['ͬ��ͬ��ͬ'])
            ToToSame = adviceDatas['ͬ��ͬ��ͬ']*100.0/(adviceDatas['ͬ��ͬ����']+adviceDatas['ͬ��ͬ��ͬ'])
            now_text = now_text + '��ͬ������ͬ���Ų�ͬ�ĸ���Ϊ��%.2f'%(ToToSame) + '%\n'
            now_text = now_text + '��ͬ������ͬ������ͬ�ĸ���Ϊ��%.2f'%(ToToDiff) + '%\n'
        if blueDatas[0]['��������ͬ']=='ͬ' and blueDatas[1]['��������ͬ']=='��': #��һ��Ϊͬ������һ��Ϊ��
            ToToDiff = adviceDatas['����ͬ����']*100.0/(adviceDatas['����ͬ����']+adviceDatas['����ͬ��ͬ'])
            ToToSame = adviceDatas['����ͬ��ͬ']*100.0/(adviceDatas['����ͬ����']+adviceDatas['����ͬ��ͬ'])
            now_text = now_text + '��ͬ������ͬ���Ų�ͬ�ĸ���Ϊ��%.2f'%(ToToSame) + '%\n'
            now_text = now_text + '��ͬ������ͬ������ͬ�ĸ���Ϊ��%.2f'%(ToToDiff) + '%\n'
        if blueDatas[0]['��������ͬ']=='��' and blueDatas[1]['��������ͬ']=='ͬ': #��һ��Ϊ��������һ��Ϊͬ
            ToToDiff = adviceDatas['ͬ��������']*100.0/(adviceDatas['ͬ��������']+adviceDatas['ͬ������ͬ'])
            ToToSame = adviceDatas['ͬ������ͬ']*100.0/(adviceDatas['ͬ��������']+adviceDatas['ͬ������ͬ'])
            now_text = now_text + '��ͬ���Ų�ͬ���Ų�ͬ�ĸ���Ϊ��%.2f'%(ToToSame) + '%\n'
            now_text = now_text + '��ͬ���Ų�ͬ������ͬ�ĸ���Ϊ��%.2f'%(ToToDiff) + '%\n'
        if blueDatas[0]['��������ͬ']=='��' and blueDatas[1]['��������ͬ']=='��': #��һ��Ϊ��������һ��Ϊ��
            ToToDiff = adviceDatas['����������']*100.0/(adviceDatas['����������']+adviceDatas['��������ͬ'])
            ToToSame = adviceDatas['��������ͬ']*100.0/(adviceDatas['����������']+adviceDatas['��������ͬ'])
            now_text = now_text + '��ͬ���Ų�ͬ���Ų�ͬ�ĸ���Ϊ��%.2f'%(ToToSame) + '%\n'
            now_text = now_text + '��ͬ���Ų�ͬ������ͬ�ĸ���Ϊ��%.2f'%(ToToDiff) + '%\n'
        #�����Է���------------------------------------------------------------------
        now_text = now_text + '\n�����Է�����\n'
        #-
        if blueDatas[0]['11��������']=='��': #��һ��Ϊ��
            ToNull = adviceDatas['������']*100.0/(adviceDatas['������']+adviceDatas['������'])
            ToBe = adviceDatas['������']*100.0/(adviceDatas['������']+adviceDatas['������'])
            now_text = now_text + '�к������޺ŵĸ���Ϊ��%.2f'%(ToNull) + '%\n'
            now_text = now_text + '�к������кŵĸ���Ϊ��%.2f'%(ToBe) + '%\n'
        if blueDatas[0]['11��������']=='��': #��һ��Ϊ��
            ToNull = adviceDatas['������']*100.0/(adviceDatas['������']+adviceDatas['������'])
            ToBe = adviceDatas['������']*100.0/(adviceDatas['������']+adviceDatas['������'])
            now_text = now_text + '�޺������޺ŵĸ���Ϊ��%.2f'%(ToNull) + '%\n'
            now_text = now_text + '�޺������кŵĸ���Ϊ��%.2f'%(ToBe) + '%\n'
        #--
        if blueDatas[0]['11��������']=='��' and blueDatas[1]['11��������']=='��': #��һ��Ϊ�У�����һ��Ϊ��
            ToToNull = adviceDatas['����������']*100.0/(adviceDatas['����������']+adviceDatas['����������'])
            ToToBe = adviceDatas['����������']*100.0/(adviceDatas['����������']+adviceDatas['����������'])
            now_text = now_text + '�к������к������޺ŵĸ���Ϊ��%.2f'%(ToToNull) + '%\n'
            now_text = now_text + '�к������к������кŵĸ���Ϊ��%.2f'%(ToToBe) + '%\n'
        if blueDatas[0]['11��������']=='��' and blueDatas[1]['11��������']=='��': #��һ��Ϊ�У�����һ��Ϊ��
            ToToNull = adviceDatas['����������']*100.0/(adviceDatas['����������']+adviceDatas['����������'])
            ToToBe = adviceDatas['����������']*100.0/(adviceDatas['����������']+adviceDatas['����������'])
            now_text = now_text + '�к������к������޺ŵĸ���Ϊ��%.2f'%(ToToNull) + '%\n'
            now_text = now_text + '�к������к������кŵĸ���Ϊ��%.2f'%(ToToBe) + '%\n'
        if blueDatas[0]['11��������']=='��' and blueDatas[1]['11��������']=='��': #��һ��Ϊ�ޣ�����һ��Ϊ��
            ToToNull = adviceDatas['����������']*100.0/(adviceDatas['����������']+adviceDatas['����������'])
            ToToBe = adviceDatas['����������']*100.0/(adviceDatas['����������']+adviceDatas['����������'])
            now_text = now_text + '�к������޺������޺ŵĸ���Ϊ��%.2f'%(ToToNull) + '%\n'
            now_text = now_text + '�к������޺������кŵĸ���Ϊ��%.2f'%(ToToBe) + '%\n'
        if blueDatas[0]['11��������']=='��' and blueDatas[1]['11��������']=='��': #��һ��Ϊ�ޣ�����һ��Ϊ��
            ToToNull = adviceDatas['����������']*100.0/(adviceDatas['����������']+adviceDatas['����������'])
            ToToBe = adviceDatas['����������']*100.0/(adviceDatas['����������']+adviceDatas['����������'])
            now_text = now_text + '�޺������޺������޺ŵĸ���Ϊ��%.2f'%(ToToNull) + '%\n'
            now_text = now_text + '�޺������޺������кŵĸ���Ϊ��%.2f'%(ToToBe) + '%\n'

        self.textCtrl1.AppendText(now_text+'\n')#��ʾ���ڷ���

      
        #�Ƽ�����
        advice_text = '%s���Ƽ����룺'%(int(data_array[0][0])+1) #�����Ƽ�
        
        advice_1 = [] #�Ƽ�����ż�����루�ȶ���һ�£����������ȵ������ɴ���
        advice_2 = [] #�Ƽ������䡱����
        advice_3 = [] #�Ƽ�����С������
        advice_4 = [] #�Ƽ���ͬ��������
        advice_5 = [] #�Ƽ������ޡ�����
        
        blue_odd = ['01','03','05','07','09','11','13','15']
        blue_even = ['02','04','05','06','10','12','14','16']
        #blue_hot = blue_hot #�������blueAdvice����ֱ�ӵõ�
        #blue_cold = blue_cold 
        blue_small = ['01','02','03','04','05','06','07','08']
        blue_big = ['09','10','11','12','13','14','15','16']
        blue_same = [] #ͬ
        blue_diff = [] #��
        blue_null = [] #��
        blue_be = []   #��
        
        #�����ͬ�ţ�+-3��    
        if 1+3<=int(data_array[0][7])<=16-3: #�������
            for i in range(int(data_array[0][7])-3, int(data_array[0][7])+3+1):
                blue_same.append('%.2d'%i)
        if int(data_array[0][7])<1+3: #С��4�����
            for i in range(1, int(data_array[0][7])+3+1):
                blue_same.append('%.2d'%i)
            for j in range(int(data_array[0][7])+16-3, 16+1):
                blue_same.append('%.2d'%j)
        if 16-3<int(data_array[0][7]): #����13�����
            for i in range(int(data_array[0][7])-3, 16+1):
                blue_same.append('%.2d'%i)
            for j in range(1, int(data_array[0][7])-16+3+1):
                blue_same.append('%.2d'%j)
        #�����ͬ��                   
        for i in range(0, 16):
            if '%.2d'%(i+1) not in blue_same:
                blue_diff.append('%.2d'%(i+1))
        #ͳ�Ƴ��к�
        for i in range(0, 11):
            if data_array[i][7] not in blue_be:
                blue_be.append(data_array[i][7])
        #ͳ�Ƴ��޺�
        for i in range(0, 16):
            if '%.2d'%(i+1) not in blue_be:
                blue_null.append('%.2d'%(i+1))
       
        if ToOdd+ToToOdd>ToEven+ToToEven: 
            advice_1 = blue_odd #��
            #advice_text = advice_text + '�� '
        if ToOdd+ToToOdd<ToEven+ToToEven:
            advice_1 = blue_even #ż
            #advice_text = advice_text + 'ż '
        if ToCold+ToToCold>ToHot+ToToHot: 
            advice_2 = blue_cold #��
            #advice_text = advice_text + '�� '
        if ToCold+ToToCold<ToHot+ToToHot:
            advice_2 = blue_hot #��
            #advice_text = advice_text + '�� '            
        if ToSmall+ToToSmall>ToBig+ToToBig: 
            advice_3 = blue_small #С
            #advice_text = advice_text + 'С '
        if ToSmall+ToToSmall<ToBig+ToToBig:
            advice_3 = blue_big #��
            #advice_text = advice_text + '�� '
        if ToSame+ToToSame>ToDiff+ToToDiff:
            advice_4 = blue_same #ͬ
            #advice_text = advice_text + 'ͬ '
        if ToSame+ToToSame<ToDiff+ToToDiff:
            advice_4 = blue_diff #��
            #advice_text = advice_text + '�� '
        if ToBe+ToToBe>ToNull+ToToNull:
            advice_5 = blue_be #��
            #advice_text = advice_text + '�� '
        if ToBe+ToToBe<ToDiff+ToToNull:
            advice_5 = blue_null #��
            #advice_text = advice_text + '�� '
        '''
        print advice_1
        print advice_2
        print advice_3
        print advice_4
        print advice_5
        '''
        in_advice = [0]*16 #���Ƽ������г��ֵĴ���
        for i in range(0, 16):
            if '%.2d'%(i+1) in advice_1:
                in_advice[i] = in_advice[i] + 1
            if '%.2d'%(i+1) in advice_2:
                in_advice[i] = in_advice[i] + 1
            if '%.2d'%(i+1) in advice_3:
                in_advice[i] = in_advice[i] + 1
            if '%.2d'%(i+1) in advice_4:
                in_advice[i] = in_advice[i] + 1
            if '%.2d'%(i+1) in advice_5:
                in_advice[i] = in_advice[i] + 1                 
                
        max_num = [] #������
        min_num = [] #��С����
        for i in range(0, 16):
            if in_advice[i]==max(in_advice): #�����
                max_num.append('%.2d'%(i+1))
            #if in_advice[i]<=1:                 
            if in_advice[i]==min(in_advice): #����С
                min_num.append('%.2d'%(i+1))
        #��������ʾһ��
        print '�����Ƽ�����Ϊ%d��5Ϊ���֣�'%(max(in_advice))                
        #print max_num
        #print min_num
        advice_num = [] #�Ƽ�����
        '''
        for i in range(0, 16):
            if ('%.2d'%(i+1) not in max_num) and ('%.2d'%(i+1) not in min_num):
                advice_num.append('%.2d'%(i+1))
        '''
        for i in range(0, 16):
            if '%.2d'%(i+1) in max_num:
                advice_num.append('%.2d'%(i+1))

        advice_text = advice_text + '\n%s\n'%(str(advice_num))
        advice_text = advice_text + '�����Ƽ�����Ϊ%d��5Ϊ���֣�'%(max(in_advice))
        self.textCtrl1.AppendText(advice_text) #��ʾ�����Ƽ�
        #��������ʾһ��
        print '�Ƽ�����Ϊ:%s'%advice_text



