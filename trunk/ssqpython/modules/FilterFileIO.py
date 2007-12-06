#! usr/bin/python
# -*- coding:utf-8 -*-
# otherrrr@gmail.com
# 过滤参数文件读写

import locale

def readFilterFileToArray(): #读取过滤参数
    '''将过滤条件.txt读出，并转换成数组'''
    f = open(u'data/过滤条件.txt', 'r')
    filter_array_temp = f.readlines()
    f.close()

    #显示一下
    print (u'读取过滤条件%d组'%(len(filter_array_temp)-3)).encode(locale.getdefaultlocale()[1])
    
    for i in range(0, len(filter_array_temp)):
        if '==BEGIN==' in filter_array_temp[i]:
            pos_begin = i #开始位置
    for i in range(0, len(filter_array_temp)):
        if '==END==' in filter_array_temp[i]:
            pos_end = i #结束位置

    filter_array = []

    for i in range(pos_begin+1, pos_end):
        filter_term = [u'第几项', u'名称', u'是否启用', u'范围', u'说明']

        filter_term[0] =  filter_array_temp[i].split('()')[0]
        filter_term[1] =  filter_array_temp[i].split('()')[1]
        filter_term[2] =  filter_array_temp[i].split('()')[2].decode('utf-8') #20071203
        filter_term[3] =  filter_array_temp[i].split('()')[3]
        filter_term[4] =  filter_array_temp[i].split('()')[4][:-1]

        filter_array.append(filter_term)

    return filter_array
