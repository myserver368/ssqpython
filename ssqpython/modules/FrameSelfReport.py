#! usr/bin/python
# -*- coding:utf-8 -*-
#Boa:Frame:FrameReport
# otherrrr@gmail.com
# 自选数据兑奖查看报告面板

import wx
import os
import locale

def create(parent, fileName, data_array):
    return FrameReport(parent, fileName, data_array)

[wxID_FRAMEREPORT, wxID_FRAMEREPORTTEXTCTRL1, 
] = [wx.NewId() for _init_ctrls in range(2)]

class FrameReport(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAMEREPORT, name=u'FrameSelfReport',
              parent=prnt, pos=wx.Point(329, 221), size=wx.Size(398, 277),
              style=wx.DEFAULT_FRAME_STYLE,
              title=u'\u81ea\u9009\u6570\u636e\u5bf9\u5956')
        self.SetClientSize(wx.Size(390, 250))
        self.SetIcon(wx.Icon(u'pic/report.ico',wx.BITMAP_TYPE_ICO))

        self.textCtrl1 = wx.TextCtrl(id=wxID_FRAMEREPORTTEXTCTRL1,
              name='textCtrl1', parent=self, pos=wx.Point(0, 0),
              size=wx.Size(390, 250), style=wx.TE_MULTILINE,
              value=u'\u663e\u793a\u81ea\u9009\u6570\u636e\u5bf9\u5956\u7ed3\u679c')

    def __init__(self, parent, fileName, data_array):
        self._init_ctrls(parent)
        #命令行提示
        print (u'FrameSelfReport启动').encode(locale.getdefaultlocale()[1])
        #读取自选数据
        f = open(fileName, 'r')
        s = f.readlines()
        f.close()
        #数据处理
        predict_data = []
        for i in range(0, len(s)):
            t = []
            for j in range(0, 7):
                t.append(s[i][0+j*3:2+j*3])
            predict_data.append(t)
        #显示面板清空
        self.textCtrl1.Clear()
        #生成报告
        report = '自选数据兑奖结果:\n[共%d组]\n'%(len(s))
        #判断自选数据是否有篮球
        if predict_data[0][6]=='':
            report = report + '(统计时不包括篮球)\n'
            #统计各球相同的情况
            same = [0,0,0,0,0,0,0]
            #统计所有大于等于4的情况
            big4 = ''
            for j in range(0, len(predict_data)):
                count = 0 #计数
                for k in range(0, 6):
                    if predict_data[j][k] in data_array[0][1:6+1]:
                        count = count + 1
                same[count] = same[count] + 1
                # 记录下所有>=4的情况
                if count>=4:
                    big4 = big4 + '第%d组:%s %s %s %s %s %s中%d个号码\n'%\
                           (j+1,predict_data[j][0],predict_data[j][1],\
                            predict_data[j][2],predict_data[j][3],\
                            predict_data[j][4],predict_data[j][5],\
                            count)
            report = report + '----6球相同%s注\n'%same[6]
            report = report + '----5球相同%s注\n'%same[5]
            report = report + '----4球相同%s注\n'%same[4]
            report = report + '----3球相同%s注\n'%same[3]
            report = report + '----2球相同%s注\n'%same[2]
            report = report + '----1球相同%s注\n'%same[1]
            report = report + '----0球相同%s注\n'%same[0]
            if big4!='':
                report = report + '\n中4个号码以上的有：\n' + big4
        else:
            report = report + '(统计时未考虑快乐星期天和快乐假日!)\n'
            #统计各种中奖情况(共计10种)
            #4+0/5+0/6+0/0+1/1+1/2+1/3+1/4+1/5+1/6+1
            goal = [0,0,0,0,0,0,0,0,0,0]
            #统计各种未中奖的情况（共计4种）
            #0+0/1+0/2+0/3+0
            no_goal = [0,0,0,0]
            #统计中奖金额
            money = 0
            almost = False #奖金是否不正确
            #统计所有中奖情况
            detail = ''            
            for j in range(0, len(predict_data)):
                count_red = 0 #红球计数
                for k in range(0, 6):
                    if predict_data[j][k] in data_array[0][1:6+1]:
                        count_red = count_red + 1
                count_blue = 0 #篮球计数
                if predict_data[j][6]==data_array[0][7]:
                    count_blue = count_blue + 1
                #是否中了篮球
                if count_blue==0:
                    #统计各种未中奖情况
                    if count_red==0:
                        no_goal[0] = no_goal[0] + 1
                    if count_red==1:
                        no_goal[1] = no_goal[1] + 1
                    if count_red==2:
                        no_goal[2] = no_goal[2] + 1
                    if count_red==3:
                        no_goal[3] = no_goal[3] + 1
                    #统计各种中奖情况
                    if count_red==4:
                        goal[0] = goal[0] + 1
                        money = money + 10
                        detail = detail + '第%.2d组:%s %s %s %s %s %s+%s中4+0\n'%\
                                 (j+1,predict_data[j][0],predict_data[j][1],\
                                  predict_data[j][2],predict_data[j][3],\
                                  predict_data[j][4],predict_data[j][5],\
                                  predict_data[j][6])
                    if count_red==5:
                        goal[1] = goal[1] + 1
                        money = money + 200
                        detail = detail + '第%.2d组:%s %s %s %s %s %s+%s中5+0\n'%\
                                 (j+1,predict_data[j][0],predict_data[j][1],\
                                  predict_data[j][2],predict_data[j][3],\
                                  predict_data[j][4],predict_data[j][5],\
                                  predict_data[j][6])                       
                    if count_red==6:
                        goal[2] = goal[2] + 1
                        almost = True
                        money = money + 100000
                        detail = detail + '第%.2d组:%s %s %s %s %s %s+%s中6+0\n'%\
                                 (j+1,predict_data[j][0],predict_data[j][1],\
                                  predict_data[j][2],predict_data[j][3],\
                                  predict_data[j][4],predict_data[j][5],\
                                  predict_data[j][6])                   
                if count_blue==1:
                    if count_red==0:
                        goal[3] = goal[3] + 1
                        money = money + 5
                        detail = detail + '第%.2d组:%s %s %s %s %s %s+%s中0+1\n'%\
                                 (j+1,predict_data[j][0],predict_data[j][1],\
                                  predict_data[j][2],predict_data[j][3],\
                                  predict_data[j][4],predict_data[j][5],\
                                  predict_data[j][6])                     
                    if count_red==1:
                        goal[4] = goal[4] + 1
                        money = money + 5
                        detail = detail + '第%.2d组:%s %s %s %s %s %s+%s中1+1\n'%\
                                 (j+1,predict_data[j][0],predict_data[j][1],\
                                  predict_data[j][2],predict_data[j][3],\
                                  predict_data[j][4],predict_data[j][5],\
                                  predict_data[j][6])                          
                    if count_red==2:
                        goal[5] = goal[5] + 1
                        money = money + 5
                        detail = detail + '第%.2d组:%s %s %s %s %s %s+%s中2+1\n'%\
                                 (j+1,predict_data[j][0],predict_data[j][1],\
                                  predict_data[j][2],predict_data[j][3],\
                                  predict_data[j][4],predict_data[j][5],\
                                  predict_data[j][6])                         
                    if count_red==3:
                        goal[6] = goal[6] + 1
                        money = money + 10
                        detail = detail + '第%.2d组:%s %s %s %s %s %s+%s中3+1\n'%\
                                 (j+1,predict_data[j][0],predict_data[j][1],\
                                  predict_data[j][2],predict_data[j][3],\
                                  predict_data[j][4],predict_data[j][5],\
                                  predict_data[j][6])                          
                    if count_red==4:
                        goal[7] = goal[7] + 1
                        money = money + 200
                        detail = detail + '第%.2d组:%s %s %s %s %s %s+%s中4+1\n'%\
                                 (j+1,predict_data[j][0],predict_data[j][1],\
                                  predict_data[j][2],predict_data[j][3],\
                                  predict_data[j][4],predict_data[j][5],\
                                  predict_data[j][6])                          
                    if count_red==5:
                        goal[8] = goal[8] + 1
                        money = money + 3000
                        detail = detail + '第%.2d组:%s %s %s %s %s %s+%s中5+1\n'%\
                                 (j+1,predict_data[j][0],predict_data[j][1],\
                                  predict_data[j][2],predict_data[j][3],\
                                  predict_data[j][4],predict_data[j][5],\
                                  predict_data[j][6])                          
                    if count_red==6:
                        goal[9] = goal[9] + 1
                        almost = True
                        money = money + 1000000
                        detail = detail + '第%.2d组:%s %s %s %s %s %s+%s中6+1\n'%\
                                 (j+1,predict_data[j][0],predict_data[j][1],\
                                  predict_data[j][2],predict_data[j][3],\
                                  predict_data[j][4],predict_data[j][5],\
                                  predict_data[j][6])                           
            if money==0:
                report = report + '很遗憾，未中奖！\n'
                report = report + '红球0篮球0的情况共:%d组\n'%no_goal[0]
                report = report + '红球1篮球0的情况共:%d组\n'%no_goal[1]
                report = report + '红球2篮球0的情况共:%d组\n'%no_goal[2]
                report = report + '红球3篮球0的情况共:%d组\n'%no_goal[3]
            if money>0 and almost==True:
                report = report + '奖金为:%d元\n'%money
                report = report + '(中大奖了！准确中奖金额请咨询福彩官方)\n'
                report = report + '红球3篮球0的情况共:%d组\n'%no_goal[3]
                report = report + '红球4篮球0的情况共:%d组\n'%goal[0]
                report = report + '红球5篮球0的情况共:%d组\n'%goal[1]
                report = report + '红球6篮球0的情况共:%d组\n'%goal[2]
                report = report + '红球0篮球1的情况共:%d组\n'%goal[3]
                report = report + '红球1篮球1的情况共:%d组\n'%goal[4]
                report = report + '红球2篮球1的情况共:%d组\n'%goal[5]
                report = report + '红球3篮球1的情况共:%d组\n'%goal[6]
                report = report + '红球4篮球1的情况共:%d组\n'%goal[7]
                report = report + '红球5篮球1的情况共:%d组\n'%goal[8]
                report = report + '红球6篮球1的情况共:%d组\n'%goal[9]
                report = report + '\n%s'%detail
            if money>0 and almost==False:
                report = report + '奖金为:%d元\n'%money
                report = report + '红球3篮球0的情况共:%d组\n'%no_goal[3]
                report = report + '红球4篮球0的情况共:%d组\n'%goal[0]
                report = report + '红球5篮球0的情况共:%d组\n'%goal[1]
                report = report + '红球6篮球0的情况共:%d组\n'%goal[2]
                report = report + '红球0篮球1的情况共:%d组\n'%goal[3]
                report = report + '红球1篮球1的情况共:%d组\n'%goal[4]
                report = report + '红球2篮球1的情况共:%d组\n'%goal[5]
                report = report + '红球3篮球1的情况共:%d组\n'%goal[6]
                report = report + '红球4篮球1的情况共:%d组\n'%goal[7]
                report = report + '红球5篮球1的情况共:%d组\n'%goal[8]
                report = report + '红球6篮球1的情况共:%d组\n'%goal[9]
                report = report + '\n%s'%detail
        #将报告添加到显示面板中
        self.textCtrl1.AppendText(report.decode('utf-8'))

        
