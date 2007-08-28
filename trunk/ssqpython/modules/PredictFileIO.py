# -*- coding: cp936 -*-
# otherrrr@gmail.com
# Ԥ�������ļ���д

import os

def writePredictData(data_array, data_f, filter_array, num_pool): #Ԥ������д���ļ�
    '''�½���Ӧ���ڵ��ļ��У�������д��Ԥ�������ļ�
       ������д���Ӧ�Ĺ��������ļ���
    '''
    #����
    date = '%s'%(int(data_array[0][0])+1)
    #������Ŀ¼
    try:
        os.mkdir(date)
    except OSError: #����ļ����Ѵ��ڣ������ִ˴���
        pass
    #����Ŀ¼�д�����д���ļ�2007XXXԤ������.txt
    f = open('%s/%sԤ������.txt'%(date,date), 'w')
    #д����
    for i in range(0, len(data_f)):
        #�������ʹ��һ����ѭ���Ļ����Ứ�Ѹ���ʱ��
        f.write('%.2d %.2d %.2d %.2d %.2d %.2d\n'\
                %(data_f[i][0],data_f[i][1],data_f[i][2],data_f[i][3],data_f[i][4],data_f[i][5]))
    f.close()   
    #����Ŀ¼�д�����д���ļ�2007XXX��������.txt
    f = open('%s/%s��������.txt'%(date,date), 'w')
    f.write('     ()����         ()�Ƿ�����()��Χ\n')
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
    f.write('==')
    for i in range(0, len(num_pool)):
        f.write('%.2d'%num_pool[i]+',')
    f.write('==\n')
    f.close()
    
def readPredictData(date): #��ȡԤ�����ݺ͹�������
    '''��ȡԤ�����ݺ�ʹ�õ��Ĺ�������'''   
    #��Ԥ������
    f = open('%s/%sԤ������.txt'%(date,date), 'r')
    tmp = f.readlines() 
    f.close()
    predict_data = [] #Ԥ������
    for i in range(0, len(tmp)):
        predict_data.append([tmp[i][0:2],tmp[i][3:5],tmp[i][6:8],\
                             tmp[i][9:11],tmp[i][12:14],tmp[i][15:17]])
    #����������
    f = open('%s/%s��������.txt'%(date,date), 'r')
    tmp = f.readlines()
    f.close()
    predict_filter = [] #ʹ�õĹ�������
    tmp_m = tmp[2:-1]#ȥ����β
    for i in range(0, len(tmp_m)): 
        if '��' in tmp_m[i]: #ȷ����ʹ�á�
            term = ['�ڼ���', '����', '�Ƿ�����', '��Χ']
            term[0] =  tmp_m[i].split('()')[0]
            term[1] =  tmp_m[i].split('()')[1]
            term[2] =  tmp_m[i].split('()')[2]
            term[3] =  tmp_m[i].split('()')[3]
            predict_filter.append(term)
        else:
            pass

    #��ȡѡ�����
    select_num = [] #����أ�����͹��������Ǹ����в�ͬ���Ǹ���int�͵�list�������str�͵�
    for i in range(0, (len(tmp[-1])-4)/3):
        select_num.append(tmp[-1][i*3+2:i*3+4])
    return predict_data, predict_filter, select_num


