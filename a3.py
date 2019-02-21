import pandas as pd
import numpy as np
from pandas import Series,DataFrame
import math
import scipy
#import pydotplus
import graphviz#绘图库
from sklearn.tree import export_graphviz#用于画决策树图
from sklearn.model_selection import train_test_split#实现对训练测试数据的打乱和比例分配
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score#用于计算准确率
np.set_printoptions(suppress=True)#设置不用科学计数输出
import matplotlib.pyplot as plt


df=pd.read_csv('job.csv',encoding='gbk')
#print(df1.dtypes) #查看各行的数据格式
#print(df1.shape)
#print(df1.head())

#例如，希望对名字为k2的列进行去重，
#df1.drop_duplicates(['k2'])
    print("-------")
#Pandas提供了duplicated、Index.duplicated、drop_duplicates函数来标记及删除重复记录
#将相同的工作进行筛选，筛选结果为df2
    df2=df1.drop_duplicates(['post','company','city','education','experience'])
#df2=df1.drop_duplicates(['post','size','type','city','direction','education','experience'])
#print(df2.dtypes)
#print(df2.shape)
#print(df2.head())

#df2.loc[(df2[""]>100)]  #筛选语句

#决策树的实现
#特征值：公司规模（size），公司性质（type），城市（city），学历（education），工作方向（classify），工资（ave)
#预测值：经验要求（experience）
    kn=df2.loc[:, ['size', 'type','city','education','classify','ave','experience']]
#print(kn.head())
#对特征值进行处理
#size：20,21,51，101，301,500->(20,21,51),(101,301),500:1,2,3
#type:民营/私企，股份制，国企，合资，上市公司，事业单位，外商独资,其他：1,2,3,4,5,6,7,8
#city：北京，上海，重庆，天津，广州，深圳：1，2,3,4,5,6
#education：本科，初中，大专，高职，高中，其他，硕士，职高，中技，中职，中专->本科，(大专，高职），硕士，本科以下（初中，高中），中等学校（中技，中职，中专，职高）,其他:1,2,3,4,5,6
#clssify:编程开发，测试，云平台，界面设计，游戏，游戏，数据分析，其他->1,2,3,4,5,6,7,8
#salary：根据ave设定.。面试，5000以下，5000-15000,15000-50000,50000以上：1,2,3,4,5

#a[a>0]=-a 表示将a中所有大于0的数转化为负值
    kn1=kn.replace({"北京":1,"上海":2,"重庆":3,"天津":4,"广州":5,"深圳":6})
    kn1=kn1.replace({"民营/私企":1,"股份制":2,"国企":3,"合资":4,"上市公司":5,"事业单位":6,"外商独资":7,"其他":8})
    kn1=kn1.replace({"编程开发":1,"测试":2,"云平台":3,"界面设计":4,"游戏":5,"互联网":6,"数据分析":7,"其他":8})
    kn1["sizes"]=0
    def number_to_size(number):
        if number <100:
           return 1
        elif number ==500:
            return 3
        else:
            return 2
    kn1["sizes"] = kn["size"].map(number_to_size)
    kn1["salary"]=0
    def number_to_salary(number):
        if number ==0:
            return 1
        elif number>0&number<=5000:
            return 2
        elif number>5000&number<=15000:
            return 3
        elif number>15000&number<=50000:
            return 4
        else:
            return 5
    kn1["salary"] = kn["ave"].map(number_to_salary)

#之前其他都换为了8，现在需要换回来
    kn1 = kn1.replace({'education':8},'其他')
    kn1["edu"]=0
    education_to_edu = {
    '本科':1,
    '高职':2,
    '大专':2,
    '硕士':3,
    '初中':4,
    '高中':4,
    '中技':5,
    '中职':5,
    '中专':5,
    '职高':5,
    '其他':6 }
    kn1['edu'] = kn['education'].map(education_to_edu)

    kn1["expr"]=0
    education_to_edu = {
    '经验应届生':1,
    '经验在读':2,
    '经验1年':3,
    '经验2年':4,
    '经验3年':5,
    '经验4年':6,
    '经验5年':6,
    '经验6年':6,
    '经验7年':6,
    '经验8年':6,
    '经验9年': 6,
    '经验10年': 6,
}
    kn1['expr'] = kn['experience'].map(education_to_edu)
#print(kn1.dtypes)

#提取特征值
    features=kn1.loc[:, ['sizes', 'type','city','edu','classify','salary']]
    print(features.dtypes)
    targets=kn1.loc[:,['expr']]
    print(targets.dtypes)

    features_train,features_test,targets_train,targets_test=train_test_split(features,targets,test_size=0.3,random_state=20)
    number_train=len(features_train)
    number_test=len(features_test)
#print(features_train)
#print(features_test)

#训练模型
#model=DecisionTreeClassifier()#默认基尼系数
    model=DecisionTreeClassifier(criterion="entropy")
    model.fit(features_train,targets_train)

    pre=model.predict(features_test)
    dat=targets_test.values.flatten()
    print(pre)
    print(dat)
    rate=accuracy_score(dat,pre)

    print(rate)#计算真确值

#model.predict([])#可以进行预测
    predict=model.predict([[a,b,c,d,e,f]])
    print(predict)

#画决策树
    image=export_graphviz(model,out_file=None,feature_names=["sizes","type","city","edu","classify","salary"],class_names=["经验在读","经验应届生","经验1年","经验2年","经验3年","三年以上"])
    print(image)
    graphviz.Source(image)

    return predict,number_train,number_test,rate


