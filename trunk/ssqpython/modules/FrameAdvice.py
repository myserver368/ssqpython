#Boa:Frame:FrameAdvice
# -*- coding: cp936 -*-
# otherrrr@gmail.com
# 蓝球推荐面板

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
        
        
        data_array = readDataFileToArray() #读取开奖数据
        blue_times, blue_step, blue_drop = blueCoumpute(data_array) #读取篮球出球次数
        blueDatas, adviceDatas, blue_hot, blue_cold = blueAdvice(data_array, blue_times) #读取相关数据
        
        self.textCtrl1.Clear() #清空屏幕
        self.textCtrl1.SetFont(wx.Font(10, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "")) #字体设置
        
        last_text = '' #前期分析
        last_text = last_text + '最近5期开奖篮球的相关数据：\n'
        for i in range(4, -1, -1):
            last_text = last_text + '%s %s %s %s %s '%(data_array[i][0],data_array[i][7],\
                                                        blueDatas[i]['奇偶'],blueDatas[i]['热冷'],blueDatas[i]['大小'])
            if blueDatas[i]['与上期相同']=='同':
                last_text = last_text + '与上期相同 '
            else:
                last_text = last_text + '与上期不同 '
            if blueDatas[i]['11期内有无']=='有':
                last_text = last_text + '11期内有\n'
            else:
                last_text = last_text + '11期内无\n'

        self.textCtrl1.AppendText(last_text+'\n')#显示上期分析
        
        now_text = '' #本期分析
        #奇偶性分析------------------------------------------------------------------
        now_text = now_text + '奇偶性分析：\n'
        #-
        if blueDatas[0]['奇偶']=='奇': #上一期为奇
            ToOdd = adviceDatas['奇连奇']*100.0/(adviceDatas['奇连奇']+adviceDatas['奇连偶']) #连着奇
            ToEven = adviceDatas['奇连偶']*100.0/(adviceDatas['奇连奇']+adviceDatas['奇连偶']) #连着偶
            now_text = now_text + '奇数连着奇数的概率为：%.2f'%(ToOdd) + '%\n'
            now_text = now_text + '奇数连着偶数的概率为：%.2f'%(ToEven) + '%\n'            
        if blueDatas[0]['奇偶']=='偶': #上一期为偶
            ToOdd = adviceDatas['偶连奇']*100.0/(adviceDatas['偶连奇']+adviceDatas['偶连偶'])
            ToEven = adviceDatas['偶连偶']*100.0/(adviceDatas['偶连奇']+adviceDatas['偶连偶'])          
            now_text = now_text + '偶数连着奇数的概率为：%.2f'%(ToOdd) + '%\n'
            now_text = now_text + '偶数连着偶数的概率为：%.2f'%(ToEven) + '%\n'
        #--   
        if blueDatas[0]['奇偶']=='奇' and blueDatas[1]['奇偶']=='奇': #上一期为奇，上上一期为奇
            ToToOdd = adviceDatas['奇连奇连奇']*100.0/(adviceDatas['奇连奇连奇']+adviceDatas['奇连奇连偶']) #连连着奇
            ToToEven = adviceDatas['奇连奇连偶']*100.0/(adviceDatas['奇连奇连奇']+adviceDatas['奇连奇连偶']) #连连着偶
            now_text = now_text + '奇数连着奇数连着奇数的概率为：%.2f'%(ToToOdd) + '%\n'
            now_text = now_text + '奇数连着奇数连着偶数的概率为：%.2f'%(ToToEven) + '%\n'
        if blueDatas[0]['奇偶']=='奇' and blueDatas[1]['奇偶']=='偶': #上一期为奇，上上一期为偶
            ToToOdd = adviceDatas['偶连奇连奇']*100.0/(adviceDatas['偶连奇连奇']+adviceDatas['偶连奇连偶'])
            ToToEven = adviceDatas['偶连奇连偶']*100.0/(adviceDatas['偶连奇连奇']+adviceDatas['偶连奇连偶'])
            now_text = now_text + '偶数连着奇数连着奇数的概率为：%.2f'%(ToToOdd) + '%\n'
            now_text = now_text + '偶数连着奇数连着偶数的概率为：%.2f'%(ToToEven) + '%\n'             
        if blueDatas[0]['奇偶']=='偶' and blueDatas[1]['奇偶']=='奇': #上一期为偶，上上一期为奇
            ToToOdd = adviceDatas['奇连偶连奇']*100.0/(adviceDatas['奇连偶连奇']+adviceDatas['奇连偶连偶'])
            ToToEven = adviceDatas['奇连偶连偶']*100.0/(adviceDatas['奇连偶连奇']+adviceDatas['奇连偶连偶'])
            now_text = now_text + '奇数连着偶数连着奇数的概率为：%.2f'%(ToToOdd) + '%\n'
            now_text = now_text + '奇数连着偶数连着偶数的概率为：%.2f'%(ToToEven) + '%\n'            
        if blueDatas[0]['奇偶']=='偶' and blueDatas[1]['奇偶']=='偶': #上一期为偶，上上一期为偶
            ToToOdd = adviceDatas['偶连偶连奇']*100.0/(adviceDatas['偶连偶连奇']+adviceDatas['偶连偶连偶'])
            ToToEven = adviceDatas['偶连偶连偶']*100.0/(adviceDatas['偶连偶连奇']+adviceDatas['偶连偶连偶'])           
            now_text = now_text + '偶数连着偶数连着奇数的概率为：%.2f'%(ToToOdd) + '%\n'
            now_text = now_text + '偶数连着偶数连着偶数的概率为：%.2f'%(ToToEven) + '%\n'         
        #热冷性分析------------------------------------------------------------------
        now_text = now_text + '\n热冷性分析：\n'
        #-
        if blueDatas[0]['热冷']=='热': #上一期为热
            ToCold = adviceDatas['热连冷']*100.0/(adviceDatas['热连冷']+adviceDatas['热连热'])
            ToHot = adviceDatas['热连热']*100.0/(adviceDatas['热连冷']+adviceDatas['热连热'])
            now_text = now_text + '热号连着冷号的概率为：%.2f'%(ToCold) + '%\n'
            now_text = now_text + '热号连着热号的概率为：%.2f'%(ToHot) + '%\n'
        if blueDatas[0]['热冷']=='冷': #上一期为冷
            ToCold = adviceDatas['冷连冷']*100.0/(adviceDatas['冷连冷']+adviceDatas['冷连热'])
            ToHot = adviceDatas['冷连热']*100.0/(adviceDatas['冷连冷']+adviceDatas['冷连热'])
            now_text = now_text + '冷号连着冷号的概率为：%.2f'%(ToCold) + '%\n'
            now_text = now_text + '冷号连着热号的概率为：%.2f'%(ToHot) + '%\n'
        #--
        if blueDatas[0]['热冷']=='热' and blueDatas[1]['热冷']=='热': #上一期为热，上上一期为热
            ToToCold = adviceDatas['热连热连冷']*100.0/(adviceDatas['热连热连冷']+adviceDatas['热连热连热'])
            ToToHot = adviceDatas['热连热连热']*100.0/(adviceDatas['热连热连冷']+adviceDatas['热连热连热'])
            now_text = now_text + '热号连着热号连着冷号的概率为：%.2f'%(ToToCold) + '%\n'
            now_text = now_text + '热号连着热号连着热号的概率为：%.2f'%(ToToHot) + '%\n'
        if blueDatas[0]['热冷']=='热' and blueDatas[1]['热冷']=='冷': #上一期为热，上上一期为冷
            ToToCold = adviceDatas['冷连热连冷']*100.0/(adviceDatas['冷连热连冷']+adviceDatas['冷连热连热'])
            ToToHot = adviceDatas['冷连热连热']*100.0/(adviceDatas['冷连热连冷']+adviceDatas['冷连热连热'])
            now_text = now_text + '热号连着热号连着冷号的概率为：%.2f'%(ToToCold) + '%\n'
            now_text = now_text + '热号连着热号连着热号的概率为：%.2f'%(ToToHot) + '%\n'
        if blueDatas[0]['热冷']=='冷' and blueDatas[1]['热冷']=='热': #上一期为冷，上上一期为热
            ToToCold = adviceDatas['热连冷连冷']*100.0/(adviceDatas['热连冷连冷']+adviceDatas['热连冷连热'])
            ToToHot = adviceDatas['热连冷连热']*100.0/(adviceDatas['热连冷连冷']+adviceDatas['热连冷连热'])
            now_text = now_text + '热号连着冷号连着冷号的概率为：%.2f'%(ToToCold) + '%\n'
            now_text = now_text + '热号连着冷号连着热号的概率为：%.2f'%(ToToHot) + '%\n'
        if blueDatas[0]['热冷']=='冷' and blueDatas[1]['热冷']=='冷': #上一期为冷，上上一期为冷
            ToToCold = adviceDatas['冷连冷连冷']*100.0/(adviceDatas['冷连冷连冷']+adviceDatas['冷连冷连热'])
            ToToHot = adviceDatas['冷连冷连热']*100.0/(adviceDatas['冷连冷连冷']+adviceDatas['冷连冷连热'])
            now_text = now_text + '冷号连着冷号连着冷号的概率为：%.2f'%(ToToCold) + '%\n'
            now_text = now_text + '冷号连着冷号连着热号的概率为：%.2f'%(ToToHot) + '%\n'
        #大小性分析------------------------------------------------------------------
        now_text = now_text + '\n大小性分析：\n'
        #-
        if blueDatas[0]['大小']=='大': #上一期为大
            ToSmall = adviceDatas['大连小']*100.0/(adviceDatas['大连小']+adviceDatas['大连大'])
            ToBig = adviceDatas['大连大']*100.0/(adviceDatas['大连小']+adviceDatas['大连大'])
            now_text = now_text + '大号连着小号的概率为：%.2f'%(ToSmall) + '%\n'
            now_text = now_text + '大号连着大号的概率为：%.2f'%(ToBig) + '%\n'
        if blueDatas[0]['大小']=='小': #上一期为小
            ToSmall = adviceDatas['小连小']*100.0/(adviceDatas['小连小']+adviceDatas['小连大'])
            ToBig = adviceDatas['小连大']*100.0/(adviceDatas['小连小']+adviceDatas['小连大'])
            now_text = now_text + '小号连着小号的概率为：%.2f'%(ToSmall) + '%\n'
            now_text = now_text + '小号连着大号的概率为：%.2f'%(ToBig) + '%\n'
        #--
        if blueDatas[0]['大小']=='大' and blueDatas[1]['大小']=='大': #上一期为大，上上一期为大
            ToToSmall = adviceDatas['大连大连小']*100.0/(adviceDatas['大连大连小']+adviceDatas['大连大连大'])
            ToToBig = adviceDatas['大连大连大']*100.0/(adviceDatas['大连大连小']+adviceDatas['大连大连大'])
            now_text = now_text + '大号连着大号连着小号的概率为：%.2f'%(ToToSmall) + '%\n'
            now_text = now_text + '大号连着大号连着大号的概率为：%.2f'%(ToToBig) + '%\n'
        if blueDatas[0]['大小']=='大' and blueDatas[1]['大小']=='小': #上一期为大，上上一期为小
            ToToSmall = adviceDatas['小连大连小']*100.0/(adviceDatas['小连大连小']+adviceDatas['小连大连大'])
            ToToBig = adviceDatas['小连大连大']*100.0/(adviceDatas['小连大连小']+adviceDatas['小连大连大'])
            now_text = now_text + '大号连着大号连着小号的概率为：%.2f'%(ToToSmall) + '%\n'
            now_text = now_text + '大号连着大号连着大号的概率为：%.2f'%(ToToBig) + '%\n'
        if blueDatas[0]['大小']=='小' and blueDatas[1]['大小']=='大': #上一期为小，上上一期为大
            ToToSmall = adviceDatas['大连小连小']*100.0/(adviceDatas['大连小连小']+adviceDatas['大连小连大'])
            ToToBig = adviceDatas['大连小连大']*100.0/(adviceDatas['大连小连小']+adviceDatas['大连小连大'])
            now_text = now_text + '大号连着小号连着小号的概率为：%.2f'%(ToToSmall) + '%\n'
            now_text = now_text + '大号连着小号连着大号的概率为：%.2f'%(ToToBig) + '%\n'
        if blueDatas[0]['大小']=='小' and blueDatas[1]['大小']=='小': #上一期为小，上上一期为小
            ToToSmall = adviceDatas['小连小连小']*100.0/(adviceDatas['小连小连小']+adviceDatas['小连小连大'])
            ToToBig = adviceDatas['小连小连大']*100.0/(adviceDatas['小连小连小']+adviceDatas['小连小连大'])
            now_text = now_text + '小号连着小号连着小号的概率为：%.2f'%(ToToSmall) + '%\n'
            now_text = now_text + '小号连着小号连着大号的概率为：%.2f'%(ToToBig) + '%\n'
        #相同性分析------------------------------------------------------------------
        now_text = now_text + '\n相同性分析：\n'
        #-
        if blueDatas[0]['与上期相同']=='同': #上一期为同
            ToDiff = adviceDatas['同连不']*100.0/(adviceDatas['同连不']+adviceDatas['同连同'])
            ToSame = adviceDatas['同连同']*100.0/(adviceDatas['同连不']+adviceDatas['同连同'])
            now_text = now_text + '相同连着不同的概率为：%.2f'%(ToSame) + '%\n'
            now_text = now_text + '相同连着相同的概率为：%.2f'%(ToDiff) + '%\n'
        if blueDatas[0]['与上期相同']=='不': #上一期为不
            ToDiff = adviceDatas['不连不']*100.0/(adviceDatas['不连不']+adviceDatas['不连同'])
            ToSame = adviceDatas['不连同']*100.0/(adviceDatas['不连不']+adviceDatas['不连同'])
            now_text = now_text + '不同连着不同的概率为：%.2f'%(ToSame) + '%\n'
            now_text = now_text + '不同连着相同的概率为：%.2f'%(ToDiff) + '%\n'
        #--
        if blueDatas[0]['与上期相同']=='同' and blueDatas[1]['与上期相同']=='同': #上一期为同，上上一期为同
            ToToDiff = adviceDatas['同连同连不']*100.0/(adviceDatas['同连同连不']+adviceDatas['同连同连同'])
            ToToSame = adviceDatas['同连同连同']*100.0/(adviceDatas['同连同连不']+adviceDatas['同连同连同'])
            now_text = now_text + '相同连着相同连着不同的概率为：%.2f'%(ToToSame) + '%\n'
            now_text = now_text + '相同连着相同连着相同的概率为：%.2f'%(ToToDiff) + '%\n'
        if blueDatas[0]['与上期相同']=='同' and blueDatas[1]['与上期相同']=='不': #上一期为同，上上一期为不
            ToToDiff = adviceDatas['不连同连不']*100.0/(adviceDatas['不连同连不']+adviceDatas['不连同连同'])
            ToToSame = adviceDatas['不连同连同']*100.0/(adviceDatas['不连同连不']+adviceDatas['不连同连同'])
            now_text = now_text + '相同连着相同连着不同的概率为：%.2f'%(ToToSame) + '%\n'
            now_text = now_text + '相同连着相同连着相同的概率为：%.2f'%(ToToDiff) + '%\n'
        if blueDatas[0]['与上期相同']=='不' and blueDatas[1]['与上期相同']=='同': #上一期为不，上上一期为同
            ToToDiff = adviceDatas['同连不连不']*100.0/(adviceDatas['同连不连不']+adviceDatas['同连不连同'])
            ToToSame = adviceDatas['同连不连同']*100.0/(adviceDatas['同连不连不']+adviceDatas['同连不连同'])
            now_text = now_text + '相同连着不同连着不同的概率为：%.2f'%(ToToSame) + '%\n'
            now_text = now_text + '相同连着不同连着相同的概率为：%.2f'%(ToToDiff) + '%\n'
        if blueDatas[0]['与上期相同']=='不' and blueDatas[1]['与上期相同']=='不': #上一期为不，上上一期为不
            ToToDiff = adviceDatas['不连不连不']*100.0/(adviceDatas['不连不连不']+adviceDatas['不连不连同'])
            ToToSame = adviceDatas['不连不连同']*100.0/(adviceDatas['不连不连不']+adviceDatas['不连不连同'])
            now_text = now_text + '不同连着不同连着不同的概率为：%.2f'%(ToToSame) + '%\n'
            now_text = now_text + '不同连着不同连着相同的概率为：%.2f'%(ToToDiff) + '%\n'
        #有无性分析------------------------------------------------------------------
        now_text = now_text + '\n有无性分析：\n'
        #-
        if blueDatas[0]['11期内有无']=='有': #上一期为有
            ToNull = adviceDatas['有连无']*100.0/(adviceDatas['有连无']+adviceDatas['有连有'])
            ToBe = adviceDatas['有连有']*100.0/(adviceDatas['有连无']+adviceDatas['有连有'])
            now_text = now_text + '有号连着无号的概率为：%.2f'%(ToNull) + '%\n'
            now_text = now_text + '有号连着有号的概率为：%.2f'%(ToBe) + '%\n'
        if blueDatas[0]['11期内有无']=='无': #上一期为无
            ToNull = adviceDatas['无连无']*100.0/(adviceDatas['无连无']+adviceDatas['无连有'])
            ToBe = adviceDatas['无连有']*100.0/(adviceDatas['无连无']+adviceDatas['无连有'])
            now_text = now_text + '无号连着无号的概率为：%.2f'%(ToNull) + '%\n'
            now_text = now_text + '无号连着有号的概率为：%.2f'%(ToBe) + '%\n'
        #--
        if blueDatas[0]['11期内有无']=='有' and blueDatas[1]['11期内有无']=='有': #上一期为有，上上一期为有
            ToToNull = adviceDatas['有连有连无']*100.0/(adviceDatas['有连有连无']+adviceDatas['有连有连有'])
            ToToBe = adviceDatas['有连有连有']*100.0/(adviceDatas['有连有连无']+adviceDatas['有连有连有'])
            now_text = now_text + '有号连着有号连着无号的概率为：%.2f'%(ToToNull) + '%\n'
            now_text = now_text + '有号连着有号连着有号的概率为：%.2f'%(ToToBe) + '%\n'
        if blueDatas[0]['11期内有无']=='有' and blueDatas[1]['11期内有无']=='无': #上一期为有，上上一期为无
            ToToNull = adviceDatas['无连有连无']*100.0/(adviceDatas['无连有连无']+adviceDatas['无连有连有'])
            ToToBe = adviceDatas['无连有连有']*100.0/(adviceDatas['无连有连无']+adviceDatas['无连有连有'])
            now_text = now_text + '有号连着有号连着无号的概率为：%.2f'%(ToToNull) + '%\n'
            now_text = now_text + '有号连着有号连着有号的概率为：%.2f'%(ToToBe) + '%\n'
        if blueDatas[0]['11期内有无']=='无' and blueDatas[1]['11期内有无']=='有': #上一期为无，上上一期为有
            ToToNull = adviceDatas['有连无连无']*100.0/(adviceDatas['有连无连无']+adviceDatas['有连无连有'])
            ToToBe = adviceDatas['有连无连有']*100.0/(adviceDatas['有连无连无']+adviceDatas['有连无连有'])
            now_text = now_text + '有号连着无号连着无号的概率为：%.2f'%(ToToNull) + '%\n'
            now_text = now_text + '有号连着无号连着有号的概率为：%.2f'%(ToToBe) + '%\n'
        if blueDatas[0]['11期内有无']=='无' and blueDatas[1]['11期内有无']=='无': #上一期为无，上上一期为无
            ToToNull = adviceDatas['无连无连无']*100.0/(adviceDatas['无连无连无']+adviceDatas['无连无连有'])
            ToToBe = adviceDatas['无连无连有']*100.0/(adviceDatas['无连无连无']+adviceDatas['无连无连有'])
            now_text = now_text + '无号连着无号连着无号的概率为：%.2f'%(ToToNull) + '%\n'
            now_text = now_text + '无号连着无号连着有号的概率为：%.2f'%(ToToBe) + '%\n'

        self.textCtrl1.AppendText(now_text+'\n')#显示本期分析

      
        #推荐估算
        advice_text = '%s期推荐号码：'%(int(data_array[0][0])+1) #最终推荐
        
        advice_1 = [] #推荐“奇偶”号码（先定义一下，以免出现相等的情况造成错误）
        advice_2 = [] #推荐“热冷”号码
        advice_3 = [] #推荐“大小”号码
        advice_4 = [] #推荐“同不”号码
        advice_5 = [] #推荐“有无”号码
        
        blue_odd = ['01','03','05','07','09','11','13','15']
        blue_even = ['02','04','05','06','10','12','14','16']
        #blue_hot = blue_hot #热冷会在blueAdvice里面直接得到
        #blue_cold = blue_cold 
        blue_small = ['01','02','03','04','05','06','07','08']
        blue_big = ['09','10','11','12','13','14','15','16']
        blue_same = [] #同
        blue_diff = [] #不
        blue_null = [] #有
        blue_be = []   #无
        
        #算出相同号（+-3）    
        if 1+3<=int(data_array[0][7])<=16-3: #正常情况
            for i in range(int(data_array[0][7])-3, int(data_array[0][7])+3+1):
                blue_same.append('%.2d'%i)
        if int(data_array[0][7])<1+3: #小与4的情况
            for i in range(1, int(data_array[0][7])+3+1):
                blue_same.append('%.2d'%i)
            for j in range(int(data_array[0][7])+16-3, 16+1):
                blue_same.append('%.2d'%j)
        if 16-3<int(data_array[0][7]): #大于13的情况
            for i in range(int(data_array[0][7])-3, 16+1):
                blue_same.append('%.2d'%i)
            for j in range(1, int(data_array[0][7])-16+3+1):
                blue_same.append('%.2d'%j)
        #算出不同号                   
        for i in range(0, 16):
            if '%.2d'%(i+1) not in blue_same:
                blue_diff.append('%.2d'%(i+1))
        #统计出有号
        for i in range(0, 11):
            if data_array[i][7] not in blue_be:
                blue_be.append(data_array[i][7])
        #统计出无号
        for i in range(0, 16):
            if '%.2d'%(i+1) not in blue_be:
                blue_null.append('%.2d'%(i+1))
       
        if ToOdd+ToToOdd>ToEven+ToToEven: 
            advice_1 = blue_odd #奇
            #advice_text = advice_text + '奇 '
        if ToOdd+ToToOdd<ToEven+ToToEven:
            advice_1 = blue_even #偶
            #advice_text = advice_text + '偶 '
        if ToCold+ToToCold>ToHot+ToToHot: 
            advice_2 = blue_cold #冷
            #advice_text = advice_text + '冷 '
        if ToCold+ToToCold<ToHot+ToToHot:
            advice_2 = blue_hot #热
            #advice_text = advice_text + '热 '            
        if ToSmall+ToToSmall>ToBig+ToToBig: 
            advice_3 = blue_small #小
            #advice_text = advice_text + '小 '
        if ToSmall+ToToSmall<ToBig+ToToBig:
            advice_3 = blue_big #大
            #advice_text = advice_text + '大 '
        if ToSame+ToToSame>ToDiff+ToToDiff:
            advice_4 = blue_same #同
            #advice_text = advice_text + '同 '
        if ToSame+ToToSame<ToDiff+ToToDiff:
            advice_4 = blue_diff #不
            #advice_text = advice_text + '不 '
        if ToBe+ToToBe>ToNull+ToToNull:
            advice_5 = blue_be #有
            #advice_text = advice_text + '有 '
        if ToBe+ToToBe<ToDiff+ToToNull:
            advice_5 = blue_null #无
            #advice_text = advice_text + '无 '
        '''
        print advice_1
        print advice_2
        print advice_3
        print advice_4
        print advice_5
        '''
        in_advice = [0]*16 #在推荐条件中出现的次数
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
                
        max_num = [] #最大号码
        min_num = [] #最小号码
        for i in range(0, 16):
            #if in_advice[i]>=4: 
            if in_advice[i]==max(in_advice): #是最大
                max_num.append('%.2d'%(i+1))
            #if in_advice[i]<=1:                 
            if in_advice[i]==min(in_advice): #是最小
                min_num.append('%.2d'%(i+1))
        #print max_num
        #print min_num
        advice_num = [] #推荐号码
        for i in range(0, 16):
            if ('%.2d'%(i+1) not in max_num) and ('%.2d'%(i+1) not in min_num):
                advice_num.append('%.2d'%(i+1))

        advice_text = advice_text + '\n%s\n'%(str(advice_num))
        self.textCtrl1.AppendText(advice_text) #显示最终推荐



