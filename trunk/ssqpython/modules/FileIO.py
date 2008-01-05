#! usr/bin/python
# -*- coding:utf-8 -*-
# otherrrr@gmail.com
# 文件的读取和写入

import locale

def DataParaFileRead(filename): #全部参数读取
    '''传入值：filename(str)，
传出值：data_para_array(list)'''
    #显示一下
    print (u'读取“全部参数.txt”').encode(locale.getdefaultlocale()[1])
    #全部参数
    data_para_array = []    
    #打开文件
    f = open(filename, 'r')
    s = f.readlines()
    f.close()
    #数据转换
    for st in s:
        #数据参数中的一期（72项，v1.0.3）
        data_para_one = {'1号位':0,'2号位':0,'3号位':0,\
                         '4号位':0,'5号位':0,'6号位':0,\
                         '总和值':0,'前4位和值':0,'后4位和值':0,\
                         '奇数':0,'偶数':0,\
                         '61间隔':0,'21间隔':0,'41间隔':0,'43间隔':0,'52间隔':0,'63间隔':0,'65间隔':0,'质数':0,\
                         '除3余0':0,'除3余1':0,'除3余2':0,\
                         '除4余0':0,'除4余1':0,'除4余2':0,'除4余3':0,\
                         '除5余0':0,'除5余1':0,'除5余2':0,'除5余3':0,'除5余4':0,\
                         '除6余0':0,'除6余1':0,'除6余2':0,'除6余3':0,'除6余4':0,'除6余5':0,\
                         '除7余0':0,'除7余1':0,'除7余2':0,'除7余3':0,'除7余4':0,'除7余5':0,'除7余6':0,\
                         '高值区':0,'低值区':0,\
                         '区间1':0,'区间2':0,'区间3':0,\
                         '连号':0,'同尾':0,'开奖号码和':0,'尾号和':0,'AC值':0,\
                         '热号全':0,'温号全':0,'冷号全':0,\
                         '1期重号':0,'3期重号':0,'5期重号':0,'1期临近值':0,\
                         '3期个数':0,'5期个数':0,'7期个数':0,'9期个数':0,\
                         '遗漏值和':0,'固定投注':0,'长列表':0,\
                         '三分之一':0,'三分之二':0,'三分之三':0,\
                         '往期数据':0}
        #赋值
        data_para_one['1号位'] = int(st.split('-')[1])
        data_para_one['2号位'] = int(st.split('-')[2])
        data_para_one['3号位'] = int(st.split('-')[3])
        data_para_one['4号位'] = int(st.split('-')[4])
        data_para_one['5号位'] = int(st.split('-')[5])
        data_para_one['6号位'] = int(st.split('-')[6])
        data_para_one['总和值'] = int(st.split('-')[7])
        data_para_one['前4位和值'] = int(st.split('-')[8])
        data_para_one['后4位和值'] = int(st.split('-')[9])
        data_para_one['奇数'] = int(st.split('-')[10])
        data_para_one['偶数'] = int(st.split('-')[11])
        data_para_one['61间隔'] = int(st.split('-')[12])
        data_para_one['21间隔'] = int(st.split('-')[13])
        data_para_one['41间隔'] = int(st.split('-')[14])
        data_para_one['43间隔'] = int(st.split('-')[15])
        data_para_one['52间隔'] = int(st.split('-')[16])
        data_para_one['63间隔'] = int(st.split('-')[17])
        data_para_one['65间隔'] = int(st.split('-')[18])
        data_para_one['质数'] = int(st.split('-')[19])
        data_para_one['除3余0'] = int(st.split('-')[20])
        data_para_one['除3余1'] = int(st.split('-')[21])
        data_para_one['除3余2'] = int(st.split('-')[22])
        data_para_one['除4余0'] = int(st.split('-')[23])
        data_para_one['除4余1'] = int(st.split('-')[24])
        data_para_one['除4余2'] = int(st.split('-')[25])
        data_para_one['除4余3'] = int(st.split('-')[26])
        data_para_one['除5余0'] = int(st.split('-')[27])
        data_para_one['除5余1'] = int(st.split('-')[28])
        data_para_one['除5余2'] = int(st.split('-')[29])
        data_para_one['除5余3'] = int(st.split('-')[30])
        data_para_one['除5余4'] = int(st.split('-')[31])
        data_para_one['除6余0'] = int(st.split('-')[32])
        data_para_one['除6余1'] = int(st.split('-')[33])
        data_para_one['除6余2'] = int(st.split('-')[34])
        data_para_one['除6余3'] = int(st.split('-')[35])
        data_para_one['除6余4'] = int(st.split('-')[36])
        data_para_one['除6余5'] = int(st.split('-')[37])
        data_para_one['除7余0'] = int(st.split('-')[38])
        data_para_one['除7余1'] = int(st.split('-')[39])
        data_para_one['除7余2'] = int(st.split('-')[40])
        data_para_one['除7余3'] = int(st.split('-')[41])
        data_para_one['除7余4'] = int(st.split('-')[42])
        data_para_one['除7余5'] = int(st.split('-')[43])
        data_para_one['除7余6'] = int(st.split('-')[44])
        data_para_one['高值区'] = int(st.split('-')[45])
        data_para_one['低值区'] = int(st.split('-')[46])
        data_para_one['区间1'] = int(st.split('-')[47])
        data_para_one['区间2'] = int(st.split('-')[48])
        data_para_one['区间3'] = int(st.split('-')[49])
        data_para_one['连号'] = int(st.split('-')[50])
        data_para_one['同尾'] = int(st.split('-')[51])
        data_para_one['开奖号码和'] = int(st.split('-')[52])
        data_para_one['尾号和'] = int(st.split('-')[53])
        data_para_one['AC值'] = int(st.split('-')[54])
        data_para_one['热号全'] = int(st.split('-')[55])
        data_para_one['温号全'] = int(st.split('-')[56])
        data_para_one['冷号全'] = int(st.split('-')[57])
        data_para_one['1期重号'] = int(st.split('-')[58])
        data_para_one['3期重号'] = int(st.split('-')[59])
        data_para_one['5期重号'] = int(st.split('-')[60])
        data_para_one['1期临近值'] = int(st.split('-')[61])
        data_para_one['3期个数'] = int(st.split('-')[62])
        data_para_one['5期个数'] = int(st.split('-')[63])
        data_para_one['7期个数'] = int(st.split('-')[64])
        data_para_one['9期个数'] = int(st.split('-')[65])
        data_para_one['遗漏值和'] = int(st.split('-')[66])
        data_para_one['固定投注'] = int(st.split('-')[67])
        data_para_one['长列表'] = int(st.split('-')[68])
        data_para_one['三分之一'] = int(st.split('-')[69])
        data_para_one['三分之二'] = int(st.split('-')[70])
        data_para_one['三分之三'] = int(st.split('-')[71])
        data_para_one['往期数据'] = int(st.split('-')[72])

        #添加到总列表中
        data_para_array.append(data_para_one)
    #返回全部参数
    return data_para_array

def DataParaFileWrite(data_para_array, data_array): #参数文件写入
    '''传入值：data_para_array(list)/data_array(list)，
传出值：NULL'''
    #显示一下
    print (u'创建“全部参数.txt”').encode(locale.getdefaultlocale()[1])
    f = open(u'data/全部参数.txt', 'w')
    for i in range(0, len(data_array)): #共72个参数，另添加首位期号，共73个
        f.write('%s-%s-%s-\
%s-%s-%s-%s-%s-%s-%s-%s-%s-%s-\
%s-%s-%s-%s-%s-%s-%s-%s-%s-%s-\
%s-%s-%s-%s-%s-%s-%s-%s-%s-%s-\
%s-%s-%s-%s-%s-%s-%s-%s-%s-%s-\
%s-%s-%s-%s-%s-%s-%s-%s-%s-%s-\
%s-%s-%s-%s-%s-%s-%s-%s-%s-%s-\
%s-%s-%s-%s-%s-%s-%s-%s-%s-%s-\n'\
                        %(data_array[i][0],data_para_array[i]['1号位'],\
                          data_para_array[i]['2号位'],data_para_array[i]['3号位'],\
                          data_para_array[i]['4号位'],data_para_array[i]['5号位'],\
                          data_para_array[i]['6号位'],data_para_array[i]['总和值'],\
                          data_para_array[i]['前4位和值'],data_para_array[i]['后4位和值'],\
                          data_para_array[i]['奇数'],data_para_array[i]['偶数'],\
                          data_para_array[i]['61间隔'],data_para_array[i]['21间隔'],\
                          data_para_array[i]['41间隔'],data_para_array[i]['43间隔'],\
                          data_para_array[i]['52间隔'],data_para_array[i]['63间隔'],\
                          data_para_array[i]['65间隔'],data_para_array[i]['质数'],\
                          data_para_array[i]['除3余0'],data_para_array[i]['除3余1'],\
                          data_para_array[i]['除3余2'],data_para_array[i]['除4余0'],\
                          data_para_array[i]['除4余1'],data_para_array[i]['除4余2'],\
                          data_para_array[i]['除4余3'],data_para_array[i]['除5余0'],\
                          data_para_array[i]['除5余1'],data_para_array[i]['除5余2'],\
                          data_para_array[i]['除5余3'],data_para_array[i]['除5余4'],\
                          data_para_array[i]['除6余0'],data_para_array[i]['除6余1'],\
                          data_para_array[i]['除6余2'],data_para_array[i]['除6余3'],\
                          data_para_array[i]['除6余4'],data_para_array[i]['除6余5'],\
                          data_para_array[i]['除7余0'],data_para_array[i]['除7余1'],\
                          data_para_array[i]['除7余2'],data_para_array[i]['除7余3'],\
                          data_para_array[i]['除7余4'],data_para_array[i]['除7余5'],\
                          data_para_array[i]['除7余6'],data_para_array[i]['高值区'],\
                          data_para_array[i]['低值区'],data_para_array[i]['区间1'],\
                          data_para_array[i]['区间2'],data_para_array[i]['区间3'],\
                          data_para_array[i]['连号'],data_para_array[i]['同尾'],\
                          data_para_array[i]['开奖号码和'],data_para_array[i]['尾号和'],\
                          data_para_array[i]['AC值'],data_para_array[i]['热号全'],\
                          data_para_array[i]['温号全'],data_para_array[i]['冷号全'],\
                          data_para_array[i]['1期重号'],data_para_array[i]['3期重号'],\
                          data_para_array[i]['5期重号'],data_para_array[i]['1期临近值'],\
                          data_para_array[i]['3期个数'],data_para_array[i]['5期个数'],\
                          data_para_array[i]['7期个数'],data_para_array[i]['9期个数'],\
                          data_para_array[i]['遗漏值和'],data_para_array[i]['固定投注'],\
                          data_para_array[i]['长列表'],data_para_array[i]['三分之一'],\
                          data_para_array[i]['三分之二'],data_para_array[i]['三分之三'],\
                          data_para_array[i]['往期数据']
                          ))            
    f.close()   

def XmlWrite(filename,data_array,data_para_array,redOrder,redTimes): #创建用于Flash读取的xml
    '''传入值：filename(str),data_array(list),data_para_array(list),redOrder(list),redTimes(list)，
传出值：NULL'''
    #显示一下
    print (u'写“近期数据.xml”').encode(locale.getdefaultlocale()[1])
    #打开文件
    f = open(filename, 'w')
    f.write('<?xml version="1.0" encoding="utf-8"?>\n')
    ##写入最近20期开奖号码
    f.write('<datas>\n') 
    for i in range(0, 20):
        f.write('    <data0%d>\n'%i)
        f.write('        <data date=\'%s\''%data_array[i][0])
        for j in range(1, 6+1):
            f.write(' red0%d=\'%d\''%(j,int(data_array[i][j])))
        f.write('/>\n')
        f.write('    </data0%d>\n'%i)
    f.write('</datas>\n')
    ##写入期数对应信息(9期）
    f.write('<dateInfos>\n')
    for i in range(0, 9):
        f.write('    <dateInfo%.2d>\n'%i)
        f.write('        <dateInfo sum=\'%d\' odd=\'%d\' even=\'%d\' maxArea=\'%d\'/>\n'\
                %(data_para_array[i]['总和值'],data_para_array[i]['奇数'],\
                  data_para_array[i]['偶数'],data_para_array[i]['61间隔']))
        f.write('    </dateInfo%.2d>\n'%i)
    f.write('</dateInfos>\n')
    ##写入号码对应信息
    f.write('<numInfos>\n')
    for i in range(0, 33):
        ###热温冷
        if '%.2d'%(i+1) in redOrder[:11]:
            #热号
            hwc = 'h'
        elif '%.2d'%(i+1) in redOrder[11:22]:
            #温号
            hwc = 'w'
        else:
            #冷号
            hwc = 'c'
        ###平均出号期数
        avg_ap = '%.2f'%(len(data_array)*1.0/redTimes[i])
        ###当前未出期数
        for j in range(0, len(data_array)):
            if '%.2d'%(i+1) in data_array[j][1:7]:
                n_ap = j
                break
        ###写文件
        f.write('    <numInfo%.2d>\n'%i)
        f.write('        <numInfo hwc=\'%s\' avg_ap=\'%s\' n_ap=\'%d\'/>\n'\
                %(hwc,avg_ap,n_ap))
        f.write('    </numInfo%.2d>\n'%i)
    f.write('</numInfos>\n')
    #关闭文件
    f.close()
