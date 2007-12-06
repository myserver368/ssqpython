#! usr/bin/python
# -*- coding:utf-8 -*-
# otherrrr@gmail.com
# 开奖数据文件读写

import locale

def readDataFileToString(): #读取开奖数据
    '''读取开奖数据.txt，得到string变量'''
    f = open(u'data/开奖数据.txt', 'r')
    data_string  = f.read()
    f.close()

    return data_string
    
def readDataFileToArray(): #读取开奖数据
    '''读取开奖数据.txt，得到list变量'''
    f = open(u'data/开奖数据.txt', 'r')
    data_array_temp  = f.readlines()
    f.close()

    data_array = []
    
    for i in range(0, len(data_array_temp)):
        data_term = [u'日期', u'红球1', u'红球2', u'红球3', u'红球4', u'红球5', u'红球6', '蓝球']
        #用"分裂"方式读取
        '''
        data_term[0] = data_array_temp[i].split(' ')[0]
        data_term[1] = data_array_temp[i].split(' ')[1].split(',')[0]
        data_term[2] = data_array_temp[i].split(' ')[1].split(',')[1]
        data_term[3] = data_array_temp[i].split(' ')[1].split(',')[2]
        data_term[4] = data_array_temp[i].split(' ')[1].split(',')[3]
        data_term[5] = data_array_temp[i].split(' ')[1].split(',')[4]
        data_term[6] = data_array_temp[i].split(' ')[1].split(',')[5][0:2]
        data_term[7] = data_array_temp[i].split('+')[1][0:2]
        '''
        #用"位数"方式读取
        ##可防止用户将空格作为号码之间的间隔（虽然用户应该按照我的方式来，但是预防万一）
        data_term[0] = data_array_temp[i][0:7]
        data_term[1] = data_array_temp[i][8:10]
        data_term[2] = data_array_temp[i][11:13]
        data_term[3] = data_array_temp[i][14:16]
        data_term[4] = data_array_temp[i][17:19]
        data_term[5] = data_array_temp[i][20:22]
        data_term[6] = data_array_temp[i][23:25]
        data_term[7] = data_array_temp[i][26:28]
        
        data_array.append(data_term)

    #命令行提示
    print (u'读取开奖数据%d组'%(len(data_array))).encode(locale.getdefaultlocale()[1])
    
    return data_array

def writeStringToDataFile(data_string): #写入开奖数据
    '''将string写入开奖数据.txt中'''
    f = open(u'data/开奖数据.txt', 'w')
    f.write(data_string)
    f.close()

    #命令行提示
    print u'写入开奖数据'.encode(locale.getdefaultlocale()[1])  
