# -*- coding: cp936 -*-
# otherrrr@gmail.com
# ���˲����ļ���д

def readFilterFileToArray(): #��ȡ���˲���
    '''����������.txt��������ת��������'''
    f = open('��������.txt', 'r')
    filter_array_temp = f.readlines()
    f.close()

    for i in range(0, len(filter_array_temp)):
        if '==BEGIN==' in filter_array_temp[i]:
            pos_begin = i #��ʼλ��
    for i in range(0, len(filter_array_temp)):
        if '==END==' in filter_array_temp[i]:
            pos_end = i #����λ��

    filter_array = []

    for i in range(pos_begin+1, pos_end):
        filter_term = ['�ڼ���', '����', '�Ƿ�����', '��Χ', '˵��']
        filter_term[0] =  filter_array_temp[i].split('()')[0]
        filter_term[1] =  filter_array_temp[i].split('()')[1]
        filter_term[2] =  filter_array_temp[i].split('()')[2]
        filter_term[3] =  filter_array_temp[i].split('()')[3]
        filter_term[4] =  filter_array_temp[i].split('()')[4][:-1]

        filter_array.append(filter_term)

    return filter_array
