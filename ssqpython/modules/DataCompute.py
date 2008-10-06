#! usr/bin/python
# -*- coding:utf-8 -*-
# otherrrr@gmail.com
# 数据计算

import time
import locale

def redOrderCoumpute(data_array): #红球冷热温号全计算
    '''计算红球各个球的出球次数，并按照次数排列'''
    #命令行显示一下
    print (u'计算红球冷热温号（固定）').encode(locale.getdefaultlocale()[1])
    #---------------------------------------------------------------------------
    #热号全
    redOrder = [] #按序排列的球号
    redTimes = [] #对应球号的次数
    for i in range(0, 33):
        redTimes.append(0) #次数初始化
    for i in range(0, len(data_array)): #计算出出球次数
        for j in range(1, 6+1):
            redTimes[int(data_array[i][j])-1] = redTimes[int(data_array[i][j])-1] + 1    
    '''
    for i in range(0, 33):
        redTimes.append(0) #次数初始化
        redOrder.append('%.2d'%(i+1)) #球号初始化
 
    for i in range(0, len(data_array)): #计算出出球次数
        for j in range(1, 6+1):
            redTimes[int(data_array[i][j])-1] = redTimes[int(data_array[i][j])-1] + 1

    #从大到小排序
    for i in range(0, 33):
        for j in range(0, len(redTimes)-1):
            if redTimes[j]<redTimes[j+1]:
                #替换－次数
                tmp = redTimes[j]
                redTimes[j] = redTimes[j+1]
                redTimes[j+1] = tmp
                #替换－球号
                tmp = redOrder[j]
                redOrder[j] = redOrder[j+1]
                redOrder[j+1] = tmp
    '''            
    #固定之（原因：如果出现温号升级热号的情况，则统计上有失误）
    redOrder = ['20','14','30','32','03','21','01','26','04','07','08',\
                '18','17','16','27','05','31','11','12','10','25','13',\
                '19','22','28','02','06','09','23','29','33','24','15']
    #print redOrder
    return redOrder, redTimes

def dataParaCompute(data_array, redOrder, bet_array): #开奖数据的参数计算
    '''根据开奖数据计算出各项参数，可用来计算百分比，也可以用来单独显示'''
    #命令行显示一下
    print (u'计算开奖数据的参数').encode(locale.getdefaultlocale()[1])
    #为什么要单独算这个呢？是因为将来如果需要单独显示其中的某一项就可以直接用了
    data_para_array = [] #所有数据参数列表

    for i in range(0, len(data_array)):
        #数据参数中的一期（共72项，与过滤条件数目相同） #1.0.3
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
        #1号位
        data_para_one['1号位'] = int(data_array[i][1])
        #2号位
        data_para_one['2号位'] = int(data_array[i][2])
        #3号位
        data_para_one['3号位'] = int(data_array[i][3])
        #4号位
        data_para_one['4号位'] = int(data_array[i][4])
        #5号位
        data_para_one['5号位'] = int(data_array[i][5])
        #6号位
        data_para_one['6号位'] = int(data_array[i][6])
        #计算总和值
        sum_num = 0 
        for j in range(1, 6+1):
            sum_num = sum_num + int(data_array[i][j])
        data_para_one['总和值'] = sum_num
        #计算前4位和值
        sum14_num = 0 
        for j in range(1, 4+1):
            sum14_num = sum14_num + int(data_array[i][j])
        data_para_one['前4位和值'] = sum14_num
        #计算后4位和值
        sum36_num = 0 
        for j in range(3, 6+1):
            sum36_num = sum36_num + int(data_array[i][j])
        data_para_one['后4位和值'] = sum36_num
        #计算奇数个数
        odd_num = 0 
        for j in range(1, 6+1):
            if int(data_array[i][j])%2==1:
                odd_num = odd_num + 1
        data_para_one['奇数'] = odd_num
        #计算偶数个数
        even_num = 6 - odd_num
        data_para_one['偶数'] = even_num
        #计算61间隔（最大间隔值）
        max_space_61 = int(data_array[i][6]) - int(data_array[i][1]) 
        data_para_one['61间隔'] = max_space_61
        #计算21间隔
        max_space_21 = int(data_array[i][2]) - int(data_array[i][1]) 
        data_para_one['21间隔'] = max_space_21        
        #计算41间隔
        max_space_41 = int(data_array[i][4]) - int(data_array[i][1]) 
        data_para_one['41间隔'] = max_space_41
        #计算43间隔
        max_space_43 = int(data_array[i][4]) - int(data_array[i][3]) 
        data_para_one['43间隔'] = max_space_43        
        #计算52间隔
        max_space_52 = int(data_array[i][5]) - int(data_array[i][2]) 
        data_para_one['52间隔'] = max_space_52
        #计算63间隔
        max_space_63 = int(data_array[i][6]) - int(data_array[i][3]) 
        data_para_one['63间隔'] = max_space_63
        #计算65间隔
        max_space_65 = int(data_array[i][6]) - int(data_array[i][5]) 
        data_para_one['65间隔'] = max_space_65           
        #计算质数个数
        prime_num = 0 
        for j in range(1, 6+1):
            if int(data_array[i][j]) in [2,3,5,7,11,13,17,19,23,29,31]:
                prime_num = prime_num + 1   
        data_para_one['质数'] = prime_num  
        #计算除3余0个数
        residue_num30 = 0 
        for j in range(1, 6+1):
            if int(data_array[i][j]) in [3,6,9,12,15,18,21,24,27,30,33]: #这个也可以换成#if int(data_array[i][j])%3==0:
                residue_num30 = residue_num30 + 1
        data_para_one['除3余0'] = residue_num30       
        #计算除3余1个数
        residue_num31 = 0 
        for j in range(1, 6+1):
            if int(data_array[i][j]) in [1,4,7,10,13,16,19,22,25,28,31]:
                residue_num31 = residue_num31 + 1
        data_para_one['除3余1'] = residue_num31  
        #计算除3余2个数
        residue_num32 = 0 
        for j in range(1, 6+1):
            if int(data_array[i][j]) in [2,5,8,11,14,17,20,23,26,29,32]:
                residue_num32 = residue_num32 + 1
        data_para_one['除3余2'] = residue_num32
        #计算除4余0个数
        residue_num40 = 0 
        for j in range(1, 6+1):
            if int(data_array[i][j]) in [4,8,12,16,20,24,28,32]:
                residue_num40 = residue_num40 + 1
        data_para_one['除4余0'] = residue_num40
        #计算除4余1个数
        residue_num41 = 0 
        for j in range(1, 6+1):
            if int(data_array[i][j]) in [1,5,9,13,17,21,25,29,33]:
                residue_num41 = residue_num41 + 1
        data_para_one['除4余1'] = residue_num41
        #计算除4余2个数
        residue_num42 = 0 
        for j in range(1, 6+1):
            if int(data_array[i][j]) in [2,6,10,14,18,22,26,30]:
                residue_num42 = residue_num42 + 1
        data_para_one['除4余2'] = residue_num42
        #计算除4余3个数
        residue_num43 = 0 
        for j in range(1, 6+1):
            if int(data_array[i][j]) in [3,7,11,15,19,23,27,31]:
                residue_num43 = residue_num43 + 1
        data_para_one['除4余3'] = residue_num43        
        #计算除5余0个数
        residue_num50 = 0 
        for j in range(1, 6+1):
            if int(data_array[i][j]) in [5,10,15,20,25,30]:
                residue_num50 = residue_num50 + 1
        data_para_one['除5余0'] = residue_num50
        #计算除5余1个数
        residue_num51 = 0 
        for j in range(1, 6+1):
            if int(data_array[i][j]) in [1,6,11,16,21,26,31]:
                residue_num51 = residue_num51 + 1
        data_para_one['除5余1'] = residue_num51
        #计算除5余2个数
        residue_num52 = 0 
        for j in range(1, 6+1):
            if int(data_array[i][j]) in [2,7,12,17,22,27,32]:
                residue_num52 = residue_num52 + 1
        data_para_one['除5余2'] = residue_num52
        #计算除5余3个数
        residue_num53 = 0 
        for j in range(1, 6+1):
            if int(data_array[i][j]) in [3,8,13,18,23,28,33]:
                residue_num53 = residue_num53 + 1
        data_para_one['除5余3'] = residue_num53
        #计算除5余4个数
        residue_num54 = 0 
        for j in range(1, 6+1):
            if int(data_array[i][j]) in [4,9,14,19,24,29]:
                residue_num54 = residue_num54 + 1
        data_para_one['除5余4'] = residue_num54
        #计算除6余0个数
        residue_num60 = 0 
        for j in range(1, 6+1):
            if int(data_array[i][j]) in [6,12,18,24,30]:
                residue_num60 = residue_num60 + 1
        data_para_one['除6余0'] = residue_num60
        #计算除6余1个数
        residue_num61 = 0 
        for j in range(1, 6+1):
            if int(data_array[i][j]) in [1,7,13,19,25,31]:
                residue_num61 = residue_num61 + 1
        data_para_one['除6余1'] = residue_num61
        #计算除6余2个数
        residue_num62 = 0 
        for j in range(1, 6+1):
            if int(data_array[i][j]) in [2,8,14,20,26,32]:
                residue_num62 = residue_num62 + 1
        data_para_one['除6余2'] = residue_num62
        #计算除6余3个数
        residue_num63 = 0 
        for j in range(1, 6+1):
            if int(data_array[i][j]) in [3,9,15,21,27,33]:
                residue_num63 = residue_num63 + 1
        data_para_one['除6余3'] = residue_num63
        #计算除6余4个数
        residue_num64 = 0 
        for j in range(1, 6+1):
            if int(data_array[i][j]) in [4,10,16,22,28]:
                residue_num64 = residue_num64 + 1
        data_para_one['除6余4'] = residue_num64
        #计算除6余5个数
        residue_num65 = 0 
        for j in range(1, 6+1):
            if int(data_array[i][j]) in [5,11,17,23,29]:
                residue_num65 = residue_num65 + 1
        data_para_one['除6余5'] = residue_num65         
        #计算除7余0个数
        residue_num70 = 0 
        for j in range(1, 6+1):
            if int(data_array[i][j]) in [7,14,21,28]:
                residue_num70 = residue_num70 + 1
        data_para_one['除7余0'] = residue_num70
        #计算除7余1个数
        residue_num71 = 0 
        for j in range(1, 6+1):
            if int(data_array[i][j]) in [1,8,15,22,29]:
                residue_num71 = residue_num71 + 1
        data_para_one['除7余1'] = residue_num71
        #计算除7余2个数
        residue_num72 = 0 
        for j in range(1, 6+1):
            if int(data_array[i][j]) in [2,9,16,23,30]:
                residue_num72 = residue_num72 + 1
        data_para_one['除7余2'] = residue_num72
        #计算除7余3个数
        residue_num73 = 0 
        for j in range(1, 6+1):
            if int(data_array[i][j]) in [3,10,17,24,31]:
                residue_num73 = residue_num73 + 1
        data_para_one['除7余3'] = residue_num73
        #计算除7余4个数
        residue_num74 = 0 
        for j in range(1, 6+1):
            if int(data_array[i][j]) in [4,11,18,25,32]:
                residue_num74 = residue_num74 + 1
        data_para_one['除7余4'] = residue_num74
        #计算除7余5个数
        residue_num75 = 0 
        for j in range(1, 6+1):
            if int(data_array[i][j]) in [5,12,19,26,33]:
                residue_num75 = residue_num75 + 1
        data_para_one['除7余5'] = residue_num75
        #计算除7余6个数
        residue_num76 = 0 
        for j in range(1, 6+1):
            if int(data_array[i][j]) in [6,13,20,27]:
                residue_num76 = residue_num76 + 1
        data_para_one['除7余6'] = residue_num76         
        #计算高值区中的出号个数
        high_num = 0 
        for j in range(1, 6+1):
            if int(data_array[i][j])>17:
                high_num = high_num + 1   
        data_para_one['高值区'] = high_num  
        #计算低值区中的出号个数
        low_num = 0 
        for j in range(1, 6+1):
            if int(data_array[i][j])<17:
                low_num = low_num + 1  
        data_para_one['低值区'] = low_num 
        #计算区间1中的出号个数
        area1_num = 0 
        for j in range(1, 6+1):
            if int(data_array[i][j])<12:
                area1_num = area1_num + 1
        data_para_one['区间1'] = area1_num
        #计算区间2中的出号个数
        area2_num = 0 
        for j in range(1, 6+1):
            if 11<int(data_array[i][j])<23:
                area2_num = area2_num + 1        
        data_para_one['区间2'] = area2_num  
        #计算区间3中的出号个数
        area3_num = 0 
        for j in range(1, 6+1):
            if int(data_array[i][j])>22:
                area3_num = area3_num + 1
        data_para_one['区间3'] = area3_num  
        #计算连号个数
        continuous_num = 0 
        for j in range(1, 5+1):
            if int(data_array[i][j+1])-int(data_array[i][j])==1:
                continuous_num = continuous_num + 1
        data_para_one['连号'] = continuous_num
        #计算同尾组数
        same_nail_num = 0
        times = [] #次数
        for j in range(0, 9+1):
            times.append(0) 
        for j in range(1, 6+1):
            times[(int(data_array[i][j])%10)] = times[(int(data_array[i][j])%10)] + 1
        for j in range(0, 9+1):
            if times[j]>1:
                same_nail_num = same_nail_num + 1
        data_para_one['同尾'] = same_nail_num
        #计算开奖号码和（开奖号码拆分为12个数字，它们的和）
        sum_12 = 0
        for j in range(1, 6+1):
            sum_12 = sum_12 + int(data_array[i][j])%10
            sum_12 = sum_12 + int(data_array[i][j])/10
        data_para_one['开奖号码和'] = sum_12
        #计算尾号和
        nail_sum = 0
        for j in range(1, 6+1):
            nail_sum = nail_sum + int(data_array[i][j])%10
        data_para_one['尾号和'] = nail_sum
        #计算AC值范围
        ac_num = 0
        details = [] #具体数据，最多为15
        for t1 in range(1, 6+1):
            for t2 in range(t1+1, 6+1):
                if (int(data_array[i][t2]) - int(data_array[i][t1])) in details:
                    continue
                else:
                    details.append(int(data_array[i][t2]) - int(data_array[i][t1]))
        ac_num = len(details) - (6-1) #为什么是(6-1)，去百度一下吧，这里只能告诉你，6是因为有6个红球，呵呵
        data_para_one['AC值'] = ac_num   
        #计算热号全个数
        hot_num = 0
        for j in range(1, 6+1):
            if data_array[i][j] in redOrder[:11]: #热号就是出球次数排在前11位的
                hot_num = hot_num + 1
        data_para_one['热号全'] = hot_num
        #计算温号全个数
        warm_num = 0
        for j in range(1, 6+1):
            if data_array[i][j] in redOrder[11:22]:
                warm_num = warm_num + 1
        data_para_one['温号全'] = warm_num
        #计算冷号全个数
        cold_num = 0
        for j in range(1, 6+1):
            if data_array[i][j] in redOrder[22:]:
                cold_num = cold_num + 1
        data_para_one['冷号全'] = cold_num    
        #计算1期重号个数
        repeat1_num = 0
        if i==(len(data_array)-1): #第1期没有上一期
            repeat1_num = 0
        else:
            for j in range(1, 6+1):
                if data_array[i][j] in data_array[i+1][1:6+1]:
                    repeat1_num = repeat1_num + 1
        data_para_one['1期重号'] = repeat1_num
        #计算3期重号个数
        repeat3_num = 0
        if i>=(len(data_array)-3): #前3期没有前3期
            repeat3_num = 0
        else:
            l3_a = data_array[i+1][1:6+1] + data_array[i+2][1:6+1] + data_array[i+3][1:6+1] #3期合并列表
            l3_d = [] #删除相同项之后的3期合并列表
            for j in range(0, len(l3_a)):
                if l3_a[j] not in l3_a[j+1:]:
                    l3_d.append(l3_a[j])    
            for j in range(1, 6+1):
                if data_array[i][j] in l3_d:
                    repeat3_num = repeat3_num + 1
        data_para_one['3期重号'] = repeat3_num        
        #计算5期重号个数
        repeat5_num = 0
        if i>=(len(data_array)-5): #前5期没有前5期
            repeat5_num = 0
        else:
            l5_a = data_array[i+1][1:6+1] + data_array[i+2][1:6+1] + data_array[i+3][1:6+1] +\
                   data_array[i+4][1:6+1] + data_array[i+5][1:6+1]#5期合并列表
            l5_d = [] #删除相同项之后的5期合并列表
            for j in range(0, len(l5_a)):
                if l5_a[j] not in l5_a[j+1:]:
                    l5_d.append(l5_a[j])    
            for j in range(1, 6+1):
                if data_array[i][j] in l5_d:
                    repeat5_num = repeat5_num + 1
        data_para_one['5期重号'] = repeat5_num
        #计算10期重号个数（即5期之前的5期）
        repeat10_num = 0
        if i>=(len(data_array)-10): #前10期没有前10期
            repeat10_num = 0
        else:
            l10_a = data_array[i+1+5][1:6+1] + data_array[i+2+5][1:6+1] + data_array[i+3+5][1:6+1] +\
                   data_array[i+4+5][1:6+1] + data_array[i+5+5][1:6+1]#5期之前的5期合并列表
            l10_d = [] #删除相同项之后的5期合并列表
            for j in range(0, len(l10_a)):
                if l10_a[j] not in l10_a[j+1:]:
                    l10_d.append(l10_a[j])    
            for j in range(1, 6+1):
                if data_array[i][j] in l10_d:
                    repeat10_num = repeat10_num + 1
        data_para_one['10期重号'] = repeat10_num
        #1期临近值
        near_num = 0
        if i==(len(data_array)-1): #第1期没有上一期
            near_num = 0
        else:
            tmp_list = [] #临时数组，将上一期中所有＋1/－1的数存起来，注意是int型
            for j in range(1, 6+1):
                tmp_list.append(int(data_array[i+1][j])-1)
                tmp_list.append(int(data_array[i+1][j])+1)
            for j in range(1, 6+1):
                if int(data_array[i][j]) in tmp_list:
                    near_num = near_num + 1
        data_para_one['1期临近值'] = near_num
        #3期个数
        num_l3 = 0
        if i>=(len(data_array)-2): #前2期不行呀
            num_l3 = 0
        else:
            l3_a = data_array[i][1:6+1] + data_array[i+1][1:6+1] + data_array[i+2][1:6+1] #3期合并列表
            l3_d = [] #删除相同项之后的3期合并列表
            for j in range(0, len(l3_a)):
                if l3_a[j] not in l3_a[j+1:]:
                    l3_d.append(l3_a[j])
            num_l3 = len(l3_d)
        data_para_one['3期个数'] = num_l3
        #5期个数
        num_l5 = 0
        if i>=(len(data_array)-4): #前4期不行呀
            num_l5 = 0
        else:
            l5_a = data_array[i][1:6+1] + data_array[i+1][1:6+1] + data_array[i+2][1:6+1] +\
                   data_array[i+3][1:6+1] + data_array[i+4][1:6+1]#5期合并列表
            l5_d = [] #删除相同项之后的5期合并列表
            for j in range(0, len(l5_a)):
                if l5_a[j] not in l5_a[j+1:]:
                    l5_d.append(l5_a[j])
            num_l5 = len(l5_d)
        data_para_one['5期个数'] = num_l5
        #7期个数
        num_l7 = 0
        if i>=(len(data_array)-6): #前6期不行呀
            num_l7 = 0
        else:
            l7_a = data_array[i][1:6+1] + data_array[i+1][1:6+1] + data_array[i+2][1:6+1] +\
                   data_array[i+3][1:6+1] + data_array[i+4][1:6+1] + data_array[i+5][1:6+1] +\
                   data_array[i+6][1:6+1]#7期合并列表
            l7_d = [] #删除相同项之后的7期合并列表
            for j in range(0, len(l7_a)):
                if l7_a[j] not in l7_a[j+1:]:
                    l7_d.append(l7_a[j])
            num_l7 = len(l7_d)
        data_para_one['7期个数'] = num_l7
        #9期个数
        num_l9 = 0
        if i>=(len(data_array)-8): #前8期不行呀
            num_l9 = 0
        else:
            l9_a = data_array[i][1:6+1] + data_array[i+1][1:6+1] + data_array[i+2][1:6+1] +\
                   data_array[i+3][1:6+1] + data_array[i+4][1:6+1] + data_array[i+5][1:6+1] +\
                   data_array[i+6][1:6+1] + data_array[i+7][1:6+1] + data_array[i+8][1:6+1]#9期合并列表
            l9_d = [] #删除相同项之后的9期合并列表
            for j in range(0, len(l9_a)):
                if l9_a[j] not in l9_a[j+1:]:
                    l9_d.append(l9_a[j])
            num_l9 = len(l9_d)
        data_para_one['9期个数'] = num_l9
        #遗漏值和
        miss_sum = 0
        if i>=(len(data_array)-26): #前26期无
            miss_sum = 0
        else:
            for j in range(1, 6+1):
                for k in range(i+1, len(data_array)):
                    if data_array[i][j] in data_array[k][1:6+1]:
                        miss_sum = miss_sum + (k-i)
                        break
        data_para_one['遗漏值和'] = miss_sum
        #固定投注过滤
        num_fix = 0
        for j in range(0, len(bet_array)):
            num_tmp = 0 #临时最大值
            for k in range(0, 6):
                if bet_array[j][k] in data_array[i][1:6+1]:
                    num_tmp = num_tmp + 1
            if num_tmp>num_fix:
                num_fix = num_tmp
        data_para_one['固定投注'] = num_fix
        #长列表
        long_list_num = 0
        long_list = ['01','02','05','07','10','11','13','14',\
                     '17','18','19','20','21','22','23','24',\
                     '26','27','28','29','30','32','33']#5组共23个
        for j in range(1, 6+1):
            if data_array[i][j] in long_list:
                long_list_num = long_list_num + 1
        data_para_one['长列表'] = long_list_num
        #三分之一
        div31_num = 0
        div31_list = ['01','03','04','05','07','08','14','17',\
                      '18','20','22','26','27','30','32']#共15个
        for j in range(1, 6+1):
            if data_array[i][j] in div31_list:
                div31_num = div31_num + 1
        data_para_one['三分之一'] = div31_num
        #三分之二
        div32_num = 0
        div32_list = ['01','02','03','04','05','07','08','14',\
                      '17','18','20','21','27','30','32']#共15个
        for j in range(1, 6+1):
            if data_array[i][j] in div32_list:
                div32_num = div32_num + 1
        data_para_one['三分之二'] = div32_num
        #三分之三（只有204/619!!）
        div33_num = 0
        div33_list = ['02','03','04','05','08','14','17','18',\
                      '20','21','22','26','27','30','32']#共15个
        for j in range(1, 6+1):
            if data_array[i][j] in div33_list:
                div33_num = div33_num + 1
        data_para_one['三分之三'] = div33_num         
        #往期数据
        ##其实类似这种的，都应该从第100期开始算做正常数据
        num_old = 0           
        if i<(len(data_array)-1): #第1期没有往期数据
            for j in range(i+1, len(data_array)-1): #这里太慢了
                num_tmp = 0 #临时最大值
                for k in range(1, 6+1):
                    #加一个判断，加快速度
                    if k==4 and num_tmp<num_old - 2:
                        break                    
                    if data_array[i][k] in data_array[j][1:6+1]:
                        num_tmp = num_tmp + 1
                if num_tmp>num_old:
                    num_old = num_tmp
        else:
            num_old = 0
        data_para_one['往期数据'] = num_old
        #添加到总列表中
        data_para_array.append(data_para_one)
    
    return data_para_array

def percentCompute(filter_array, data_para_array): #百分比计算
    '''根据过滤参数计算过滤正确程度的百分比'''
    #命令行显示一下
    #print u'计算过滤参数的百分比'
    #百分比
    percent_array = []
    
    for i in range(0, len(filter_array)):
        #初始化为0
        percent_array.append(0) 
        #最大值/最小值均为str格式。范围均包含本身
        min_num = int(filter_array[i][3].split('-')[0]) #最小值
        max_num = int(filter_array[i][3].split('-')[1]) #最大值
        count = 0 #计数  
        #各过滤条件
        if '1号位' in filter_array[i][1]:
            for j in range(0, len(data_para_array)):
                if data_para_array[j]['1号位']>=min_num and data_para_array[j]['1号位']<=max_num:
                    count = count + 1
            #计算百分比
            percent_array[i] = '%.2f'%(count*100.0/len(data_para_array))                     
        if '2号位' in filter_array[i][1]:
            for j in range(0, len(data_para_array)):
                if data_para_array[j]['2号位']>=min_num and data_para_array[j]['2号位']<=max_num:
                    count = count + 1
            percent_array[i] = '%.2f'%(count*100.0/len(data_para_array)) 
        if '3号位' in filter_array[i][1]:
            for j in range(0, len(data_para_array)):
                if data_para_array[j]['3号位']>=min_num and data_para_array[j]['3号位']<=max_num:
                    count = count + 1
            percent_array[i] = '%.2f'%(count*100.0/len(data_para_array)) 
        if '4号位' in filter_array[i][1]:
            for j in range(0, len(data_para_array)):
                if data_para_array[j]['4号位']>=min_num and data_para_array[j]['4号位']<=max_num:
                    count = count + 1
            percent_array[i] = '%.2f'%(count*100.0/len(data_para_array)) 
        if '5号位' in filter_array[i][1]:
            for j in range(0, len(data_para_array)):
                if data_para_array[j]['5号位']>=min_num and data_para_array[j]['5号位']<=max_num:
                    count = count + 1
            percent_array[i] = '%.2f'%(count*100.0/len(data_para_array)) 
        if '6号位' in filter_array[i][1]:
            for j in range(0, len(data_para_array)):
                if data_para_array[j]['6号位']>=min_num and data_para_array[j]['6号位']<=max_num:
                    count = count + 1
            percent_array[i] = '%.2f'%(count*100.0/len(data_para_array)) 
        if '总和值' in filter_array[i][1]:
            for j in range(0, len(data_para_array)):
                if data_para_array[j]['总和值']>=min_num and data_para_array[j]['总和值']<=max_num:
                    count = count + 1
            percent_array[i] = '%.2f'%(count*100.0/len(data_para_array))
        if '前4位和值' in filter_array[i][1]:
            for j in range(0, len(data_para_array)):
                if data_para_array[j]['前4位和值']>=min_num and data_para_array[j]['前4位和值']<=max_num:
                    count = count + 1
            percent_array[i] = '%.2f'%(count*100.0/len(data_para_array))
        if '后4位和值' in filter_array[i][1]:
            for j in range(0, len(data_para_array)):
                if data_para_array[j]['后4位和值']>=min_num and data_para_array[j]['后4位和值']<=max_num:
                    count = count + 1
            percent_array[i] = '%.2f'%(count*100.0/len(data_para_array))             
        if '奇数' in filter_array[i][1]:
            for j in range(0, len(data_para_array)):
                if data_para_array[j]['奇数']>=min_num and data_para_array[j]['奇数']<=max_num:
                    count = count + 1
            percent_array[i] = '%.2f'%(count*100.0/len(data_para_array)) 
        if '偶数' in filter_array[i][1]:
            for j in range(0, len(data_para_array)):
                if data_para_array[j]['偶数']>=min_num and data_para_array[j]['偶数']<=max_num:
                    count = count + 1
            percent_array[i] = '%.2f'%(count*100.0/len(data_para_array)) 
        if '61间隔' in filter_array[i][1]:
            for j in range(0, len(data_para_array)):
                if data_para_array[j]['61间隔']>=min_num and data_para_array[j]['61间隔']<=max_num:
                    count = count + 1
            percent_array[i] = '%.2f'%(count*100.0/len(data_para_array))
        if '21间隔' in filter_array[i][1]:
            for j in range(0, len(data_para_array)):
                if data_para_array[j]['21间隔']>=min_num and data_para_array[j]['21间隔']<=max_num:
                    count = count + 1
            percent_array[i] = '%.2f'%(count*100.0/len(data_para_array))            
        if '41间隔' in filter_array[i][1]:
            for j in range(0, len(data_para_array)):
                if data_para_array[j]['41间隔']>=min_num and data_para_array[j]['41间隔']<=max_num:
                    count = count + 1
            percent_array[i] = '%.2f'%(count*100.0/len(data_para_array))
        if '43间隔' in filter_array[i][1]:
            for j in range(0, len(data_para_array)):
                if data_para_array[j]['43间隔']>=min_num and data_para_array[j]['43间隔']<=max_num:
                    count = count + 1
            percent_array[i] = '%.2f'%(count*100.0/len(data_para_array))            
        if '52间隔' in filter_array[i][1]:
            for j in range(0, len(data_para_array)):
                if data_para_array[j]['52间隔']>=min_num and data_para_array[j]['52间隔']<=max_num:
                    count = count + 1
            percent_array[i] = '%.2f'%(count*100.0/len(data_para_array))
        if '63间隔' in filter_array[i][1]:
            for j in range(0, len(data_para_array)):
                if data_para_array[j]['63间隔']>=min_num and data_para_array[j]['63间隔']<=max_num:
                    count = count + 1
            percent_array[i] = '%.2f'%(count*100.0/len(data_para_array))
        if '65间隔' in filter_array[i][1]:
            for j in range(0, len(data_para_array)):
                if data_para_array[j]['65间隔']>=min_num and data_para_array[j]['65间隔']<=max_num:
                    count = count + 1
            percent_array[i] = '%.2f'%(count*100.0/len(data_para_array))              
        if '质数' in filter_array[i][1]:
            for j in range(0, len(data_para_array)):
                if data_para_array[j]['质数']>=min_num and data_para_array[j]['质数']<=max_num:
                    count = count + 1
            percent_array[i] = '%.2f'%(count*100.0/len(data_para_array)) 
        if '除3余0' in filter_array[i][1]:
            for j in range(0, len(data_para_array)):
                if data_para_array[j]['除3余0']>=min_num and data_para_array[j]['除3余0']<=max_num:
                    count = count + 1
            percent_array[i] = '%.2f'%(count*100.0/len(data_para_array)) 
        if '除3余1' in filter_array[i][1]:
            for j in range(0, len(data_para_array)):
                if data_para_array[j]['除3余1']>=min_num and data_para_array[j]['除3余1']<=max_num:
                    count = count + 1
            percent_array[i] = '%.2f'%(count*100.0/len(data_para_array)) 
        if '除3余2' in filter_array[i][1]:
            for j in range(0, len(data_para_array)):
                if data_para_array[j]['除3余2']>=min_num and data_para_array[j]['除3余2']<=max_num:
                    count = count + 1
            percent_array[i] = '%.2f'%(count*100.0/len(data_para_array))
        if '除4余0' in filter_array[i][1]:
            for j in range(0, len(data_para_array)):
                if data_para_array[j]['除4余0']>=min_num and data_para_array[j]['除4余0']<=max_num:
                    count = count + 1
            percent_array[i] = '%.2f'%(count*100.0/len(data_para_array))
        if '除4余1' in filter_array[i][1]:
            for j in range(0, len(data_para_array)):
                if data_para_array[j]['除4余1']>=min_num and data_para_array[j]['除4余1']<=max_num:
                    count = count + 1
            percent_array[i] = '%.2f'%(count*100.0/len(data_para_array))
        if '除4余2' in filter_array[i][1]:
            for j in range(0, len(data_para_array)):
                if data_para_array[j]['除4余2']>=min_num and data_para_array[j]['除4余2']<=max_num:
                    count = count + 1
            percent_array[i] = '%.2f'%(count*100.0/len(data_para_array))
        if '除4余3' in filter_array[i][1]:
            for j in range(0, len(data_para_array)):
                if data_para_array[j]['除4余3']>=min_num and data_para_array[j]['除4余3']<=max_num:
                    count = count + 1
            percent_array[i] = '%.2f'%(count*100.0/len(data_para_array))                  
        if '除5余0' in filter_array[i][1]:
            for j in range(0, len(data_para_array)):
                if data_para_array[j]['除5余0']>=min_num and data_para_array[j]['除5余0']<=max_num:
                    count = count + 1
            percent_array[i] = '%.2f'%(count*100.0/len(data_para_array))
        if '除5余1' in filter_array[i][1]:
            for j in range(0, len(data_para_array)):
                if data_para_array[j]['除5余1']>=min_num and data_para_array[j]['除5余1']<=max_num:
                    count = count + 1
            percent_array[i] = '%.2f'%(count*100.0/len(data_para_array))
        if '除5余2' in filter_array[i][1]:
            for j in range(0, len(data_para_array)):
                if data_para_array[j]['除5余2']>=min_num and data_para_array[j]['除5余2']<=max_num:
                    count = count + 1
            percent_array[i] = '%.2f'%(count*100.0/len(data_para_array))
        if '除5余3' in filter_array[i][1]:
            for j in range(0, len(data_para_array)):
                if data_para_array[j]['除5余3']>=min_num and data_para_array[j]['除5余3']<=max_num:
                    count = count + 1
            percent_array[i] = '%.2f'%(count*100.0/len(data_para_array))
        if '除5余4' in filter_array[i][1]:
            for j in range(0, len(data_para_array)):
                if data_para_array[j]['除5余4']>=min_num and data_para_array[j]['除5余4']<=max_num:
                    count = count + 1
            percent_array[i] = '%.2f'%(count*100.0/len(data_para_array))
        if '除6余0' in filter_array[i][1]:
            for j in range(0, len(data_para_array)):
                if data_para_array[j]['除6余0']>=min_num and data_para_array[j]['除6余0']<=max_num:
                    count = count + 1
            percent_array[i] = '%.2f'%(count*100.0/len(data_para_array))
        if '除6余1' in filter_array[i][1]:
            for j in range(0, len(data_para_array)):
                if data_para_array[j]['除6余1']>=min_num and data_para_array[j]['除6余1']<=max_num:
                    count = count + 1
            percent_array[i] = '%.2f'%(count*100.0/len(data_para_array))
        if '除6余2' in filter_array[i][1]:
            for j in range(0, len(data_para_array)):
                if data_para_array[j]['除6余2']>=min_num and data_para_array[j]['除6余2']<=max_num:
                    count = count + 1
            percent_array[i] = '%.2f'%(count*100.0/len(data_para_array))
        if '除6余3' in filter_array[i][1]:
            for j in range(0, len(data_para_array)):
                if data_para_array[j]['除6余3']>=min_num and data_para_array[j]['除6余3']<=max_num:
                    count = count + 1
            percent_array[i] = '%.2f'%(count*100.0/len(data_para_array))
        if '除6余4' in filter_array[i][1]:
            for j in range(0, len(data_para_array)):
                if data_para_array[j]['除6余4']>=min_num and data_para_array[j]['除6余4']<=max_num:
                    count = count + 1
            percent_array[i] = '%.2f'%(count*100.0/len(data_para_array))
        if '除6余5' in filter_array[i][1]:
            for j in range(0, len(data_para_array)):
                if data_para_array[j]['除6余5']>=min_num and data_para_array[j]['除6余5']<=max_num:
                    count = count + 1
            percent_array[i] = '%.2f'%(count*100.0/len(data_para_array))                
        if '除7余0' in filter_array[i][1]:
            for j in range(0, len(data_para_array)):
                if data_para_array[j]['除7余0']>=min_num and data_para_array[j]['除7余0']<=max_num:
                    count = count + 1
            percent_array[i] = '%.2f'%(count*100.0/len(data_para_array))
        if '除7余1' in filter_array[i][1]:
            for j in range(0, len(data_para_array)):
                if data_para_array[j]['除7余1']>=min_num and data_para_array[j]['除7余1']<=max_num:
                    count = count + 1
            percent_array[i] = '%.2f'%(count*100.0/len(data_para_array))
        if '除7余2' in filter_array[i][1]:
            for j in range(0, len(data_para_array)):
                if data_para_array[j]['除7余2']>=min_num and data_para_array[j]['除7余2']<=max_num:
                    count = count + 1
            percent_array[i] = '%.2f'%(count*100.0/len(data_para_array))
        if '除7余3' in filter_array[i][1]:
            for j in range(0, len(data_para_array)):
                if data_para_array[j]['除7余3']>=min_num and data_para_array[j]['除7余3']<=max_num:
                    count = count + 1
            percent_array[i] = '%.2f'%(count*100.0/len(data_para_array))
        if '除7余4' in filter_array[i][1]:
            for j in range(0, len(data_para_array)):
                if data_para_array[j]['除7余4']>=min_num and data_para_array[j]['除7余4']<=max_num:
                    count = count + 1
            percent_array[i] = '%.2f'%(count*100.0/len(data_para_array))
        if '除7余5' in filter_array[i][1]:
            for j in range(0, len(data_para_array)):
                if data_para_array[j]['除7余5']>=min_num and data_para_array[j]['除7余5']<=max_num:
                    count = count + 1
            percent_array[i] = '%.2f'%(count*100.0/len(data_para_array))
        if '除7余6' in filter_array[i][1]:
            for j in range(0, len(data_para_array)):
                if data_para_array[j]['除7余6']>=min_num and data_para_array[j]['除7余6']<=max_num:
                    count = count + 1
            percent_array[i] = '%.2f'%(count*100.0/len(data_para_array))              
        if '高值区' in filter_array[i][1]:
            for j in range(0, len(data_para_array)):
                if data_para_array[j]['高值区']>=min_num and data_para_array[j]['高值区']<=max_num:
                    count = count + 1
            percent_array[i] = '%.2f'%(count*100.0/len(data_para_array)) 
        if '低值区' in filter_array[i][1]:
            for j in range(0, len(data_para_array)):
                if data_para_array[j]['低值区']>=min_num and data_para_array[j]['低值区']<=max_num:
                    count = count + 1
            percent_array[i] = '%.2f'%(count*100.0/len(data_para_array)) 
        if '区间1' in filter_array[i][1]:
            for j in range(0, len(data_para_array)):
                if data_para_array[j]['区间1']>=min_num and data_para_array[j]['区间1']<=max_num:
                    count = count + 1
            percent_array[i] = '%.2f'%(count*100.0/len(data_para_array)) 
        if '区间2' in filter_array[i][1]:
            for j in range(0, len(data_para_array)):
                if data_para_array[j]['区间2']>=min_num and data_para_array[j]['区间2']<=max_num:
                    count = count + 1
            percent_array[i] = '%.2f'%(count*100.0/len(data_para_array))
        if '区间3' in filter_array[i][1]:
            for j in range(0, len(data_para_array)):
                if data_para_array[j]['区间3']>=min_num and data_para_array[j]['区间3']<=max_num:
                    count = count + 1
            percent_array[i] = '%.2f'%(count*100.0/len(data_para_array)) 
        if '连号' in filter_array[i][1]:
            for j in range(0, len(data_para_array)):
                if data_para_array[j]['连号']>=min_num and data_para_array[j]['连号']<=max_num:
                    count = count + 1
            percent_array[i] = '%.2f'%(count*100.0/len(data_para_array))
        if '同尾' in filter_array[i][1]:
            for j in range(0, len(data_para_array)):
                if data_para_array[j]['同尾']>=min_num and data_para_array[j]['同尾']<=max_num:
                    count = count + 1
            percent_array[i] = '%.2f'%(count*100.0/len(data_para_array))
        if '开奖号码和' in filter_array[i][1]:
            for j in range(0, len(data_para_array)):
                if data_para_array[j]['开奖号码和']>=min_num and data_para_array[j]['开奖号码和']<=max_num:
                    count = count + 1
            percent_array[i] = '%.2f'%(count*100.0/len(data_para_array))
        if '尾号和' in filter_array[i][1]:
            for j in range(0, len(data_para_array)):
                if data_para_array[j]['尾号和']>=min_num and data_para_array[j]['尾号和']<=max_num:
                    count = count + 1
            percent_array[i] = '%.2f'%(count*100.0/len(data_para_array))              
        if 'AC值' in filter_array[i][1]:
            for j in range(0, len(data_para_array)):
                if data_para_array[j]['AC值']>=min_num and data_para_array[j]['AC值']<=max_num:
                    count = count + 1
            percent_array[i] = '%.2f'%(count*100.0/len(data_para_array)) 
        if '热号全' in filter_array[i][1]:
            for j in range(0, len(data_para_array)):
                if data_para_array[j]['热号全']>=min_num and data_para_array[j]['热号全']<=max_num:
                    count = count + 1
            percent_array[i] = '%.2f'%(count*100.0/len(data_para_array)) 
        if '温号全' in filter_array[i][1]:
            for j in range(0, len(data_para_array)):
                if data_para_array[j]['温号全']>=min_num and data_para_array[j]['温号全']<=max_num:
                    count = count + 1
            percent_array[i] = '%.2f'%(count*100.0/len(data_para_array)) 
        if '冷号全' in filter_array[i][1]:
            for j in range(0, len(data_para_array)):
                if data_para_array[j]['冷号全']>=min_num and data_para_array[j]['冷号全']<=max_num:
                    count = count + 1
            percent_array[i] = '%.2f'%(count*100.0/len(data_para_array)) 
        if '1期重号' in filter_array[i][1]:
            for j in range(0, len(data_para_array)-1):
                if data_para_array[j]['1期重号']>=min_num and data_para_array[j]['1期重号']<=max_num:
                    count = count + 1
            percent_array[i] = '%.2f'%(count*100.0/(len(data_para_array)-1)) #总数要少1期
        if '3期重号' in filter_array[i][1]:
            for j in range(0, len(data_para_array)-3):
                if data_para_array[j]['3期重号']>=min_num and data_para_array[j]['3期重号']<=max_num:
                    count = count + 1
            percent_array[i] = '%.2f'%(count*100.0/(len(data_para_array)-3)) #总数要少3期                    
        if '5期重号' in filter_array[i][1]:
            for j in range(0, len(data_para_array)-5):
                if data_para_array[j]['5期重号']>=min_num and data_para_array[j]['5期重号']<=max_num:
                    count = count + 1
            percent_array[i] = '%.2f'%(count*100.0/(len(data_para_array)-5)) #总数要少5期
        if '10期重号' in filter_array[i][1]:
            for j in range(0, len(data_para_array)):
                if data_para_array[j]['10期重号']>=min_num and data_para_array[j]['10期重号']<=max_num:
                    count = count + 1
            percent_array[i] = '%.2f'%(count*100.0/(len(data_para_array)-10)) #总数要少10期              
        if '1期临近值' in filter_array[i][1]:
            for j in range(0, len(data_para_array)-1):
                if data_para_array[j]['1期临近值']>=min_num and data_para_array[j]['1期临近值']<=max_num:
                    count = count + 1
            percent_array[i] = '%.2f'%(count*100.0/((len(data_para_array)-1))) #总数要少1期
        if '3期个数' in filter_array[i][1]:
            for j in range(0, len(data_para_array)):
                if data_para_array[j]['3期个数']>=min_num and data_para_array[j]['3期个数']<=max_num:
                    count = count + 1
            percent_array[i] = '%.2f'%(count*100.0/((len(data_para_array)-2))) #总数要少2期
        if '5期个数' in filter_array[i][1]:
            for j in range(0, len(data_para_array)):
                if data_para_array[j]['5期个数']>=min_num and data_para_array[j]['5期个数']<=max_num:
                    count = count + 1
            percent_array[i] = '%.2f'%(count*100.0/((len(data_para_array)-4))) #总数要少4期
        if '7期个数' in filter_array[i][1]:
            for j in range(0, len(data_para_array)):
                if data_para_array[j]['7期个数']>=min_num and data_para_array[j]['7期个数']<=max_num:
                    count = count + 1
            percent_array[i] = '%.2f'%(count*100.0/((len(data_para_array)-6))) #总数要少6期
        if '9期个数' in filter_array[i][1]:
            for j in range(0, len(data_para_array)):
                if data_para_array[j]['9期个数']>=min_num and data_para_array[j]['9期个数']<=max_num:
                    count = count + 1
            percent_array[i] = '%.2f'%(count*100.0/((len(data_para_array)-8))) #总数要少8期
        if '遗漏值和' in filter_array[i][1]:
            for j in range(0, len(data_para_array)):
                if data_para_array[j]['遗漏值和']>=min_num and data_para_array[j]['遗漏值和']<=max_num:
                    count = count + 1
            percent_array[i] = '%.2f'%(count*100.0/((len(data_para_array)-26))) #总数要少26期#因为最后出现的号29是在第26期出现的           
        if '固定投注' in filter_array[i][1]:
            for j in range(0, len(data_para_array)):
                if data_para_array[j]['固定投注']>=min_num and data_para_array[j]['固定投注']<=max_num:
                    count = count + 1                
            percent_array[i] = '%.2f'%(count*100.0/(len(data_para_array)))
        if '长列表' in filter_array[i][1]:
            for j in range(0, len(data_para_array)):
                if data_para_array[j]['长列表']>=min_num and data_para_array[j]['长列表']<=max_num:
                    count = count + 1                
            percent_array[i] = '%.2f'%(count*100.0/(len(data_para_array)))
        if '三分之一' in filter_array[i][1]:
            for j in range(0, len(data_para_array)):
                if data_para_array[j]['三分之一']>=min_num and data_para_array[j]['三分之一']<=max_num:
                    count = count + 1                
            percent_array[i] = '%.2f'%(count*100.0/(len(data_para_array)))
        if '三分之二' in filter_array[i][1]:
            for j in range(0, len(data_para_array)):
                if data_para_array[j]['三分之二']>=min_num and data_para_array[j]['三分之二']<=max_num:
                    count = count + 1                
            percent_array[i] = '%.2f'%(count*100.0/(len(data_para_array)))
        if '三分之三' in filter_array[i][1]:
            for j in range(0, len(data_para_array)):
                if data_para_array[j]['三分之三']>=min_num and data_para_array[j]['三分之三']<=max_num:
                    count = count + 1                
            percent_array[i] = '%.2f'%(count*100.0/(len(data_para_array)))                
        if '往期数据' in filter_array[i][1]:
            for j in range(0, 100): #只考虑最近100期（20071129）
            #for j in range(0, len(data_para_array)):
                if data_para_array[j]['往期数据']>=min_num and data_para_array[j]['往期数据']<=max_num:
                    count = count + 1                
            #percent_array[i] = '%.2f'%(count*100.0/(len(data_para_array)-1)) #总数要少1期
            percent_array[i] = '%.2f'%(count*100.0/100)
    #返回数据    
    return percent_array

def dataFiltrate(data_array, data_f, step, filter_array, redOrder, bet_array):#数据过滤
    '''过滤数据，并返回结果'''
    #最大值/最小值均为str格式。范围均包含本身
    min_num = int(filter_array[step-1][3].split('-')[0]) #最小值
    max_num = int(filter_array[step-1][3].split('-')[1]) #最大值
    #临时数组
    data_f_tmp = []
    #被过滤掉的数据（20071225）
    data_f_down = []
    #各过滤条件
    if '1号位' in filter_array[step-1][1]:
        for i in range(0, len(data_f)):
            if min_num<=data_f[i][0]<=max_num:
                data_f_tmp.append(data_f[i])
            else:#所有的条件都加上（20071225）
                data_f_down.append(data_f[i])#所有的条件都加上（20071225）
    if '2号位' in filter_array[step-1][1]:
        for i in range(0, len(data_f)):
            if min_num<=data_f[i][1]<=max_num:
                data_f_tmp.append(data_f[i])
            else:
                data_f_down.append(data_f[i])                
    if '3号位' in filter_array[step-1][1]:
        for i in range(0, len(data_f)):
            if min_num<=data_f[i][2]<=max_num:
                data_f_tmp.append(data_f[i])
            else:
                data_f_down.append(data_f[i])                
    if '4号位' in filter_array[step-1][1]:
        for i in range(0, len(data_f)):
            if min_num<=data_f[i][3]<=max_num:
                data_f_tmp.append(data_f[i])
            else:
                data_f_down.append(data_f[i])                
    if '5号位' in filter_array[step-1][1]:
        for i in range(0, len(data_f)):
            if min_num<=data_f[i][4]<=max_num:
                data_f_tmp.append(data_f[i])
            else:
                data_f_down.append(data_f[i])                
    if '6号位' in filter_array[step-1][1]:
        for i in range(0, len(data_f)):
            if min_num<=data_f[i][5]<=max_num:
                data_f_tmp.append(data_f[i])
            else:
                data_f_down.append(data_f[i])                 
    if '总和值' in filter_array[step-1][1]:
        for i in range(0, len(data_f)):
            sum_num = 0
            for j in range(0, 6):
                sum_num = sum_num + data_f[i][j]
            if min_num<=sum_num<=max_num:
                data_f_tmp.append(data_f[i])
            else:
                data_f_down.append(data_f[i])                 
    if '前4位和值' in filter_array[step-1][1]:
        for i in range(0, len(data_f)):
            sum14_num = 0
            for j in range(0, 4):
                sum14_num = sum14_num + data_f[i][j]
            if min_num<=sum14_num<=max_num:
                data_f_tmp.append(data_f[i])
            else:
                data_f_down.append(data_f[i])                 
    if '后4位和值' in filter_array[step-1][1]:
        for i in range(0, len(data_f)):
            sum36_num = 0
            for j in range(2, 6):
                sum36_num = sum36_num + data_f[i][j]
            if min_num<=sum36_num<=max_num:
                data_f_tmp.append(data_f[i])
            else:
                data_f_down.append(data_f[i])                 
    if '奇数' in filter_array[step-1][1]:
        for i in range(0, len(data_f)):
            odd_num = 0 
            for j in range(0, 6):
                if data_f[i][j]%2==1:
                    odd_num = odd_num + 1
            if min_num<=odd_num<=max_num:
                data_f_tmp.append(data_f[i])
            else:
                data_f_down.append(data_f[i])                 
    if '偶数' in filter_array[step-1][1]:
        for i in range(0, len(data_f)):
            even_num = 0 
            for j in range(0, 6):
                if data_f[i][j]%2==0:
                    even_num = even_num + 1
            if min_num<=even_num<=max_num:
                data_f_tmp.append(data_f[i])
            else:
                data_f_down.append(data_f[i])                 
    if '61间隔' in filter_array[step-1][1]:
        for i in range(0, len(data_f)):
            max_space_61 = data_f[i][5] - data_f[i][0]
            if min_num<=max_space_61<=max_num:
                data_f_tmp.append(data_f[i])
            else:
                data_f_down.append(data_f[i])                 
    if '21间隔' in filter_array[step-1][1]:
        for i in range(0, len(data_f)):
            max_space_21 = data_f[i][1] - data_f[i][0]
            if min_num<=max_space_21<=max_num:
                data_f_tmp.append(data_f[i])
            else:
                data_f_down.append(data_f[i])                 
    if '41间隔' in filter_array[step-1][1]:
        for i in range(0, len(data_f)):
            max_space_41 = data_f[i][3] - data_f[i][0]
            if min_num<=max_space_41<=max_num:
                data_f_tmp.append(data_f[i])
            else:
                data_f_down.append(data_f[i])                 
    if '43间隔' in filter_array[step-1][1]:
        for i in range(0, len(data_f)):
            max_space_43 = data_f[i][3] - data_f[i][2]
            if min_num<=max_space_43<=max_num:
                data_f_tmp.append(data_f[i])
            else:
                data_f_down.append(data_f[i])                
    if '52间隔' in filter_array[step-1][1]:
        for i in range(0, len(data_f)):
            max_space_52 = data_f[i][4] - data_f[i][1]
            if min_num<=max_space_52<=max_num:
                data_f_tmp.append(data_f[i])
            else:
                data_f_down.append(data_f[i])                
    if '63间隔' in filter_array[step-1][1]:
        for i in range(0, len(data_f)):
            max_space_63 = data_f[i][5] - data_f[i][2]
            if min_num<=max_space_63<=max_num:
                data_f_tmp.append(data_f[i])
            else:
                data_f_down.append(data_f[i])                
    if '65间隔' in filter_array[step-1][1]:
        for i in range(0, len(data_f)):
            max_space_65 = data_f[i][5] - data_f[i][4]
            if min_num<=max_space_65<=max_num:
                data_f_tmp.append(data_f[i])
            else:
                data_f_down.append(data_f[i])                
    if '质数' in filter_array[step-1][1]:
        for i in range(0, len(data_f)):
            prime_num = 0  
            for j in range(0, 6):
                if data_f[i][j] in [2,3,5,7,11,13,17,19,23,29,31]:
                    prime_num = prime_num + 1
            if min_num<=prime_num<=max_num:
                data_f_tmp.append(data_f[i])
            else:
                data_f_down.append(data_f[i])                
    if '除3余0' in filter_array[step-1][1]:
        for i in range(0, len(data_f)):
            residue_num30 = 0  
            for j in range(0, 6):
                if data_f[i][j] in [3,6,9,12,15,18,21,24,27,30,33]:
                    residue_num30 = residue_num30 + 1
            if min_num<=residue_num30<=max_num:
                data_f_tmp.append(data_f[i])
            else:
                data_f_down.append(data_f[i])                
    if '除3余1' in filter_array[step-1][1]:
        for i in range(0, len(data_f)):
            residue_num31 = 0  
            for j in range(0, 6):
                if data_f[i][j] in [1,4,7,10,13,16,19,22,25,28,31]:
                    residue_num31 = residue_num31 + 1
            if min_num<=residue_num31<=max_num:
                data_f_tmp.append(data_f[i])
            else:
                data_f_down.append(data_f[i])                
    if '除3余2' in filter_array[step-1][1]:
        for i in range(0, len(data_f)):
            residue_num32 = 0  
            for j in range(0, 6):
                if data_f[i][j] in [2,5,8,11,14,17,20,23,26,29,32]:
                    residue_num32 = residue_num32 + 1
            if min_num<=residue_num32<=max_num:
                data_f_tmp.append(data_f[i])
            else:
                data_f_down.append(data_f[i])                
    if '除4余0' in filter_array[step-1][1]:
        for i in range(0, len(data_f)):
            residue_num40 = 0  
            for j in range(0, 6):
                if data_f[i][j] in [4,8,12,16,20,24,28,32]:
                    residue_num40 = residue_num40 + 1
            if min_num<=residue_num40<=max_num:
                data_f_tmp.append(data_f[i])
            else:
                data_f_down.append(data_f[i])                
    if '除4余1' in filter_array[step-1][1]:
        for i in range(0, len(data_f)):
            residue_num41 = 0  
            for j in range(0, 6):
                if data_f[i][j] in [1,5,9,13,17,21,25,29,33]:
                    residue_num41 = residue_num41 + 1
            if min_num<=residue_num41<=max_num:
                data_f_tmp.append(data_f[i])
            else:
                data_f_down.append(data_f[i])                
    if '除4余2' in filter_array[step-1][1]:
        for i in range(0, len(data_f)):
            residue_num42 = 0  
            for j in range(0, 6):
                if data_f[i][j] in [2,6,10,14,18,22,26,30]:
                    residue_num42 = residue_num42 + 1
            if min_num<=residue_num42<=max_num:
                data_f_tmp.append(data_f[i])
            else:
                data_f_down.append(data_f[i])                
    if '除4余3' in filter_array[step-1][1]:
        for i in range(0, len(data_f)):
            residue_num43 = 0  
            for j in range(0, 6):
                if data_f[i][j] in [3,7,11,15,19,23,27,31]:
                    residue_num43 = residue_num43 + 1
            if min_num<=residue_num43<=max_num:
                data_f_tmp.append(data_f[i])
            else:
                data_f_down.append(data_f[i])                
    if '除5余0' in filter_array[step-1][1]:
        for i in range(0, len(data_f)):
            residue_num50 = 0  
            for j in range(0, 6):
                if data_f[i][j] in [5,10,15,20,25,30]:
                    residue_num50 = residue_num50 + 1
            if min_num<=residue_num50<=max_num:
                data_f_tmp.append(data_f[i])
            else:
                data_f_down.append(data_f[i])                
    if '除5余1' in filter_array[step-1][1]:
        for i in range(0, len(data_f)):
            residue_num51 = 0  
            for j in range(0, 6):
                if data_f[i][j] in [1,6,11,16,21,26,31]:
                    residue_num51 = residue_num51 + 1
            if min_num<=residue_num51<=max_num:
                data_f_tmp.append(data_f[i])
            else:
                data_f_down.append(data_f[i])                
    if '除5余2' in filter_array[step-1][1]:
        for i in range(0, len(data_f)):
            residue_num52 = 0  
            for j in range(0, 6):
                if data_f[i][j] in [2,7,12,17,22,27,32]:
                    residue_num52 = residue_num52 + 1
            if min_num<=residue_num52<=max_num:
                data_f_tmp.append(data_f[i])
            else:
                data_f_down.append(data_f[i])                
    if '除5余3' in filter_array[step-1][1]:
        for i in range(0, len(data_f)):
            residue_num53 = 0  
            for j in range(0, 6):
                if data_f[i][j] in [3,8,13,18,23,28,33]:
                    residue_num53 = residue_num53 + 1
            if min_num<=residue_num53<=max_num:
                data_f_tmp.append(data_f[i])
            else:
                data_f_down.append(data_f[i])                
    if '除5余4' in filter_array[step-1][1]:
        for i in range(0, len(data_f)):
            residue_num54 = 0  
            for j in range(0, 6):
                if data_f[i][j] in [4,9,14,19,24,29]:
                    residue_num54 = residue_num54 + 1
            if min_num<=residue_num54<=max_num:
                data_f_tmp.append(data_f[i])
            else:
                data_f_down.append(data_f[i])                
    if '除6余0' in filter_array[step-1][1]:
        for i in range(0, len(data_f)):
            residue_num60 = 0  
            for j in range(0, 6):
                if data_f[i][j] in [6,12,18,24,30]:
                    residue_num60 = residue_num60 + 1
            if min_num<=residue_num60<=max_num:
                data_f_tmp.append(data_f[i])
            else:
                data_f_down.append(data_f[i])                
    if '除6余1' in filter_array[step-1][1]:
        for i in range(0, len(data_f)):
            residue_num61 = 0  
            for j in range(0, 6):
                if data_f[i][j] in [1,7,13,19,25,31]:
                    residue_num61 = residue_num61 + 1
            if min_num<=residue_num61<=max_num:
                data_f_tmp.append(data_f[i])
            else:
                data_f_down.append(data_f[i])                
    if '除6余2' in filter_array[step-1][1]:
        for i in range(0, len(data_f)):
            residue_num62 = 0  
            for j in range(0, 6):
                if data_f[i][j] in [2,8,14,20,26,32]:
                    residue_num62 = residue_num62 + 1
            if min_num<=residue_num62<=max_num:
                data_f_tmp.append(data_f[i])
            else:
                data_f_down.append(data_f[i])                
    if '除6余3' in filter_array[step-1][1]:
        for i in range(0, len(data_f)):
            residue_num63 = 0  
            for j in range(0, 6):
                if data_f[i][j] in [3,9,15,21,27,33]:
                    residue_num63 = residue_num63 + 1
            if min_num<=residue_num63<=max_num:
                data_f_tmp.append(data_f[i])
            else:
                data_f_down.append(data_f[i])                
    if '除6余4' in filter_array[step-1][1]:
        for i in range(0, len(data_f)):
            residue_num64 = 0  
            for j in range(0, 6):
                if data_f[i][j] in [4,10,16,22,28]:
                    residue_num64 = residue_num64 + 1
            if min_num<=residue_num64<=max_num:
                data_f_tmp.append(data_f[i])
            else:
                data_f_down.append(data_f[i])                
    if '除6余5' in filter_array[step-1][1]:
        for i in range(0, len(data_f)):
            residue_num65 = 0  
            for j in range(0, 6):
                if data_f[i][j] in [5,11,17,23,29]:
                    residue_num65 = residue_num65 + 1
            if min_num<=residue_num65<=max_num:
                data_f_tmp.append(data_f[i])
            else:
                data_f_down.append(data_f[i])                
    if '除7余0' in filter_array[step-1][1]:
        for i in range(0, len(data_f)):
            residue_num70 = 0  
            for j in range(0, 6):
                if data_f[i][j] in [7,14,21,28]:
                    residue_num70 = residue_num70 + 1
            if min_num<=residue_num70<=max_num:
                data_f_tmp.append(data_f[i])
            else:
                data_f_down.append(data_f[i])                
    if '除7余1' in filter_array[step-1][1]:
        for i in range(0, len(data_f)):
            residue_num71 = 0  
            for j in range(0, 6):
                if data_f[i][j] in [1,8,15,22,29]:
                    residue_num71 = residue_num71 + 1
            if min_num<=residue_num71<=max_num:
                data_f_tmp.append(data_f[i])
            else:
                data_f_down.append(data_f[i])                
    if '除7余2' in filter_array[step-1][1]:
        for i in range(0, len(data_f)):
            residue_num72 = 0  
            for j in range(0, 6):
                if data_f[i][j] in [2,9,16,23,30]:
                    residue_num72 = residue_num72 + 1
            if min_num<=residue_num72<=max_num:
                data_f_tmp.append(data_f[i])
            else:
                data_f_down.append(data_f[i])                
    if '除7余3' in filter_array[step-1][1]:
        for i in range(0, len(data_f)):
            residue_num73 = 0  
            for j in range(0, 6):
                if data_f[i][j] in [3,10,17,24,31]:
                    residue_num73 = residue_num73 + 1
            if min_num<=residue_num73<=max_num:
                data_f_tmp.append(data_f[i])
            else:
                data_f_down.append(data_f[i])                
    if '除7余4' in filter_array[step-1][1]:
        for i in range(0, len(data_f)):
            residue_num74 = 0  
            for j in range(0, 6):
                if data_f[i][j] in [4,11,18,25,32]:
                    residue_num74 = residue_num74 + 1
            if min_num<=residue_num74<=max_num:
                data_f_tmp.append(data_f[i])
            else:
                data_f_down.append(data_f[i])                
    if '除7余5' in filter_array[step-1][1]:
        for i in range(0, len(data_f)):
            residue_num75 = 0  
            for j in range(0, 6):
                if data_f[i][j] in [5,12,19,26,33]:
                    residue_num75 = residue_num75 + 1
            if min_num<=residue_num75<=max_num:
                data_f_tmp.append(data_f[i])
            else:
                data_f_down.append(data_f[i])                
    if '除7余6' in filter_array[step-1][1]:
        for i in range(0, len(data_f)):
            residue_num76 = 0  
            for j in range(0, 6):
                if data_f[i][j] in [6,13,20,27]:
                    residue_num76 = residue_num76 + 1
            if min_num<=residue_num76<=max_num:
                data_f_tmp.append(data_f[i])
            else:
                data_f_down.append(data_f[i])                
    if '高值区' in filter_array[step-1][1]:
        for i in range(0, len(data_f)):
            high_num = 0  
            for j in range(0, 6):
                if data_f[i][j]>17:
                    high_num = high_num + 1
            if min_num<=high_num<=max_num:
                data_f_tmp.append(data_f[i])
            else:
                data_f_down.append(data_f[i])                
    if '低值区' in filter_array[step-1][1]:
        for i in range(0, len(data_f)):
            low_num = 0  
            for j in range(0, 6):
                if data_f[i][j]<17:
                    low_num = low_num + 1
            if min_num<=low_num<=max_num:
                data_f_tmp.append(data_f[i])
            else:
                data_f_down.append(data_f[i])                
    if '区间1' in filter_array[step-1][1]:
        for i in range(0, len(data_f)):
            area1_num = 0  
            for j in range(0, 6):
                if data_f[i][j]<12:
                    area1_num = area1_num + 1
            if min_num<=area1_num<=max_num:
                data_f_tmp.append(data_f[i])
            else:
                data_f_down.append(data_f[i])                
    if '区间2' in filter_array[step-1][1]:
        for i in range(0, len(data_f)):
            area2_num = 0  
            for j in range(0, 6):
                if 11<data_f[i][j]<23:
                    area2_num = area2_num + 1
            if min_num<=area2_num<=max_num:
                data_f_tmp.append(data_f[i])
            else:
                data_f_down.append(data_f[i])                
    if '区间3' in filter_array[step-1][1]:
        for i in range(0, len(data_f)):
            area3_num = 0  
            for j in range(0, 6):
                if data_f[i][j]>22:
                    area3_num = area3_num + 1
            if min_num<=area3_num<=max_num:
                data_f_tmp.append(data_f[i])
            else:
                data_f_down.append(data_f[i])                
    if '连号' in filter_array[step-1][1]:
        for i in range(0, len(data_f)):
            continuous_num = 0  
            for j in range(0, 5):
                if data_f[i][j+1] - data_f[i][j]==1:
                    continuous_num = continuous_num + 1
            if min_num<=continuous_num<=max_num:
                data_f_tmp.append(data_f[i])
            else:
                data_f_down.append(data_f[i])                
    if '同尾' in filter_array[step-1][1]:
        for i in range(0, len(data_f)):
            same_nail_num = 0
            times = [] #次数
            for j in range(0, 9+1):
                times.append(0) 
            for j in range(0, 6):
                times[(int(data_f[i][j])%10)] = times[(int(data_f[i][j])%10)] + 1
            for j in range(0, 9+1):
                if times[j]>1:
                    same_nail_num = same_nail_num + 1                 
            if min_num<=same_nail_num<=max_num:
                data_f_tmp.append(data_f[i])
            else:
                data_f_down.append(data_f[i])                
    if '开奖号码和' in filter_array[step-1][1]:
        for i in range(0, len(data_f)):
            sum_12 = 0
            for j in range(0, 6):
                sum_12 = sum_12 + int(data_f[i][j])%10
                sum_12 = sum_12 + int(data_f[i][j])/10
            if min_num<=sum_12<=max_num:
                data_f_tmp.append(data_f[i])
            else:
                data_f_down.append(data_f[i])                
    if '尾号和' in filter_array[step-1][1]:
        for i in range(0, len(data_f)):
            nail_sum = 0
            for j in range(0, 6):
                nail_sum = nail_sum + int(data_f[i][j])%10
            if min_num<=nail_sum<=max_num:
                data_f_tmp.append(data_f[i])
            else:
                data_f_down.append(data_f[i])                
    if 'AC值' in filter_array[step-1][1]:
        for i in range(0, len(data_f)):
            ac_num = 0  
            details = []
            for t1 in range(0, 6):
                for t2 in range(t1+1, 6):
                    if (data_f[i][t2] - data_f[i][t1]) in details:
                        continue
                    else:
                        details.append(data_f[i][t2] - data_f[i][t1])
            ac_num = len(details) - (6-1)
            if min_num<=ac_num<=max_num:
                data_f_tmp.append(data_f[i])
            else:
                data_f_down.append(data_f[i])                
    if '热号全' in filter_array[step-1][1]:
        for i in range(0, len(data_f)):
            hot_num = 0  
            for j in range(0, 6):
                if '%.2d'%(data_f[i][j]) in redOrder[:11]:
                    hot_num = hot_num + 1
            if min_num<=hot_num<=max_num:
                data_f_tmp.append(data_f[i])
            else:
                data_f_down.append(data_f[i])                
    if '温号全' in filter_array[step-1][1]:
        for i in range(0, len(data_f)):
            warm_num = 0  
            for j in range(0, 6):
                if '%.2d'%(data_f[i][j]) in redOrder[11:22]:
                    warm_num = warm_num + 1
            if min_num<=warm_num<=max_num:
                data_f_tmp.append(data_f[i])
            else:
                data_f_down.append(data_f[i])                
    if '冷号全' in filter_array[step-1][1]:
        for i in range(0, len(data_f)):
            cold_num = 0  
            for j in range(0, 6):
                if '%.2d'%(data_f[i][j]) in redOrder[22:]:
                    cold_num = cold_num + 1
            if min_num<=cold_num<=max_num:
                data_f_tmp.append(data_f[i])
            else:
                data_f_down.append(data_f[i])                
    if '热号100' in filter_array[step-1][1]:
        for i in range(0, len(data_f)):
            hot100_num = 0  
            for j in range(0, 6):
                if '%.2d'%(data_f[i][j]) in redOrder100[:11]:
                    hot100_num = hot100_num + 1
            if min_num<=hot100_num<=max_num:
                data_f_tmp.append(data_f[i])
            else:
                data_f_down.append(data_f[i])                
    if '1期重号' in filter_array[step-1][1]:
        for i in range(0, len(data_f)):
            repeat1_num = 0  
            for j in range(0, 6):
                if '%.2d'%(data_f[i][j]) in data_array[0][1:6+1]:
                    repeat1_num = repeat1_num + 1
            if min_num<=repeat1_num<=max_num:
                data_f_tmp.append(data_f[i])
            else:
                data_f_down.append(data_f[i])                
    if '3期重号' in filter_array[step-1][1]:
        tmp_list = [] #临时数组(int)，前3期的数据（没有重复的）
        for j in range(1, 6+1):
            if int(data_array[0][j]) not in tmp_list:
                tmp_list.append(int(data_array[0][j]))
            if int(data_array[1][j]) not in tmp_list:
                tmp_list.append(int(data_array[1][j]))
            if int(data_array[2][j]) not in tmp_list:
                tmp_list.append(int(data_array[2][j]))                
        for i in range(0, len(data_f)):
            repeat3_num = 0  
            for j in range(0, 6):
                if data_f[i][j] in tmp_list:
                    repeat3_num = repeat3_num + 1
            if min_num<=repeat3_num<=max_num:
                data_f_tmp.append(data_f[i])
            else:
                data_f_down.append(data_f[i])                
    if '5期重号' in filter_array[step-1][1]:
        tmp_list = [] #临时数组(int)，前5期的数据（没有重复的）
        for j in range(1, 6+1):
            if int(data_array[0][j]) not in tmp_list:
                tmp_list.append(int(data_array[0][j]))
            if int(data_array[1][j]) not in tmp_list:
                tmp_list.append(int(data_array[1][j]))
            if int(data_array[2][j]) not in tmp_list:
                tmp_list.append(int(data_array[2][j]))
            if int(data_array[3][j]) not in tmp_list:
                tmp_list.append(int(data_array[3][j]))
            if int(data_array[4][j]) not in tmp_list:
                tmp_list.append(int(data_array[4][j]))                  
        for i in range(0, len(data_f)):
            repeat5_num = 0  
            for j in range(0, 6):
                if data_f[i][j] in tmp_list:
                    repeat5_num = repeat5_num + 1
            if min_num<=repeat5_num<=max_num:
                data_f_tmp.append(data_f[i])
            else:
                data_f_down.append(data_f[i])                
    if '10期重号' in filter_array[step-1][1]:
        tmp_list = [] #临时数组(int)，前5+4期的数据（没有重复的）
        #在添加'10期重号'的时候感觉上面那个“4”好像不对～～
        for j in range(1, 6+1):
            #2007-07-26改
            if int(data_array[0+5][j]) not in tmp_list:
                tmp_list.append(int(data_array[0][j]))
            if int(data_array[1+5][j]) not in tmp_list:
                tmp_list.append(int(data_array[1][j]))
            if int(data_array[2+5][j]) not in tmp_list:
                tmp_list.append(int(data_array[2][j]))
            if int(data_array[3+5][j]) not in tmp_list:
                tmp_list.append(int(data_array[3][j]))
            if int(data_array[4+5][j]) not in tmp_list:
                tmp_list.append(int(data_array[4][j]))
            '''
            if int(data_array[5+5][j]) not in tmp_list:
                tmp_list.append(int(data_array[5][j]))
            if int(data_array[6+5][j]) not in tmp_list:
                tmp_list.append(int(data_array[6][j]))
            if int(data_array[7+5][j]) not in tmp_list:
                tmp_list.append(int(data_array[7][j]))
            if int(data_array[8+5][j]) not in tmp_list:
                tmp_list.append(int(data_array[8][j]))
            if int(data_array[9+5][j]) not in tmp_list:
                tmp_list.append(int(data_array[9][j]))
            '''
        for i in range(0, len(data_f)):
            repeat10_num = 0  
            for j in range(0, 6):
                if data_f[i][j] in tmp_list:
                    repeat10_num = repeat10_num + 1
            if min_num<=repeat10_num<=max_num:
                data_f_tmp.append(data_f[i])
            else:
                data_f_down.append(data_f[i])                
    if '1期临近值' in filter_array[step-1][1]:
        tmp_list = [] #临时数组(int)，将上一期中所有＋1/－1的数存起来
        for j in range(1, 6+1):
            tmp_list.append(int(data_array[0][j])-1)
            tmp_list.append(int(data_array[0][j])+1)        
        for i in range(0, len(data_f)):
            near_num = 0
            for j in range(0, 6):
                if data_f[i][j] in tmp_list:
                    near_num = near_num + 1
            if min_num<=near_num<=max_num:
                data_f_tmp.append(data_f[i])
            else:
                data_f_down.append(data_f[i])                
    if '3期个数' in filter_array[step-1][1]:
        tmp_list = [] #临时数组(int)，前2期的数据（没有重复的）
        for j in range(1, 6+1):
            if int(data_array[0][j]) not in tmp_list:
                tmp_list.append(int(data_array[0][j]))
            if int(data_array[1][j]) not in tmp_list:
                tmp_list.append(int(data_array[1][j]))
        for i in range(0, len(data_f)):
            num_l3 = len(tmp_list)
            for j in range(0, 6):
                if data_f[i][j] not in tmp_list:
                    num_l3 = num_l3 + 1
            if min_num<=num_l3<=max_num:
                data_f_tmp.append(data_f[i])
            else:
                data_f_down.append(data_f[i])                
    if '5期个数' in filter_array[step-1][1]:
        tmp_list = [] #临时数组(int)，前4期的数据（没有重复的）
        for j in range(1, 6+1):
            if int(data_array[0][j]) not in tmp_list:
                tmp_list.append(int(data_array[0][j]))
            if int(data_array[1][j]) not in tmp_list:
                tmp_list.append(int(data_array[1][j]))
            if int(data_array[2][j]) not in tmp_list:
                tmp_list.append(int(data_array[2][j]))
            if int(data_array[3][j]) not in tmp_list:
                tmp_list.append(int(data_array[3][j]))                
        for i in range(0, len(data_f)):
            num_l5 = len(tmp_list)
            for j in range(0, 6):
                if data_f[i][j] not in tmp_list:
                    num_l5 = num_l5 + 1
            if min_num<=num_l5<=max_num:
                data_f_tmp.append(data_f[i])
            else:
                data_f_down.append(data_f[i])                
    if '7期个数' in filter_array[step-1][1]:
        tmp_list = [] #临时数组(int)，前6期的数据（没有重复的）
        for j in range(1, 6+1):
            if int(data_array[0][j]) not in tmp_list:
                tmp_list.append(int(data_array[0][j]))
            if int(data_array[1][j]) not in tmp_list:
                tmp_list.append(int(data_array[1][j]))
            if int(data_array[2][j]) not in tmp_list:
                tmp_list.append(int(data_array[2][j]))
            if int(data_array[3][j]) not in tmp_list:
                tmp_list.append(int(data_array[3][j]))
            if int(data_array[4][j]) not in tmp_list:
                tmp_list.append(int(data_array[4][j]))
            if int(data_array[5][j]) not in tmp_list:
                tmp_list.append(int(data_array[5][j]))
        for i in range(0, len(data_f)):
            num_l7 = len(tmp_list)
            for j in range(0, 6):
                if data_f[i][j] not in tmp_list:
                    num_l7 = num_l7 + 1
            if min_num<=num_l7<=max_num:
                data_f_tmp.append(data_f[i])
            else:
                data_f_down.append(data_f[i])                
    if '9期个数' in filter_array[step-1][1]:
        tmp_list = [] #临时数组(int)，前8期的数据（没有重复的）
        for j in range(1, 6+1):
            if int(data_array[0][j]) not in tmp_list:
                tmp_list.append(int(data_array[0][j]))
            if int(data_array[1][j]) not in tmp_list:
                tmp_list.append(int(data_array[1][j]))
            if int(data_array[2][j]) not in tmp_list:
                tmp_list.append(int(data_array[2][j]))
            if int(data_array[3][j]) not in tmp_list:
                tmp_list.append(int(data_array[3][j]))
            if int(data_array[4][j]) not in tmp_list:
                tmp_list.append(int(data_array[4][j]))
            if int(data_array[5][j]) not in tmp_list:
                tmp_list.append(int(data_array[5][j]))
            if int(data_array[6][j]) not in tmp_list:
                tmp_list.append(int(data_array[6][j]))
            if int(data_array[7][j]) not in tmp_list:
                tmp_list.append(int(data_array[7][j]))                
        for i in range(0, len(data_f)):
            num_l9 = len(tmp_list)
            for j in range(0, 6):
                if data_f[i][j] not in tmp_list:
                    num_l9 = num_l9 + 1
            if min_num<=num_l9<=max_num:
                data_f_tmp.append(data_f[i])
            else:
                data_f_down.append(data_f[i])                
    if '遗漏值和' in filter_array[step-1][1]:
        for i in range(0, len(data_f)):
            miss_sum = 0
            for j in range(0, 6):
                for k in range(0, len(data_array)):
                    if '%.2d'%data_f[i][j] in data_array[k][1:6+1]: #注意data_f是int型的list
                        miss_sum = miss_sum + (k+1)
                        break
            if min_num<=miss_sum<=max_num:
                data_f_tmp.append(data_f[i])
            else:
                data_f_down.append(data_f[i])                
    if '固定投注' in filter_array[step-1][1]:
        for i in range(0, len(data_f)):
            num_fix = 0
            for j in range(0, len(bet_array)):
                num_tmp = 0
                for k in range(0, 6):
                    if int(bet_array[j][k]) in data_f[i]:
                        num_tmp = num_tmp + 1
                if num_tmp>num_fix:
                    num_fix = num_tmp            
            if min_num<=num_fix<=max_num:
                data_f_tmp.append(data_f[i])
            else:
                data_f_down.append(data_f[i])                
    if '长列表' in filter_array[step-1][1]:
        long_list = ['01','02','05','07','10','11','13','14',\
                     '17','18','19','20','21','22','23','24',\
                     '26','27','28','29','30','32','33']#5组共23个        
        for i in range(0, len(data_f)):
            long_list_num = 0
            for j in range(0, 6):
                if '%.2d'%(data_f[i][j]) in long_list:
                    long_list_num = long_list_num + 1
            if min_num<=long_list_num<=max_num:
                data_f_tmp.append(data_f[i])
            else:
                data_f_down.append(data_f[i])                
    if '三分之一' in filter_array[step-1][1]:
        div31_list = ['01','03','04','05','07','08','14','17',\
                     '18','20','22','26','27','30','32']#共15个        
        for i in range(0, len(data_f)):
            div31_num = 0
            for j in range(0, 6):
                if '%.2d'%(data_f[i][j]) in div31_list:
                    div31_num = div31_num + 1
            if min_num<=div31_num<=max_num:
                data_f_tmp.append(data_f[i])
            else:
                data_f_down.append(data_f[i])                
    if '三分之二' in filter_array[step-1][1]: 
        div32_list = ['01','02','03','04','05','07','08','14',\
                      '17','18','20','21','27','30','32']#共15个        
        for i in range(0, len(data_f)):
            div32_num = 0
            for j in range(0, 6):
                if '%.2d'%(data_f[i][j]) in div32_list:
                    div32_num = div32_num + 1
            if min_num<=div32_num<=max_num:
                data_f_tmp.append(data_f[i])
            else:
                data_f_down.append(data_f[i])                
    if '三分之三' in filter_array[step-1][1]: #只有204/614!!
        div33_list = ['02','03','04','05','08','14','17','18',\
                      '20','21','22','26','27','30','32']#共15个        
        for i in range(0, len(data_f)):
            div33_num = 0
            for j in range(0, 6):
                if '%.2d'%(data_f[i][j]) in div33_list:
                    div33_num = div33_num + 1
            if min_num<=div33_num<=max_num:                
                data_f_tmp.append(data_f[i])
            else:
                data_f_down.append(data_f[i])                
    if '往期数据' in filter_array[step-1][1]:
        t1 = time.time()
        if min_num==4 and max_num==5:
            #新的过滤方法
            ##  8818-->8821  | 49s-->9s(14s)
            print (u'注：使用[4,5](新)，花费').encode(locale.getdefaultlocale()[1]),
            for i in range(0, len(data_f)):
                #这个版本没有误差率了
                option1 = True
                option2 = False
                data_ft = '%.2d %.2d %.2d %.2d %.2d %.2d'\
                          %(data_f[i][0],data_f[i][1],data_f[i][2],data_f[i][3],data_f[i][4],data_f[i][5])
                for j in range(0, len(data_array)):
                    if data_ft==' '.join(data_array[j][1:7]):
                        option1 = False
                        break
                if option1:
                    for j in range(0, len(data_array)):
                        num_tmp = 0                    
                        for k in range(1, 7):
                            if data_array[j][k] in data_ft:
                                num_tmp = num_tmp + 1
                        if num_tmp>3:
                            option2 = True
                            break
                if option2==True:
                    data_f_tmp.append(data_f[i])
                else:
                    data_f_down.append(data_f[i])                    
                '''#这个版本有误差
                option = False
                data_ft = '%.2d %.2d %.2d %.2d %.2d %.2d'\
                          %(data_f[i][0],data_f[i][1],data_f[i][2],data_f[i][3],data_f[i][4],data_f[i][5])
                for j in range(0, len(data_array)):
                    #'01 07 14 16 18 25'
                    #'05 08 18 23 25 31'
                    #'08 13 17 21 23 32'
                    ##判断是否=6（为啥上面三注判断不出来呢？而下面两注就可以呢？？）
                    #'01 05 08 13 18 25'
                    #'04 08 13 18 26 30'
                    if data_ft==' '.join(data_array[j][1:7]):
                        option = False
                        break
                    else:
                        ##判断是否>3
                        num_tmp = 0                    
                        for k in range(1, 7):
                            if data_array[j][k] in data_ft:
                                num_tmp = num_tmp + 1
                        if num_tmp>3:
                            option = True
                            break
                if option==True:
                    data_f_tmp.append(data_f[i])
                else:
                    pass
                '''
        elif min_num==4 and max_num==4: 
            #修改后的过滤方法 #在旧的基础上
            ##50s-->25s
            print (u'注：使用[4,4](修)，花费').encode(locale.getdefaultlocale()[1]),
            option = False
            for i in range(0, len(data_f)):
                option = False
                data_ft = '%.2d %.2d %.2d %.2d %.2d %.2d'\
                          %(data_f[i][0],data_f[i][1],data_f[i][2],data_f[i][3],data_f[i][4],data_f[i][5])                
                for j in range(0, len(data_array)):
                    num_tmp = 0
                    for k in range(1, 7):    
                        if data_array[j][k] in data_ft:
                            num_tmp = num_tmp + 1
                        if k==4 and num_tmp==1:
                            break
                    if num_tmp>4: 
                        option = False
                        break
                    if num_tmp==4:
                        option = True
                if option:
                    data_f_tmp.append(data_f[i])
                else:
                    data_f_down.append(data_f[i])                    
        else:
            print (u'注：使用普通过滤方法，花费').encode(locale.getdefaultlocale()[1]),
            #这里太慢了!!!!
            for i in range(0, len(data_f)):
                num_old = 0
                #这里太慢了!!!!
                for j in range(0, len(data_array)):
                    num_tmp = 0
                    #for k in range(0, 6): #这里错了
                    for k in range(1, 6+1):    
                        #加一个判断，加快一些速度
                        if k==4 and num_tmp<num_old -2:
                            break
                        if int(data_array[j][k]) in data_f[i]:
                            num_tmp = num_tmp + 1
                    if num_tmp>num_old:
                        num_old = num_tmp
                if min_num<=num_old<=max_num:
                    data_f_tmp.append(data_f[i])
                else:
                    data_f_down.append(data_f[i])                    
        t2 = time.time()
        print '%.2f'%(t2-t1),(u'秒').encode(locale.getdefaultlocale()[1])
    #转换回去
    #data_f = data_f_tmp 
    #返回数据    
    #return data_f
    #直接将临时数组传回去也可以，不知道哪样会更“经济”一些
    return data_f_tmp, data_f_down

def blueCoumpute(data_array): #蓝球统计及计算
    '''计算蓝球各球的出球次数、步长和遗漏值'''
    blue_times = [] #蓝球各球的出球次数
    for i in range(0, 16): #初始化
        blue_times.append(0)
    for i in range(0, len(data_array)):
        blue_times[int(data_array[i][7])-1] = blue_times[int(data_array[i][7])-1] + 1

    blue_step = [] #蓝球各球的出球步长
    for i in range(0, 16): 
        blue_step.append(len(data_array)/blue_times[i])
        
    blue_drop = [] #蓝球的遗漏值（即多少期未出现）
    for i in range(0, 16): #初始化
        blue_drop.append(0)
    for i in range(0, len(data_array)): #倒序
        if blue_drop[int(data_array[i][7])-1]==0:
            blue_drop[int(data_array[i][7])-1] = i + 1 
    return blue_times, blue_step, blue_drop

def blueAdvice(data_array, blue_times):
    '''计算篮球推荐所需要的所有参数'''

    #算出热号和冷号
    blue_hot = []
    blue_cold = []
    sum_tmp = 0 #次数统计
    while True:
        for i in range(0, len(blue_times)):
            if blue_times[i]==max(blue_times): #判断是不是最大的
                blue_hot.append('%.2d'%(i+1))
                sum_tmp = sum_tmp + blue_times[i]
                blue_times[i] = 0 #把最大整成0
                break
        if (sum_tmp*2)>=len(data_array): #判断次数之和是否到了一半
            break
    for i in range(0, len(blue_times)): #不等于0的就是cold
        if blue_times[i]!=0:
            blue_cold.append('%.2d'%(i+1))
    
    blueDatas = [] #篮球相关数据
    for i in range(0, len(data_array)):
        t = {'奇偶':'','热冷':'','大小':'','与上期相同':'','与红球相同':'','5期内有无':'','11期内有无':''}
        #奇偶
        if int(data_array[i][7])%2==0:
            t['奇偶'] = '偶'
        else:
            t['奇偶'] = '奇'
        #热冷
        if data_array[i][7] in blue_hot:
            t['热冷'] = '热'
        else:
            t['热冷'] = '冷'
        #大小
        if int(data_array[i][7])>8:
            t['大小'] = '大'
        else:
            t['大小'] = '小'
        #与上期相同（包括+3和-3）
        if i<len(data_array)-1 and (int(data_array[i+1][7])-3)<=int(data_array[i][7])<=(int(data_array[i+1][7])+3):
            t['与上期相同'] = '同'
        elif i<len(data_array)-1 and (int(data_array[i+1][7])+3)>16 and int(data_array[i][7])<=(int(data_array[i+1][7])-16+3):
            t['与上期相同'] = '同'
        elif i<len(data_array)-1 and (int(data_array[i+1][7])-3)<0 and (int(data_array[i+1][7])+16-3)<=int(data_array[i][7]):
            t['与上期相同'] = '同'            
        else:
            t['与上期相同'] = '不'
        #与红球相同（这个其实没什么用）（因为现在完全不能考虑红蓝配合）
        if data_array[i][7] in data_array[i][1:7]:
            t['与红球相同'] = '同'
        else:
            t['与红球相同'] = '不'
        #5期内有无（这个其实没什么用）（必须得50％对50％才行）
        if i>len(data_array)-6:
            t['5期内有无'] = '无'
        elif data_array[i][7]==data_array[i+1][7] or \
             data_array[i][7]==data_array[i+2][7] or \
             data_array[i][7]==data_array[i+3][7] or \
             data_array[i][7]==data_array[i+4][7] or \
             data_array[i][7]==data_array[i+5][7]:
            t['5期内有无'] = '有'
        else:
            t['5期内有无'] = '无'
        #11期内有无
        if i>len(data_array)-12:
            t['11期内有无'] = '无'
        elif data_array[i][7]==data_array[i+1][7] or \
             data_array[i][7]==data_array[i+2][7] or \
             data_array[i][7]==data_array[i+3][7] or \
             data_array[i][7]==data_array[i+4][7] or \
             data_array[i][7]==data_array[i+5][7] or \
             data_array[i][7]==data_array[i+6][7] or \
             data_array[i][7]==data_array[i+7][7] or \
             data_array[i][7]==data_array[i+8][7] or \
             data_array[i][7]==data_array[i+9][7] or \
             data_array[i][7]==data_array[i+10][7] or \
             data_array[i][7]==data_array[i+11][7]:
            t['11期内有无'] = '有'
        else:
            t['11期内有无'] = '无'            

        blueDatas.append(t)
            
    #推荐需要用到的参考数据    
    adviceDatas = {'奇连奇':0,'奇连偶':0, \
                   '偶连奇':0,'偶连偶':0, \
                   '奇连奇连奇':0,'奇连奇连偶':0, \
                   '奇连偶连奇':0,'奇连偶连偶':0, \
                   '偶连奇连奇':0,'偶连奇连偶':0, \
                   '偶连偶连奇':0,'偶连偶连偶':0, \
                   '热连冷':0,'热连热':0, \
                   '冷连冷':0,'冷连热':0, \
                   '热连热连冷':0,'热连热连热':0, \
                   '冷连热连冷':0,'冷连热连热':0, \
                   '热连冷连冷':0,'热连冷连热':0, \
                   '冷连冷连冷':0,'冷连冷连热':0, \
                   '大连小':0,'大连大':0, \
                   '小连小':0,'小连大':0, \
                   '大连大连小':0,'大连大连大':0, \
                   '大连小连小':0,'大连小连大':0, \
                   '小连大连小':0,'小连大连大':0, \
                   '小连小连小':0,'小连小连大':0, \
                   '同连不':0,'同连同':0, \
                   '不连不':0,'不连同':0, \
                   '同连同连不':0,'同连同连同':0, \
                   '不连同连不':0,'不连同连同':0, \
                   '同连不连不':0,'同连不连同':0, \
                   '不连不连不':0,'不连不连同':0, \
                   '有连无':0,'有连有':0, \
                   '无连无':0,'无连有':0, \
                   '有连有连无':0,'有连有连有':0, \
                   '无连有连无':0,'无连有连有':0, \
                   '有连无连无':0,'有连无连有':0, \
                   '无连无连无':0,'无连无连有':0                 
                   }
    #奇偶性
    for i in range(0, len(blueDatas)-1):
        if blueDatas[i]['奇偶']=='奇' and blueDatas[i+1]['奇偶']=='奇':
            adviceDatas['奇连奇'] = adviceDatas['奇连奇'] + 1
        if blueDatas[i]['奇偶']=='偶' and blueDatas[i+1]['奇偶']=='奇':
            adviceDatas['奇连偶'] = adviceDatas['奇连偶'] + 1
        if blueDatas[i]['奇偶']=='奇' and blueDatas[i+1]['奇偶']=='偶':
            adviceDatas['偶连奇'] = adviceDatas['偶连奇'] + 1
        if blueDatas[i]['奇偶']=='偶' and blueDatas[i+1]['奇偶']=='偶':
            adviceDatas['偶连偶'] = adviceDatas['偶连偶'] + 1              
    for i in range(0, len(blueDatas)-2):
        if blueDatas[i]['奇偶']=='奇' and blueDatas[i+1]['奇偶']=='奇' and blueDatas[i+2]['奇偶']=='奇':
            adviceDatas['奇连奇连奇'] = adviceDatas['奇连奇连奇'] + 1
        if blueDatas[i]['奇偶']=='偶' and blueDatas[i+1]['奇偶']=='奇' and blueDatas[i+2]['奇偶']=='奇':
            adviceDatas['奇连奇连偶'] = adviceDatas['奇连奇连偶'] + 1
        if blueDatas[i]['奇偶']=='奇' and blueDatas[i+1]['奇偶']=='偶' and blueDatas[i+2]['奇偶']=='奇':
            adviceDatas['奇连偶连奇'] = adviceDatas['奇连偶连奇'] + 1
        if blueDatas[i]['奇偶']=='偶' and blueDatas[i+1]['奇偶']=='偶' and blueDatas[i+2]['奇偶']=='奇':
            adviceDatas['奇连偶连偶'] = adviceDatas['奇连偶连偶'] + 1
        if blueDatas[i]['奇偶']=='奇' and blueDatas[i+1]['奇偶']=='奇' and blueDatas[i+2]['奇偶']=='偶':
            adviceDatas['偶连奇连奇'] = adviceDatas['偶连奇连奇'] + 1
        if blueDatas[i]['奇偶']=='偶' and blueDatas[i+1]['奇偶']=='奇' and blueDatas[i+2]['奇偶']=='偶':
            adviceDatas['偶连奇连偶'] = adviceDatas['偶连奇连偶'] + 1
        if blueDatas[i]['奇偶']=='奇' and blueDatas[i+1]['奇偶']=='偶' and blueDatas[i+2]['奇偶']=='偶':
            adviceDatas['偶连偶连奇'] = adviceDatas['偶连偶连奇'] + 1
        if blueDatas[i]['奇偶']=='偶' and blueDatas[i+1]['奇偶']=='偶' and blueDatas[i+2]['奇偶']=='偶':
            adviceDatas['偶连偶连偶'] = adviceDatas['偶连偶连偶'] + 1
    #热冷性
    for i in range(0, len(blueDatas)-1):
        if blueDatas[i]['热冷']=='冷' and blueDatas[i+1]['热冷']=='热':
            adviceDatas['热连冷'] = adviceDatas['热连冷'] + 1
        if blueDatas[i]['热冷']=='热' and blueDatas[i+1]['热冷']=='热':
            adviceDatas['热连热'] = adviceDatas['热连热'] + 1
        if blueDatas[i]['热冷']=='冷' and blueDatas[i+1]['热冷']=='冷':
            adviceDatas['冷连冷'] = adviceDatas['冷连冷'] + 1
        if blueDatas[i]['热冷']=='热' and blueDatas[i+1]['热冷']=='冷':
            adviceDatas['冷连热'] = adviceDatas['冷连热'] + 1
    for i in range(0, len(blueDatas)-2):
        if blueDatas[i]['热冷']=='冷' and blueDatas[i+1]['热冷']=='热' and blueDatas[i+2]['热冷']=='热':
            adviceDatas['热连热连冷'] = adviceDatas['热连热连冷'] + 1
        if blueDatas[i]['热冷']=='热' and blueDatas[i+1]['热冷']=='热' and blueDatas[i+2]['热冷']=='热':
            adviceDatas['热连热连热'] = adviceDatas['热连热连热'] + 1
        if blueDatas[i]['热冷']=='冷' and blueDatas[i+1]['热冷']=='热' and blueDatas[i+2]['热冷']=='冷':
            adviceDatas['冷连热连冷'] = adviceDatas['冷连热连冷'] + 1
        if blueDatas[i]['热冷']=='热' and blueDatas[i+1]['热冷']=='热' and blueDatas[i+2]['热冷']=='冷':
            adviceDatas['冷连热连热'] = adviceDatas['冷连热连热'] + 1
        if blueDatas[i]['热冷']=='冷' and blueDatas[i+1]['热冷']=='冷' and blueDatas[i+2]['热冷']=='热':
            adviceDatas['热连冷连冷'] = adviceDatas['热连冷连冷'] + 1
        if blueDatas[i]['热冷']=='热' and blueDatas[i+1]['热冷']=='冷' and blueDatas[i+2]['热冷']=='热':
            adviceDatas['热连冷连热'] = adviceDatas['热连冷连热'] + 1
        if blueDatas[i]['热冷']=='冷' and blueDatas[i+1]['热冷']=='冷' and blueDatas[i+2]['热冷']=='冷':
            adviceDatas['冷连冷连冷'] = adviceDatas['冷连冷连冷'] + 1
        if blueDatas[i]['热冷']=='热' and blueDatas[i+1]['热冷']=='冷' and blueDatas[i+2]['热冷']=='冷':
            adviceDatas['冷连冷连热'] = adviceDatas['冷连冷连热'] + 1
    #大小性
    for i in range(0, len(blueDatas)-1):
        if blueDatas[i]['大小']=='小' and blueDatas[i+1]['大小']=='大':
            adviceDatas['大连小'] = adviceDatas['大连小'] + 1
        if blueDatas[i]['大小']=='大' and blueDatas[i+1]['大小']=='大':
            adviceDatas['大连大'] = adviceDatas['大连大'] + 1
        if blueDatas[i]['大小']=='小' and blueDatas[i+1]['大小']=='小':
            adviceDatas['小连小'] = adviceDatas['小连小'] + 1
        if blueDatas[i]['大小']=='大' and blueDatas[i+1]['大小']=='小':
            adviceDatas['小连大'] = adviceDatas['小连大'] + 1
    for i in range(0, len(blueDatas)-2):
        if blueDatas[i]['大小']=='小' and blueDatas[i+1]['大小']=='大' and blueDatas[i+2]['大小']=='大':
            adviceDatas['大连大连小'] = adviceDatas['大连大连小'] + 1
        if blueDatas[i]['大小']=='大' and blueDatas[i+1]['大小']=='大' and blueDatas[i+2]['大小']=='大':
            adviceDatas['大连大连大'] = adviceDatas['大连大连大'] + 1
        if blueDatas[i]['大小']=='小' and blueDatas[i+1]['大小']=='大' and blueDatas[i+2]['大小']=='小':
            adviceDatas['小连大连小'] = adviceDatas['小连大连小'] + 1
        if blueDatas[i]['大小']=='大' and blueDatas[i+1]['大小']=='大' and blueDatas[i+2]['大小']=='小':
            adviceDatas['小连大连大'] = adviceDatas['小连大连大'] + 1
        if blueDatas[i]['大小']=='小' and blueDatas[i+1]['大小']=='小' and blueDatas[i+2]['大小']=='大':
            adviceDatas['大连小连小'] = adviceDatas['大连小连小'] + 1
        if blueDatas[i]['大小']=='大' and blueDatas[i+1]['大小']=='小' and blueDatas[i+2]['大小']=='大':
            adviceDatas['大连小连大'] = adviceDatas['大连小连大'] + 1
        if blueDatas[i]['大小']=='小' and blueDatas[i+1]['大小']=='小' and blueDatas[i+2]['大小']=='小':
            adviceDatas['小连小连小'] = adviceDatas['小连小连小'] + 1
        if blueDatas[i]['大小']=='大' and blueDatas[i+1]['大小']=='小' and blueDatas[i+2]['大小']=='小':
            adviceDatas['小连小连大'] = adviceDatas['小连小连大'] + 1
    #相同性
    for i in range(0, len(blueDatas)-1):
        if blueDatas[i]['与上期相同']=='不' and blueDatas[i+1]['与上期相同']=='同':
            adviceDatas['同连不'] = adviceDatas['同连不'] + 1
        if blueDatas[i]['与上期相同']=='同' and blueDatas[i+1]['与上期相同']=='同':
            adviceDatas['同连同'] = adviceDatas['同连同'] + 1
        if blueDatas[i]['与上期相同']=='不' and blueDatas[i+1]['与上期相同']=='不':
            adviceDatas['不连不'] = adviceDatas['不连不'] + 1
        if blueDatas[i]['与上期相同']=='同' and blueDatas[i+1]['与上期相同']=='不':
            adviceDatas['不连同'] = adviceDatas['不连同'] + 1
    for i in range(0, len(blueDatas)-2):
        if blueDatas[i]['与上期相同']=='不' and blueDatas[i+1]['与上期相同']=='同' and blueDatas[i+2]['与上期相同']=='同':
            adviceDatas['同连同连不'] = adviceDatas['同连同连不'] + 1
        if blueDatas[i]['与上期相同']=='同' and blueDatas[i+1]['与上期相同']=='同' and blueDatas[i+2]['与上期相同']=='同':
            adviceDatas['同连同连同'] = adviceDatas['同连同连同'] + 1
        if blueDatas[i]['与上期相同']=='不' and blueDatas[i+1]['与上期相同']=='同' and blueDatas[i+2]['与上期相同']=='不':
            adviceDatas['不连同连不'] = adviceDatas['不连同连不'] + 1
        if blueDatas[i]['与上期相同']=='同' and blueDatas[i+1]['与上期相同']=='同' and blueDatas[i+2]['与上期相同']=='不':
            adviceDatas['不连同连同'] = adviceDatas['不连同连同'] + 1
        if blueDatas[i]['与上期相同']=='不' and blueDatas[i+1]['与上期相同']=='不' and blueDatas[i+2]['与上期相同']=='同':
            adviceDatas['同连不连不'] = adviceDatas['同连不连不'] + 1
        if blueDatas[i]['与上期相同']=='同' and blueDatas[i+1]['与上期相同']=='不' and blueDatas[i+2]['与上期相同']=='同':
            adviceDatas['同连不连同'] = adviceDatas['同连不连同'] + 1
        if blueDatas[i]['与上期相同']=='不' and blueDatas[i+1]['与上期相同']=='不' and blueDatas[i+2]['与上期相同']=='不':
            adviceDatas['不连不连不'] = adviceDatas['不连不连不'] + 1
        if blueDatas[i]['与上期相同']=='同' and blueDatas[i+1]['与上期相同']=='不' and blueDatas[i+2]['与上期相同']=='不':
            adviceDatas['不连不连同'] = adviceDatas['不连不连同'] + 1
    #有无性
    for i in range(0, len(blueDatas)-1):
        if blueDatas[i]['11期内有无']=='无' and blueDatas[i+1]['11期内有无']=='有':
            adviceDatas['有连无'] = adviceDatas['有连无'] + 1
        if blueDatas[i]['11期内有无']=='有' and blueDatas[i+1]['11期内有无']=='有':
            adviceDatas['有连有'] = adviceDatas['有连有'] + 1
        if blueDatas[i]['11期内有无']=='无' and blueDatas[i+1]['11期内有无']=='无':
            adviceDatas['无连无'] = adviceDatas['无连无'] + 1
        if blueDatas[i]['11期内有无']=='有' and blueDatas[i+1]['11期内有无']=='无':
            adviceDatas['无连有'] = adviceDatas['无连有'] + 1
    for i in range(0, len(blueDatas)-2):
        if blueDatas[i]['11期内有无']=='无' and blueDatas[i+1]['11期内有无']=='有' and blueDatas[i+2]['11期内有无']=='有':
            adviceDatas['有连有连无'] = adviceDatas['有连有连无'] + 1
        if blueDatas[i]['11期内有无']=='有' and blueDatas[i+1]['11期内有无']=='有' and blueDatas[i+2]['11期内有无']=='有':
            adviceDatas['有连有连有'] = adviceDatas['有连有连有'] + 1
        if blueDatas[i]['11期内有无']=='无' and blueDatas[i+1]['11期内有无']=='有' and blueDatas[i+2]['11期内有无']=='无':
            adviceDatas['无连有连无'] = adviceDatas['无连有连无'] + 1
        if blueDatas[i]['11期内有无']=='有' and blueDatas[i+1]['11期内有无']=='有' and blueDatas[i+2]['11期内有无']=='无':
            adviceDatas['无连有连有'] = adviceDatas['无连有连有'] + 1
        if blueDatas[i]['11期内有无']=='无' and blueDatas[i+1]['11期内有无']=='无' and blueDatas[i+2]['11期内有无']=='有':
            adviceDatas['有连无连无'] = adviceDatas['有连无连无'] + 1
        if blueDatas[i]['11期内有无']=='有' and blueDatas[i+1]['11期内有无']=='无' and blueDatas[i+2]['11期内有无']=='有':
            adviceDatas['有连无连有'] = adviceDatas['有连无连有'] + 1
        if blueDatas[i]['11期内有无']=='无' and blueDatas[i+1]['11期内有无']=='无' and blueDatas[i+2]['11期内有无']=='无':
            adviceDatas['无连无连无'] = adviceDatas['无连无连无'] + 1
        if blueDatas[i]['11期内有无']=='有' and blueDatas[i+1]['11期内有无']=='无' and blueDatas[i+2]['11期内有无']=='无':
            adviceDatas['无连无连有'] = adviceDatas['无连无连有'] + 1
            
    #返回数据
    return blueDatas, adviceDatas, blue_hot, blue_cold
