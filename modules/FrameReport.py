# -*- coding: cp936 -*-
# otherrrr@gmail.com
# �������ݲ鿴�������

import wx
import os

from modules.DataFileIO import readDataFileToArray
from modules.PredictFileIO import readPredictData
from modules.DataCompute import redOrderCoumput, dataParaCompute

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
        
        #��ȡ��������
        data_array = readDataFileToArray()
        #��ʾ������
        self.textCtrl1.Clear()
        #���㲢�õ����ݲ���
        redOrder, redTimes = redOrderCoumput(data_array)
        data_para_array = dataParaCompute(data_array, redOrder) 
        #����һ�ڵ��ں�
        date = int(data_array[0][0])
        for i in range(0, 3):
            #�ж��Ƿ����Ԥ�����ݣ����3�ڣ������ж��ļ����Ƿ����
            if '%s'%date in os.listdir(os.curdir):
                #��ȡԤ�������ļ���ʹ�õ��Ĺ��������ļ��������ʽ��
                predict_data, predict_filter =readPredictData(date)
                #�ж�Ԥ�������뿪��������ͬ���
                same = [0,0,0,0,0,0,0]
                for j in range(0, len(predict_data)):
                    count = 0 #����
                    for k in range(0, 6):
                        if predict_data[j][k] in data_array[i][1:6+1]:
                            count = count + 1
                    same[count] = same[count] + 1
                #�жϹ��������������
                filter_wrong = [] #��������б�
                wrong_detail = ['��������','Ԥ�ⷶΧ����','Ԥ�ⷶΧ����','ʵ��ֵ'] #������ϸ˵��
                for j in range(0, len(predict_filter)):
                    tmp_1 = predict_filter[j][1] #ʹ�õ��Ĺ�����������
                    tmp_2 = tmp_1.split(' ')[0] #ȥ�����ƺ���Ŀո�
                    tmp_3 = data_para_array[i][tmp_2] #�������ݵĶ�Ӧ����ֵ
                    min_num = int(predict_filter[j][3].split('-')[0]) #ʹ�õ��Ĺ�����������Сֵ
                    max_num = int(predict_filter[j][3].split('-')[1]) #ʹ�õ��Ĺ������������ֵ
                    #�ж��Ƿ���ڵ�����Сֵ��С�ڵ������ֵ���������������������ӵ������б���  
                    if tmp_3<min_num or tmp_3>max_num:
                        wrong_detail = [tmp_2,min_num,max_num,tmp_3]
                        filter_wrong.append(wrong_detail)
                #���ɱ���
                report = ''
                report = report + '====%d��==================\n'%date
                report = report + '��������:%s,%s,%s,%s,%s,%s+%s\n'\
                         %(data_array[i][1],data_array[i][2],data_array[i][3],\
                           data_array[i][4],data_array[i][5],data_array[i][6],data_array[i][7])
                report = report + 'Ԥ������:%s��\n'%(len(predict_data))
                report = report + '----6����ͬ%sע\n'%same[6]
                report = report + '----5����ͬ%sע\n'%same[5]
                report = report + '----4����ͬ%sע\n'%same[4]
                report = report + '----3����ͬ%sע\n'%same[3]
                report = report + '----2����ͬ%sע\n'%same[2]
                report = report + '----1����ͬ%sע\n'%same[1]
                report = report + '----0����ͬ%sע\n'%same[0]
                report = report + '��������:%s��\n'%(len(predict_filter))
                report = report + '----��ȷ:%s��\n'%(len(predict_filter)-len(filter_wrong))
                report = report + '----����:%s��\n'%(len(filter_wrong))
                if len(filter_wrong)!=0: #����д���Ļ�����ʾ֮
                    for j in range(0, len(filter_wrong)):
                        report = report + '--------%s--------Ԥ�ⷶΧ[%s,%s]--ʵ��ֵ(%s)\n'\
                                 %(filter_wrong[j][0],filter_wrong[j][1],filter_wrong[j][2],filter_wrong[j][3],)
                report = report + '==============================='
                #��������ӵ���ʾ�����
                self.textCtrl1.AppendText(report)
                #ֹͣ����
                break
            else:
                self.textCtrl1.AppendText('δ�ҵ�%s��Ԥ�����ݣ�\n\n'%date)
                #�ں�-1����������
                date = date - 1
        #���3��֮��δ�ҵ�����һ����ʾ
        if date==(int(data_array[0][0])-3):
            self.textCtrl1.AppendText('���3�ھ���Ԥ�����ݣ�')
        
