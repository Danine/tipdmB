import pickle
import features
import os

def getdata(path):
    data_input = open(npath,'rb')
    data = pickle.load(data_input)
    data_input.close()
    return data

count = 0
path = u'png'
document = os.listdir(path)
peoples = []
for i in document:
    try:
        ndocu = os.listdir(path + '/' + i)
        for k in ndocu:
            npath = path + '/' + i + '/' + k
            if 'people' in k:
                data = getdata(npath)
                
                for i in data:
                    if type(i).__name__ == 'list':
                        if i not in peoples:
                            peoples.append(i)
                    else:
                        temp = [i for i in data]
                        if temp not in peoples:
                            peoples.append(temp)
    except:
            print(path + '/' + i)
data_output = open(path + '/' + 'people.pkl', 'wb')
pickle.dump(peoples, data_output)
data_output.close()

