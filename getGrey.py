import matplotlib.pyplot as plt
import dicom
import os

def getpng(path):
    data = plt.imread(path)
    return data#.tolist()

pieces = []
path = u'C:/Users/Tyson/Desktop/Teddy/png/1001/arterial phase'
pngs = os.listdir(path)
simple = []
for i in pngs:
    if 'mask' in i:
        simple.append(getpng(path + '/' + i))

notsimp = []
for i in pngs:
    if 'mask' not in i:
        notsimp.append(getpng(path + '/' + i))

for i in range(len(simple)):
    for j in range(len(simple[i])):
        for k in range(len(simple[i][j])):
            if simple[i][j][k] == 0:
                notsimp[i][j][k] = 0
            else:
                notsimp[i][j][k] *= 4096

plt.figure()
plt.subplot(1,2,1)
plt.imshow(notsimp[7])
plt.subplot(1,2,2)
plt.imshow(simple[7])
plt.show()

