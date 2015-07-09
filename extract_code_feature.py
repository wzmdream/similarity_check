# -*- coding: utf-8 -*-
import re
import math
import pickle

# 载入 IDF
fh = open('IDF.dat', 'rb')
IDF = pickle.load(fh)
fh.close()

# 定义特征
patterns = [r'\bimport\b', r'\bclass\b', r'\bdef\b', r'\bif\b|\belif\b', r'\belse\b', \
            r'\bfor\b', r'\bwhile\b', r'\+', r'\-', r'\*', r'/', r'%', r'[^=]=[^=]', \
            r'==', r'>', r'<', r'\band\b', r'\bor\b', r'\bnot\b', r'\bTrue\b', \
            r'\bFalse\b', r'\bNone\b', r'\.', r',', r'\:', r'\'|\"', r'\[|\]', \
            r'\(|\)', r'\{|\}', r'\bin\b', r'\bis\b', r'\breturn\b']
                
def preprocessing(pyfile):
    # 读文件
    try:
        with open(pyfile, 'r', encoding = 'utf-8', errors = 'ignore') as fh:
            lines = fh.readlines()
    except IOError as ioerr:
        print('文件错误：' + str(ioerr))
        return None
    
    # 合并行
    source_code = ''
    for line in lines:
        new_line = re.sub(r'#.*', '', line) # 去掉单行注释
        if re.search(r'\w', new_line):      # 如果不是空白行
            new_line = re.sub(r'^[ \t]+', '', new_line) # 去掉缩进
            source_code += new_line
    
    # 去掉 docstring
    source_code = re.sub(r'(\'{3}|\"{3}).*(\'{3}|\"{3})\s', '', source_code, flags = re.DOTALL)
    
    # 断开的多行恢复为单行 
    return re.sub(r'\\[ \t]*\n', '', source_code)
    
    
def extract_feature(pyfile):
    processed_code = preprocessing(pyfile)

    feature = []  
    for p in patterns:
        feature.append(len(re.findall(p, processed_code)))
    
    # 不根据代码的行数调整词频   
    #line_count = len(processed_code.split('\n'))
    #feature =  [f / line_count for f in feature]
    
    # 利用 IDF 调整特征
    for i in range(len(feature)):
        feature[i] *= IDF[i]
   
    return normalization(feature)
    

# 为了反映代码量在判别差异性中的重要性，实际中未对特征向量进行规则化
# 规则化（将 feature 的模调整为1）
def normalization(feature):   
    magnitude = math.sqrt(sum([f**2 for f in feature]))
    return [f / magnitude for f in feature]


# 测试
if __name__ == '__main__':
    file = 'c:\\py_files2\\shoot.py'
    print(extract_feature(file))
