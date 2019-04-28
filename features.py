import math

# n = (len(data) * 512 *512)

def zhifangtu(data):
    histogram = [0 for _ in range(512)]
    summ = 0
    for i in range(len(data)):
        for j in range(512):
            for k in range(512):
                histogram[j] += data[i][j][k]
    #             summ += data[i][j][k]
    # for i in range(len(data)):
    #     for j in range(512):
    #         for k in range(512):
    #             histogram[j] /= summ
    return histogram

def meann(data):
    summ = 0
    for i in range(len(data)):
        for j in range(512):
            for k in range(512):
                summ += data[i][j][k]
    mean = summ / (len(data) * 512 *512)
    return mean


def fangcha(data):
    mean = meann(data)
    summ = 0
    for i in range(len(data)):
        for j in range(512):
            for k in range(512):
                summ = summ + (data[i][j][k] - mean)**2
    variance = summ / ((len(data) * 512 *512) - 1)
    return variance

def piandu(data):
    mean = meann(data)
    sum1 = sum2 = 0
    for i in range(len(data)):
        for j in range(512):
            for k in range(512):
                sum1 = sum1 + (data[i][j][k] - mean)**3
                sum2 = sum2 + (data[i][j][k] - mean)**2
    sum1 /= (len(data) * 512 *512)
    sum2 = (math.sqrt(sum2/(len(data) * 512 *512)))**3
    skewness = sum1/sum2
    return skewness

def fengdu(data):
    mean = meann(data)
    sum1 = sum2 = 0
    for i in range(len(data)):
        for j in range(512):
            for k in range(512):
                sum1 = sum1 + (data[i][j][k] - mean)**4
                sum2 = sum2 + (data[i][j][k] - mean)**2
    sum1 /= (len(data) * 512 *512)
    sum2 = (math.sqrt(sum2/(len(data) * 512 *512)))**2
    kurtosis = sum1/sum2
    return kurtosis

def junyunxing(data):
    uniformity = 0
    histogram = zhifangtu(data)
    for i in range(512):
        uniformity = uniformity + histogram[i]**2
    return uniformity

def shang(data):
    entropy = 0
    histogram = zhifangtu(data)
    for i in range(512):
        if histogram[i] != 0:
            entropy = entropy + histogram[i] * math.log2(histogram[i])
    return entropy

def tiji(data):
    volumn = 0
    for i in range(len(data)):
        for j in range(512):
            for k in range(512):
                if data[i][j][k] > -1024:
                    volumn += 1
    return volumn

def CTqujian(data):
    b = []
    for i in range(len(data)):
        b.append([])
        for j in range(512):
            b[i].append([])
            for k in range(512):
                if data[i][j][k] == 0:
                    b[i][j].append(-1)
                else:
                    b[i][j].append((data[i][j][k]-1) / 256)
    return b

x = [1,0,0,-1,0,0,1,1,0,-1,-1,0,1]
y = [0,1,0,0,-1,0,1,0,1,-1,0,-1,1]
z = [0,0,1,0,0,-1,0,1,1,0,-1,-1,1]

def GLCM(data, b):
    GLCMl = []
    for d in range(13):
        GLCMl.append([])
        for m in range(16):
            GLCMl[d].append([])
            for n in range(16):
                GLCMl[d][m].append(0)
        for i in range(len(data)):
            for j in range(512):
                for k in range(512):
                    if not (j + x[d] < 0 or j + x[d] > 511 or k + y[d] < 0 or k + y[d] > 511 or i + z[d] < 0 or i + z[d] >= len(data)):
                        if (b[i][j][k] != -1 and b[i + z[d]][j + x[d]][k + y[d]] != -1):
                            GLCMl[d][int(b[i][j][k])][int(b[i + z[d]][j + x[d]][k + y[d]])] += 1
    return GLCMl

def zixiangguan(data, GLCMl):
    autocorrelation = 0
    for i in range(13):
        for j in range(16):
            for k in range(16):
                autocorrelation = autocorrelation + (i + 1) * (j + i) * GLCMl[i][j][k]
    return autocorrelation

def jiquanqushi(data, GLCMl):
    cluster_tendency = 0
    meanx = []; meany = []
    for i in range(13):
        meanx.append([])
        meany.append([])
        for j in range(16):
            meanx[i].append(0)
            meany[i].append(0)
    for d in range(13):
        for i in range(16):
            for j in range(16):
                meanx[d][i] += GLCMl[d][i][j]
                meany[d][j] += GLCMl[d][i][j]
    for d in range(13):
        for i in range(16):
            meanx[d][i] /= 16
            meany[d][j] /= 16
    for d in range(13):
        for i in range(16):
            for j in range(16):
                cluster_tendency = cluster_tendency + (i + j + meanx[d][i] + meany[d][j])**2 * GLCMl[d][i][j]
    cluster_tendency /= 13
    return cluster_tendency

def cuzhuangtuqi(data, GLCMl):
    cluster_prominence = 0
    meanx = []; meany = []
    for i in range(13):
        meanx.append([])
        meany.append([])
        for j in range(16):
            meanx[i].append(0)
            meany[i].append(0)
    for d in range(13):
        for i in range(16):
            for j in range(16):
                meanx[d][i] += GLCMl[d][i][j]
                meany[d][j] += GLCMl[d][i][j]
    for d in range(13):
        for i in range(16):
            meanx[d][i] /= 16
            meany[d][j] /= 16
    for d in range(13):
        for i in range(16):
            for j in range(16):
                cluster_prominence = cluster_prominence + (i + j + meanx[d][i] + meany[d][j])**4 * GLCMl[d][i][j]
    return cluster_prominence

def GLCMjunyunxing(data, GLCMl):
    homogeneity = 0
    for d in range(13):
        for i in range(16):
            for j in range(16):
                homogeneity = homogeneity + GLCMl[d][i][j] / (1 + abs(i - j))
    homogeneity /= 13
    return homogeneity

def GLCMshang(data, GLCMl):
    entropy = 0
    entropyd = [0 for _ in range(13)]
    for d in range(13):
        for i in range(16):
            for j in range(16):
                if GLCMl[d][i][j] != 0:
                    entropyd[d] = GLCMl[d][i][j] * math.log2(GLCMl[d][i][j])
                    entropy += entropyd[d]
    entropy /= 13
    return entropy

def IMC1(data, GLCMl):
    imc1 = 0
    sumx = []; sumy = []
    for i in range(13):
        sumx.append([])
        sumy.append([])
        for j in range(16):
            sumx[i].append(0)
            sumy[i].append(0)
    for d in range(13):
        for i in range(16):
            for j in range(16):
                sumx[d][i] += GLCMl[d][i][j]
                sumy[d][j] += GLCMl[d][i][j]
    hx = [0 for _ in range(13)]
    hy = [0 for _ in range(13)]
    hxy = [0 for _ in range(13)]
    for d in range(13):
        for i in range(16):
            if sumx[d][i] != 0 and sumy[d][i] != 0:
                hx[d] = hx[d] - sumx[d][i] * math.log2(sumx[d][i])
                hy[d] = hy[d] - sumy[d][i] * math.log2(sumy[d][i])
    entropyd = [0 for _ in range(13)]
    for d in range(13):
        for i in range(16):
            for j in range(16):
                if GLCMl[d][i][j] != 0:
                    entropyd[d] = GLCMl[d][i][j] * math.log2(GLCMl[d][i][j])
                if hx[d] * hy[d] != 0:
                    hxy[d] = hxy[d] - GLCMl[d][i][j] * math.log2(hx[d] * hy[d])
    for d in range(13):
        imc1 = imc1 + (entropyd[d] - hxy[d]) / max(hx[d], hy[d])
    imc1 /= 13
    return imc1

def GLRL(data, b):
    GLRLl = []
    for d in range(13):
        GLRLl.append([])
        for m in range(16):
            GLRLl[d].append([])
            for n in range(512):
                GLRLl[d][m].append(0)
    for d in range(13):
        for i in range(len(data)):
            for j in range(512):
                for k in range(512):
                    if not (j + x[d] < 0 or j + x[d] > 511 or k + y[d] < 0 or k + y[d] > 511 or i + z[d] < 0 or i + z[d] >= len(data)):
                        if (b[i][j][k] != -1):
                            if ((j - x[d] < 0 or j - x[d] > 511 or k - y[d] < 0 or k - y[d] > 511 or i - z[d] < 0 or i - z[d] >= len(data)) or b[i][j][k] != b[i - z[d]][j - x[d]][k - y[d]]):
                                sum = 1; xx = j + x[d]; yy = k + y[d]; zz = i + z[d]
                                while (not(xx < 0 or xx > 511 or yy < 0 or yy > 511 or zz < 0 or zz >= len(data)) and b[i][j][k] == b[zz][xx][yy]):
                                    sum += 1
                                    xx += x[d]
                                    yy += y[d]
                                    zz += z[d]
                                GLRLl[d][int(b[i][j][k])][sum] += 1
    return GLRLl

def SRE(data, GLRLl):
    sre = 0
    sum1 = [0 for _ in range(13)]
    sum2 = [0 for _ in range(13)]
    for d in range(13):
        for i in range(16):
            for j in range(512):
                sum1[d] = sum1[d] + GLRLl[d][i][j] / ((j + 1) * (j + 1))
                sum2[d] = sum2[d] + GLRLl[d][i][j]
    for d in range(13):
        sre = sre + sum1[d] / sum2[d]
    sre /= 13
    return sre

def LRE(data, GLRLl):
    lre = 0
    sum1 = [0 for _ in range(13)]
    sum2 = [0 for _ in range(13)]
    for d in range(13):
        for i in range(16):
            for j in range(512):
                sum1[d] = sum1[d] + GLRLl[d][i][j] * ((j + 1) * (j + 1))
                sum2[d] = sum2[d] + GLRLl[d][i][j]
    for d in range(13):
        lre = lre + sum1[d] / sum2[d]
    lre /= 13
    return lre

def LGLRE(data, GLRLl):
    lglre = 0
    sum1 = [0 for _ in range(13)]
    sum2 = [0 for _ in range(13)]
    for d in range(13):
        for i in range(16):
            for j in range(512):
                sum1[d] = sum1[d] + GLRLl[d][i][j] / ((i + 1) * (i + 1))
                sum2[d] = sum2[d] + GLRLl[d][i][j]
    for d in range(13):
        lglre = lglre + sum1[d] / sum2[d]
    lglre /= 13
    return lglre

def HGLRE(data, GLRLl):
    hglre = 0
    sum1 = [0 for _ in range(13)]
    sum2 = [0 for _ in range(13)]
    for d in range(13):
        for i in range(16):
            for j in range(512):
                sum1[d] = sum1[d] + GLRLl[d][i][j] * ((i + 1) * (i + 1))
                sum2[d] = sum2[d] + GLRLl[d][i][j]
    for d in range(13):
        hglre = hglre + sum1[d] / sum2[d]
    hglre /= 13
    return hglre

def GLN(data, GLRLl):
    gln = 0
    sum1 = [0 for _ in range(13)]
    sum2 = [0 for _ in range(13)]
    for d in range(13):
        for i in range(16):
            p = 0
            for j in range(512):
                p = p + GLRLl[d][i][j]
                sum2[d] = sum2[d] + GLRLl[d][i][j]
            sum1[d] = sum1[d] + p**2
    for d in range(13):
        gln = gln + sum1[d] / sum2[d]
    gln /= 13
    return gln

def RLN(data, GLRLl):
    rln = 0
    sum1 = [0 for _ in range(13)]
    sum2 = [0 for _ in range(13)]
    for d in range(13):
        for j in range(512):
            p = 0
            for i in range(16):
                p = p + GLRLl[d][i][j]
                sum2[d] = sum2[d] + GLRLl[d][i][j]
            sum1[d] = sum1[d] + p**2
    for d in range(13):
        rln = rln + sum1[d] / sum2[d]
    rln /= 13
    return rln

def RP(data, GLRLl):
    np = 0; rp = 0
    for i in range(len(data)):
        for j in range(512):
            for k in range(512):
                if data[i][j][k] > -1024:
                    np += data[i][j][k]
    for d in range(13):
        for i in range(16):
            for j in range(512):
                rp += GLRLl[d][i][j]
    rp /= np
    rp /= 13
    return rp