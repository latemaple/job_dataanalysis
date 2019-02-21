import pandas as pd
import numpy as np
from pandas import Series,DataFrame
import matplotlib.pyplot as plt
# 设置全局字体
plt.rcParams['font.sans-serif'] = ['SimHei']
np.set_printoptions(suppress=True)#设置不用科学计数输出

# 设置全局字体，数据可视化的需要


def p1(df2):
    fig1 = plt.figure(1,facecolor = 'white')#设置视图画布1

#城市分布
    ax1=fig1.add_subplot(221)
    ax1.set_title('城市分布',color='red')
    x1 = df2.city.value_counts().values    #各城市的数量
    labels = list(df2.city.value_counts().index[:6])#各块的标签
    explode = tuple([0.1,0.1,0.1,0.1,0.1,0.1])
    plt.pie(x1,explode=explode,labels=labels,autopct='%1.1f%%',textprops={'color':'black'})
    plt.axis('equal')#显示为等比例圆形

    print(df2.dtypes)

#公司类型
    ax2 = fig1.add_subplot(222)
    ax2.set_title('公司类型',color='red')
    x2 = df2.type.value_counts().values    #各公司类型的数量
    labels2 = list(df2.type.value_counts().index[:8])#各块的标签
    print(x2)
    print(labels2)
    explode = tuple([0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1])
    plt.pie(x2,explode=explode,labels=labels2,autopct='%1.1f%%',textprops={'color':'black'})
    plt.axis('equal')#显示为等比例圆形

#经验
    df2=df2.replace({"经验在读":"经验应届生","经验4年":"三年以上","经验5年":"三年以上","经验6年":"三年以上","经验7年":"三年以上","经验8年":"三年以上","经验9年":"三年以上","经验10年":"三年以上"})
    ax3 = fig1.add_subplot(223)
    ax3.set_title('经验要求',color='red')
    x3 = df2.experience.value_counts().values
    labels3 = list(df2.experience.value_counts().index[:5])#各块的标签
    print(x3)
    print(labels3)
    explode = tuple([0.1,0.1,0.1,0.1,0.1])
#plt.pie(x3,labels=labels3,autopct='%1.1f%%',textprops={'color':'black'})
    plt.pie(x3,explode=explode,labels=labels3,autopct='%1.1f%%',textprops={'color':'black'})
    plt.axis('equal')#显示为等比例圆形


#工作方向
    ax4 = fig1.add_subplot(224)
    ax4.set_title('工作方向',color='red')
    x4 = df2.classify.value_counts().values    #各公司类型的数量
    labels4 = list(df2.classify.value_counts().index[:8])#各块的标签
    print(x4)
    print(labels4)
#explode = tuple([0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1])
    plt.pie(x4,labels=labels4,autopct='%1.1f%%',textprops={'color':'black'})
#plt.pie(x3,explode=explode,labels=labels3,autopct='%1.1f%%',textprops={'color':'yellow'})
    plt.axis('equal')#显示为等比例圆形

    plt.savefig("vis1.png")
 #   plt.show()#显示图片
    plt.close()

def p2(df2):
    fig2 = plt.figure(2,facecolor = 'gray')#设置视图画布2
#学历要求
    ax5 = fig2.add_subplot(111)
    ax5.set_title('学历需求',color='black')
    x5 = df2.education.value_counts().values    #各公司类型的数量
    labels5 = list(df2.education.value_counts().index[:11])#各块的标签
    print(x5)
    print(labels5)
    plt.bar(left=labels5,height=x5,color='gray',width=0.8)
    plt.xlabel('学历类别')
    plt.ylabel('人数')
    plt.savefig("vis2.png")
 #   plt.show()  # 显示图片
    plt.close()


#工资df3
#各个工作方向的平均工资
def p3(df2):
    df3=df2.loc[:, ['classify','ave']]
    print(df3.head())
    cla1=int(df3.loc[(df3["classify"]=="编程开发")].ave.mean())
    cla2=int(df3.loc[(df3["classify"]=="测试")].ave.mean())
    cla3=int(df3.loc[(df3["classify"]=="云平台")].ave.mean())
    cla4=int(df3.loc[(df3["classify"]=="界面设计")].ave.mean())
    cla5=int(df3.loc[(df3["classify"]=="游戏")].ave.mean())
    cla6=int(df3.loc[(df3["classify"]=="互联网")].ave.mean())
    cla7=int(df3.loc[(df3["classify"]=="数据分析")].ave.mean())
    cla8=int(df3.loc[(df3["classify"]=="其他")].ave.mean())

    cla=[cla1,cla2,cla3,cla4,cla5,cla6,cla7,cla8]
    print("------")
#print(cla)
    fig3 = plt.figure(3,facecolor = 'gray')#设置视图画布2
    ax6 = fig3.add_subplot(111)
    ax6.set_title('平均工资',color='black')
    x6 = cla    #各方向的平均工资
    labels6 = ["编程开发","测试","云平台","界面设计","游戏","互联网","数据分析","其他"]#各块的标签
    print(x6)
    print(labels6)
    plt.bar(left=labels6,height=x6,color='gray',width=0.8)
    plt.xlabel('工作方向')
    plt.ylabel('平均工资')
    plt.savefig("vis3.png")
  #  plt.show()  # 显示图片
    plt.close()

def p4(df1):
#排名靠前的工作岗位#
    print("----------------------------------------------")#对数据开始处理
#找出重复的数据，df4是series类型，是一维的
    df4=df1.duplicated(['post','company','city','education','experience'])
#print(df4.head(20))
#print(df4.index)
#print(df4.values)

#将判断结果存入dataframe
    df5 = DataFrame(df4.values) #创建DataFrame对象
    df5.columns = ['judge'] #修改列名，[]中内容数量需要与dataframe中相同

#将原表和判断表连接
    df1_5=pd.concat([df1,df5], axis=1)#两个表水平连接
#print(df1_5.shape)
#print(df1_5.head())
#print(df1_5.dtypes)
#对重复工作的权重进行显示
    df6=df1_5.loc[(df1_5["judge"])]  #筛选语句，筛选出重复出现的工作
#print(df1.city.value_counts()) #方法用于统计各值出现的频率：
#查看重复的工作中
    df7=df6.post.value_counts()#功能：返回包含唯一值计数的对象。结果对象将按降序排列，以便第一个元素是最常出现的元素。 不包括默认的NA值。
    print(df7.head(20))
    print("---------")
    x7 = list(df7.index[3:13])#series的标签
    labels7 =df7.values[3:13]#values:保存数组
    print(x7)
    print(labels7)

    fig4 = plt.figure(4,facecolor = 'gray')#设置视图画布
    ax7 = fig4.add_subplot(122)
    ax7.set_title('排名靠前的工作岗位',color='black')
    plt.bar(left=0,bottom=x7,width=labels7,color='gray',height=0.5,orientation="horizontal")
    plt.xlabel('数量')
    plt.ylabel('工作岗位名称')
    plt.savefig("vis4.png")
 #   plt.show()  # 显示图片
    plt.close()

def save():
    df1 = pd.read_csv('E:\data\day16.csv', encoding='gbk')

    print(df1.dtypes)  # 查看各行的数据格式
    print(df1.shape)
    # print(df1.head())

    # 例如，希望对名字为k2的列进行去重，
    # df1.drop_duplicates(['k2'])
    print("-------")
    # Pandas提供了duplicated、Index.duplicated、drop_duplicates函数来标记及删除重复记录
    # 将相同的工作进行筛选，筛选结果为df2
    df2 = df1.drop_duplicates(['post', 'company', 'city', 'education', 'experience'])
    print(df2.dtypes)
    print(df2.shape)
    # print(df2.head())

    # df2.loc[(df2[""]>100)]  #筛选语句

    # 再用count()来看一下统计出来的城市数量
    number = df2.city.value_counts().count()
    print(number)
    nlist = df2.city.value_counts()
    print(nlist)
    p1(df2)
    p2(df2)
    p3(df2)
    p4(df1)

    return 1

if __name__ == '__main__':
    save()

