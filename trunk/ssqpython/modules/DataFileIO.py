# -*- coding: cp936 -*-
# otherrrr@gmail.com
# ���������ļ���д

def readDataFileToString(): #��ȡ��������
    '''��ȡ��������.txt���õ�string����'''
    f = open('��������.txt', 'r')
    data_string  = f.read()
    f.close()

    return data_string
    
def readDataFileToArray(): #��ȡ��������
    '''��ȡ��������.txt���õ�list����'''
    f = open('��������.txt', 'r')
    data_array_temp  = f.readlines()
    f.close()

    data_array = []
    
    for i in range(0, len(data_array_temp)):
        data_term = ['����', '����1', '����2', '����3', '����4', '����5', '����6', '����']
        #Ҳ����ֱ�Ӷ�ȡ"λ��"����������"����"(split)
        data_term[0] =  data_array_temp[i].split(' ')[0]
        data_term[1] =  data_array_temp[i].split(' ')[1].split(',')[0]
        data_term[2] =  data_array_temp[i].split(' ')[1].split(',')[1]
        data_term[3] =  data_array_temp[i].split(' ')[1].split(',')[2]
        data_term[4] =  data_array_temp[i].split(' ')[1].split(',')[3]
        data_term[5] =  data_array_temp[i].split(' ')[1].split(',')[4]
        data_term[6] =  data_array_temp[i].split(' ')[1].split(',')[5][0:2]
        data_term[7] =  data_array_temp[i].split('+')[1][0:2]

        data_array.append(data_term)
    return data_array

def writeStringToDataFile(data_string): #д�뿪������
    '''��stringд�뿪������.txt��'''
    f = open('��������.txt', 'w')
    f.write(data_string)
    f.close()
