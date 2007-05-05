# -*- coding: cp936 -*-
# otherrrr@gmail.com
# 预测数据文件读写

import os

def writePredictData(data_array, data_f, filter_array): #预测数据写入文件
    '''新建对应日期的文件夹，创建并写入预测数据文件
       创建并写入对应的过滤条件文件加
    '''
    #期数
    date = '%s'%(int(data_array[0][0])+1)
    #创建新目录
    try:
        os.mkdir(date)
    except OSError: #如果文件夹已存在，则会出现此错误
        pass
    #在新目录中创建并写入文件2007XXX预测数据.txt
    f = open('%s/%s预测数据.txt'%(date,date), 'w')
    #写数据
    for i in range(0, len(data_f)):
        #这里如果使用一个子循环的话，会花费更多时间
        f.write('%.2d %.2d %.2d %.2d %.2d %.2d\n'\
                %(data_f[i][0],data_f[i][1],data_f[i][2],data_f[i][3],data_f[i][4],data_f[i][5]))
    f.close()   
    #在新目录中创建并写入文件2007XXX过滤条件.txt
    f = open('%s/%s过滤条件.txt'%(date,date), 'w')
    f.write('     ()名称         ()是否启用()范围\n')
    f.write('==BEGIN=============================\n')
    for i in range(0, len(filter_array)):
        f.write('%s'%(filter_array[i][0]))
        f.write('()')
        f.write('%s'%(filter_array[i][1]))
        f.write('()')
        f.write('%s'%(filter_array[i][2]))
        f.write('()')
        f.write('%s'%(filter_array[i][3]))
        f.write('\n')
    f.write('==END===============================\n')
    f.close()
    
def readPredictData(date): #读取预测数据和过滤条件
    '''读取预测数据和使用到的过滤条件'''   
    #读预测数据
    f = open('%s/%s预测数据.txt'%(date,date), 'r')
    tmp = f.readlines() 
    f.close()
    predict_data = [] #预测数据
    for i in range(0, len(tmp)):
        predict_data.append([tmp[i][0:2],tmp[i][3:5],tmp[i][6:8],\
                             tmp[i][9:11],tmp[i][12:14],tmp[i][15:17]])
    #读过滤条件
    f = open('%s/%s过滤条件.txt'%(date,date), 'r')
    tmp = f.readlines()
    f.close()
    tmp = tmp[2:-1] #去掉首尾
    predict_filter = [] #使用的过滤条件
    for i in range(0, len(tmp)):
        if '是' in tmp[i]: #确定“使用”
            term = ['第几项', '名称', '是否启用', '范围']
            term[0] =  tmp[i].split('()')[0]
            term[1] =  tmp[i].split('()')[1]
            term[2] =  tmp[i].split('()')[2]
            term[3] =  tmp[i].split('()')[3]
            predict_filter.append(term)
        else:
            pass

    return predict_data, predict_filter


