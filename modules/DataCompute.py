# -*- coding: cp936 -*-
# otherrrr@gmail.com
# 数据计算

def redOrderCoumput(data_array): #红球冷热温号计算
    '''计算红球各个球的出球次数，并按照次数排列'''
    redOrder = [] #按序排列的球号
    redTimes = [] #对应球号的次数

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
                
    return redOrder, redTimes

def dataParaCompute(data_array, redOrder): #开奖数据的参数计算
    '''根据开奖数据计算出各项参数，可用来计算百分比，也可以用来单独显示'''
    #为什么要单独算这个呢？是因为将来如果需要单独显示其中的某一项就可以直接用了
    data_para_array = [] #所有数据参数列表

    for i in range(0, len(data_array)):
        #数据参数中的一期（共28项，与过滤条件数目相同） #0.9.2
        data_para_one = {'1号位':0,'2号位':0,'3号位':0,\
                         '4号位':0,'5号位':0,'6号位':0,\
                         '合值':0,'奇数':0,'偶数':0,\
                         '最大间隔':0,'质数':0,\
                         '除3余0':0,'除3余1':0,'除3余2':0,\
                         '高值区':0,'低值区':0,\
                         '区间1':0,'区间2':0,'区间3':0,\
                         '连号':0,'AC值':0,\
                         '热号':0,'温号':0,'冷号':0,\
                         '1期重号':0,'5期重号':0,'1期临近值':0,\
                         '3期个数':0,'5期个数':0} 
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
        #计算合值
        sum_num = 0 
        for j in range(1, 6+1):
            sum_num = sum_num + int(data_array[i][j])
        data_para_one['合值'] = sum_num
        #计算奇数个数
        odd_num = 0 
        for j in range(1, 6+1):
            if int(data_array[i][j])%2==1:
                odd_num = odd_num + 1
        data_para_one['奇数'] = odd_num
        #计算偶数个数
        even_num = 6 - odd_num
        data_para_one['偶数'] = even_num
        #计算最大间隔值
        max_space = int(data_array[i][6]) - int(data_array[i][1]) 
        data_para_one['最大间隔'] = max_space  
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
        #计算热号个数
        hot_num = 0
        for j in range(1, 6+1):
            if data_array[i][j] in redOrder[:11]: #热号就是出球次数排在前11位的
                hot_num = hot_num + 1
        data_para_one['热号'] = hot_num
        #计算温号个数
        warm_num = 0
        for j in range(1, 6+1):
            if data_array[i][j] in redOrder[11:22]:
                warm_num = warm_num + 1
        data_para_one['温号'] = warm_num
        #计算冷号个数
        cold_num = 0
        for j in range(1, 6+1):
            if data_array[i][j] in redOrder[22:]:
                cold_num = cold_num + 1
        data_para_one['冷号'] = cold_num
        #计算1期重号个数
        repeat1_num = 0
        if i==(len(data_array)-1): #第1期没有上一期
            repeat1_num = 0
        else:
            for j in range(1, 6+1):
                if data_array[i][j] in data_array[i+1][1:6+1]:
                    repeat1_num = repeat1_num + 1
        data_para_one['1期重号'] = repeat1_num
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
        #添加到总列表中
        data_para_array.append(data_para_one)
    
    return data_para_array

def percentCompute(filter_array, data_para_array): #百分比计算
    '''根据过滤参数计算过滤正确程度的百分比'''
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
        if '合值' in filter_array[i][1]:
            for j in range(0, len(data_para_array)):
                if data_para_array[j]['合值']>=min_num and data_para_array[j]['合值']<=max_num:
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
        if '最大间隔' in filter_array[i][1]:
            for j in range(0, len(data_para_array)):
                if data_para_array[j]['最大间隔']>=min_num and data_para_array[j]['最大间隔']<=max_num:
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
        if 'AC值' in filter_array[i][1]:
            for j in range(0, len(data_para_array)):
                if data_para_array[j]['AC值']>=min_num and data_para_array[j]['AC值']<=max_num:
                    count = count + 1
            percent_array[i] = '%.2f'%(count*100.0/len(data_para_array)) 
        if '热号' in filter_array[i][1]:
            for j in range(0, len(data_para_array)):
                if data_para_array[j]['热号']>=min_num and data_para_array[j]['热号']<=max_num:
                    count = count + 1
            percent_array[i] = '%.2f'%(count*100.0/len(data_para_array)) 
        if '温号' in filter_array[i][1]:
            for j in range(0, len(data_para_array)):
                if data_para_array[j]['温号']>=min_num and data_para_array[j]['温号']<=max_num:
                    count = count + 1
            percent_array[i] = '%.2f'%(count*100.0/len(data_para_array)) 
        if '冷号' in filter_array[i][1]:
            for j in range(0, len(data_para_array)):
                if data_para_array[j]['冷号']>=min_num and data_para_array[j]['冷号']<=max_num:
                    count = count + 1
            percent_array[i] = '%.2f'%(count*100.0/len(data_para_array)) 
        if '1期重号' in filter_array[i][1]:
            for j in range(0, len(data_para_array)):
                if data_para_array[j]['1期重号']>=min_num and data_para_array[j]['1期重号']<=max_num:
                    count = count + 1
            percent_array[i] = '%.2f'%(count*100.0/(len(data_para_array)-1)) #总数要少1期
        if '5期重号' in filter_array[i][1]:
            for j in range(0, len(data_para_array)):
                if data_para_array[j]['5期重号']>=min_num and data_para_array[j]['5期重号']<=max_num:
                    count = count + 1
            percent_array[i] = '%.2f'%(count*100.0/(len(data_para_array)-5)) #总数要少5期            
        if '1期临近值' in filter_array[i][1]:
            for j in range(0, len(data_para_array)):
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
    #返回数据    
    return percent_array

def dataFiltrate(data_array, data_f, step, filter_array, redOrder):#数据过滤
    '''过滤数据，并返回结果'''
    #最大值/最小值均为str格式。范围均包含本身
    min_num = int(filter_array[step-1][3].split('-')[0]) #最小值
    max_num = int(filter_array[step-1][3].split('-')[1]) #最大值
    #临时数组
    data_f_tmp = [] 
    #各过滤条件
    if '1号位' in filter_array[step-1][1]:
        for i in range(0, len(data_f)):
            if min_num<=data_f[i][0]<=max_num:
                data_f_tmp.append(data_f[i])
    if '2号位' in filter_array[step-1][1]:
        for i in range(0, len(data_f)):
            if min_num<=data_f[i][1]<=max_num:
                data_f_tmp.append(data_f[i])
    if '3号位' in filter_array[step-1][1]:
        for i in range(0, len(data_f)):
            if min_num<=data_f[i][2]<=max_num:
                data_f_tmp.append(data_f[i])
    if '4号位' in filter_array[step-1][1]:
        for i in range(0, len(data_f)):
            if min_num<=data_f[i][3]<=max_num:
                data_f_tmp.append(data_f[i])
    if '5号位' in filter_array[step-1][1]:
        for i in range(0, len(data_f)):
            if min_num<=data_f[i][4]<=max_num:
                data_f_tmp.append(data_f[i])
    if '6号位' in filter_array[step-1][1]:
        for i in range(0, len(data_f)):
            if min_num<=data_f[i][5]<=max_num:
                data_f_tmp.append(data_f[i])  
    if '合值' in filter_array[step-1][1]:
        for i in range(0, len(data_f)):
            sum_num = 0
            for j in range(0, 6):
                sum_num = sum_num + data_f[i][j]
            if min_num<=sum_num<=max_num:
                data_f_tmp.append(data_f[i])       
    if '奇数' in filter_array[step-1][1]:
        for i in range(0, len(data_f)):
            odd_num = 0 
            for j in range(0, 6):
                if data_f[i][j]%2==1:
                    odd_num = odd_num + 1
            if min_num<=odd_num<=max_num:
                data_f_tmp.append(data_f[i])  
    if '偶数' in filter_array[step-1][1]:
        for i in range(0, len(data_f)):
            even_num = 0 
            for j in range(0, 6):
                if data_f[i][j]%2==0:
                    even_num = even_num + 1
            if min_num<=even_num<=max_num:
                data_f_tmp.append(data_f[i])   
    if '最大间隔' in filter_array[step-1][1]:
        for i in range(0, len(data_f)):
            max_space = data_f[i][5] - data_f[i][0]
            if min_num<=max_space<=max_num:
                data_f_tmp.append(data_f[i])  
    if '质数' in filter_array[step-1][1]:
        for i in range(0, len(data_f)):
            prime_num = 0  
            for j in range(0, 6):
                if data_f[i][j] in [2,3,5,7,11,13,17,19,23,29,31]:
                    prime_num = prime_num + 1
            if min_num<=prime_num<=max_num:
                data_f_tmp.append(data_f[i]) 
    if '除3余0' in filter_array[step-1][1]:
        for i in range(0, len(data_f)):
            residue_num30 = 0  
            for j in range(0, 6):
                if data_f[i][j] in [3,6,9,12,15,18,21,24,27,30,33]:
                    residue_num30 = residue_num30 + 1
            if min_num<=residue_num30<=max_num:
                data_f_tmp.append(data_f[i]) 
    if '除3余1' in filter_array[step-1][1]:
        for i in range(0, len(data_f)):
            residue_num31 = 0  
            for j in range(0, 6):
                if data_f[i][j] in [1,4,7,10,13,16,19,22,25,28,31]:
                    residue_num31 = residue_num31 + 1
            if min_num<=residue_num31<=max_num:
                data_f_tmp.append(data_f[i])  
    if '除3余2' in filter_array[step-1][1]:
        for i in range(0, len(data_f)):
            residue_num32 = 0  
            for j in range(0, 6):
                if data_f[i][j] in [2,5,8,11,14,17,20,23,26,29,32]:
                    residue_num32 = residue_num32 + 1
            if min_num<=residue_num32<=max_num:
                data_f_tmp.append(data_f[i])     
    if '高值区' in filter_array[step-1][1]:
        for i in range(0, len(data_f)):
            high_num = 0  
            for j in range(0, 6):
                if data_f[i][j]>17:
                    high_num = high_num + 1
            if min_num<=high_num<=max_num:
                data_f_tmp.append(data_f[i])   
    if '低值区' in filter_array[step-1][1]:
        for i in range(0, len(data_f)):
            low_num = 0  
            for j in range(0, 6):
                if data_f[i][j]<17:
                    low_num = low_num + 1
            if min_num<=low_num<=max_num:
                data_f_tmp.append(data_f[i])     
    if '区间1' in filter_array[step-1][1]:
        for i in range(0, len(data_f)):
            area1_num = 0  
            for j in range(0, 6):
                if data_f[i][j]<12:
                    area1_num = area1_num + 1
            if min_num<=area1_num<=max_num:
                data_f_tmp.append(data_f[i])   
    if '区间2' in filter_array[step-1][1]:
        for i in range(0, len(data_f)):
            area2_num = 0  
            for j in range(0, 6):
                if 11<data_f[i][j]<23:
                    area2_num = area2_num + 1
            if min_num<=area2_num<=max_num:
                data_f_tmp.append(data_f[i]) 
    if '区间3' in filter_array[step-1][1]:
        for i in range(0, len(data_f)):
            area3_num = 0  
            for j in range(0, 6):
                if data_f[i][j]>22:
                    area3_num = area3_num + 1
            if min_num<=area3_num<=max_num:
                data_f_tmp.append(data_f[i])     
    if '连号' in filter_array[step-1][1]:
        for i in range(0, len(data_f)):
            continuous_num = 0  
            for j in range(0, 5):
                if data_f[i][j+1] - data_f[i][j]==1:
                    continuous_num = continuous_num + 1
            if min_num<=continuous_num<=max_num:
                data_f_tmp.append(data_f[i])    
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
    if '热号' in filter_array[step-1][1]:
        for i in range(0, len(data_f)):
            hot_num = 0  
            for j in range(0, 6):
                if '%.2d'%(data_f[i][j]) in redOrder[:11]:
                    hot_num = hot_num + 1
            if min_num<=hot_num<=max_num:
                data_f_tmp.append(data_f[i]) 
    if '温号' in filter_array[step-1][1]:
        for i in range(0, len(data_f)):
            warm_num = 0  
            for j in range(0, 6):
                if '%.2d'%(data_f[i][j]) in redOrder[11:22]:
                    warm_num = warm_num + 1
            if min_num<=warm_num<=max_num:
                data_f_tmp.append(data_f[i])  
    if '冷号' in filter_array[step-1][1]:
        for i in range(0, len(data_f)):
            cold_num = 0  
            for j in range(0, 6):
                if '%.2d'%(data_f[i][j]) in redOrder[22:]:
                    cold_num = cold_num + 1
            if min_num<=cold_num<=max_num:
                data_f_tmp.append(data_f[i])
    if '1期重号' in filter_array[step-1][1]:
        for i in range(0, len(data_f)):
            repeat1_num = 0  
            for j in range(0, 6):
                if '%.2d'%(data_f[i][j]) in data_array[0][1:6+1]:
                    repeat1_num = repeat1_num + 1
            if min_num<=repeat1_num<=max_num:
                data_f_tmp.append(data_f[i])
    if '5期重号' in filter_array[step-1][1]:
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
            if int(data_array[4][j]) not in tmp_list:
                tmp_list.append(int(data_array[4][j]))                  
        for i in range(0, len(data_f)):
            repeat5_num = 0  
            for j in range(0, 6):
                if data_f[i][j] in tmp_list:
                    repeat5_num = repeat5_num + 1
            if min_num<=repeat5_num<=max_num:
                data_f_tmp.append(data_f[i])                
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
    #转换回去
    data_f = data_f_tmp 
    #返回数据    
    return data_f #直接将临时数组传回去也可以，不知道哪样会更“经济”一些
