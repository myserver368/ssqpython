# -*- coding: cp936 -*-
# otherrrr@gmail.com
# �̶�Ͷע�ļ���ȡ

def readBetFileToArray():
    f = open('�̶�Ͷע.txt', 'r')
    bet_array_temp  = f.readlines()
    f.close()

    bet_array = []
    
    for i in range(0, len(bet_array_temp)-1):
        
        bet_term = ['����1', '����2', '����3', '����4', '����5', '����6', '����']

        bet_term[0] =  bet_array_temp[i].split('+')[0].split(',')[0]
        bet_term[1] =  bet_array_temp[i].split('+')[0].split(',')[1]
        bet_term[2] =  bet_array_temp[i].split('+')[0].split(',')[2]
        bet_term[3] =  bet_array_temp[i].split('+')[0].split(',')[3]
        bet_term[4] =  bet_array_temp[i].split('+')[0].split(',')[4]
        bet_term[5] =  bet_array_temp[i].split('+')[0].split(',')[5][0:2]
        bet_term[6] =  bet_array_temp[i].split('+')[1][0:2]

        bet_array.append(bet_term)
        
    return bet_array
