# -*- coding: cp936 -*-
# otherrrr@gmail.com
# ���ݼ���

def redOrderCoumpute(data_array): #���������º�ȫ����
    '''������������ĳ�������������մ�������'''
    #---------------------------------------------------------------------------
    #�Ⱥ�ȫ
    redOrder = [] #�������е����
    redTimes = [] #��Ӧ��ŵĴ���
    '''
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
    '''            
    #�̶�֮
    redOrder = ['20','14','30','32','03','21','01','26','04','07','08',\
                '18','17','16','27','05','31','11','12','10','25','13',\
                '19','22','28','02','06','09','23','29','33','24','15']
    #print redOrder
    return redOrder, redTimes

def dataParaCompute(data_array, redOrder, bet_array): #�������ݵĲ�������
    '''���ݿ������ݼ�����������������������ٷֱȣ�Ҳ��������������ʾ'''
    #ΪʲôҪ����������أ�����Ϊ���������Ҫ������ʾ���е�ĳһ��Ϳ���ֱ������
    data_para_array = [] #�������ݲ����б�

    for i in range(0, len(data_array)):
        #���ݲ����е�һ�ڣ���69������������Ŀ��ͬ�� #0.9.7
        data_para_one = {'1��λ':0,'2��λ':0,'3��λ':0,\
                         '4��λ':0,'5��λ':0,'6��λ':0,\
                         '�ܺ�ֵ':0,'ǰ4λ��ֵ':0,'��4λ��ֵ':0,\
                         '����':0,'ż��':0,\
                         '61���':0,'21���':0,'41���':0,'43���':0,'52���':0,'63���':0,'65���':0,'����':0,\
                         '��3��0':0,'��3��1':0,'��3��2':0,\
                         '��4��0':0,'��4��1':0,'��4��2':0,'��4��3':0,\
                         '��5��0':0,'��5��1':0,'��5��2':0,'��5��3':0,'��5��4':0,\
                         '��6��0':0,'��6��1':0,'��6��2':0,'��6��3':0,'��6��4':0,'��6��5':0,\
                         '��7��0':0,'��7��1':0,'��7��2':0,'��7��3':0,'��7��4':0,'��7��5':0,'��7��6':0,\
                         '��ֵ��':0,'��ֵ��':0,\
                         '����1':0,'����2':0,'����3':0,\
                         '����':0,'ͬβ':0,'���������':0,'β�ź�':0,'ACֵ':0,\
                         '�Ⱥ�ȫ':0,'�º�ȫ':0,'���ȫ':0,\
                         '1���غ�':0,'3���غ�':0,'5���غ�':0,'10���غ�':0,'1���ٽ�ֵ':0,\
                         '3�ڸ���':0,'5�ڸ���':0,'7�ڸ���':0,'9�ڸ���':0,\
                         '��©ֵ��':0,'�̶�Ͷע':0,'���б�':0,\
                         '����֮һ':0,'����֮��':0,'����֮��':0,\
                         '��������':0} 
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
        #�����ܺ�ֵ
        sum_num = 0 
        for j in range(1, 6+1):
            sum_num = sum_num + int(data_array[i][j])
        data_para_one['�ܺ�ֵ'] = sum_num
        #����ǰ4λ��ֵ
        sum14_num = 0 
        for j in range(1, 4+1):
            sum14_num = sum14_num + int(data_array[i][j])
        data_para_one['ǰ4λ��ֵ'] = sum14_num
        #�����4λ��ֵ
        sum36_num = 0 
        for j in range(3, 6+1):
            sum36_num = sum36_num + int(data_array[i][j])
        data_para_one['��4λ��ֵ'] = sum36_num
        #������������
        odd_num = 0 
        for j in range(1, 6+1):
            if int(data_array[i][j])%2==1:
                odd_num = odd_num + 1
        data_para_one['����'] = odd_num
        #����ż������
        even_num = 6 - odd_num
        data_para_one['ż��'] = even_num
        #����61����������ֵ��
        max_space_61 = int(data_array[i][6]) - int(data_array[i][1]) 
        data_para_one['61���'] = max_space_61
        #����21���
        max_space_21 = int(data_array[i][2]) - int(data_array[i][1]) 
        data_para_one['21���'] = max_space_21        
        #����41���
        max_space_41 = int(data_array[i][4]) - int(data_array[i][1]) 
        data_para_one['41���'] = max_space_41
        #����43���
        max_space_43 = int(data_array[i][4]) - int(data_array[i][3]) 
        data_para_one['43���'] = max_space_43        
        #����52���
        max_space_52 = int(data_array[i][5]) - int(data_array[i][2]) 
        data_para_one['52���'] = max_space_52
        #����63���
        max_space_63 = int(data_array[i][6]) - int(data_array[i][3]) 
        data_para_one['63���'] = max_space_63
        #����65���
        max_space_65 = int(data_array[i][6]) - int(data_array[i][5]) 
        data_para_one['65���'] = max_space_65           
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
        #�����4��0����
        residue_num40 = 0 
        for j in range(1, 6+1):
            if int(data_array[i][j]) in [4,8,12,16,20,24,28,32]:
                residue_num40 = residue_num40 + 1
        data_para_one['��4��0'] = residue_num40
        #�����4��1����
        residue_num41 = 0 
        for j in range(1, 6+1):
            if int(data_array[i][j]) in [1,5,9,13,17,21,25,29,33]:
                residue_num41 = residue_num41 + 1
        data_para_one['��4��1'] = residue_num41
        #�����4��2����
        residue_num42 = 0 
        for j in range(1, 6+1):
            if int(data_array[i][j]) in [2,6,10,14,18,22,26,30]:
                residue_num42 = residue_num42 + 1
        data_para_one['��4��2'] = residue_num42
        #�����4��3����
        residue_num43 = 0 
        for j in range(1, 6+1):
            if int(data_array[i][j]) in [3,7,11,15,19,23,27,31]:
                residue_num43 = residue_num43 + 1
        data_para_one['��4��3'] = residue_num43        
        #�����5��0����
        residue_num50 = 0 
        for j in range(1, 6+1):
            if int(data_array[i][j]) in [5,10,15,20,25,30]:
                residue_num50 = residue_num50 + 1
        data_para_one['��5��0'] = residue_num50
        #�����5��1����
        residue_num51 = 0 
        for j in range(1, 6+1):
            if int(data_array[i][j]) in [1,6,11,16,21,26,31]:
                residue_num51 = residue_num51 + 1
        data_para_one['��5��1'] = residue_num51
        #�����5��2����
        residue_num52 = 0 
        for j in range(1, 6+1):
            if int(data_array[i][j]) in [2,7,12,17,22,27,32]:
                residue_num52 = residue_num52 + 1
        data_para_one['��5��2'] = residue_num52
        #�����5��3����
        residue_num53 = 0 
        for j in range(1, 6+1):
            if int(data_array[i][j]) in [3,8,13,18,23,28,33]:
                residue_num53 = residue_num53 + 1
        data_para_one['��5��3'] = residue_num53
        #�����5��4����
        residue_num54 = 0 
        for j in range(1, 6+1):
            if int(data_array[i][j]) in [4,9,14,19,24,29]:
                residue_num54 = residue_num54 + 1
        data_para_one['��5��4'] = residue_num54
        #�����6��0����
        residue_num60 = 0 
        for j in range(1, 6+1):
            if int(data_array[i][j]) in [6,12,18,24,30]:
                residue_num60 = residue_num60 + 1
        data_para_one['��6��0'] = residue_num60
        #�����6��1����
        residue_num61 = 0 
        for j in range(1, 6+1):
            if int(data_array[i][j]) in [1,7,13,19,25,31]:
                residue_num61 = residue_num61 + 1
        data_para_one['��6��1'] = residue_num61
        #�����6��2����
        residue_num62 = 0 
        for j in range(1, 6+1):
            if int(data_array[i][j]) in [2,8,14,20,26,32]:
                residue_num62 = residue_num62 + 1
        data_para_one['��6��2'] = residue_num62
        #�����6��3����
        residue_num63 = 0 
        for j in range(1, 6+1):
            if int(data_array[i][j]) in [3,9,15,21,27,33]:
                residue_num63 = residue_num63 + 1
        data_para_one['��6��3'] = residue_num63
        #�����6��4����
        residue_num64 = 0 
        for j in range(1, 6+1):
            if int(data_array[i][j]) in [4,10,16,22,28]:
                residue_num64 = residue_num64 + 1
        data_para_one['��6��4'] = residue_num64
        #�����6��5����
        residue_num65 = 0 
        for j in range(1, 6+1):
            if int(data_array[i][j]) in [5,11,17,23,29]:
                residue_num65 = residue_num65 + 1
        data_para_one['��6��5'] = residue_num65         
        #�����7��0����
        residue_num70 = 0 
        for j in range(1, 6+1):
            if int(data_array[i][j]) in [7,14,21,28]:
                residue_num70 = residue_num70 + 1
        data_para_one['��7��0'] = residue_num70
        #�����7��1����
        residue_num71 = 0 
        for j in range(1, 6+1):
            if int(data_array[i][j]) in [1,8,15,22,29]:
                residue_num71 = residue_num71 + 1
        data_para_one['��7��1'] = residue_num71
        #�����7��2����
        residue_num72 = 0 
        for j in range(1, 6+1):
            if int(data_array[i][j]) in [2,9,16,23,30]:
                residue_num72 = residue_num72 + 1
        data_para_one['��7��2'] = residue_num72
        #�����7��3����
        residue_num73 = 0 
        for j in range(1, 6+1):
            if int(data_array[i][j]) in [3,10,17,24,31]:
                residue_num73 = residue_num73 + 1
        data_para_one['��7��3'] = residue_num73
        #�����7��4����
        residue_num74 = 0 
        for j in range(1, 6+1):
            if int(data_array[i][j]) in [4,11,18,25,32]:
                residue_num74 = residue_num74 + 1
        data_para_one['��7��4'] = residue_num74
        #�����7��5����
        residue_num75 = 0 
        for j in range(1, 6+1):
            if int(data_array[i][j]) in [5,12,19,26,33]:
                residue_num75 = residue_num75 + 1
        data_para_one['��7��5'] = residue_num75
        #�����7��6����
        residue_num76 = 0 
        for j in range(1, 6+1):
            if int(data_array[i][j]) in [6,13,20,27]:
                residue_num76 = residue_num76 + 1
        data_para_one['��7��6'] = residue_num76         
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
        #����ͬβ����
        same_nail_num = 0
        times = [] #����
        for j in range(0, 9+1):
            times.append(0) 
        for j in range(1, 6+1):
            times[(int(data_array[i][j])%10)] = times[(int(data_array[i][j])%10)] + 1
        for j in range(0, 9+1):
            if times[j]>1:
                same_nail_num = same_nail_num + 1
        data_para_one['ͬβ'] = same_nail_num
        #���㿪������ͣ�����������Ϊ12�����֣����ǵĺͣ�
        sum_12 = 0
        for j in range(1, 6+1):
            sum_12 = sum_12 + int(data_array[i][j])%10
            sum_12 = sum_12 + int(data_array[i][j])/10
        data_para_one['���������'] = sum_12
        #����β�ź�
        nail_sum = 0
        for j in range(1, 6+1):
            nail_sum = nail_sum + int(data_array[i][j])%10
        data_para_one['β�ź�'] = nail_sum
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
        #�����Ⱥ�ȫ����
        hot_num = 0
        for j in range(1, 6+1):
            if data_array[i][j] in redOrder[:11]: #�Ⱥž��ǳ����������ǰ11λ��
                hot_num = hot_num + 1
        data_para_one['�Ⱥ�ȫ'] = hot_num
        #�����º�ȫ����
        warm_num = 0
        for j in range(1, 6+1):
            if data_array[i][j] in redOrder[11:22]:
                warm_num = warm_num + 1
        data_para_one['�º�ȫ'] = warm_num
        #�������ȫ����
        cold_num = 0
        for j in range(1, 6+1):
            if data_array[i][j] in redOrder[22:]:
                cold_num = cold_num + 1
        data_para_one['���ȫ'] = cold_num    
        #����1���غŸ���
        repeat1_num = 0
        if i==(len(data_array)-1): #��1��û����һ��
            repeat1_num = 0
        else:
            for j in range(1, 6+1):
                if data_array[i][j] in data_array[i+1][1:6+1]:
                    repeat1_num = repeat1_num + 1
        data_para_one['1���غ�'] = repeat1_num
        #����3���غŸ���
        repeat3_num = 0
        if i>=(len(data_array)-3): #ǰ3��û��ǰ3��
            repeat3_num = 0
        else:
            l3_a = data_array[i+1][1:6+1] + data_array[i+2][1:6+1] + data_array[i+3][1:6+1] #3�ںϲ��б�
            l3_d = [] #ɾ����ͬ��֮���3�ںϲ��б�
            for j in range(0, len(l3_a)):
                if l3_a[j] not in l3_a[j+1:]:
                    l3_d.append(l3_a[j])    
            for j in range(1, 6+1):
                if data_array[i][j] in l3_d:
                    repeat3_num = repeat3_num + 1
        data_para_one['3���غ�'] = repeat3_num        
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
        #����10���غŸ�������5��֮ǰ��5�ڣ�
        repeat10_num = 0
        if i>=(len(data_array)-10): #ǰ10��û��ǰ10��
            repeat10_num = 0
        else:
            l10_a = data_array[i+1+5][1:6+1] + data_array[i+2+5][1:6+1] + data_array[i+3+5][1:6+1] +\
                   data_array[i+4+5][1:6+1] + data_array[i+5+5][1:6+1]#5��֮ǰ��5�ںϲ��б�
            l10_d = [] #ɾ����ͬ��֮���5�ںϲ��б�
            for j in range(0, len(l10_a)):
                if l10_a[j] not in l10_a[j+1:]:
                    l10_d.append(l10_a[j])    
            for j in range(1, 6+1):
                if data_array[i][j] in l10_d:
                    repeat10_num = repeat10_num + 1
        data_para_one['10���غ�'] = repeat10_num
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
        #7�ڸ���
        num_l7 = 0
        if i>=(len(data_array)-6): #ǰ6�ڲ���ѽ
            num_l7 = 0
        else:
            l7_a = data_array[i][1:6+1] + data_array[i+1][1:6+1] + data_array[i+2][1:6+1] +\
                   data_array[i+3][1:6+1] + data_array[i+4][1:6+1] + data_array[i+5][1:6+1] +\
                   data_array[i+6][1:6+1]#7�ںϲ��б�
            l7_d = [] #ɾ����ͬ��֮���7�ںϲ��б�
            for j in range(0, len(l7_a)):
                if l7_a[j] not in l7_a[j+1:]:
                    l7_d.append(l7_a[j])
            num_l7 = len(l7_d)
        data_para_one['7�ڸ���'] = num_l7
        #9�ڸ���
        num_l9 = 0
        if i>=(len(data_array)-8): #ǰ8�ڲ���ѽ
            num_l9 = 0
        else:
            l9_a = data_array[i][1:6+1] + data_array[i+1][1:6+1] + data_array[i+2][1:6+1] +\
                   data_array[i+3][1:6+1] + data_array[i+4][1:6+1] + data_array[i+5][1:6+1] +\
                   data_array[i+6][1:6+1] + data_array[i+7][1:6+1] + data_array[i+8][1:6+1]#9�ںϲ��б�
            l9_d = [] #ɾ����ͬ��֮���9�ںϲ��б�
            for j in range(0, len(l9_a)):
                if l9_a[j] not in l9_a[j+1:]:
                    l9_d.append(l9_a[j])
            num_l9 = len(l9_d)
        data_para_one['9�ڸ���'] = num_l9
        #��©ֵ��
        miss_sum = 0
        if i>=(len(data_array)-26): #ǰ26����
            miss_sum = 0
        else:
            for j in range(1, 6+1):
                for k in range(i+1, len(data_array)):
                    if data_array[i][j] in data_array[k][1:6+1]:
                        miss_sum = miss_sum + (k-i)
                        break
        data_para_one['��©ֵ��'] = miss_sum
        #�̶�Ͷע����
        num_fix = 0
        for j in range(0, len(bet_array)):
            num_tmp = 0 #��ʱ���ֵ
            for k in range(0, 6):
                if bet_array[j][k] in data_array[i][1:6+1]:
                    num_tmp = num_tmp + 1
            if num_tmp>num_fix:
                num_fix = num_tmp
        data_para_one['�̶�Ͷע'] = num_fix
        #���б�
        long_list_num = 0
        long_list = ['01','02','05','07','10','11','13','14',\
                     '17','18','19','20','21','22','23','24',\
                     '26','27','28','29','30','32','33']#5�鹲23��
        for j in range(1, 6+1):
            if data_array[i][j] in long_list:
                long_list_num = long_list_num + 1
        data_para_one['���б�'] = long_list_num
        #����֮һ
        div31_num = 0
        div31_list = ['01','03','04','05','07','08','14','17',\
                      '18','20','22','26','27','30','32']#��15��
        for j in range(1, 6+1):
            if data_array[i][j] in div31_list:
                div31_num = div31_num + 1
        data_para_one['����֮һ'] = div31_num
        #����֮��
        div32_num = 0
        div32_list = ['01','02','03','04','05','07','08','14',\
                      '17','18','20','21','27','30','32']#��15��
        for j in range(1, 6+1):
            if data_array[i][j] in div32_list:
                div32_num = div32_num + 1
        data_para_one['����֮��'] = div32_num
        #����֮����ֻ��204/619!!��
        div33_num = 0
        div33_list = ['02','03','04','05','08','14','17','18',\
                      '20','21','22','26','27','30','32']#��15��
        for j in range(1, 6+1):
            if data_array[i][j] in div33_list:
                div33_num = div33_num + 1
        data_para_one['����֮��'] = div33_num         
        #��������
        num_old = 0           
        if i<(len(data_array)-1): #��1��û����������
            for j in range(i+1, len(data_array)-1): #����̫����
                num_tmp = 0 #��ʱ���ֵ
                for k in range(1, 6+1):
                    #��һ���жϣ��ӿ��ٶ�
                    if k==4 and num_tmp<num_old - 2:
                        break                    
                    if data_array[i][k] in data_array[j][1:6+1]:
                        num_tmp = num_tmp + 1
                if num_tmp>num_old:
                    num_old = num_tmp
        else:
            num_old = 0
        data_para_one['��������'] = num_old
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
        if '�ܺ�ֵ' in filter_array[i][1]:
            for j in range(0, len(data_para_array)):
                if data_para_array[j]['�ܺ�ֵ']>=min_num and data_para_array[j]['�ܺ�ֵ']<=max_num:
                    count = count + 1
            percent_array[i] = '%.2f'%(count*100.0/len(data_para_array))
        if 'ǰ4λ��ֵ' in filter_array[i][1]:
            for j in range(0, len(data_para_array)):
                if data_para_array[j]['ǰ4λ��ֵ']>=min_num and data_para_array[j]['ǰ4λ��ֵ']<=max_num:
                    count = count + 1
            percent_array[i] = '%.2f'%(count*100.0/len(data_para_array))
        if '��4λ��ֵ' in filter_array[i][1]:
            for j in range(0, len(data_para_array)):
                if data_para_array[j]['��4λ��ֵ']>=min_num and data_para_array[j]['��4λ��ֵ']<=max_num:
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
        if '61���' in filter_array[i][1]:
            for j in range(0, len(data_para_array)):
                if data_para_array[j]['61���']>=min_num and data_para_array[j]['61���']<=max_num:
                    count = count + 1
            percent_array[i] = '%.2f'%(count*100.0/len(data_para_array))
        if '21���' in filter_array[i][1]:
            for j in range(0, len(data_para_array)):
                if data_para_array[j]['21���']>=min_num and data_para_array[j]['21���']<=max_num:
                    count = count + 1
            percent_array[i] = '%.2f'%(count*100.0/len(data_para_array))            
        if '41���' in filter_array[i][1]:
            for j in range(0, len(data_para_array)):
                if data_para_array[j]['41���']>=min_num and data_para_array[j]['41���']<=max_num:
                    count = count + 1
            percent_array[i] = '%.2f'%(count*100.0/len(data_para_array))
        if '43���' in filter_array[i][1]:
            for j in range(0, len(data_para_array)):
                if data_para_array[j]['43���']>=min_num and data_para_array[j]['43���']<=max_num:
                    count = count + 1
            percent_array[i] = '%.2f'%(count*100.0/len(data_para_array))            
        if '52���' in filter_array[i][1]:
            for j in range(0, len(data_para_array)):
                if data_para_array[j]['52���']>=min_num and data_para_array[j]['52���']<=max_num:
                    count = count + 1
            percent_array[i] = '%.2f'%(count*100.0/len(data_para_array))
        if '63���' in filter_array[i][1]:
            for j in range(0, len(data_para_array)):
                if data_para_array[j]['63���']>=min_num and data_para_array[j]['63���']<=max_num:
                    count = count + 1
            percent_array[i] = '%.2f'%(count*100.0/len(data_para_array))
        if '65���' in filter_array[i][1]:
            for j in range(0, len(data_para_array)):
                if data_para_array[j]['65���']>=min_num and data_para_array[j]['65���']<=max_num:
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
        if '��4��0' in filter_array[i][1]:
            for j in range(0, len(data_para_array)):
                if data_para_array[j]['��4��0']>=min_num and data_para_array[j]['��4��0']<=max_num:
                    count = count + 1
            percent_array[i] = '%.2f'%(count*100.0/len(data_para_array))
        if '��4��1' in filter_array[i][1]:
            for j in range(0, len(data_para_array)):
                if data_para_array[j]['��4��1']>=min_num and data_para_array[j]['��4��1']<=max_num:
                    count = count + 1
            percent_array[i] = '%.2f'%(count*100.0/len(data_para_array))
        if '��4��2' in filter_array[i][1]:
            for j in range(0, len(data_para_array)):
                if data_para_array[j]['��4��2']>=min_num and data_para_array[j]['��4��2']<=max_num:
                    count = count + 1
            percent_array[i] = '%.2f'%(count*100.0/len(data_para_array))
        if '��4��3' in filter_array[i][1]:
            for j in range(0, len(data_para_array)):
                if data_para_array[j]['��4��3']>=min_num and data_para_array[j]['��4��3']<=max_num:
                    count = count + 1
            percent_array[i] = '%.2f'%(count*100.0/len(data_para_array))                  
        if '��5��0' in filter_array[i][1]:
            for j in range(0, len(data_para_array)):
                if data_para_array[j]['��5��0']>=min_num and data_para_array[j]['��5��0']<=max_num:
                    count = count + 1
            percent_array[i] = '%.2f'%(count*100.0/len(data_para_array))
        if '��5��1' in filter_array[i][1]:
            for j in range(0, len(data_para_array)):
                if data_para_array[j]['��5��1']>=min_num and data_para_array[j]['��5��1']<=max_num:
                    count = count + 1
            percent_array[i] = '%.2f'%(count*100.0/len(data_para_array))
        if '��5��2' in filter_array[i][1]:
            for j in range(0, len(data_para_array)):
                if data_para_array[j]['��5��2']>=min_num and data_para_array[j]['��5��2']<=max_num:
                    count = count + 1
            percent_array[i] = '%.2f'%(count*100.0/len(data_para_array))
        if '��5��3' in filter_array[i][1]:
            for j in range(0, len(data_para_array)):
                if data_para_array[j]['��5��3']>=min_num and data_para_array[j]['��5��3']<=max_num:
                    count = count + 1
            percent_array[i] = '%.2f'%(count*100.0/len(data_para_array))
        if '��5��4' in filter_array[i][1]:
            for j in range(0, len(data_para_array)):
                if data_para_array[j]['��5��4']>=min_num and data_para_array[j]['��5��4']<=max_num:
                    count = count + 1
            percent_array[i] = '%.2f'%(count*100.0/len(data_para_array))
        if '��6��0' in filter_array[i][1]:
            for j in range(0, len(data_para_array)):
                if data_para_array[j]['��6��0']>=min_num and data_para_array[j]['��6��0']<=max_num:
                    count = count + 1
            percent_array[i] = '%.2f'%(count*100.0/len(data_para_array))
        if '��6��1' in filter_array[i][1]:
            for j in range(0, len(data_para_array)):
                if data_para_array[j]['��6��1']>=min_num and data_para_array[j]['��6��1']<=max_num:
                    count = count + 1
            percent_array[i] = '%.2f'%(count*100.0/len(data_para_array))
        if '��6��2' in filter_array[i][1]:
            for j in range(0, len(data_para_array)):
                if data_para_array[j]['��6��2']>=min_num and data_para_array[j]['��6��2']<=max_num:
                    count = count + 1
            percent_array[i] = '%.2f'%(count*100.0/len(data_para_array))
        if '��6��3' in filter_array[i][1]:
            for j in range(0, len(data_para_array)):
                if data_para_array[j]['��6��3']>=min_num and data_para_array[j]['��6��3']<=max_num:
                    count = count + 1
            percent_array[i] = '%.2f'%(count*100.0/len(data_para_array))
        if '��6��4' in filter_array[i][1]:
            for j in range(0, len(data_para_array)):
                if data_para_array[j]['��6��4']>=min_num and data_para_array[j]['��6��4']<=max_num:
                    count = count + 1
            percent_array[i] = '%.2f'%(count*100.0/len(data_para_array))
        if '��6��5' in filter_array[i][1]:
            for j in range(0, len(data_para_array)):
                if data_para_array[j]['��6��5']>=min_num and data_para_array[j]['��6��5']<=max_num:
                    count = count + 1
            percent_array[i] = '%.2f'%(count*100.0/len(data_para_array))                
        if '��7��0' in filter_array[i][1]:
            for j in range(0, len(data_para_array)):
                if data_para_array[j]['��7��0']>=min_num and data_para_array[j]['��7��0']<=max_num:
                    count = count + 1
            percent_array[i] = '%.2f'%(count*100.0/len(data_para_array))
        if '��7��1' in filter_array[i][1]:
            for j in range(0, len(data_para_array)):
                if data_para_array[j]['��7��1']>=min_num and data_para_array[j]['��7��1']<=max_num:
                    count = count + 1
            percent_array[i] = '%.2f'%(count*100.0/len(data_para_array))
        if '��7��2' in filter_array[i][1]:
            for j in range(0, len(data_para_array)):
                if data_para_array[j]['��7��2']>=min_num and data_para_array[j]['��7��2']<=max_num:
                    count = count + 1
            percent_array[i] = '%.2f'%(count*100.0/len(data_para_array))
        if '��7��3' in filter_array[i][1]:
            for j in range(0, len(data_para_array)):
                if data_para_array[j]['��7��3']>=min_num and data_para_array[j]['��7��3']<=max_num:
                    count = count + 1
            percent_array[i] = '%.2f'%(count*100.0/len(data_para_array))
        if '��7��4' in filter_array[i][1]:
            for j in range(0, len(data_para_array)):
                if data_para_array[j]['��7��4']>=min_num and data_para_array[j]['��7��4']<=max_num:
                    count = count + 1
            percent_array[i] = '%.2f'%(count*100.0/len(data_para_array))
        if '��7��5' in filter_array[i][1]:
            for j in range(0, len(data_para_array)):
                if data_para_array[j]['��7��5']>=min_num and data_para_array[j]['��7��5']<=max_num:
                    count = count + 1
            percent_array[i] = '%.2f'%(count*100.0/len(data_para_array))
        if '��7��6' in filter_array[i][1]:
            for j in range(0, len(data_para_array)):
                if data_para_array[j]['��7��6']>=min_num and data_para_array[j]['��7��6']<=max_num:
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
        if 'ͬβ' in filter_array[i][1]:
            for j in range(0, len(data_para_array)):
                if data_para_array[j]['ͬβ']>=min_num and data_para_array[j]['ͬβ']<=max_num:
                    count = count + 1
            percent_array[i] = '%.2f'%(count*100.0/len(data_para_array))
        if '���������' in filter_array[i][1]:
            for j in range(0, len(data_para_array)):
                if data_para_array[j]['���������']>=min_num and data_para_array[j]['���������']<=max_num:
                    count = count + 1
            percent_array[i] = '%.2f'%(count*100.0/len(data_para_array))
        if 'β�ź�' in filter_array[i][1]:
            for j in range(0, len(data_para_array)):
                if data_para_array[j]['β�ź�']>=min_num and data_para_array[j]['β�ź�']<=max_num:
                    count = count + 1
            percent_array[i] = '%.2f'%(count*100.0/len(data_para_array))              
        if 'ACֵ' in filter_array[i][1]:
            for j in range(0, len(data_para_array)):
                if data_para_array[j]['ACֵ']>=min_num and data_para_array[j]['ACֵ']<=max_num:
                    count = count + 1
            percent_array[i] = '%.2f'%(count*100.0/len(data_para_array)) 
        if '�Ⱥ�ȫ' in filter_array[i][1]:
            for j in range(0, len(data_para_array)):
                if data_para_array[j]['�Ⱥ�ȫ']>=min_num and data_para_array[j]['�Ⱥ�ȫ']<=max_num:
                    count = count + 1
            percent_array[i] = '%.2f'%(count*100.0/len(data_para_array)) 
        if '�º�ȫ' in filter_array[i][1]:
            for j in range(0, len(data_para_array)):
                if data_para_array[j]['�º�ȫ']>=min_num and data_para_array[j]['�º�ȫ']<=max_num:
                    count = count + 1
            percent_array[i] = '%.2f'%(count*100.0/len(data_para_array)) 
        if '���ȫ' in filter_array[i][1]:
            for j in range(0, len(data_para_array)):
                if data_para_array[j]['���ȫ']>=min_num and data_para_array[j]['���ȫ']<=max_num:
                    count = count + 1
            percent_array[i] = '%.2f'%(count*100.0/len(data_para_array)) 
        if '1���غ�' in filter_array[i][1]:
            for j in range(0, len(data_para_array)):
                if data_para_array[j]['1���غ�']>=min_num and data_para_array[j]['1���غ�']<=max_num:
                    count = count + 1
            percent_array[i] = '%.2f'%(count*100.0/(len(data_para_array)-1)) #����Ҫ��1��
        if '3���غ�' in filter_array[i][1]:
            for j in range(0, len(data_para_array)):
                if data_para_array[j]['3���غ�']>=min_num and data_para_array[j]['3���غ�']<=max_num:
                    count = count + 1
            percent_array[i] = '%.2f'%(count*100.0/(len(data_para_array)-3)) #����Ҫ��3��                    
        if '5���غ�' in filter_array[i][1]:
            for j in range(0, len(data_para_array)):
                if data_para_array[j]['5���غ�']>=min_num and data_para_array[j]['5���غ�']<=max_num:
                    count = count + 1
            percent_array[i] = '%.2f'%(count*100.0/(len(data_para_array)-5)) #����Ҫ��5��
        if '10���غ�' in filter_array[i][1]:
            for j in range(0, len(data_para_array)):
                if data_para_array[j]['10���غ�']>=min_num and data_para_array[j]['10���غ�']<=max_num:
                    count = count + 1
            percent_array[i] = '%.2f'%(count*100.0/(len(data_para_array)-10)) #����Ҫ��10��              
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
        if '7�ڸ���' in filter_array[i][1]:
            for j in range(0, len(data_para_array)):
                if data_para_array[j]['7�ڸ���']>=min_num and data_para_array[j]['7�ڸ���']<=max_num:
                    count = count + 1
            percent_array[i] = '%.2f'%(count*100.0/((len(data_para_array)-6))) #����Ҫ��6��
        if '9�ڸ���' in filter_array[i][1]:
            for j in range(0, len(data_para_array)):
                if data_para_array[j]['9�ڸ���']>=min_num and data_para_array[j]['9�ڸ���']<=max_num:
                    count = count + 1
            percent_array[i] = '%.2f'%(count*100.0/((len(data_para_array)-8))) #����Ҫ��8��
        if '��©ֵ��' in filter_array[i][1]:
            for j in range(0, len(data_para_array)):
                if data_para_array[j]['��©ֵ��']>=min_num and data_para_array[j]['��©ֵ��']<=max_num:
                    count = count + 1
            percent_array[i] = '%.2f'%(count*100.0/((len(data_para_array)-26))) #����Ҫ��26��#��Ϊ�����ֵĺ�29���ڵ�26�ڳ��ֵ�           
        if '�̶�Ͷע' in filter_array[i][1]:
            for j in range(0, len(data_para_array)):
                if data_para_array[j]['�̶�Ͷע']>=min_num and data_para_array[j]['�̶�Ͷע']<=max_num:
                    count = count + 1                
            percent_array[i] = '%.2f'%(count*100.0/(len(data_para_array)))
        if '���б�' in filter_array[i][1]:
            for j in range(0, len(data_para_array)):
                if data_para_array[j]['���б�']>=min_num and data_para_array[j]['���б�']<=max_num:
                    count = count + 1                
            percent_array[i] = '%.2f'%(count*100.0/(len(data_para_array)))
        if '����֮һ' in filter_array[i][1]:
            for j in range(0, len(data_para_array)):
                if data_para_array[j]['����֮һ']>=min_num and data_para_array[j]['����֮һ']<=max_num:
                    count = count + 1                
            percent_array[i] = '%.2f'%(count*100.0/(len(data_para_array)))
        if '����֮��' in filter_array[i][1]:
            for j in range(0, len(data_para_array)):
                if data_para_array[j]['����֮��']>=min_num and data_para_array[j]['����֮��']<=max_num:
                    count = count + 1                
            percent_array[i] = '%.2f'%(count*100.0/(len(data_para_array)))
        if '����֮��' in filter_array[i][1]:
            for j in range(0, len(data_para_array)):
                if data_para_array[j]['����֮��']>=min_num and data_para_array[j]['����֮��']<=max_num:
                    count = count + 1                
            percent_array[i] = '%.2f'%(count*100.0/(len(data_para_array)))                
        if '��������' in filter_array[i][1]:
            for j in range(0, len(data_para_array)):
                if data_para_array[j]['��������']>=min_num and data_para_array[j]['��������']<=max_num:
                    count = count + 1                
            percent_array[i] = '%.2f'%(count*100.0/(len(data_para_array)-1)) #����Ҫ��1��            
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
    if '�ܺ�ֵ' in filter_array[step-1][1]:
        for i in range(0, len(data_f)):
            sum_num = 0
            for j in range(0, 6):
                sum_num = sum_num + data_f[i][j]
            if min_num<=sum_num<=max_num:
                data_f_tmp.append(data_f[i])
    if 'ǰ4λ��ֵ' in filter_array[step-1][1]:
        for i in range(0, len(data_f)):
            sum14_num = 0
            for j in range(0, 4):
                sum14_num = sum14_num + data_f[i][j]
            if min_num<=sum14_num<=max_num:
                data_f_tmp.append(data_f[i])
    if '��4λ��ֵ' in filter_array[step-1][1]:
        for i in range(0, len(data_f)):
            sum36_num = 0
            for j in range(2, 6):
                sum36_num = sum36_num + data_f[i][j]
            if min_num<=sum36_num<=max_num:
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
    if '61���' in filter_array[step-1][1]:
        for i in range(0, len(data_f)):
            max_space_61 = data_f[i][5] - data_f[i][0]
            if min_num<=max_space_61<=max_num:
                data_f_tmp.append(data_f[i])
    if '21���' in filter_array[step-1][1]:
        for i in range(0, len(data_f)):
            max_space_21 = data_f[i][1] - data_f[i][0]
            if min_num<=max_space_21<=max_num:
                data_f_tmp.append(data_f[i])                
    if '41���' in filter_array[step-1][1]:
        for i in range(0, len(data_f)):
            max_space_41 = data_f[i][3] - data_f[i][0]
            if min_num<=max_space_41<=max_num:
                data_f_tmp.append(data_f[i])
    if '43���' in filter_array[step-1][1]:
        for i in range(0, len(data_f)):
            max_space_43 = data_f[i][3] - data_f[i][2]
            if min_num<=max_space_43<=max_num:
                data_f_tmp.append(data_f[i])                
    if '52���' in filter_array[step-1][1]:
        for i in range(0, len(data_f)):
            max_space_52 = data_f[i][4] - data_f[i][1]
            if min_num<=max_space_52<=max_num:
                data_f_tmp.append(data_f[i])
    if '63���' in filter_array[step-1][1]:
        for i in range(0, len(data_f)):
            max_space_63 = data_f[i][5] - data_f[i][2]
            if min_num<=max_space_63<=max_num:
                data_f_tmp.append(data_f[i])
    if '65���' in filter_array[step-1][1]:
        for i in range(0, len(data_f)):
            max_space_65 = data_f[i][5] - data_f[i][4]
            if min_num<=max_space_65<=max_num:
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
    if '��4��0' in filter_array[step-1][1]:
        for i in range(0, len(data_f)):
            residue_num40 = 0  
            for j in range(0, 6):
                if data_f[i][j] in [4,8,12,16,20,24,28,32]:
                    residue_num40 = residue_num40 + 1
            if min_num<=residue_num40<=max_num:
                data_f_tmp.append(data_f[i])
    if '��4��1' in filter_array[step-1][1]:
        for i in range(0, len(data_f)):
            residue_num41 = 0  
            for j in range(0, 6):
                if data_f[i][j] in [1,5,9,13,17,21,25,29,33]:
                    residue_num41 = residue_num41 + 1
            if min_num<=residue_num41<=max_num:
                data_f_tmp.append(data_f[i])
    if '��4��2' in filter_array[step-1][1]:
        for i in range(0, len(data_f)):
            residue_num42 = 0  
            for j in range(0, 6):
                if data_f[i][j] in [2,6,10,14,18,22,26,30]:
                    residue_num42 = residue_num42 + 1
            if min_num<=residue_num42<=max_num:
                data_f_tmp.append(data_f[i])
    if '��4��3' in filter_array[step-1][1]:
        for i in range(0, len(data_f)):
            residue_num43 = 0  
            for j in range(0, 6):
                if data_f[i][j] in [3,7,11,15,19,23,27,31]:
                    residue_num43 = residue_num43 + 1
            if min_num<=residue_num43<=max_num:
                data_f_tmp.append(data_f[i])                 
    if '��5��0' in filter_array[step-1][1]:
        for i in range(0, len(data_f)):
            residue_num50 = 0  
            for j in range(0, 6):
                if data_f[i][j] in [5,10,15,20,25,30]:
                    residue_num50 = residue_num50 + 1
            if min_num<=residue_num50<=max_num:
                data_f_tmp.append(data_f[i])
    if '��5��1' in filter_array[step-1][1]:
        for i in range(0, len(data_f)):
            residue_num51 = 0  
            for j in range(0, 6):
                if data_f[i][j] in [1,6,11,16,21,26,31]:
                    residue_num51 = residue_num51 + 1
            if min_num<=residue_num51<=max_num:
                data_f_tmp.append(data_f[i])
    if '��5��2' in filter_array[step-1][1]:
        for i in range(0, len(data_f)):
            residue_num52 = 0  
            for j in range(0, 6):
                if data_f[i][j] in [2,7,12,17,22,27,32]:
                    residue_num52 = residue_num52 + 1
            if min_num<=residue_num52<=max_num:
                data_f_tmp.append(data_f[i])
    if '��5��3' in filter_array[step-1][1]:
        for i in range(0, len(data_f)):
            residue_num53 = 0  
            for j in range(0, 6):
                if data_f[i][j] in [3,8,13,18,23,28,33]:
                    residue_num53 = residue_num53 + 1
            if min_num<=residue_num53<=max_num:
                data_f_tmp.append(data_f[i])
    if '��5��4' in filter_array[step-1][1]:
        for i in range(0, len(data_f)):
            residue_num54 = 0  
            for j in range(0, 6):
                if data_f[i][j] in [4,9,14,19,24,29]:
                    residue_num54 = residue_num54 + 1
            if min_num<=residue_num54<=max_num:
                data_f_tmp.append(data_f[i])
    if '��6��0' in filter_array[step-1][1]:
        for i in range(0, len(data_f)):
            residue_num60 = 0  
            for j in range(0, 6):
                if data_f[i][j] in [6,12,18,24,30]:
                    residue_num60 = residue_num60 + 1
            if min_num<=residue_num60<=max_num:
                data_f_tmp.append(data_f[i])
    if '��6��1' in filter_array[step-1][1]:
        for i in range(0, len(data_f)):
            residue_num61 = 0  
            for j in range(0, 6):
                if data_f[i][j] in [1,7,13,19,25,31]:
                    residue_num61 = residue_num61 + 1
            if min_num<=residue_num61<=max_num:
                data_f_tmp.append(data_f[i])
    if '��6��2' in filter_array[step-1][1]:
        for i in range(0, len(data_f)):
            residue_num62 = 0  
            for j in range(0, 6):
                if data_f[i][j] in [2,8,14,20,26,32]:
                    residue_num62 = residue_num62 + 1
            if min_num<=residue_num62<=max_num:
                data_f_tmp.append(data_f[i])
    if '��6��3' in filter_array[step-1][1]:
        for i in range(0, len(data_f)):
            residue_num63 = 0  
            for j in range(0, 6):
                if data_f[i][j] in [3,9,15,21,27,33]:
                    residue_num63 = residue_num63 + 1
            if min_num<=residue_num63<=max_num:
                data_f_tmp.append(data_f[i])
    if '��6��4' in filter_array[step-1][1]:
        for i in range(0, len(data_f)):
            residue_num64 = 0  
            for j in range(0, 6):
                if data_f[i][j] in [4,10,16,22,28]:
                    residue_num64 = residue_num64 + 1
            if min_num<=residue_num64<=max_num:
                data_f_tmp.append(data_f[i])
    if '��6��5' in filter_array[step-1][1]:
        for i in range(0, len(data_f)):
            residue_num65 = 0  
            for j in range(0, 6):
                if data_f[i][j] in [5,11,17,23,29]:
                    residue_num65 = residue_num65 + 1
            if min_num<=residue_num65<=max_num:
                data_f_tmp.append(data_f[i])                
    if '��7��0' in filter_array[step-1][1]:
        for i in range(0, len(data_f)):
            residue_num70 = 0  
            for j in range(0, 6):
                if data_f[i][j] in [7,14,21,28]:
                    residue_num70 = residue_num70 + 1
            if min_num<=residue_num70<=max_num:
                data_f_tmp.append(data_f[i])
    if '��7��1' in filter_array[step-1][1]:
        for i in range(0, len(data_f)):
            residue_num71 = 0  
            for j in range(0, 6):
                if data_f[i][j] in [1,8,15,22,29]:
                    residue_num71 = residue_num71 + 1
            if min_num<=residue_num71<=max_num:
                data_f_tmp.append(data_f[i])
    if '��7��2' in filter_array[step-1][1]:
        for i in range(0, len(data_f)):
            residue_num72 = 0  
            for j in range(0, 6):
                if data_f[i][j] in [2,9,16,23,30]:
                    residue_num72 = residue_num72 + 1
            if min_num<=residue_num72<=max_num:
                data_f_tmp.append(data_f[i])
    if '��7��3' in filter_array[step-1][1]:
        for i in range(0, len(data_f)):
            residue_num73 = 0  
            for j in range(0, 6):
                if data_f[i][j] in [3,10,17,24,31]:
                    residue_num73 = residue_num73 + 1
            if min_num<=residue_num73<=max_num:
                data_f_tmp.append(data_f[i])     
    if '��7��4' in filter_array[step-1][1]:
        for i in range(0, len(data_f)):
            residue_num74 = 0  
            for j in range(0, 6):
                if data_f[i][j] in [4,11,18,25,32]:
                    residue_num74 = residue_num74 + 1
            if min_num<=residue_num74<=max_num:
                data_f_tmp.append(data_f[i])
    if '��7��5' in filter_array[step-1][1]:
        for i in range(0, len(data_f)):
            residue_num75 = 0  
            for j in range(0, 6):
                if data_f[i][j] in [5,12,19,26,33]:
                    residue_num75 = residue_num75 + 1
            if min_num<=residue_num75<=max_num:
                data_f_tmp.append(data_f[i])
    if '��7��6' in filter_array[step-1][1]:
        for i in range(0, len(data_f)):
            residue_num76 = 0  
            for j in range(0, 6):
                if data_f[i][j] in [6,13,20,27]:
                    residue_num76 = residue_num76 + 1
            if min_num<=residue_num76<=max_num:
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
    if 'ͬβ' in filter_array[step-1][1]:
        for i in range(0, len(data_f)):
            same_nail_num = 0
            times = [] #����
            for j in range(0, 9+1):
                times.append(0) 
            for j in range(0, 6):
                times[(int(data_f[i][j])%10)] = times[(int(data_f[i][j])%10)] + 1
            for j in range(0, 9+1):
                if times[j]>1:
                    same_nail_num = same_nail_num + 1                 
            if min_num<=same_nail_num<=max_num:
                data_f_tmp.append(data_f[i])
    if '���������' in filter_array[step-1][1]:
        for i in range(0, len(data_f)):
            sum_12 = 0
            for j in range(0, 6):
                sum_12 = sum_12 + int(data_f[i][j])%10
                sum_12 = sum_12 + int(data_f[i][j])/10
            if min_num<=sum_12<=max_num:
                data_f_tmp.append(data_f[i])
    if 'β�ź�' in filter_array[step-1][1]:
        for i in range(0, len(data_f)):
            nail_sum = 0
            for j in range(0, 6):
                nail_sum = nail_sum + int(data_f[i][j])%10
            if min_num<=nail_sum<=max_num:
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
    if '�Ⱥ�ȫ' in filter_array[step-1][1]:
        for i in range(0, len(data_f)):
            hot_num = 0  
            for j in range(0, 6):
                if '%.2d'%(data_f[i][j]) in redOrder[:11]:
                    hot_num = hot_num + 1
            if min_num<=hot_num<=max_num:
                data_f_tmp.append(data_f[i]) 
    if '�º�ȫ' in filter_array[step-1][1]:
        for i in range(0, len(data_f)):
            warm_num = 0  
            for j in range(0, 6):
                if '%.2d'%(data_f[i][j]) in redOrder[11:22]:
                    warm_num = warm_num + 1
            if min_num<=warm_num<=max_num:
                data_f_tmp.append(data_f[i])  
    if '���ȫ' in filter_array[step-1][1]:
        for i in range(0, len(data_f)):
            cold_num = 0  
            for j in range(0, 6):
                if '%.2d'%(data_f[i][j]) in redOrder[22:]:
                    cold_num = cold_num + 1
            if min_num<=cold_num<=max_num:
                data_f_tmp.append(data_f[i])
    if '�Ⱥ�100' in filter_array[step-1][1]:
        for i in range(0, len(data_f)):
            hot100_num = 0  
            for j in range(0, 6):
                if '%.2d'%(data_f[i][j]) in redOrder100[:11]:
                    hot100_num = hot100_num + 1
            if min_num<=hot100_num<=max_num:
                data_f_tmp.append(data_f[i])
    if '1���غ�' in filter_array[step-1][1]:
        for i in range(0, len(data_f)):
            repeat1_num = 0  
            for j in range(0, 6):
                if '%.2d'%(data_f[i][j]) in data_array[0][1:6+1]:
                    repeat1_num = repeat1_num + 1
            if min_num<=repeat1_num<=max_num:
                data_f_tmp.append(data_f[i])
    if '3���غ�' in filter_array[step-1][1]:
        tmp_list = [] #��ʱ����(int)��ǰ3�ڵ����ݣ�û���ظ��ģ�
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
    if '5���غ�' in filter_array[step-1][1]:
        tmp_list = [] #��ʱ����(int)��ǰ5�ڵ����ݣ�û���ظ��ģ�
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
    if '10���غ�' in filter_array[step-1][1]:
        tmp_list = [] #��ʱ����(int)��ǰ5+4�ڵ����ݣ�û���ظ��ģ�
        #�����'10���غ�'��ʱ��о������Ǹ���4�����񲻶ԡ���
        for j in range(1, 6+1):
            #2007-07-26��
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
    if '7�ڸ���' in filter_array[step-1][1]:
        tmp_list = [] #��ʱ����(int)��ǰ6�ڵ����ݣ�û���ظ��ģ�
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
    if '9�ڸ���' in filter_array[step-1][1]:
        tmp_list = [] #��ʱ����(int)��ǰ8�ڵ����ݣ�û���ظ��ģ�
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
    if '��©ֵ��' in filter_array[step-1][1]:
        for i in range(0, len(data_f)):
            miss_sum = 0
            for j in range(0, 6):
                for k in range(0, len(data_array)):
                    if '%.2d'%data_f[i][j] in data_array[k][1:6+1]: #ע��data_f��int�͵�list
                        miss_sum = miss_sum + (k+1)
                        break
            if min_num<=miss_sum<=max_num:
                data_f_tmp.append(data_f[i])               
    if '�̶�Ͷע' in filter_array[step-1][1]:
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
    if '���б�' in filter_array[step-1][1]:
        long_list = ['01','02','05','07','10','11','13','14',\
                     '17','18','19','20','21','22','23','24',\
                     '26','27','28','29','30','32','33']#5�鹲23��        
        for i in range(0, len(data_f)):
            long_list_num = 0
            for j in range(0, 6):
                if '%.2d'%(data_f[i][j]) in long_list:
                    long_list_num = long_list_num + 1
            if min_num<=long_list_num<=max_num:
                data_f_tmp.append(data_f[i])
    if '����֮һ' in filter_array[step-1][1]:
        div31_list = ['01','03','04','05','07','08','14','17',\
                     '18','20','22','26','27','30','32']#��15��        
        for i in range(0, len(data_f)):
            div31_num = 0
            for j in range(0, 6):
                if '%.2d'%(data_f[i][j]) in div31_list:
                    div31_num = div31_num + 1
            if min_num<=div31_num<=max_num:
                data_f_tmp.append(data_f[i])
    if '����֮��' in filter_array[step-1][1]: 
        div32_list = ['01','02','03','04','05','07','08','14',\
                      '17','18','20','21','27','30','32']#��15��        
        for i in range(0, len(data_f)):
            div32_num = 0
            for j in range(0, 6):
                if '%.2d'%(data_f[i][j]) in div32_list:
                    div32_num = div32_num + 1
            if min_num<=div32_num<=max_num:
                data_f_tmp.append(data_f[i])
    if '����֮��' in filter_array[step-1][1]: #ֻ��204/614!!
        div33_list = ['02','03','04','05','08','14','17','18',\
                      '20','21','22','26','27','30','32']#��15��        
        for i in range(0, len(data_f)):
            div33_num = 0
            for j in range(0, 6):
                if '%.2d'%(data_f[i][j]) in div33_list:
                    div33_num = div33_num + 1
            if min_num<=div33_num<=max_num:                
                data_f_tmp.append(data_f[i])                 
    if '��������' in filter_array[step-1][1]:
        for i in range(0, len(data_f)):
            num_old = 0
            #����̫����!!!!
            for j in range(0, len(data_array)):
                num_tmp = 0
                #for k in range(0, 6): #�������
                for k in range(1, 6+1):    
                    #��һ���жϣ��ӿ�һЩ�ٶ�
                    if k==4 and num_tmp<num_old -2:
                        break
                    if int(data_array[j][k]) in data_f[i]:
                        num_tmp = num_tmp + 1
                if num_tmp>num_old:
                    num_old = num_tmp
            if min_num<=num_old<=max_num:
                data_f_tmp.append(data_f[i])
    #ת����ȥ
    data_f = data_f_tmp 
    #��������    
    return data_f
    #ֱ�ӽ���ʱ���鴫��ȥҲ���ԣ���֪��������������á�һЩ

def blueCoumpute(data_array): #����ͳ�Ƽ�����
    '''�����������ĳ����������������©ֵ'''
    blue_times = [] #�������ĳ������
    for i in range(0, 16): #��ʼ��
        blue_times.append(0)
    for i in range(0, len(data_array)):
        blue_times[int(data_array[i][7])-1] = blue_times[int(data_array[i][7])-1] + 1

    blue_step = [] #�������ĳ��򲽳�
    for i in range(0, 16): 
        blue_step.append(len(data_array)/blue_times[i])
        
    blue_drop = [] #�������©ֵ����������δ���֣�
    for i in range(0, 16): #��ʼ��
        blue_drop.append(0)
    for i in range(0, len(data_array)): #����
        if blue_drop[int(data_array[i][7])-1]==0:
            blue_drop[int(data_array[i][7])-1] = i + 1 
    return blue_times, blue_step, blue_drop

def blueAdvice(data_array, blue_times):
    '''���������Ƽ�����Ҫ�����в���'''

    #����Ⱥź����
    blue_hot = []
    blue_cold = []
    sum_tmp = 0 #����ͳ��
    while True:
        for i in range(0, len(blue_times)):
            if blue_times[i]==max(blue_times): #�ж��ǲ�������
                blue_hot.append('%.2d'%(i+1))
                sum_tmp = sum_tmp + blue_times[i]
                blue_times[i] = 0 #���������0
                break
        if (sum_tmp*2)>=len(data_array): #�жϴ���֮���Ƿ���һ��
            break
    for i in range(0, len(blue_times)): #������0�ľ���cold
        if blue_times[i]!=0:
            blue_cold.append('%.2d'%(i+1))
    
    blueDatas = [] #�����������
    for i in range(0, len(data_array)):
        t = {'��ż':'','����':'','��С':'','��������ͬ':'','�������ͬ':'','5��������':'','11��������':''}
        #��ż
        if int(data_array[i][7])%2==0:
            t['��ż'] = 'ż'
        else:
            t['��ż'] = '��'
        #����
        if data_array[i][7] in blue_hot:
            t['����'] = '��'
        else:
            t['����'] = '��'
        #��С
        if int(data_array[i][7])>8:
            t['��С'] = '��'
        else:
            t['��С'] = 'С'
        #��������ͬ������+3��-3��
        if i<len(data_array)-1 and (int(data_array[i+1][7])-3)<=int(data_array[i][7])<=(int(data_array[i+1][7])+3):
            t['��������ͬ'] = 'ͬ'
        elif i<len(data_array)-1 and (int(data_array[i+1][7])+3)>16 and int(data_array[i][7])<=(int(data_array[i+1][7])-16+3):
            t['��������ͬ'] = 'ͬ'
        elif i<len(data_array)-1 and (int(data_array[i+1][7])-3)<0 and (int(data_array[i+1][7])+16-3)<=int(data_array[i][7]):
            t['��������ͬ'] = 'ͬ'            
        else:
            t['��������ͬ'] = '��'
        #�������ͬ�������ʵûʲô�ã�����Ϊ������ȫ���ܿ��Ǻ�����ϣ�
        if data_array[i][7] in data_array[i][1:7]:
            t['�������ͬ'] = 'ͬ'
        else:
            t['�������ͬ'] = '��'
        #5�������ޣ������ʵûʲô�ã��������50����50�����У�
        if i>len(data_array)-6:
            t['5��������'] = '��'
        elif data_array[i][7]==data_array[i+1][7] or \
             data_array[i][7]==data_array[i+2][7] or \
             data_array[i][7]==data_array[i+3][7] or \
             data_array[i][7]==data_array[i+4][7] or \
             data_array[i][7]==data_array[i+5][7]:
            t['5��������'] = '��'
        else:
            t['5��������'] = '��'
        #11��������
        if i>len(data_array)-12:
            t['11��������'] = '��'
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
            t['11��������'] = '��'
        else:
            t['11��������'] = '��'            

        blueDatas.append(t)
            
    #�Ƽ���Ҫ�õ��Ĳο�����    
    adviceDatas = {'������':0,'����ż':0, \
                   'ż����':0,'ż��ż':0, \
                   '����������':0,'��������ż':0, \
                   '����ż����':0,'����ż��ż':0, \
                   'ż��������':0,'ż������ż':0, \
                   'ż��ż����':0,'ż��ż��ż':0, \
                   '������':0,'������':0, \
                   '������':0,'������':0, \
                   '����������':0,'����������':0, \
                   '����������':0,'����������':0, \
                   '����������':0,'����������':0, \
                   '����������':0,'����������':0, \
                   '����С':0,'������':0, \
                   'С��С':0,'С����':0, \
                   '��������С':0,'����������':0, \
                   '����С��С':0,'����С����':0, \
                   'С������С':0,'С��������':0, \
                   'С��С��С':0,'С��С����':0, \
                   'ͬ����':0,'ͬ��ͬ':0, \
                   '������':0,'����ͬ':0, \
                   'ͬ��ͬ����':0,'ͬ��ͬ��ͬ':0, \
                   '����ͬ����':0,'����ͬ��ͬ':0, \
                   'ͬ��������':0,'ͬ������ͬ':0, \
                   '����������':0,'��������ͬ':0, \
                   '������':0,'������':0, \
                   '������':0,'������':0, \
                   '����������':0,'����������':0, \
                   '����������':0,'����������':0, \
                   '����������':0,'����������':0, \
                   '����������':0,'����������':0                 
                   }
    #��ż��
    for i in range(0, len(blueDatas)-1):
        if blueDatas[i]['��ż']=='��' and blueDatas[i+1]['��ż']=='��':
            adviceDatas['������'] = adviceDatas['������'] + 1
        if blueDatas[i]['��ż']=='ż' and blueDatas[i+1]['��ż']=='��':
            adviceDatas['����ż'] = adviceDatas['����ż'] + 1
        if blueDatas[i]['��ż']=='��' and blueDatas[i+1]['��ż']=='ż':
            adviceDatas['ż����'] = adviceDatas['ż����'] + 1
        if blueDatas[i]['��ż']=='ż' and blueDatas[i+1]['��ż']=='ż':
            adviceDatas['ż��ż'] = adviceDatas['ż��ż'] + 1              
    for i in range(0, len(blueDatas)-2):
        if blueDatas[i]['��ż']=='��' and blueDatas[i+1]['��ż']=='��' and blueDatas[i+2]['��ż']=='��':
            adviceDatas['����������'] = adviceDatas['����������'] + 1
        if blueDatas[i]['��ż']=='ż' and blueDatas[i+1]['��ż']=='��' and blueDatas[i+2]['��ż']=='��':
            adviceDatas['��������ż'] = adviceDatas['��������ż'] + 1
        if blueDatas[i]['��ż']=='��' and blueDatas[i+1]['��ż']=='ż' and blueDatas[i+2]['��ż']=='��':
            adviceDatas['����ż����'] = adviceDatas['����ż����'] + 1
        if blueDatas[i]['��ż']=='ż' and blueDatas[i+1]['��ż']=='ż' and blueDatas[i+2]['��ż']=='��':
            adviceDatas['����ż��ż'] = adviceDatas['����ż��ż'] + 1
        if blueDatas[i]['��ż']=='��' and blueDatas[i+1]['��ż']=='��' and blueDatas[i+2]['��ż']=='ż':
            adviceDatas['ż��������'] = adviceDatas['ż��������'] + 1
        if blueDatas[i]['��ż']=='ż' and blueDatas[i+1]['��ż']=='��' and blueDatas[i+2]['��ż']=='ż':
            adviceDatas['ż������ż'] = adviceDatas['ż������ż'] + 1
        if blueDatas[i]['��ż']=='��' and blueDatas[i+1]['��ż']=='ż' and blueDatas[i+2]['��ż']=='ż':
            adviceDatas['ż��ż����'] = adviceDatas['ż��ż����'] + 1
        if blueDatas[i]['��ż']=='ż' and blueDatas[i+1]['��ż']=='ż' and blueDatas[i+2]['��ż']=='ż':
            adviceDatas['ż��ż��ż'] = adviceDatas['ż��ż��ż'] + 1
    #������
    for i in range(0, len(blueDatas)-1):
        if blueDatas[i]['����']=='��' and blueDatas[i+1]['����']=='��':
            adviceDatas['������'] = adviceDatas['������'] + 1
        if blueDatas[i]['����']=='��' and blueDatas[i+1]['����']=='��':
            adviceDatas['������'] = adviceDatas['������'] + 1
        if blueDatas[i]['����']=='��' and blueDatas[i+1]['����']=='��':
            adviceDatas['������'] = adviceDatas['������'] + 1
        if blueDatas[i]['����']=='��' and blueDatas[i+1]['����']=='��':
            adviceDatas['������'] = adviceDatas['������'] + 1
    for i in range(0, len(blueDatas)-2):
        if blueDatas[i]['����']=='��' and blueDatas[i+1]['����']=='��' and blueDatas[i+2]['����']=='��':
            adviceDatas['����������'] = adviceDatas['����������'] + 1
        if blueDatas[i]['����']=='��' and blueDatas[i+1]['����']=='��' and blueDatas[i+2]['����']=='��':
            adviceDatas['����������'] = adviceDatas['����������'] + 1
        if blueDatas[i]['����']=='��' and blueDatas[i+1]['����']=='��' and blueDatas[i+2]['����']=='��':
            adviceDatas['����������'] = adviceDatas['����������'] + 1
        if blueDatas[i]['����']=='��' and blueDatas[i+1]['����']=='��' and blueDatas[i+2]['����']=='��':
            adviceDatas['����������'] = adviceDatas['����������'] + 1
        if blueDatas[i]['����']=='��' and blueDatas[i+1]['����']=='��' and blueDatas[i+2]['����']=='��':
            adviceDatas['����������'] = adviceDatas['����������'] + 1
        if blueDatas[i]['����']=='��' and blueDatas[i+1]['����']=='��' and blueDatas[i+2]['����']=='��':
            adviceDatas['����������'] = adviceDatas['����������'] + 1
        if blueDatas[i]['����']=='��' and blueDatas[i+1]['����']=='��' and blueDatas[i+2]['����']=='��':
            adviceDatas['����������'] = adviceDatas['����������'] + 1
        if blueDatas[i]['����']=='��' and blueDatas[i+1]['����']=='��' and blueDatas[i+2]['����']=='��':
            adviceDatas['����������'] = adviceDatas['����������'] + 1
    #��С��
    for i in range(0, len(blueDatas)-1):
        if blueDatas[i]['��С']=='С' and blueDatas[i+1]['��С']=='��':
            adviceDatas['����С'] = adviceDatas['����С'] + 1
        if blueDatas[i]['��С']=='��' and blueDatas[i+1]['��С']=='��':
            adviceDatas['������'] = adviceDatas['������'] + 1
        if blueDatas[i]['��С']=='С' and blueDatas[i+1]['��С']=='С':
            adviceDatas['С��С'] = adviceDatas['С��С'] + 1
        if blueDatas[i]['��С']=='��' and blueDatas[i+1]['��С']=='С':
            adviceDatas['С����'] = adviceDatas['С����'] + 1
    for i in range(0, len(blueDatas)-2):
        if blueDatas[i]['��С']=='С' and blueDatas[i+1]['��С']=='��' and blueDatas[i+2]['��С']=='��':
            adviceDatas['��������С'] = adviceDatas['��������С'] + 1
        if blueDatas[i]['��С']=='��' and blueDatas[i+1]['��С']=='��' and blueDatas[i+2]['��С']=='��':
            adviceDatas['����������'] = adviceDatas['����������'] + 1
        if blueDatas[i]['��С']=='С' and blueDatas[i+1]['��С']=='��' and blueDatas[i+2]['��С']=='С':
            adviceDatas['С������С'] = adviceDatas['С������С'] + 1
        if blueDatas[i]['��С']=='��' and blueDatas[i+1]['��С']=='��' and blueDatas[i+2]['��С']=='С':
            adviceDatas['С��������'] = adviceDatas['С��������'] + 1
        if blueDatas[i]['��С']=='С' and blueDatas[i+1]['��С']=='С' and blueDatas[i+2]['��С']=='��':
            adviceDatas['����С��С'] = adviceDatas['����С��С'] + 1
        if blueDatas[i]['��С']=='��' and blueDatas[i+1]['��С']=='С' and blueDatas[i+2]['��С']=='��':
            adviceDatas['����С����'] = adviceDatas['����С����'] + 1
        if blueDatas[i]['��С']=='С' and blueDatas[i+1]['��С']=='С' and blueDatas[i+2]['��С']=='С':
            adviceDatas['С��С��С'] = adviceDatas['С��С��С'] + 1
        if blueDatas[i]['��С']=='��' and blueDatas[i+1]['��С']=='С' and blueDatas[i+2]['��С']=='С':
            adviceDatas['С��С����'] = adviceDatas['С��С����'] + 1
    #��ͬ��
    for i in range(0, len(blueDatas)-1):
        if blueDatas[i]['��������ͬ']=='��' and blueDatas[i+1]['��������ͬ']=='ͬ':
            adviceDatas['ͬ����'] = adviceDatas['ͬ����'] + 1
        if blueDatas[i]['��������ͬ']=='ͬ' and blueDatas[i+1]['��������ͬ']=='ͬ':
            adviceDatas['ͬ��ͬ'] = adviceDatas['ͬ��ͬ'] + 1
        if blueDatas[i]['��������ͬ']=='��' and blueDatas[i+1]['��������ͬ']=='��':
            adviceDatas['������'] = adviceDatas['������'] + 1
        if blueDatas[i]['��������ͬ']=='ͬ' and blueDatas[i+1]['��������ͬ']=='��':
            adviceDatas['����ͬ'] = adviceDatas['����ͬ'] + 1
    for i in range(0, len(blueDatas)-2):
        if blueDatas[i]['��������ͬ']=='��' and blueDatas[i+1]['��������ͬ']=='ͬ' and blueDatas[i+2]['��������ͬ']=='ͬ':
            adviceDatas['ͬ��ͬ����'] = adviceDatas['ͬ��ͬ����'] + 1
        if blueDatas[i]['��������ͬ']=='ͬ' and blueDatas[i+1]['��������ͬ']=='ͬ' and blueDatas[i+2]['��������ͬ']=='ͬ':
            adviceDatas['ͬ��ͬ��ͬ'] = adviceDatas['ͬ��ͬ��ͬ'] + 1
        if blueDatas[i]['��������ͬ']=='��' and blueDatas[i+1]['��������ͬ']=='ͬ' and blueDatas[i+2]['��������ͬ']=='��':
            adviceDatas['����ͬ����'] = adviceDatas['����ͬ����'] + 1
        if blueDatas[i]['��������ͬ']=='ͬ' and blueDatas[i+1]['��������ͬ']=='ͬ' and blueDatas[i+2]['��������ͬ']=='��':
            adviceDatas['����ͬ��ͬ'] = adviceDatas['����ͬ��ͬ'] + 1
        if blueDatas[i]['��������ͬ']=='��' and blueDatas[i+1]['��������ͬ']=='��' and blueDatas[i+2]['��������ͬ']=='ͬ':
            adviceDatas['ͬ��������'] = adviceDatas['ͬ��������'] + 1
        if blueDatas[i]['��������ͬ']=='ͬ' and blueDatas[i+1]['��������ͬ']=='��' and blueDatas[i+2]['��������ͬ']=='ͬ':
            adviceDatas['ͬ������ͬ'] = adviceDatas['ͬ������ͬ'] + 1
        if blueDatas[i]['��������ͬ']=='��' and blueDatas[i+1]['��������ͬ']=='��' and blueDatas[i+2]['��������ͬ']=='��':
            adviceDatas['����������'] = adviceDatas['����������'] + 1
        if blueDatas[i]['��������ͬ']=='ͬ' and blueDatas[i+1]['��������ͬ']=='��' and blueDatas[i+2]['��������ͬ']=='��':
            adviceDatas['��������ͬ'] = adviceDatas['��������ͬ'] + 1
    #������
    for i in range(0, len(blueDatas)-1):
        if blueDatas[i]['11��������']=='��' and blueDatas[i+1]['11��������']=='��':
            adviceDatas['������'] = adviceDatas['������'] + 1
        if blueDatas[i]['11��������']=='��' and blueDatas[i+1]['11��������']=='��':
            adviceDatas['������'] = adviceDatas['������'] + 1
        if blueDatas[i]['11��������']=='��' and blueDatas[i+1]['11��������']=='��':
            adviceDatas['������'] = adviceDatas['������'] + 1
        if blueDatas[i]['11��������']=='��' and blueDatas[i+1]['11��������']=='��':
            adviceDatas['������'] = adviceDatas['������'] + 1
    for i in range(0, len(blueDatas)-2):
        if blueDatas[i]['11��������']=='��' and blueDatas[i+1]['11��������']=='��' and blueDatas[i+2]['11��������']=='��':
            adviceDatas['����������'] = adviceDatas['����������'] + 1
        if blueDatas[i]['11��������']=='��' and blueDatas[i+1]['11��������']=='��' and blueDatas[i+2]['11��������']=='��':
            adviceDatas['����������'] = adviceDatas['����������'] + 1
        if blueDatas[i]['11��������']=='��' and blueDatas[i+1]['11��������']=='��' and blueDatas[i+2]['11��������']=='��':
            adviceDatas['����������'] = adviceDatas['����������'] + 1
        if blueDatas[i]['11��������']=='��' and blueDatas[i+1]['11��������']=='��' and blueDatas[i+2]['11��������']=='��':
            adviceDatas['����������'] = adviceDatas['����������'] + 1
        if blueDatas[i]['11��������']=='��' and blueDatas[i+1]['11��������']=='��' and blueDatas[i+2]['11��������']=='��':
            adviceDatas['����������'] = adviceDatas['����������'] + 1
        if blueDatas[i]['11��������']=='��' and blueDatas[i+1]['11��������']=='��' and blueDatas[i+2]['11��������']=='��':
            adviceDatas['����������'] = adviceDatas['����������'] + 1
        if blueDatas[i]['11��������']=='��' and blueDatas[i+1]['11��������']=='��' and blueDatas[i+2]['11��������']=='��':
            adviceDatas['����������'] = adviceDatas['����������'] + 1
        if blueDatas[i]['11��������']=='��' and blueDatas[i+1]['11��������']=='��' and blueDatas[i+2]['11��������']=='��':
            adviceDatas['����������'] = adviceDatas['����������'] + 1
            
    #��������
    return blueDatas, adviceDatas, blue_hot, blue_cold
