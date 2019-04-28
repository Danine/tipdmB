path = 'D:/libsvm-3.23/python'
import os
import sys
import pickle
import csv
sys.path.append(path)
from svmutil import *

def getdata(path):
    data_input = open(path+'/people.pkl','rb')
    data = pickle.load(data_input)
    data_input.close()
    return data
yinyang = []
filename = u'png/set.csv'
with open(filename) as f:
    reader = csv.reader(f)
    head_row = next(reader)
    for row in reader:
        # 行号从2开始
        yinyang.append(row[3])

path = u'png'
document = os.listdir(path)
a = getdata(path)
