#! usr/bin/python
# -*- coding:utf-8 -*-
#Boa:Frame:FrameReport
# otherrrr@gmail.com
# 过滤数据查看报告面板

import wx
import os
import locale

from DataFileIO import readDataFileToArray
from PredictFileIO import readPredictData
from BetFileIO import readBetFileToArray
from DataCompute import redOrderCoumpute, dataParaCompute

def create(parent):
    return FrameReport(parent)

[wxID_FRAMEREPORT, wxID_FRAMEREPORTTEXTCTRL1, 
] = [wx.NewId() for _init_ctrls in range(2)]

class FrameReport(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAMEREPORT, name=u'FrameReport',
              parent=prnt, pos=wx.Point(329, 221), size=wx.Size(398, 277),
              style=wx.DEFAULT_FRAME_STYLE,
              title=u'\u9884\u6d4b\u6570\u636e\u5bf9\u5956')
        self.SetClientSize(wx.Size(390, 250))
        self.SetIcon(wx.Icon(u'pic/report.ico',
              wx.BITMAP_TYPE_ICO))

        self.textCtrl1 = wx.TextCtrl(id=wxID_FRAMEREPORTTEXTCTRL1,
              name='textCtrl1', parent=self, pos=wx.Point(0, 0),
              size=wx.Size(390, 250), style=wx.TE_MULTILINE,
              value=u'\u663e\u793a\u9884\u6d4b\u6570\u636e\u5bf9\u5956\u7ed3\u679c')

    def __init__(self, parent):
        self._init_ctrls(parent)
        #命令行提示
        print (u'FrameReport启动').encode(locale.getdefaultlocale()[1])
        
        #读取开奖数据
        data_array = readDataFileToArray()
        #显示面板清空
        self.textCtrl1.Clear()
        #计算并得到数据参数
        redOrder, redTimes = redOrderCoumpute(data_array)
        bet_array = readBetFileToArray()
        data_para_array = dataParaCompute(data_array, redOrder, bet_array) 
        #最新一期的期号
        #date = int(data_array[0][0])
        for i in range(0, len(data_array)):#20080309--10期改成所有期
            date = int(data_array[i][0])
            #判断是否存在预测数据（最近800期），即判断文件夹是否存在
            if '%s'%date in os.listdir(os.curdir):
                #读取预测数据文件和使用到的过滤条件文件（数组格式）
                predict_data, predict_filter, select_num =readPredictData(date)
                #判断预测数据与开奖号码相同情况
                same = [0,0,0,0,0,0,0]
                #20080309（添加>5的注数显示）
                msg5 = '5球相同以上的：\n'
                for j in range(0, len(predict_data)):
                    count = 0 #计数
                    for k in range(0, 6):
                        if predict_data[j][k] in data_array[i][1:6+1]:
                            count = count + 1
                    same[count] = same[count] + 1
                    #在命令行窗口显示>=5的投注
                    if count>=5:
                        print predict_data[j],j+1
                        #20080309
                        msg5 = msg5 + '%s---第%s行\n'%(predict_data[j],j+1)
                #判断过滤条件正误情况
                filter_wrong = [] #错误情况列表
                wrong_detail = ['条件名称','预测范围下限','预测范围上限','实际值'] #错误详细说明
                for j in range(0, len(predict_filter)):
                    tmp_1 = predict_filter[j][1] #使用到的过滤条件名称
                    tmp_2 = tmp_1.split(' ')[0] #去掉名称后面的空格
                    tmp_3 = data_para_array[i][tmp_2] #开奖数据的对应参数值
                    min_num = int(predict_filter[j][3].split('-')[0]) #使用到的过滤条件的最小值
                    max_num = int(predict_filter[j][3].split('-')[1]) #使用到的过滤条件的最大值
                    #判断是否大于等于最小值，小于等于最大值，如果不符合条件，则添加到错误列表中  
                    if tmp_3<min_num or tmp_3>max_num:
                        wrong_detail = [tmp_2,min_num,max_num,tmp_3]
                        filter_wrong.append(wrong_detail)
                #生成报告
                report = ''
                report = report + '=%d期预测数据兑奖=\n'%date
                report = report + '开奖号码:%s,%s,%s,%s,%s,%s+%s\n'\
                         %(data_array[i][1],data_array[i][2],data_array[i][3],\
                           data_array[i][4],data_array[i][5],data_array[i][6],data_array[i][7])
                report = report + '预测数据:%s组\n'%(len(predict_data))
                report = report + '选择了%d个红球\n'%(len(select_num))
                for j in range(0, 6):#看看哪几个球没选上
                    if data_array[i][j+1] not in select_num:
                        report = report + '漏选了*' + data_array[i][j+1]+'*\n'
                report = report + '----6球相同*%s注*\n'%same[6]
                report = report + '----5球相同*%s注*\n'%same[5]
                report = report + '----4球相同*%s注*\n'%same[4]
                report = report + '----3球相同%s注\n'%same[3]
                report = report + '----2球相同%s注\n'%same[2]
                report = report + '----1球相同%s注\n'%same[1]
                report = report + '----0球相同%s注\n'%same[0]
                report = report + '使用过滤条件:%s组\n'%(len(predict_filter))
                report = report + '----正确:%s组\n'%(len(predict_filter)-len(filter_wrong))
                report = report + '----错误:%s组\n'%(len(filter_wrong))
                if len(filter_wrong)!=0: #如果有错误的话就显示之
                    for j in range(0, len(filter_wrong)):
                        report = report + '--------%s--------预测范围[%s,%s]--实际值(%s)\n'\
                                 %(filter_wrong[j][0],filter_wrong[j][1],filter_wrong[j][2],filter_wrong[j][3],)
                #20080309
                report = report + msg5 + '\n'
                #将报告添加到显示面板中
                self.textCtrl1.AppendText(report.decode('utf-8'))
                #停止查找
                #break
            #date = date - 1
            #else:
                #self.textCtrl1.AppendText(u'未找到%s期预测数据！\n\n'%date)
                #期号-1，继续查找
                #date = date - 1
        #如果10期之后还未找到，给一个提示
        #if date==(int(data_array[0][0])-800):
         #   self.textCtrl1.AppendText(u'目录下无最近800期预测数据！')
        # 如果没有任何数据，给一个提示（2008.04.07）
        if self.textCtrl1.GetValue()=='':
            self.textCtrl1.AppendText(u'目录下无任何预测数据！\n（格式应为：200XABC，即只有7位数字）')
