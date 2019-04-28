import os
import numpy as np
import pickle
import matplotlib.pyplot as plt
import cv2

def getpng(path):
    # temp = cv2.imread(path)
    # data = cv2.cvtColor(temp, cv2.COLOR_BGR2GRAY)
    data = plt.imread(path)
    return data.tolist()

count = 0
path = u'png'
document = os.listdir(path)
for i in document:
    ndocu = os.listdir(path + '/' + i)
    for j in ndocu:
        pngs = os.listdir(path + '/' + i + '/' + j)
        simple = []; notsimp = []; CT = []
        for k in pngs:
            npath = path + '/' + i + '/' + j + '/' + k
            if 'data' in k:
                break
            if 'mask' in k:
                simple.append(getpng(npath))
            elif 'mask' not in k:
                notsimp.append(getpng(npath))

        for l in range(len(simple)):
            CT.append([])
            for m in range(len(simple[l])):
                CT[l].append([])
                for n in range(len(simple[l][m])):
                    if simple[l][m][n] == 0:
                        CT[l][m].append(0)
                    else:
                        t = int(notsimp[l][m][n]*4096)
                        CT[l][m].append(t)

        data_output = open(path + '/' + i + '/' + j + '/' + 'data.pkl', 'wb')
        pickle.dump(CT, data_output)
        data_output.close()
        count += 1
        print(count)