#! usr/bin/env python
# -*- coding:utf-8 -*-
# otherrrr@gmail.com
# 主程序

import wx
import modules.FrameMain

import sys
import time
import os
#import sqlite3 #停止开发SQL相关功能

from modules.FilterFileIO import readFilterFileToArray
from modules.DataCompute import redOrderCoumpute, dataFiltrate
from modules.DataFileIO import readDataFileToArray
from modules.BetFileIO import readBetFileToArray
from modules.PredictFileIO import writePredictData
from modules.PredictFileIO import readPredictData

class SSQPythonApp(wx.App):
    def OnInit(self):
        if len(sys.argv[1:])!=0 and (sys.argv[1:][0]=='-f' or sys.argv[1:][0]=='f'): #判断是否有参数(-f)，有则直接过滤（33个球）
            #命令行显示一下
            print u'开始一步过滤(选择全部33个红球)……'
            #生成所有号码
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
            print u'生成所有号码%d组'%(len(data_f))
            #读取开奖数据
            data_array = readDataFileToArray()            
            #读取固定投注
            bet_array = readBetFileToArray()            
            #读取过滤条件
            filter_array = readFilterFileToArray()
            #计算出球次数并排列球号
            redOrder, redTimes = redOrderCoumpute(data_array)
            #显示预测的期号
            print u'预测%d期'%(int(data_array[0][0])+1)
            #开始时间
            start_time = int(time.time())            
            #开始过滤
            step = 0            
            for i in range(0, len(filter_array)):
                step = step + 1
                #filter_array[step-1][2] = '是' + filter_array[step-1][2][2:]
                filter_array[step-1][2] = u'是      ' #utf-8 20071201
                data_f_down = [] #20071225
                # 20080526 #不包括“**间隔”、“除*余*”
##                if step<12 or (step>18 and step<20) or step>44: 
##                    data_f, data_f_down = dataFiltrate(data_array, data_f, step, filter_array, redOrder, bet_array)
                data_f, data_f_down = dataFiltrate(data_array, data_f, step, filter_array, redOrder, bet_array)
                if step==1:
                    #print u'%.2d time=%d num=%d %s'%(step,int(time.time())-start_time,len(data_f),filter_array[step-1][4]) #windows
                    print u'%.2d time=%d num=%d %s'\
                          %(step,int(time.time())-start_time,len(data_f),filter_array[step-1][4].decode('utf-8')) #linux
                    last_time = int(time.time())
                else:
                    print u'%.2d time=%d num=%d %s'\
                          %(step,int(time.time())-last_time,len(data_f),filter_array[step-1][4].decode('utf-8'))
                    last_time = int(time.time())
            #终止时间
            stop_time = int(time.time())
            #写数据
            writePredictData(data_array, data_f, filter_array, num_pool)              
            #提示生成的注数和花费的时间
            print u'共生成%d注，花费%d秒'%(len(data_f),stop_time-start_time)
              
            return True
        elif len(sys.argv[1:])!=0 and (sys.argv[1:][0]=='-d' or sys.argv[1:][0]=='d'): #判断是否有参数(-d)，有则创建数据库
            '''
            预想当中使用数据库会快一些，但是实际上，不是！
            '''
            print u'此功能已停止开发!'
            exit(0) #停止开发，直接退出
            
            #查找是否不存在data.db文件
            if 'data.db' in os.listdir("data"):
                #存在
                print 'data.db已存在'
            else:
                #不存在
                # 创建并连接数据库
                con = sqlite3.connect("data/data.db")
                cur = con.cursor()
                # 数据库创建中名为data的表
                cur.execute("create table data (红球1, 红球2, 红球3, 红球4, 红球5, 红球6)")
                # 插入数据
                # 1、一组一组的插（比较慢）
                '''    
                for t1 in range(1, 33+1-5):
                    for t2 in range(t1+1, 33+1-4):
                        for t3 in range(t2+1, 33+1-3):
                            for t4 in range(t3+1, 33+1-2):
                                for t5 in range(t4+1, 33+1-1):
                                    for t6 in range(t5+1, 33+1):
                                        tt = (t1,t2,t3,t4,t5,t6)
                                        #直接这样做比较危险，所谓的SQL注入漏洞
                                        #cur.execute("""insert into data
                                        #           (红球1, 红球2, 红球3, 红球4, 红球5, 红球6)
                                        #           values(?,?,?,?,?,?)""",
                                        #           (t1,t2,t3,t4,t5,t6))
                                        cur.execute("""insert into data
                                                    (红球1, 红球2, 红球3, 红球4, 红球5, 红球6)
                                                    values(?,?,?,?,?,?)""",
                                                    (tt))                            
                '''
                # 2、一起插（一样慢）
                data = [] # 先生成数据
                for t1 in range(1, 33+1-5):
                    for t2 in range(t1+1, 33+1-4):
                        for t3 in range(t2+1, 33+1-3):
                            for t4 in range(t3+1, 33+1-2):
                                for t5 in range(t4+1, 33+1-1):
                                    for t6 in range(t5+1, 33+1):
                                        #加一些100%判断
                                        #1.一号位在1－19之间
                                        #2.二号位在2－24之间
                                        #3.三号位在3－28之间
                                        #4.四号位在5－31之间
                                        #5.五号位在7－32之间
                                        #6.六号位在11－33之间
                                        data.append((t1,t2,t3,t4,t5,t6))
                print '生成数据%d组\n'%len(data)
                cur.executemany("""insert into data
                                (红球1, 红球2, 红球3, 红球4, 红球5, 红球6)
                                values (?, ?, ?, ?, ?, ?)""",
                                data)
                # 提交操作到数据库中
                con.commit()                   
                #关闭数据库
                cur.close() 
                con.close()
      
            return True
        elif len(sys.argv[1:])!=0 and (sys.argv[1:][0]=='-o' or sys.argv[1:][0]=='o'): #判断是否有参数(-o)，有则生成过滤参数
            print u'此功能未开发完成!'

            return True
        elif len(sys.argv[1:])!=0 and (sys.argv[1:][0]=='-s' or sys.argv[1:][0]=='s'): #判断是否有参数(-s)，有则直接缩水
            print u'开始一步缩水...'
            #读取开奖数据
            data_array = readDataFileToArray()
            #数据最新一期的期号
            date = int(data_array[0][0])
            #判断是否存在预测数据，即判断文件夹是否存在
            if '%s'%(date+1) not in os.listdir(os.curdir):
                print u'没有找到对应文件夹:%s'%(date+1)
            else:
                #求得第2个缩水条件
                try: # 2008.08.16加（主要是防止没有缩水条件.txt造成的错误）
                    f = open(u'data/缩水条件.txt', 'r')
                    s = f.readlines()
                    f.close()
                    m4 = []
                    for i in range(0, len(s)):
                        t = []
                        for j in range(0, 4):
                            t.append(s[i][j*3:j*3+2])
                        m4.append(t)
                    print u'四元组个数: %d'%len(m4)
                    print u'每个四元组分布个数在0～1之间'
                    #读取过滤数据
                    predict_data, predict_filter, select_num =readPredictData(date+1)
                    print u'预测数据: %d组'%len(predict_data)
                    data_s2 = [] #使用缩水条件2后的数据
                    for i in range(0, len(predict_data)):
                        Judge = True
                        for j in range(0, len(m4)):
                            option = 0
                            for k in range(0, 4):
                                if m4[j][k] in predict_data[i]:
                                    option = option + 1
                            if option>2:
                                Judge = False
                                break
                        if Judge:
                            data_s2.append(predict_data[i])
                        if i%4000==0:
                            print i, len(data_s2)
                    print u'缩水后的数据: %d组'%len(data_s2)
                    #写出生成数据
                    print u'写入文件:%s/%s缩水数据.txt'%(date+1,date+1)
                    f = open(u'%s/%s缩水数据.txt'%(date+1,date+1), 'w')
                    for i in range(0, len(data_s2)):
                        f.write('%s %s %s %s %s %s\n'\
                                %(data_s2[i][0],data_s2[i][1],data_s2[i][2],data_s2[i][3],data_s2[i][4],data_s2[i][5]))
                    f.close()
                except:
                    print u'未找到缩水条件.txt'
            return True
        # 20080526 #判断是否有参数(-a)，有则读取“四个红球.txt”，并过滤（不包括“**间隔”、“除*余*”）
        elif len(sys.argv[1:])!=0 and (sys.argv[1:][0]=='-a' or sys.argv[1:][0]=='a'): 
            #命令行显示一下
            print u'开始四个红球过滤……'
            #读取4go.txt
            f = open(u'data/四个红球.txt', 'r')
            s = f.readlines()
            f.close()
            data_f = []
            for i in range(0, len(s)):
                t = s[i].split(']')[0].split('[')[1].split(', ')
                tt = []
                for j in range(0, len(t)):
                    tt.append(int(t[j]))
                data_f.append(tt)
            print u'读取到数据%d组'%len(data_f)
            #读取开奖数据
            data_array = readDataFileToArray()            
            #读取固定投注
            bet_array = readBetFileToArray()            
            #读取过滤条件
            filter_array = readFilterFileToArray()
            #计算出球次数并排列球号
            redOrder, redTimes = redOrderCoumpute(data_array)
            #显示预测的期号
            print u'预测%d期'%(int(data_array[0][0])+1)
            #开始时间
            start_time = int(time.time())            
            #开始过滤
            step = 0            
            for i in range(0, len(filter_array)):
                step = step + 1
                #filter_array[step-1][2] = '是' + filter_array[step-1][2][2:]
                filter_array[step-1][2] = u'是      ' #utf-8 20071201
                data_f_down = [] #20071225
##                if step<12 or (step>18 and step<20) or step>44: #不包括“**间隔”、“除*余*”
##                    data_f, data_f_down = dataFiltrate(data_array, data_f, step, filter_array, redOrder, bet_array)
                data_f, data_f_down = dataFiltrate(data_array, data_f, step, filter_array, redOrder, bet_array)
                if step==1:
                    #print u'%.2d time=%d num=%d %s'%(step,int(time.time())-start_time,len(data_f),filter_array[step-1][4]) #windows
                    print u'%.2d time=%d num=%d %s'\
                          %(step,int(time.time())-start_time,len(data_f),filter_array[step-1][4].decode('utf-8')) #linux
                    last_time = int(time.time())
                else:
                    print u'%.2d time=%d num=%d %s'\
                          %(step,int(time.time())-last_time,len(data_f),filter_array[step-1][4].decode('utf-8'))
                    last_time = int(time.time())
            #终止时间
            stop_time = int(time.time())         
            #提示生成的注数和花费的时间
            print u'共生成%d注，花费%d秒'%(len(data_f),stop_time-start_time)
            #提示过滤后的注数
            for i in range(0, len(data_f)):
                print data_f[i]
              
            return True
        # 20080526 #判断是否有参数(-b)，有则读取“四个红球.txt”，并缩水
        elif len(sys.argv[1:])!=0 and (sys.argv[1:][0]=='-b' or sys.argv[1:][0]=='b'):
            #命令行显示一下
            print u'开始四个红球过滤……'
            #读取4go.txt
            f = open(u'data/四个红球.txt', 'r')
            s = f.readlines()
            f.close()
            data_f = []
            for i in range(0, len(s)):
                t = s[i].split(']')[0].split('[')[1].split(', ')
                tt = []
                for j in range(0, len(t)):
                    tt.append('%.2d'%int(t[j]))
                data_f.append(tt)
            print u'读取到数据%d组'%len(data_f)
            #读取开奖数据
            data_array = readDataFileToArray()
            #数据最新一期的期号
            date = int(data_array[0][0])
            #读取缩水条件
            f = open(u'data/缩水条件.txt', 'r')
            s = f.readlines()
            f.close()
            m4 = []
            for i in range(0, len(s)):
                t = []
                for j in range(0, 4):
                    t.append(s[i][j*3:j*3+2])
                m4.append(t)
            print u'四元组个数: %d'%len(m4)
            print u'每个四元组分布个数在0～2之间'
            #缩水
            predict_data = data_f
            data_s2 = [] #使用缩水条件2后的数据
            for i in range(0, len(predict_data)):
                Judge = True
                for j in range(0, len(m4)):
                    option = 0
                    for k in range(0, 4):
                        if m4[j][k] in predict_data[i]:
                            option = option + 1
                    if option>2:
                        Judge = False
                        break
                if Judge:
                    data_s2.append(predict_data[i])
##                if i%4000==0:
##                    print i, len(data_s2)
            print u'缩水后的数据: %d组'%len(data_s2)
            for d in data_s2:
                print d

            return True
        # 20080526 #判断是否有参数(-e)，有则自选过滤 
        elif len(sys.argv[1:])!=0 and (sys.argv[1:][0]=='-e' or sys.argv[1:][0]=='e'):
            # 命令行提示一下
            print u'开始自选过滤...'

            #读取开奖数据
            data_array = readDataFileToArray()
            #数据最新一期的期号
            date = int(data_array[0][0])
            #判断是否存在预测数据，即判断文件夹是否存在
            if '%s'%(date+1) not in os.listdir(os.curdir):
                print u'没有找到对应文件夹:%s'%(date+1)
            else:
                # 设定被过滤的文件名
                _dir = '%s'%(date+1)
                file_name1 = u'%s预测数据.txt'%_dir
                file_name2 = u'%s缩水数据.txt'%_dir
                file_name = u''
                if file_name1.encode('gbk') in os.listdir(_dir):
                    file_name = file_name1
                if file_name2.encode('gbk') in os.listdir(_dir):
                    file_name = file_name2
                if file_name == u'':
                    print u'未找到任何文件'
                else:
                    print u'找到%s'%file_name
                    #读取对应的文件
                    f = open(_dir+'/'+file_name, 'r')
                    s = f.readlines()
                    f.close()
                    print u'文件中共有%d组数据'%len(s)                    
                    #数据格式转换
                    datas = []
                    for st in s:
                        datas.append([st[0:2],st[3:5],st[6:8],\
                                      st[9:11],st[12:14],st[15:17]])                    
                    #读取data目录下的“自选条件.txt”
                    f = open(u'data/自选条件.txt', 'r')
                    s = f.readlines()
                    f.close()
                    print u'自选条件共%d组'%(len(s))
                    #转换数据
                    options = []
                    for s_t in s:
                        if len(s_t)<5: #防止空行
                            break
                        else:
                            option = {'nums':[], 'least':0, 'most':6} #每组数据的构成:号码,下限,上限            
                            option['nums'] = s_t.split(':')[0].split(' ')
                            option['least'] = int(s_t.split(':')[1].split('-')[0])
                            option['most'] = int(s_t.split(':')[1].split('-')[1].split('\n')[0])
                            options.append(option)
                    #过滤
                    for i in range(0, len(options)):
                        new_datas = [] #定义空列表
                        for j in range(0, len(datas)):
                            option = 0
                            for k in range(0, len(options[i]['nums'])):
                                if options[i]['nums'][k] in datas[j]:
                                    option = option + 1
                            if options[i]['least']<=option<=options[i]['most']:
                                new_datas.append(datas[j])           
                        datas = new_datas
                        print u'%d:-->%d'%(i+1, len(datas))
                    #写入数据
                    f = open(u'%s/%d自选数据.txt'%(_dir,date+1), 'w')
                    for i in range(0, len(datas)):
                        f.write('%s %s %s %s %s %s\n'\
                                %(datas[i][0],datas[i][1],datas[i][2],\
                                  datas[i][3],datas[i][4],datas[i][5]))
                    f.close()
                    print u'数据已写入'
            return True
        
        elif len(sys.argv[1:])!=0 and (sys.argv[1:][0]=='-h' or sys.argv[1:][0]=='h'): #判断是否有参数(-h)，有则提示帮助
            print u'    双色蟒彩票分析软件  1.0.6'
            print u'       otherrrr@gmail.com'
            print u'http://code.google.com/p/ssqpython/'
            print u''
            print u'其他参数:'
            print u'     -f: 直接开始全部过滤'
            print u'     -s: 直接开始缩水'
            print u'     -d: 生成数据库（停止开发）'
            print u'     -a: 读取四个红球.txt并过滤'
            print u'     -b: 读取四个红球.txt并缩水'
            print u'     -e: 开始自选过滤'
            
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
