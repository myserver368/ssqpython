# -*- coding: cp936 -*-
#!/usr/bin/env python
# otherrrr@gmail.com
# 主程序

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
        if len(sys.argv[1:])!=0 and (sys.argv[1:][0]=='-f' or sys.argv[1:][0]=='f'): #判断是否有参数(-f)，有则直接过滤（33个球）
            #命令行显示一下
            print '开始一步过滤(选择全部33个红球）'
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
            print '生成所有号码%d组'%(len(data_f))
            #读取开奖数据
            data_array = readDataFileToArray()            
            #读取固定投注
            bet_array = readBetFileToArray()            
            #读取过滤条件
            filter_array = readFilterFileToArray()
            #计算出球次数并排列球号
            redOrder, redTimes = redOrderCoumpute(data_array)
            #显示预测的期号
            print '预测%d期'%(int(data_array[0][0])+1)
            #开始时间
            start_time = int(time.time())            
            #开始过滤
            step = 0            
            for i in range(0, len(filter_array)):
                step = step + 1
                filter_array[step-1][2] = '是' + filter_array[step-1][2][2:]
                data_f = dataFiltrate(data_array, data_f, step, filter_array, redOrder, bet_array)
                if step==1:
                    print '%.2d time=%d num=%d %s'%(step,int(time.time())-start_time,len(data_f),filter_array[step-1][4])
                    last_time = int(time.time())
                else:
                    print '%.2d time=%d num=%d %s'%(step,int(time.time())-last_time,len(data_f),filter_array[step-1][4])
                    last_time = int(time.time())
            #终止时间
            stop_time = int(time.time())
            #写数据
            writePredictData(data_array, data_f, filter_array, num_pool)              
            #提示生成的注数和花费的时间
            print '共生成%d注，花费%d秒'%(len(data_f),stop_time-start_time)
              
            return True
        elif len(sys.argv[1:])!=0 and (sys.argv[1:][0]=='-d' or sys.argv[1:][0]=='d'): #判断是否有参数(-d)，有则创建数据库
            '''
            预想当中使用数据库会快一些，但是实际上，不是！
            '''
            print '此功能已停止开发!'
            exit(0) #因已停止开发因此直接退出
            
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
            print '此功能未开发完成!'

            return True
        elif len(sys.argv[1:])!=0 and (sys.argv[1:][0]=='-h' or sys.argv[1:][0]=='h'): #判断是否有参数(-h)，有则提示帮助
            print '    双色蟒彩票分析软件  1.0.0'
            print '       otherrrr@gmail.com'
            print 'http://code.google.com/p/ssqpython/'
            print ''
            print '其他参数:'
            print '     -f: 直接开始全部过滤'
            print '     -d: 生成数据库（暂）'
            print '     -o: 生成过滤参数'
            
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
