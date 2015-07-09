# -*- coding: utf-8 -*-
"""
IDF (inverse document frequency)
目的：利用 IDF 调整文档特征里 TF (term frequency) 的值
公式：log(代码库代码总行数 / 含有某符号的行数)

注：
    1.代码库由 python 安装目录里的6200多个 .py 文件构成
    2.源文件都去除了注释和空行
"""

import os
import re
import math
import pickle
import extract_code_feature as ecf

py_dir = 'c:\\py_files1'
line_count = 0
term_count = [0 for p in ecf.patterns]

for file in os.listdir(py_dir):
    file_path = os.path.join(py_dir, file)
    processed_code = ecf.preprocessing(file_path)    
    line_count += len(re.findall(r'\n', processed_code))

#    方法1
#    for i, p in enumerate(ecf.patterns):
#        term_count[i] += len(re.findall(p, processed_code))
    
#    方法2
    line_list = processed_code.split('\n')
    for line in line_list:
        if re.search(r'\w', line): # 如果不是空白行
            temp = []
            for p in ecf.patterns:
                if re.search(p, line):
                    temp.append(1)
                else:
                    temp.append(0)
            for i in range(len(term_count)):
                term_count[i] += temp[i]
    
# 计算 IDF
IDF = [math.log(line_count / t) for t in term_count]
    
# 保存结果
fh = open('IDF.dat', 'wb')
pickle.dump(IDF, fh)
pickle.dump(line_count, fh)
pickle.dump(term_count, fh)
fh.close()
