# -*- coding: cp936 -*-
# otherrrr@gmail.com
# 固定投注文件读取

def readBetFileToArray():
    f = open('data/固定投注.txt', 'r')
    bet_array_temp  = f.readlines()
    f.close()

    bet_array = []
    
    for i in range(0, len(bet_array_temp)-1):
        
        bet_term = ['红球1', '红球2', '红球3', '红球4', '红球5', '红球6', '蓝球']

        bet_term[0] =  bet_array_temp[i].split('+')[0].split(',')[0]
        bet_term[1] =  bet_array_temp[i].split('+')[0].split(',')[1]
        bet_term[2] =  bet_array_temp[i].split('+')[0].split(',')[2]
        bet_term[3] =  bet_array_temp[i].split('+')[0].split(',')[3]
        bet_term[4] =  bet_array_temp[i].split('+')[0].split(',')[4]
        bet_term[5] =  bet_array_temp[i].split('+')[0].split(',')[5][0:2]
        bet_term[6] =  bet_array_temp[i].split('+')[1][0:2]

        bet_array.append(bet_term)

    #命令行提示
    print '读取固定投注%d组'%(len(bet_array))
    
    return bet_array
