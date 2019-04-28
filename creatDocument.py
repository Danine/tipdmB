import os
def create(addr):
    for i in range(1005,1109):
        os.makedirs(addr+'/'+str(i))
addr = 'C:/Users/Tyson/Desktop/png'
create(addr)