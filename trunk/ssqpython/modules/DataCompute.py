# -*- coding: cp936 -*-
# otherrrr@gmail.com
# ���ݼ���

def redOrderCoumput(data_array): #���������ºż���
    '''������������ĳ�������������մ�������'''
    redOrder = [] #�������е����
    redTimes = [] #��Ӧ��ŵĴ���

    for i in range(0, 33):
        redTimes.append(0) #������ʼ��
        redOrder.append('%.2d'%(i+1)) #��ų�ʼ��
 
    for i in range(0, len(data_array)): #������������
        for j in range(1, 6+1):
            redTimes[int(data_array[i][j])-1] = redTimes[int(data_array[i][j])-1] + 1

    #�Ӵ�С����
    for i in range(0, 33):
        for j in range(0, len(redTimes)-1):
            if redTimes[j]<redTimes[j+1]:
                #�滻������
                tmp = redTimes[j]
                redTimes[j] = redTimes[j+1]
                redTimes[j+1] = tmp
                #�滻�����
                tmp = redOrder[j]
                redOrder[j] = redOrder[j+1]
                redOrder[j+1] = tmp
                
    return redOrder, redTimes

def dataParaCompute(data_array, redOrder, bet_array): #�������ݵĲ�������
    '''���ݿ������ݼ�����������������������ٷֱȣ�Ҳ��������������ʾ'''
    #ΪʲôҪ����������أ�����Ϊ���������Ҫ������ʾ���е�ĳһ��Ϳ���ֱ������
    data_para_array = [] #�������ݲ����б�

    for i in range(0, len(data_array)):
        #���ݲ����е�һ�ڣ���28������������Ŀ��ͬ�� #0.9.2
        data_para_one = {'1��λ':0,'2��λ':0,'3��λ':0,\
                         '4��λ':0,'5��λ':0,'6��λ':0,\
                         '��ֵ':0,'����':0,'ż��':0,\
                         '�����':0,'����':0,\
                         '��3��0':0,'��3��1':0,'��3��2':0,\
                         '��ֵ��':0,'��ֵ��':0,\
                         '����1':0,'����2':0,'����3':0,\
                         '����':0,'ACֵ':0,\
                         '�Ⱥ�':0,'�º�':0,'���':0,\
                         '1���غ�':0,'5���غ�':0,'1���ٽ�ֵ':0,\
                         '3�ڸ���':0,'5�ڸ���':0,\
                         '�̶�Ͷע����':0} 
        #1��λ
        data_para_one['1��λ'] = int(data_array[i][1])
        #2��λ
        data_para_one['2��λ'] = int(data_array[i][2])
        #3��λ
        data_para_one['3��λ'] = int(data_array[i][3])
        #4��λ
        data_para_one['4��λ'] = int(data_array[i][4])
        #5��λ
        data_para_one['5��λ'] = int(data_array[i][5])
        #6��λ
        data_para_one['6��λ'] = int(data_array[i][6])
        #�����ֵ
        sum_num = 0 
        for j in range(1, 6+1):
            sum_num = sum_num + int(data_array[i][j])
        data_para_one['��ֵ'] = sum_num
        #������������
        odd_num = 0 
        for j in range(1, 6+1):
            if int(data_array[i][j])%2==1:
                odd_num = odd_num + 1
        data_para_one['����'] = odd_num
        #����ż������
        even_num = 6 - odd_num
        data_para_one['ż��'] = even_num
        #���������ֵ
        max_space = int(data_array[i][6]) - int(data_array[i][1]) 
        data_para_one['�����'] = max_space  
        #������������
        prime_num = 0 
        for j in range(1, 6+1):
            if int(data_array[i][j]) in [2,3,5,7,11,13,17,19,23,29,31]:
                prime_num = prime_num + 1   
        data_para_one['����'] = prime_num  
        #�����3��0����
        residue_num30 = 0 
        for j in range(1, 6+1):
            if int(data_array[i][j]) in [3,6,9,12,15,18,21,24,27,30,33]: #���Ҳ���Ի���#if int(data_array[i][j])%3==0:
                residue_num30 = residue_num30 + 1
        data_para_one['��3��0'] = residue_num30       
        #�����3��1����
        residue_num31 = 0 
        for j in range(1, 6+1):
            if int(data_array[i][j]) in [1,4,7,10,13,16,19,22,25,28,31]:
                residue_num31 = residue_num31 + 1
        data_para_one['��3��1'] = residue_num31  
        #�����3��2����
        residue_num32 = 0 
        for j in range(1, 6+1):
            if int(data_array[i][j]) in [2,5,8,11,14,17,20,23,26,29,32]:
                residue_num32 = residue_num32 + 1
        data_para_one['��3��2'] = residue_num32    
        #�����ֵ���еĳ��Ÿ���
        high_num = 0 
        for j in range(1, 6+1):
            if int(data_array[i][j])>17:
                high_num = high_num + 1   
        data_para_one['��ֵ��'] = high_num  
        #�����ֵ���еĳ��Ÿ���
        low_num = 0 
        for j in range(1, 6+1):
            if int(data_array[i][j])<17:
                low_num = low_num + 1  
        data_para_one['��ֵ��'] = low_num 
        #��������1�еĳ��Ÿ���
        area1_num = 0 
        for j in range(1, 6+1):
            if int(data_array[i][j])<12:
                area1_num = area1_num + 1
        data_para_one['����1'] = area1_num
        #��������2�еĳ��Ÿ���
        area2_num = 0 
        for j in range(1, 6+1):
            if 11<int(data_array[i][j])<23:
                area2_num = area2_num + 1        
        data_para_one['����2'] = area2_num  
        #��������3�еĳ��Ÿ���
        area3_num = 0 
        for j in range(1, 6+1):
            if int(data_array[i][j])>22:
                area3_num = area3_num + 1
        data_para_one['����3'] = area3_num  
        #�������Ÿ���
        continuous_num = 0 
        for j in range(1, 5+1):
            if int(data_array[i][j+1])-int(data_array[i][j])==1:
                continuous_num = continuous_num + 1 
        data_para_one['����'] = continuous_num 
        #����ACֵ��Χ
        ac_num = 0
        details = [] #�������ݣ����Ϊ15
        for t1 in range(1, 6+1):
            for t2 in range(t1+1, 6+1):
                if (int(data_array[i][t2]) - int(data_array[i][t1])) in details:
                    continue
                else:
                    details.append(int(data_array[i][t2]) - int(data_array[i][t1]))
        ac_num = len(details) - (6-1) #Ϊʲô��(6-1)��ȥ�ٶ�һ�°ɣ�����ֻ�ܸ����㣬6����Ϊ��6�����򣬺Ǻ�
        data_para_one['ACֵ'] = ac_num   
        #�����ȺŸ���
        hot_num = 0
        for j in range(1, 6+1):
            if data_array[i][j] in redOrder[:11]: #�Ⱥž��ǳ����������ǰ11λ��
                hot_num = hot_num + 1
        data_para_one['�Ⱥ�'] = hot_num
        #�����ºŸ���
        warm_num = 0
        for j in range(1, 6+1):
            if data_array[i][j] in redOrder[11:22]:
                warm_num = warm_num + 1
        data_para_one['�º�'] = warm_num
        #������Ÿ���
        cold_num = 0
        for j in range(1, 6+1):
            if data_array[i][j] in redOrder[22:]:
                cold_num = cold_num + 1
        data_para_one['���'] = cold_num
        #����1���غŸ���
        repeat1_num = 0
        if i==(len(data_array)-1): #��1��û����һ��
            repeat1_num = 0
        else:
            for j in range(1, 6+1):
                if data_array[i][j] in data_array[i+1][1:6+1]:
                    repeat1_num = repeat1_num + 1
        data_para_one['1���غ�'] = repeat1_num
        #����5���غŸ���
        repeat5_num = 0
        if i>=(len(data_array)-5): #ǰ5��û��ǰ5��
            repeat5_num = 0
        else:
            l5_a = data_array[i+1][1:6+1] + data_array[i+2][1:6+1] + data_array[i+3][1:6+1] +\
                   data_array[i+4][1:6+1] + data_array[i+5][1:6+1]#5�ںϲ��б�
            l5_d = [] #ɾ����ͬ��֮���5�ںϲ��б�
            for j in range(0, len(l5_a)):
                if l5_a[j] not in l5_a[j+1:]:
                    l5_d.append(l5_a[j])    
            for j in range(1, 6+1):
                if data_array[i][j] in l5_d:
                    repeat5_num = repeat5_num + 1
        data_para_one['5���غ�'] = repeat5_num        
        #1���ٽ�ֵ
        near_num = 0
        if i==(len(data_array)-1): #��1��û����һ��
            near_num = 0
        else:
            tmp_list = [] #��ʱ���飬����һ�������У�1/��1������������ע����int��
            for j in range(1, 6+1):
                tmp_list.append(int(data_array[i+1][j])-1)
                tmp_list.append(int(data_array[i+1][j])+1)
            for j in range(1, 6+1):
                if int(data_array[i][j]) in tmp_list:
                    near_num = near_num + 1
        data_para_one['1���ٽ�ֵ'] = near_num
        #3�ڸ���
        num_l3 = 0
        if i>=(len(data_array)-2): #ǰ2�ڲ���ѽ
            num_l3 = 0
        else:
            l3_a = data_array[i][1:6+1] + data_array[i+1][1:6+1] + data_array[i+2][1:6+1] #3�ںϲ��б�
            l3_d = [] #ɾ����ͬ��֮���3�ںϲ��б�
            for j in range(0, len(l3_a)):
                if l3_a[j] not in l3_a[j+1:]:
                    l3_d.append(l3_a[j])
            num_l3 = len(l3_d)
        data_para_one['3�ڸ���'] = num_l3
        #5�ڸ���
        num_l5 = 0
        if i>=(len(data_array)-4): #ǰ4�ڲ���ѽ
            num_l5 = 0
        else:
            l5_a = data_array[i][1:6+1] + data_array[i+1][1:6+1] + data_array[i+2][1:6+1] +\
                   data_array[i+3][1:6+1] + data_array[i+4][1:6+1]#5�ںϲ��б�
            l5_d = [] #ɾ����ͬ��֮���5�ںϲ��б�
            for j in range(0, len(l5_a)):
                if l5_a[j] not in l5_a[j+1:]:
                    l5_d.append(l5_a[j])
            num_l5 = len(l5_d)
        data_para_one['5�ڸ���'] = num_l5
        #�̶�Ͷע����
        num_fix = 0
        for j in range(0, len(bet_array)):
            num_tmp = 0
            for k in range(0, 6):
                if bet_array[j][k] in data_array[i][1:6+1]:
                    num_tmp = num_tmp + 1
            if num_tmp>num_fix:
                num_fix = num_tmp
        data_para_one['�̶�Ͷע����'] = num_fix
        #��ӵ����б���
        data_para_array.append(data_para_one)
    
    return data_para_array

def percentCompute(filter_array, data_para_array): #�ٷֱȼ���
    '''���ݹ��˲������������ȷ�̶ȵİٷֱ�'''
    #�ٷֱ�
    percent_array = []
    
    for i in range(0, len(filter_array)):
        #��ʼ��Ϊ0
        percent_array.append(0) 
        #���ֵ/��Сֵ��Ϊstr��ʽ����Χ����������
        min_num = int(filter_array[i][3].split('-')[0]) #��Сֵ
        max_num = int(filter_array[i][3].split('-')[1]) #���ֵ
        count = 0 #����  
        #����������
        if '1��λ' in filter_array[i][1]:
            for j in range(0, len(data_para_array)):
                if data_para_array[j]['1��λ']>=min_num and data_para_array[j]['1��λ']<=max_num:
                    count = count + 1
            #����ٷֱ�
            percent_array[i] = '%.2f'%(count*100.0/len(data_para_array))                     
        if '2��λ' in filter_array[i][1]:
            for j in range(0, len(data_para_array)):
                if data_para_array[j]['2��λ']>=min_num and data_para_array[j]['2��λ']<=max_num:
                    count = count + 1
            percent_array[i] = '%.2f'%(count*100.0/len(data_para_array)) 
        if '3��λ' in filter_array[i][1]:
            for j in range(0, len(data_para_array)):
                if data_para_array[j]['3��λ']>=min_num and data_para_array[j]['3��λ']<=max_num:
                    count = count + 1
            percent_array[i] = '%.2f'%(count*100.0/len(data_para_array)) 
        if '4��λ' in filter_array[i][1]:
            for j in range(0, len(data_para_array)):
                if data_para_array[j]['4��λ']>=min_num and data_para_array[j]['4��λ']<=max_num:
                    count = count + 1
            percent_array[i] = '%.2f'%(count*100.0/len(data_para_array)) 
        if '5��λ' in filter_array[i][1]:
            for j in range(0, len(data_para_array)):
                if data_para_array[j]['5��λ']>=min_num and data_para_array[j]['5��λ']<=max_num:
                    count = count + 1
            percent_array[i] = '%.2f'%(count*100.0/len(data_para_array)) 
        if '6��λ' in filter_array[i][1]:
            for j in range(0, len(data_para_array)):
                if data_para_array[j]['6��λ']>=min_num and data_para_array[j]['6��λ']<=max_num:
                    count = count + 1
            percent_array[i] = '%.2f'%(count*100.0/len(data_para_array)) 
        if '��ֵ' in filter_array[i][1]:
            for j in range(0, len(data_para_array)):
                if data_para_array[j]['��ֵ']>=min_num and data_para_array[j]['��ֵ']<=max_num:
                    count = count + 1
            percent_array[i] = '%.2f'%(count*100.0/len(data_para_array)) 
        if '����' in filter_array[i][1]:
            for j in range(0, len(data_para_array)):
                if data_para_array[j]['����']>=min_num and data_para_array[j]['����']<=max_num:
                    count = count + 1
            percent_array[i] = '%.2f'%(count*100.0/len(data_para_array)) 
        if 'ż��' in filter_array[i][1]:
            for j in range(0, len(data_para_array)):
                if data_para_array[j]['ż��']>=min_num and data_para_array[j]['ż��']<=max_num:
                    count = count + 1
            percent_array[i] = '%.2f'%(count*100.0/len(data_para_array)) 
        if '�����' in filter_array[i][1]:
            for j in range(0, len(data_para_array)):
                if data_para_array[j]['�����']>=min_num and data_para_array[j]['�����']<=max_num:
                    count = count + 1
            percent_array[i] = '%.2f'%(count*100.0/len(data_para_array)) 
        if '����' in filter_array[i][1]:
            for j in range(0, len(data_para_array)):
                if data_para_array[j]['����']>=min_num and data_para_array[j]['����']<=max_num:
                    count = count + 1
            percent_array[i] = '%.2f'%(count*100.0/len(data_para_array)) 
        if '��3��0' in filter_array[i][1]:
            for j in range(0, len(data_para_array)):
                if data_para_array[j]['��3��0']>=min_num and data_para_array[j]['��3��0']<=max_num:
                    count = count + 1
            percent_array[i] = '%.2f'%(count*100.0/len(data_para_array)) 
        if '��3��1' in filter_array[i][1]:
            for j in range(0, len(data_para_array)):
                if data_para_array[j]['��3��1']>=min_num and data_para_array[j]['��3��1']<=max_num:
                    count = count + 1
            percent_array[i] = '%.2f'%(count*100.0/len(data_para_array)) 
        if '��3��2' in filter_array[i][1]:
            for j in range(0, len(data_para_array)):
                if data_para_array[j]['��3��2']>=min_num and data_para_array[j]['��3��2']<=max_num:
                    count = count + 1
            percent_array[i] = '%.2f'%(count*100.0/len(data_para_array)) 
        if '��ֵ��' in filter_array[i][1]:
            for j in range(0, len(data_para_array)):
                if data_para_array[j]['��ֵ��']>=min_num and data_para_array[j]['��ֵ��']<=max_num:
                    count = count + 1
            percent_array[i] = '%.2f'%(count*100.0/len(data_para_array)) 
        if '��ֵ��' in filter_array[i][1]:
            for j in range(0, len(data_para_array)):
                if data_para_array[j]['��ֵ��']>=min_num and data_para_array[j]['��ֵ��']<=max_num:
                    count = count + 1
            percent_array[i] = '%.2f'%(count*100.0/len(data_para_array)) 
        if '����1' in filter_array[i][1]:
            for j in range(0, len(data_para_array)):
                if data_para_array[j]['����1']>=min_num and data_para_array[j]['����1']<=max_num:
                    count = count + 1
            percent_array[i] = '%.2f'%(count*100.0/len(data_para_array)) 
        if '����2' in filter_array[i][1]:
            for j in range(0, len(data_para_array)):
                if data_para_array[j]['����2']>=min_num and data_para_array[j]['����2']<=max_num:
                    count = count + 1
            percent_array[i] = '%.2f'%(count*100.0/len(data_para_array))
        if '����3' in filter_array[i][1]:
            for j in range(0, len(data_para_array)):
                if data_para_array[j]['����3']>=min_num and data_para_array[j]['����3']<=max_num:
                    count = count + 1
            percent_array[i] = '%.2f'%(count*100.0/len(data_para_array)) 
        if '����' in filter_array[i][1]:
            for j in range(0, len(data_para_array)):
                if data_para_array[j]['����']>=min_num and data_para_array[j]['����']<=max_num:
                    count = count + 1
            percent_array[i] = '%.2f'%(count*100.0/len(data_para_array)) 
        if 'ACֵ' in filter_array[i][1]:
            for j in range(0, len(data_para_array)):
                if data_para_array[j]['ACֵ']>=min_num and data_para_array[j]['ACֵ']<=max_num:
                    count = count + 1
            percent_array[i] = '%.2f'%(count*100.0/len(data_para_array)) 
        if '�Ⱥ�' in filter_array[i][1]:
            for j in range(0, len(data_para_array)):
                if data_para_array[j]['�Ⱥ�']>=min_num and data_para_array[j]['�Ⱥ�']<=max_num:
                    count = count + 1
            percent_array[i] = '%.2f'%(count*100.0/len(data_para_array)) 
        if '�º�' in filter_array[i][1]:
            for j in range(0, len(data_para_array)):
                if data_para_array[j]['�º�']>=min_num and data_para_array[j]['�º�']<=max_num:
                    count = count + 1
            percent_array[i] = '%.2f'%(count*100.0/len(data_para_array)) 
        if '���' in filter_array[i][1]:
            for j in range(0, len(data_para_array)):
                if data_para_array[j]['���']>=min_num and data_para_array[j]['���']<=max_num:
                    count = count + 1
            percent_array[i] = '%.2f'%(count*100.0/len(data_para_array)) 
        if '1���غ�' in filter_array[i][1]:
            for j in range(0, len(data_para_array)):
                if data_para_array[j]['1���غ�']>=min_num and data_para_array[j]['1���غ�']<=max_num:
                    count = count + 1
            percent_array[i] = '%.2f'%(count*100.0/(len(data_para_array)-1)) #����Ҫ��1��
        if '5���غ�' in filter_array[i][1]:
            for j in range(0, len(data_para_array)):
                if data_para_array[j]['5���غ�']>=min_num and data_para_array[j]['5���غ�']<=max_num:
                    count = count + 1
            percent_array[i] = '%.2f'%(count*100.0/(len(data_para_array)-5)) #����Ҫ��5��            
        if '1���ٽ�ֵ' in filter_array[i][1]:
            for j in range(0, len(data_para_array)):
                if data_para_array[j]['1���ٽ�ֵ']>=min_num and data_para_array[j]['1���ٽ�ֵ']<=max_num:
                    count = count + 1
            percent_array[i] = '%.2f'%(count*100.0/((len(data_para_array)-1))) #����Ҫ��1��
        if '3�ڸ���' in filter_array[i][1]:
            for j in range(0, len(data_para_array)):
                if data_para_array[j]['3�ڸ���']>=min_num and data_para_array[j]['3�ڸ���']<=max_num:
                    count = count + 1
            percent_array[i] = '%.2f'%(count*100.0/((len(data_para_array)-2))) #����Ҫ��2��
        if '5�ڸ���' in filter_array[i][1]:
            for j in range(0, len(data_para_array)):
                if data_para_array[j]['5�ڸ���']>=min_num and data_para_array[j]['5�ڸ���']<=max_num:
                    count = count + 1
            percent_array[i] = '%.2f'%(count*100.0/((len(data_para_array)-4))) #����Ҫ��4��
        if '�̶�Ͷע����' in filter_array[i][1]:
            for j in range(0, len(data_para_array)):
                if data_para_array[j]['�̶�Ͷע����']>=min_num and data_para_array[j]['�̶�Ͷע����']<=max_num:
                    count = count + 1                
            percent_array[i] = '%.2f'%(count*100.0/(len(data_para_array)))
    #��������    
    return percent_array

def dataFiltrate(data_array, data_f, step, filter_array, redOrder, bet_array):#���ݹ���
    '''�������ݣ������ؽ��'''
    #���ֵ/��Сֵ��Ϊstr��ʽ����Χ����������
    min_num = int(filter_array[step-1][3].split('-')[0]) #��Сֵ
    max_num = int(filter_array[step-1][3].split('-')[1]) #���ֵ
    #��ʱ����
    data_f_tmp = [] 
    #����������
    if '1��λ' in filter_array[step-1][1]:
        for i in range(0, len(data_f)):
            if min_num<=data_f[i][0]<=max_num:
                data_f_tmp.append(data_f[i])
    if '2��λ' in filter_array[step-1][1]:
        for i in range(0, len(data_f)):
            if min_num<=data_f[i][1]<=max_num:
                data_f_tmp.append(data_f[i])
    if '3��λ' in filter_array[step-1][1]:
        for i in range(0, len(data_f)):
            if min_num<=data_f[i][2]<=max_num:
                data_f_tmp.append(data_f[i])
    if '4��λ' in filter_array[step-1][1]:
        for i in range(0, len(data_f)):
            if min_num<=data_f[i][3]<=max_num:
                data_f_tmp.append(data_f[i])
    if '5��λ' in filter_array[step-1][1]:
        for i in range(0, len(data_f)):
            if min_num<=data_f[i][4]<=max_num:
                data_f_tmp.append(data_f[i])
    if '6��λ' in filter_array[step-1][1]:
        for i in range(0, len(data_f)):
            if min_num<=data_f[i][5]<=max_num:
                data_f_tmp.append(data_f[i])  
    if '��ֵ' in filter_array[step-1][1]:
        for i in range(0, len(data_f)):
            sum_num = 0
            for j in range(0, 6):
                sum_num = sum_num + data_f[i][j]
            if min_num<=sum_num<=max_num:
                data_f_tmp.append(data_f[i])       
    if '����' in filter_array[step-1][1]:
        for i in range(0, len(data_f)):
            odd_num = 0 
            for j in range(0, 6):
                if data_f[i][j]%2==1:
                    odd_num = odd_num + 1
            if min_num<=odd_num<=max_num:
                data_f_tmp.append(data_f[i])  
    if 'ż��' in filter_array[step-1][1]:
        for i in range(0, len(data_f)):
            even_num = 0 
            for j in range(0, 6):
                if data_f[i][j]%2==0:
                    even_num = even_num + 1
            if min_num<=even_num<=max_num:
                data_f_tmp.append(data_f[i])   
    if '�����' in filter_array[step-1][1]:
        for i in range(0, len(data_f)):
            max_space = data_f[i][5] - data_f[i][0]
            if min_num<=max_space<=max_num:
                data_f_tmp.append(data_f[i])  
    if '����' in filter_array[step-1][1]:
        for i in range(0, len(data_f)):
            prime_num = 0  
            for j in range(0, 6):
                if data_f[i][j] in [2,3,5,7,11,13,17,19,23,29,31]:
                    prime_num = prime_num + 1
            if min_num<=prime_num<=max_num:
                data_f_tmp.append(data_f[i]) 
    if '��3��0' in filter_array[step-1][1]:
        for i in range(0, len(data_f)):
            residue_num30 = 0  
            for j in range(0, 6):
                if data_f[i][j] in [3,6,9,12,15,18,21,24,27,30,33]:
                    residue_num30 = residue_num30 + 1
            if min_num<=residue_num30<=max_num:
                data_f_tmp.append(data_f[i]) 
    if '��3��1' in filter_array[step-1][1]:
        for i in range(0, len(data_f)):
            residue_num31 = 0  
            for j in range(0, 6):
                if data_f[i][j] in [1,4,7,10,13,16,19,22,25,28,31]:
                    residue_num31 = residue_num31 + 1
            if min_num<=residue_num31<=max_num:
                data_f_tmp.append(data_f[i])  
    if '��3��2' in filter_array[step-1][1]:
        for i in range(0, len(data_f)):
            residue_num32 = 0  
            for j in range(0, 6):
                if data_f[i][j] in [2,5,8,11,14,17,20,23,26,29,32]:
                    residue_num32 = residue_num32 + 1
            if min_num<=residue_num32<=max_num:
                data_f_tmp.append(data_f[i])     
    if '��ֵ��' in filter_array[step-1][1]:
        for i in range(0, len(data_f)):
            high_num = 0  
            for j in range(0, 6):
                if data_f[i][j]>17:
                    high_num = high_num + 1
            if min_num<=high_num<=max_num:
                data_f_tmp.append(data_f[i])   
    if '��ֵ��' in filter_array[step-1][1]:
        for i in range(0, len(data_f)):
            low_num = 0  
            for j in range(0, 6):
                if data_f[i][j]<17:
                    low_num = low_num + 1
            if min_num<=low_num<=max_num:
                data_f_tmp.append(data_f[i])     
    if '����1' in filter_array[step-1][1]:
        for i in range(0, len(data_f)):
            area1_num = 0  
            for j in range(0, 6):
                if data_f[i][j]<12:
                    area1_num = area1_num + 1
            if min_num<=area1_num<=max_num:
                data_f_tmp.append(data_f[i])   
    if '����2' in filter_array[step-1][1]:
        for i in range(0, len(data_f)):
            area2_num = 0  
            for j in range(0, 6):
                if 11<data_f[i][j]<23:
                    area2_num = area2_num + 1
            if min_num<=area2_num<=max_num:
                data_f_tmp.append(data_f[i]) 
    if '����3' in filter_array[step-1][1]:
        for i in range(0, len(data_f)):
            area3_num = 0  
            for j in range(0, 6):
                if data_f[i][j]>22:
                    area3_num = area3_num + 1
            if min_num<=area3_num<=max_num:
                data_f_tmp.append(data_f[i])     
    if '����' in filter_array[step-1][1]:
        for i in range(0, len(data_f)):
            continuous_num = 0  
            for j in range(0, 5):
                if data_f[i][j+1] - data_f[i][j]==1:
                    continuous_num = continuous_num + 1
            if min_num<=continuous_num<=max_num:
                data_f_tmp.append(data_f[i])    
    if 'ACֵ' in filter_array[step-1][1]:
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
    if '�Ⱥ�' in filter_array[step-1][1]:
        for i in range(0, len(data_f)):
            hot_num = 0  
            for j in range(0, 6):
                if '%.2d'%(data_f[i][j]) in redOrder[:11]:
                    hot_num = hot_num + 1
            if min_num<=hot_num<=max_num:
                data_f_tmp.append(data_f[i]) 
    if '�º�' in filter_array[step-1][1]:
        for i in range(0, len(data_f)):
            warm_num = 0  
            for j in range(0, 6):
                if '%.2d'%(data_f[i][j]) in redOrder[11:22]:
                    warm_num = warm_num + 1
            if min_num<=warm_num<=max_num:
                data_f_tmp.append(data_f[i])  
    if '���' in filter_array[step-1][1]:
        for i in range(0, len(data_f)):
            cold_num = 0  
            for j in range(0, 6):
                if '%.2d'%(data_f[i][j]) in redOrder[22:]:
                    cold_num = cold_num + 1
            if min_num<=cold_num<=max_num:
                data_f_tmp.append(data_f[i])
    if '1���غ�' in filter_array[step-1][1]:
        for i in range(0, len(data_f)):
            repeat1_num = 0  
            for j in range(0, 6):
                if '%.2d'%(data_f[i][j]) in data_array[0][1:6+1]:
                    repeat1_num = repeat1_num + 1
            if min_num<=repeat1_num<=max_num:
                data_f_tmp.append(data_f[i])
    if '5���غ�' in filter_array[step-1][1]:
        tmp_list = [] #��ʱ����(int)��ǰ4�ڵ����ݣ�û���ظ��ģ�
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
    if '1���ٽ�ֵ' in filter_array[step-1][1]:
        tmp_list = [] #��ʱ����(int)������һ�������У�1/��1����������
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
    if '3�ڸ���' in filter_array[step-1][1]:
        tmp_list = [] #��ʱ����(int)��ǰ2�ڵ����ݣ�û���ظ��ģ�
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
    if '5�ڸ���' in filter_array[step-1][1]:
        tmp_list = [] #��ʱ����(int)��ǰ4�ڵ����ݣ�û���ظ��ģ�
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
    if '�̶�Ͷע����' in filter_array[step-1][1]:
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
    #ת����ȥ
    data_f = data_f_tmp 
    #��������    
    return data_f #ֱ�ӽ���ʱ���鴫��ȥҲ���ԣ���֪��������������á�һЩ
