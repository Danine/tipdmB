import matplotlib.pyplot as plt
import dicom
import os
from skimage import exposure,img_as_float
# filename = "C:/Users/Tyson/Desktop/Teddy/B-Alldata/data/1002/arterial phase/10002.dcm"
# dcm = dicom.read_file(filename)
# a = [dcm.pixel_array]
# print(dcm.pixel_array)
# plt.figure()
# plt.imshow(dcm.pixel_array)
# plt.show()

def dicom2png(files):
    dcm = dicom.read_file(files)
    filename = os.path.basename(files).split('.')[0]
    imageX = dcm.pixel_array
    # temp = imageX.copy()
    # print('shape--',imageX.shape)
    # picMax = imageX.max()
    # vmin = imageX.min()
    # vmax = temp[temp<picMax].max()
    # imageX[imageX > vmax] = 0
    # imageX[imageX < vmin] = 0
    image = img_as_float(imageX)
    plt.cla()
    plt.figure('adjust_gamma', figsize=(5.12, 5.12))
    plt.subplots_adjust(top=1, bottom=0, left=0, right=1, hspace=0, wspace=0)#去边框
    plt.imshow(image)
    plt.axis('off')#设置坐标轴
    plt.savefig(filename + '.png')
    # time.sleep(1)

files = r"C:/Users/Tyson/Desktop/Teddy/B-Alldata/data/1002/arterial phase/10017.dcm"
dicom2png(files)
