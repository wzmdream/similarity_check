# -*- coding: utf-8 -*-
import os
import sys
import math
import similarity_algorithm as algoritic
import extract_code_feature as ecf

if __name__ == '__main__':


    # 提取给定目录下源文件的特征
    py_dir = 'C:\\Users\zmh\Desktop\\similarity_check_new\py_files\\WorldCupMemory.py'
    print(py_dir)
    feature=ecf.extract_feature(py_dir)	
		
		
		
	#读取已有的特征
    f = open('C:\\Users\zmh\Desktop\\similarity_check_new\\feature.txt')
    lines = f.readlines()
    f.close()
    feature_result=[]
    result_list = lines[0:]  #从第一行开始
    j=0
    for result in result_list:
        feature_result.append(result)
        #print(result)
        # print('--------------------------------------------------------------------------------')
        # j=j+1
    #print(j)
    print(type(feature_result))
    print(feature_result)
    feature_result=''.join(feature_result)
    feature_result=feature_result.split("\n")
    print(type(feature_result[0]))
    for i in range(len(feature_result)-1):
        
        #feature_result[i]=''.join(feature_result[i])
        #print(type(feature_result[i]))
        feature_result[i]=feature_result[i].split(",")
        #print(feature_result[i])

    print(type(feature_result[58][31]))
    #print(feature_result)	
    # print(type(feature_result))
    # feature_result=str(feature_result).split("\n',")
	
    # print(feature_result)
    #print(type(feature_result))
	
        

    # 相似度度量方法：algoritic.cos_similarity ， algoritic.norm2_distance 或 algoritic.divengence
    #measurement = algoritic.norm2_distance 
    #measurement = algoritic.cos_similarity
    measurement = algoritic.divergence


    # # 两两测试
    # check_result = []
    # for i in range(len(feature_list) - 1):
        # for j in range(i+1, len(feature_list)):
            # check_result.append([feature_list[i][0], feature_list[j][0], \
                               # measurement(feature_list[i][1], feature_list[j][1])])


    # # 若采用余弦定理计算相似性需要降序排序
    # if measurement is algoritic.cos_similarity:
        # check_result.sort(key = lambda item: item[2], reverse = True)
    # else:
        # check_result.sort(key = lambda item: item[2])
        

    # 显示结果
    # print(check_result[0:10])
    # for i in range(20):
        # print("{0:^25} <---> {1:^25} : {2:<7.2%}".\
            # format(check_result[i][0], check_result[i][1], check_result[i][2]))
        # # print(check_result[i])
