# -*- coding: cp936 -*-
# otherrrr@gmail.com
# 开奖数据文件读写

def readDataFileToString(): #读取开奖数据
    '''读取开奖数据.txt，得到string变量'''
    f = open('data/开奖数据.txt', 'r')
    data_string  = f.read()
    f.close()

    return data_string
    
def readDataFileToArray(): #读取开奖数据
    '''读取开奖数据.txt，得到list变量'''
    f = open('data/开奖数据.txt', 'r')
    data_array_temp  = f.readlines()
    f.close()

    data_array = []
    
    for i in range(0, len(data_array_temp)):
        data_term = ['日期', '红球1', '红球2', '红球3', '红球4', '红球5', '红球6', '蓝球']
        #也可以直接读取"位数"。现在是用"分裂"(split)
        data_term[0] =  data_array_temp[i].split(' ')[0]
        data_term[1] =  data_array_temp[i].split(' ')[1].split(',')[0]
        data_term[2] =  data_array_temp[i].split(' ')[1].split(',')[1]
        data_term[3] =  data_array_temp[i].split(' ')[1].split(',')[2]
        data_term[4] =  data_array_temp[i].split(' ')[1].split(',')[3]
        data_term[5] =  data_array_temp[i].split(' ')[1].split(',')[4]
        data_term[6] =  data_array_temp[i].split(' ')[1].split(',')[5][0:2]
        data_term[7] =  data_array_temp[i].split('+')[1][0:2]

        data_array.append(data_term)

    #命令行提示
    print '读取开奖数据%d组'%(len(data_array))
    
    return data_array

def writeStringToDataFile(data_string): #写入开奖数据
    '''将string写入开奖数据.txt中'''
    f = open('data/开奖数据.txt', 'w')
    f.write(data_string)
    f.close()

    #命令行提示
    print '写入开奖数据'    
