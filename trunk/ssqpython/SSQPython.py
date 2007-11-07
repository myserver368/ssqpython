# -*- coding: cp936 -*-
#!/usr/bin/env python
# otherrrr@gmail.com
# ������

import wx
import modules.FrameMain

import sys
import time
import os
import sqlite3

from modules.FilterFileIO import readFilterFileToArray
from modules.DataCompute import redOrderCoumpute, dataFiltrate
from modules.DataFileIO import readDataFileToArray
from modules.BetFileIO import readBetFileToArray
from modules.PredictFileIO import writePredictData

class SSQPythonApp(wx.App):
    def OnInit(self):
        if len(sys.argv[1:])!=0 and (sys.argv[1:][0]=='-f' or sys.argv[1:][0]=='f'): #�ж��Ƿ��в���(-f)������ֱ�ӹ��ˣ�33����
            #��������ʾһ��
            print '��ʼһ������(ѡ��ȫ��33������'
            #�������к���
            num_pool = [1,2,3,4,5,6,7,8,9,10,11,\
                        12,13,14,15,16,17,18,19,20,21,22,\
                        23,24,25,26,27,28,29,30,31,32,33]
            data_f = []
            pos1 = 0
            for t1 in num_pool[pos1:-5]:
                pos2 = pos1 + 1
                for t2 in num_pool[pos2:-4]:
                    pos3 = pos2 + 1
                    for t3 in num_pool[pos3:-3]:
                        pos4 = pos3 + 1
                        for t4 in num_pool[pos4:-2]:
                            pos5 = pos4 + 1
                            for t5 in num_pool[pos5:-1]:
                                pos6 = pos5 + 1
                                for t6 in num_pool[pos6:]:
                                    data_f.append([t1,t2,t3,t4,t5,t6])
                                pos5 = pos5 + 1
                            pos4 = pos4 + 1
                        pos3 = pos3 + 1
                    pos2 = pos2 + 1
                pos1 = pos1 + 1
            print '�������к���%d��'%(len(data_f))
            #��ȡ��������
            data_array = readDataFileToArray()            
            #��ȡ�̶�Ͷע
            bet_array = readBetFileToArray()            
            #��ȡ��������
            filter_array = readFilterFileToArray()
            #�������������������
            redOrder, redTimes = redOrderCoumpute(data_array)
            #��ʾԤ����ں�
            print 'Ԥ��%d��'%(int(data_array[0][0])+1)
            #��ʼʱ��
            start_time = int(time.time())            
            #��ʼ����
            step = 0            
            for i in range(0, len(filter_array)):
                step = step + 1
                filter_array[step-1][2] = '��' + filter_array[step-1][2][2:]
                data_f = dataFiltrate(data_array, data_f, step, filter_array, redOrder, bet_array)
                if step==1:
                    print '%.2d time=%d num=%d %s'%(step,int(time.time())-start_time,len(data_f),filter_array[step-1][4])
                    last_time = int(time.time())
                else:
                    print '%.2d time=%d num=%d %s'%(step,int(time.time())-last_time,len(data_f),filter_array[step-1][4])
                    last_time = int(time.time())
            #��ֹʱ��
            stop_time = int(time.time())
            #д����
            writePredictData(data_array, data_f, filter_array, num_pool)              
            #��ʾ���ɵ�ע���ͻ��ѵ�ʱ��
            print '������%dע������%d��'%(len(data_f),stop_time-start_time)
              
            return True
        elif len(sys.argv[1:])!=0 and (sys.argv[1:][0]=='-d' or sys.argv[1:][0]=='d'): #�ж��Ƿ��в���(-d)�����򴴽����ݿ�
            '''
            Ԥ�뵱��ʹ�����ݿ���һЩ������ʵ���ϣ����ǣ�
            '''
            print '�˹�����ֹͣ����!'
            exit(0) #����ֹͣ�������ֱ���˳�
            
            #�����Ƿ񲻴���data.db�ļ�
            if 'data.db' in os.listdir("data"):
                #����
                print 'data.db�Ѵ���'
            else:
                #������
                # �������������ݿ�
                con = sqlite3.connect("data/data.db")
                cur = con.cursor()
                # ���ݿⴴ������Ϊdata�ı�
                cur.execute("create table data (����1, ����2, ����3, ����4, ����5, ����6)")
                # ��������
                # 1��һ��һ��Ĳ壨�Ƚ�����
                '''    
                for t1 in range(1, 33+1-5):
                    for t2 in range(t1+1, 33+1-4):
                        for t3 in range(t2+1, 33+1-3):
                            for t4 in range(t3+1, 33+1-2):
                                for t5 in range(t4+1, 33+1-1):
                                    for t6 in range(t5+1, 33+1):
                                        tt = (t1,t2,t3,t4,t5,t6)
                                        #ֱ���������Ƚ�Σ�գ���ν��SQLע��©��
                                        #cur.execute("""insert into data
                                        #           (����1, ����2, ����3, ����4, ����5, ����6)
                                        #           values(?,?,?,?,?,?)""",
                                        #           (t1,t2,t3,t4,t5,t6))
                                        cur.execute("""insert into data
                                                    (����1, ����2, ����3, ����4, ����5, ����6)
                                                    values(?,?,?,?,?,?)""",
                                                    (tt))                            
                '''
                # 2��һ��壨һ������
                data = [] # ����������
                for t1 in range(1, 33+1-5):
                    for t2 in range(t1+1, 33+1-4):
                        for t3 in range(t2+1, 33+1-3):
                            for t4 in range(t3+1, 33+1-2):
                                for t5 in range(t4+1, 33+1-1):
                                    for t6 in range(t5+1, 33+1):
                                        #��һЩ100%�ж�
                                        #1.һ��λ��1��19֮��
                                        #2.����λ��2��24֮��
                                        #3.����λ��3��28֮��
                                        #4.�ĺ�λ��5��31֮��
                                        #5.���λ��7��32֮��
                                        #6.����λ��11��33֮��
                                        data.append((t1,t2,t3,t4,t5,t6))
                print '��������%d��\n'%len(data)
                cur.executemany("""insert into data
                                (����1, ����2, ����3, ����4, ����5, ����6)
                                values (?, ?, ?, ?, ?, ?)""",
                                data)
                # �ύ���������ݿ���
                con.commit()                   
                #�ر����ݿ�
                cur.close() 
                con.close()
      
            return True
        elif len(sys.argv[1:])!=0 and (sys.argv[1:][0]=='-o' or sys.argv[1:][0]=='o'): #�ж��Ƿ��в���(-o)���������ɹ��˲���
            print '�˹���δ�������!'

            return True
        elif len(sys.argv[1:])!=0 and (sys.argv[1:][0]=='-h' or sys.argv[1:][0]=='h'): #�ж��Ƿ��в���(-h)��������ʾ����
            print '    ˫ɫ����Ʊ�������  1.0.0'
            print '       otherrrr@gmail.com'
            print 'http://code.google.com/p/ssqpython/'
            print ''
            print '��������:'
            print '     -f: ֱ�ӿ�ʼȫ������'
            print '     -d: �������ݿ⣨�ݣ�'
            print '     -o: ���ɹ��˲���'
            
            return True
        else:
            self.main = modules.FrameMain.create(None)
            self.main.Show()
            self.SetTopWindow(self.main)
            return True
    
def main():
    application = SSQPythonApp(0)
    application.MainLoop()

if __name__ == '__main__':
    main()
