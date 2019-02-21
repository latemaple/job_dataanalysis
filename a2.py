import pandas as pd
import numpy as np
from pandas import Series,DataFrame
import math
np.set_printoptions(suppress=True)#设置不用科学计数输出
import matplotlib.pyplot as plt
# 设置全局字体
plt.rcParams['font.sans-serif'] = ['SimHei']
#   location1:  E:\data\day16.csv
#df1=pd.read_csv('E:\data\day16.csv',encoding='gbk')#########################

#print(df1.dtypes) #查看各行的数据格式
#print(df1.shape)

#print("-----------")
#通过每天工作总量，实现对未来几天的工作总量的数量预测。
#灰色预测实现
#初始化x0[]

#df12=df1.loc[df1["classify"]=="游戏"]#用于筛选各个分类方向

def location(loc):
    df1 = pd.read_csv(loc, encoding='gbk')
    return df1


def start1(loc):
    df1=location(loc)

    x0 = [0 for x in range(0, 16)]  # 定义数组初始化
    for i in range(0, 16):
        x0[i] = df1.loc[df1["day"] == i + 1].shape[0]
    #  x0[i]=df12.loc[df12["day"]==(i+1)].shape[0]
    print("x0:", x0)
    return x0

def start2(loc):
    df1=location(loc)
    df12=df1.loc[df1["classify"]=="游戏"]#用于筛选各个分类方向
    x0 = [0 for x in range(0, 16)]  # 定义数组初始化
    for i in range(0, 16):
        x0[i]=df12.loc[df12["day"]==(i+1)].shape[0]
    print("x0:", x0)
    return x0

def start3(loc):
    df1=location(loc)
    df13=df1.loc[df1["classify"]=="编程开发"]#用于筛选各个分类方向
    x0 = [0 for x in range(0, 16)]  # 定义数组初始化
    for i in range(0, 16):
        x0[i]=df13.loc[df13["day"]==(i+1)].shape[0]
    print("x0:", x0)
    return x0

def start4(loc):
    df1=location(loc)
    df14=df1.loc[df1["classify"]=="测试"]#用于筛选各个分类方向
    x0 = [0 for x in range(0, 16)]  # 定义数组初始化
    for i in range(0, 16):
        x0[i]=df14.loc[df14["day"]==(i+1)].shape[0]
    print("x0:", x0)
    return x0

def start5(loc):
    df1=location(loc)
    df15=df1.loc[df1["classify"]=="界面设计"]#用于筛选各个分类方向
    x0 = [0 for x in range(0, 16)]  # 定义数组初始化
    for i in range(0, 16):
        x0[i]=df15.loc[df15["day"]==(i+1)].shape[0]
    print("x0:", x0)
    return x0

def start6(loc):
    df1=location(loc)
    df16=df1.loc[df1["classify"]=="互联网"]#用于筛选各个分类方向
    x0 = [0 for x in range(0, 16)]  # 定义数组初始化
    for i in range(0, 16):
        x0[i]=df16.loc[df16["day"]==(i+1)].shape[0]
    print("x0:", x0)
    return x0

def start7(loc):
    df1=location(loc)
    df17=df1.loc[df1["classify"]=="云平台"]#用于筛选各个分类方向
    x0 = [0 for x in range(0, 16)]  # 定义数组初始化
    for i in range(0, 16):
        x0[i]=df17.loc[df17["day"]==(i+1)].shape[0]
    print("x0:", x0)
    return x0

def start8(loc):
    df1=location(loc)
    df18=df1.loc[df1["classify"]=="其他"]#用于筛选各个分类方向
    x0 = [0 for x in range(0, 16)]  # 定义数组初始化
    for i in range(0, 16):
        x0[i]=df18.loc[df18["day"]==(i+1)].shape[0]
    print("x0:", x0)
    return x0


def test_start(x0):
#级比检测，确保其可以使用灰色模型方法建模
    n=len(x0)   #总个数
    m1=math.exp(-2/(n+1)) #最小值
    m2=math.exp(2/(n+2))  #最大值
    print(m1,m2)
    p=[0 for x in range(15)]
    for i in range(15):
        p[i]=x0[i]/x0[i+1]
        if (p[i]<m1 or p[i]>m2):
            print("超出范围")
            break
        else:
            print(i+1,"符合")

    if(i==14):
        return "符合"
    else:
        return "不符合"

'''
def start_change(rp,x0):
    print(rp)
    c=0
    if rp=='不符合':
        x1=[0]*len(x0)
        print("mm不符合")
        while (rp=='不符合' or c<1001):
            for i in range(len(x0)):
                x1[i]=x0[i]+c
                c=c+100
                rp=test_start(x1)
        if rp=='符合':
            return rp,c-100,x1
        else:
            rp='不符合'
            return rp,c,x1

    else:
        print("mm符合")
        return p,c,x0

'''

def matx(x0):
#计算累加值,形成累加生成列x1[]
    x1=[0 for x in range(0,16)]
    for i in range(0,16):
        sum=0
        for j in range(i+1):
            sum=x0[j]+sum
        x1[i]=sum
    print("x1",x1)

#构造数据矩阵B
#构造list存储B中的第一列
    b=[0 for x in range(0,15)]
    for i in range(15):
        b[i]=(-1/2)*(x1[i]+x1[i+1])
    print(b)
    print(b[1])
    B1=np.array([b]).reshape(15,1)
    B2=np.ones((15,1))
    print(B1)
    print(B2)
    B=np.concatenate([B1,B2],axis=1)#将B1,B2组成一个矩阵
    print(B)

#构建矩阵Y
    Y=np.array([x0[1],x0[2],x0[3],x0[4],x0[5],x0[6],x0[7],x0[8],x0[9],x0[10],x0[11],x0[12],x0[13],x0[14],x0[15]]).reshape(15,1)
#print(Y)

#矩阵乘法np.dot(a,b)
#矩阵的转置np.transpose(a) 或者a.T
#numpy.linalg.inv(a) # 求逆
#计算u,a,b,
    u=(np.linalg.inv(np.dot(B.T,B)).dot(B.T)).dot(Y)
    print(u)
    a=u[0,0]
    b=u[1,0]
    print("a,b:",a,b)
    return a,b


#构建模型       x^(k+1)=(x0[1]-b/a)math.exp(-a*k)+b/a,k=1,2,3-------【k+1】可以理解为预测的数，k为预测的第几个数-1
#定义预测列表x3[]
def pre(x0,a,b):
    x3=[0 for x in range(0,19)]
    x3[0]=x0[0]
    for i in range(1,19):
        x3[i]=(x0[0]-b/a)*(math.exp((-a)*i))+b/a
    print("x3:",x3)


#最后的预测结果##########检测结果
    x4=[0 for x in range(0,19)]
    x4[0]=x3[0]
    for i in range(1,19):
        x4[i]=int(x3[i]-x3[i-1])
    print("原始数据x0:",x0)
    print("预测数据x4:",x4)

    return x4





#计算相对残差,相对残差都小于0.1符合要求
def test_end(x0,x4):
    x6=[0 for x in range(0,16)]
    for i in range(16):
        x6[i]=round(abs((x0[i]-x4[i])/x0[i]),5)
    print("相对残差x6:",x6)
    ave=round(np.mean(x6),5)
    print("ave",ave)
    return ave,x6


#可视化
def allshow(x0,x4):

 #   sx=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
#########
    names=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]


    sx = range(len(names))
##########
    sy1=x0
    sy2=x4
    plt.plot(sx,sy1)
    plt.plot(sx,sy2)
    plt.title('灰色预测结果')
    plt.plot(sx, sy1, label='实际值')
    plt.plot(sx, sy2, label='预测值')

    plt.xlabel("日期的序号表示")
    plt.ylabel("工作岗位数据量")
    plt.legend()
    ##################
    plt.xticks(sx, names, rotation=45)
    ###################
    image=plt

    return image


if __name__ == '__main__':

    x0=start1()
    p=test_start(x0)
    print(p)
    a,b=matx(x0)
    x4=pre(x0,a,b)
    ave=test_end(x0,x4)
    allshow()

