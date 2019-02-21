import pandas as pd
import numpy as np
import tkinter as tk
import matplotlib.pyplot as plt
from tkinter import scrolledtext        # 导入滚动文本框的模块
from tkinter.messagebox import showinfo
import a1
import a2
import a3


window=tk.Tk()
window.title('结果展示')
window.geometry('700x500')

label=tk.Label(window,text='工作岗位分析预测结果展示',font=('宋体',18),width=30,height=5)
label.pack()

#全局变量中定义图片
#img1= Image.open('vis1.png')  # 打开图片
#image_file1 = ImageTk.PhotoImage(img1)  # 用PIL模块的PhotoImage打开

a=a1.save()
image_file0 = tk.PhotoImage(file="0.png")
image_file1 = tk.PhotoImage(file="vis1.png")
image_file2 = tk.PhotoImage(file="vis2.png")
image_file3 = tk.PhotoImage(file="vis3.png")
image_file4 = tk.PhotoImage(file="vis4.png")

def show1():
    window1 = tk.Toplevel(window)
    window1.title('工作岗位数据可视化')
    window1.geometry('800x475')
    canvas=tk.Canvas(window1,bg='gray',height=475,width=600)
    images0 = canvas.create_image(100, 60, anchor='nw', image=image_file0)  # 图片需要在全局变量中
    canvas.pack(side='left')
    label1 = tk.Label(window1, text='岗位数量可视化', font=('宋体', 18), width=30, height=5).pack()

    def picture1():
       # img = Image.open('vis1.png')  # 打开图片
       # image_file = ImageTk.PhotoImage(img)  # 用PIL模块的PhotoImage打开
       # image_file = tk.PhotoImage(file="vis1.png")
        images1 = canvas.create_image(0,0, anchor='nw', image=image_file1)#图片需要在全局变量中
        canvas.pack()
     #   canvas.pack(side='left')
    bu1 = tk.Button(window1, text='各方向数量比例', width=22, height=3,command=picture1).pack()

    def picture2():
        images2 = canvas.create_image(0, 0, anchor='nw', image=image_file2)  # 图片需要在全局变量中
        canvas.pack()
    bu2 = tk.Button(window1, text='学历需求数量', width=22, height=3,command=picture2).pack()

    def picture3():
        images3 = canvas.create_image(0, 0, anchor='nw', image=image_file3)  # 图片需要在全局变量中
        canvas.pack()
    bu3 = tk.Button(window1, text='各岗位方向平均工资', width=22, height=3,command=picture3).pack()

    def picture4():
        images4 = canvas.create_image(0, 0, anchor='nw', image=image_file4)  # 图片需要在全局变量中
        canvas.pack()
    bu4 = tk.Button(window1, text='工作岗位需求数量', width=22, height=3,command=picture4).pack()


def show2():
    window2 = tk.Toplevel(window)
    window2.title('工作岗位数量预测')
    window2.geometry('800x475')

    labelx0=tk.Label(window2,text='实际数据',font=('宋体',15),width=20,height=2).place(x=15,y=90)
    tx0=scrolledtext.ScrolledText(window2,font=('宋体', 14),width=15,height=9)
    tx0.place(x=50,y=130)
    labelx4 = tk.Label(window2, text='检验数据', font=('宋体', 15), width=20, height=2).place(x=215, y=90)
    tx4=scrolledtext.ScrolledText(window2,font=('宋体', 14),width=15,height=9)
    tx4.place(x=250,y=130)
    labelx6 = tk.Label(window2, text='相对残差', font=('宋体', 15), width=20, height=2).place(x=415, y=90)
    tx6=scrolledtext.ScrolledText(window2,font=('宋体', 14),width=15,height=9)
    tx6.place(x=450,y=130)



    label1 = tk.Label(window2, text='岗位数量预测', font=('宋体', 20), width=30, height=3).place(x=130,y=6)
    label2 = tk.Label(window2, text='级比检测:', font=('宋体', 13), width=8, height=2).place(x=100,y=370)
    t1=tk.Text(window2,font=('宋体', 13),width=10,height=1)
    t1.place(x=200,y=380)
    label3 = tk.Label(window2, text='平均残差:', font=('宋体', 13), width=8, height=2).place(x=100,y=410)
    t2=tk.Text(window2,font=('宋体', 13),width=10,height=1)
    t2.place(x=200,y=420)

    label4 = tk.Label(window2, text='平移变换c:', font=('宋体', 13), width=15, height=2).place(x=330,y=370)
    tc=tk.Text(window2,font=('宋体', 13),width=10,height=1)
    tc.place(x=470,y=380)

    label5 = tk.Label(window2, text='变换后级比检测：', font=('宋体', 13), width=15, height=2).place(x=330,y=410)
    t3=tk.Text(window2,font=('宋体', 13),width=10,height=1)
    t3.place(x=470,y=420)

    labelp = tk.Label(window2, text='未来三天预测结果：', font=('宋体', 13), width=25, height=2).place(x=60, y=330)
    tp = tk.Text(window2, font=('宋体', 13), width=33, height=1)
    tp.place(x=250, y=340)



    global location
    location=''
    ################实现选择#######################
    def choose():
        windowch = tk.Toplevel(window2)
        windowch.title('数据选择')
        windowch.geometry('500x100')
        labelch = tk.Label(windowch, text='文件地址:', font=('宋体', 13), width=15, height=2).place(x=70, y=20)
        tch = tk.Entry(windowch,width=20)
        tch.place(x=180,y=30)

        def true():
           # global location ###########通过global设置全局变量
            global location
            location = tch.get()
            print(location)
            try:
               pd.read_csv(location,encoding='gbk')
            except Exception as e:
                location=''

        busure = tk.Button(windowch, text='确定', width=15, height=1, command=true).place(x=300, y=55)

    ###############################################
   # buchoose = tk.Button(window2, text='数据源', width=15, height=1,command=choose).place(x=1, y=1)

###########用菜单实现

    menubar = tk.Menu(window2)
    filemenu=tk.Menu(menubar)
    menubar.add_cascade(label='选项',menu=filemenu)
    filemenu.add_command(label='数据源', command=choose)
 #   filemenu.add_command(label='退出', command=window.quit)#全部退出
   # menubar.add_command(label='数据源', command=choose)
    window2.config(menu=menubar)
################################

    def text1():
        t1.delete(0.0, tk.END)  # 删除所有值
        t2.delete(0.0, tk.END) # 删除所有值
        tx0.delete(0.0, tk.END)  # 删除所有值
        tx4.delete(0.0, tk.END)  # 删除所有值
        tx6.delete(0.0, tk.END)  # 删除所有值
        t3.delete(0.0, tk.END)  # 删除所有值
        tc.delete(0.0, tk.END)  # 删除所有值
        tp.delete(0.0, tk.END)
        #先判断地址是否成功，后输出实际数据
        print(location)
        if location=='':
            tk.messagebox.showinfo(title='error', message='请输入地址')
            print("输入地址")
        else:
            x0=a2.start1(location)
            for i in range(len(x0)):
                tx0.insert('insert',i+1)
                tx0.insert('insert',':')
                tx0.insert('insert',x0[i])
                tx0.insert('insert','\n')
        #级比检测
            x0 = a2.start1(location)
            p=a2.test_start(x0)
            t1.insert('insert',p)

        # 平移变换#################
            n = 0
            while n < 10 and p == '不符合':
                c = 100
                for i in range(len(x0)):
                    x0[i] = x0[i] + c
                n = n + 1
                p = a2.test_start(x0)
            print("nnnnnnnn:", n)

            c1 = 100 * n
            tc.insert('insert', c1)
            t3.insert('insert', p)

        #结果检测
            a, b = a2.matx(x0)
            x4 = a2.pre(x0, a, b)
            ave,x6 = a2.test_end(x0,x4)
            t2.insert('insert', ave)
        #输出预测数据
            for i in range(0,len(x4)-3):
                tx4.insert('insert',i+1)
                tx4.insert('insert',':')
                tx4.insert('insert',x4[i])
                tx4.insert('insert','\n')
            for i in range(len(x6)):
                tx6.insert('insert', i+1)
                tx6.insert('insert', ':')
                tx6.insert('insert', x6[i])
                tx6.insert('insert', '\n')
            for i in range(len(x4)-3,len(x4)):
                tp.insert('insert',x4[i])
                tp.insert('insert','  ')

            x0_1 = [0] * 19
            for i in range(16):
                x0_1[i] = x0[i]
            for i in range(16, 19):
                x0_1[i] = x0[15]

            print("x0_1", x0_1)
            print(x4)

            image = a2.allshow(x0_1, x4)
            image.show()

    bu1 = tk.Button(window2, text='总数量预测', width=20, height=2,command=text1).place(x=635,y=10)

    def text2():
        t1.delete(0.0, tk.END)  # 删除所有值
        t2.delete(0.0, tk.END)  # 删除所有值
        tx0.delete(0.0, tk.END)  # 删除所有值
        tx4.delete(0.0, tk.END)  # 删除所有值
        tx6.delete(0.0, tk.END)  # 删除所有值
        t3.delete(0.0, tk.END)  # 删除所有值
        tc.delete(0.0, tk.END)  # 删除所有值
        tp.delete(0.0, tk.END)
        #先判断地址是否成功，后输出实际数据
        print(location)
        if location=='':
            tk.messagebox.showinfo(title='error', message='请输入地址')
            print("输入地址")

        else:
            x0 = a2.start2(location)
            for i in range(len(x0)):
                tx0.insert('insert', i+1)
                tx0.insert('insert', ':')
                tx0.insert('insert', x0[i])
                tx0.insert('insert', '\n')
        # 级比检测
       # x0 = a2.start2()
            p = a2.test_start(x0)
            t1.insert('insert', p)

        # 平移变换#################
            n = 0
            while n < 10 and p == '不符合':
                c = 100
                for i in range(len(x0)):
                    x0[i] = x0[i] + c
                n = n + 1
                p = a2.test_start(x0)
            print("nnnnnnnn:", n)

            c1 = 100 * n
            tc.insert('insert', c1)
            t3.insert('insert', p)

        # 结果检测
            a, b = a2.matx(x0)
            x4 = a2.pre(x0, a, b)
            ave, x6 = a2.test_end(x0, x4)
            t2.insert('insert', ave)
        # 输出预测数据
            for i in range(0,len(x4)-3):
                tx4.insert('insert', i+1)
                tx4.insert('insert', ':')
                tx4.insert('insert', x4[i])
                tx4.insert('insert', '\n')
        #输出残差值
            for i in range(len(x6)):
                tx6.insert('insert', i+1)
                tx6.insert('insert', ':')
                tx6.insert('insert', x6[i])
                tx6.insert('insert', '\n')
            for i in range(len(x4)-3,len(x4)):
                tp.insert('insert',x4[i])
                tp.insert('insert','  ')

            x0_1 = [0] * 19
            for i in range(16):
                x0_1[i] = x0[i]
            for i in range(16, 19):
                x0_1[i] = x0[15]

            print("x0_1", x0_1)
            print(x4)

            image = a2.allshow(x0_1, x4)
            image.show()

    bu2 = tk.Button(window2, text='游戏方向预测', width=20, height=2,command=text2).place(x=635,y=60)

    def text3():
        t1.delete(0.0, tk.END)  # 删除所有值
        t2.delete(0.0, tk.END)  # 删除所有值
        tx0.delete(0.0, tk.END)  # 删除所有值
        tx4.delete(0.0, tk.END)  # 删除所有值
        tx6.delete(0.0, tk.END)  # 删除所有值
        t3.delete(0.0, tk.END)  # 删除所有值
        tc.delete(0.0, tk.END)  # 删除所有值
        tp.delete(0.0, tk.END)
        #先判断地址是否成功，后输出实际数据
        print(location)
        if location=='':
            tk.messagebox.showinfo(title='error', message='请输入地址')
            print("输入地址")


        else:
            x0 = a2.start3(location)
            for i in range(len(x0)):
                tx0.insert('insert', i+1)
                tx0.insert('insert', ':')
                tx0.insert('insert', x0[i])
                tx0.insert('insert', '\n')
        # 级比检测
       # x0 = a2.start2()
            p = a2.test_start(x0)
            t1.insert('insert', p)

        # 平移变换#################
            n = 0
            while n < 10 and p == '不符合':
                c = 100
                for i in range(len(x0)):
                    x0[i] = x0[i] + c
                n = n + 1
                p = a2.test_start(x0)
            print("nnnnnnnn:", n)

            c1 = 100 * n
            tc.insert('insert', c1)
            t3.insert('insert', p)


        # 结果检测
            a, b = a2.matx(x0)
            x4 = a2.pre(x0, a, b)
            ave, x6 = a2.test_end(x0, x4)
            t2.insert('insert', ave)
        # 输出预测数据
            for i in range(0,len(x4)-3):
                tx4.insert('insert', i+1)
                tx4.insert('insert', ':')
                tx4.insert('insert', x4[i])
                tx4.insert('insert', '\n')
        #输出残差值
            for i in range(len(x6)):
                tx6.insert('insert', i+1)
                tx6.insert('insert', ':')
                tx6.insert('insert', x6[i])
                tx6.insert('insert', '\n')
            for i in range(len(x4) - 3, len(x4)):
                tp.insert('insert', x4[i])
                tp.insert('insert', '  ')


            x0_1 = [0] * 19
            for i in range(16):
                x0_1[i] = x0[i]
            for i in range(16, 19):
                x0_1[i] = x0[15]

            print("x0_1", x0_1)
            print(x4)

            image = a2.allshow(x0_1, x4)
            image.show()

    bu3 = tk.Button(window2, text='编程开发方向预测', width=20, height=2,command=text3).place(x=635, y=110)

    def text4():
        t1.delete(0.0, tk.END)  # 删除所有值
        t2.delete(0.0, tk.END)  # 删除所有值
        tx0.delete(0.0, tk.END)  # 删除所有值
        tx4.delete(0.0, tk.END)  # 删除所有值
        tx6.delete(0.0, tk.END)  # 删除所有值
        t3.delete(0.0, tk.END)  # 删除所有值
        tc.delete(0.0, tk.END)  # 删除所有值
        tp.delete(0.0, tk.END)
        #先判断地址是否成功，后输出实际数据
        print(location)
        if location=='':
            tk.messagebox.showinfo(title='error', message='请输入地址')
            print("输入地址")


        else:
            x0 = a2.start4(location)
            for i in range(len(x0)):
                tx0.insert('insert', i+1)
                tx0.insert('insert', ':')
                tx0.insert('insert', x0[i])
                tx0.insert('insert', '\n')
        # 级比检测
       # x0 = a2.start2()
            p = a2.test_start(x0)
            t1.insert('insert', p)


        #平移变换#################
            n=0
            while n<10 and p=='不符合':
                c=100
                for i in range(len(x0)):
                    x0[i]=x0[i]+c
                n=n+1
                p=a2.test_start(x0)
            print("nnnnnnnn:",n)

            c1=100*n
            tc.insert('insert',c1)
            t3.insert('insert',p)



        # 结果检测
            a, b = a2.matx(x0)
            x4 = a2.pre(x0, a, b)
        #对结果变换
            for i in range(len(x4)):
                x4[i]=x4[i]-c1
            for i in range(len(x0)):#画图前将x0回到原始数据
                x0[i]=x0[i]-c1

            ave, x6 = a2.test_end(x0, x4)
            t2.insert('insert', ave)

        # 输出预测数据
            for i in range(0,len(x4)-3):
                tx4.insert('insert', i+1)
                tx4.insert('insert', ':')
                tx4.insert('insert', x4[i])
                tx4.insert('insert', '\n')
        #输出残差值
            for i in range(len(x6)):
                tx6.insert('insert', i+1)
                tx6.insert('insert', ':')
                tx6.insert('insert', x6[i])
                tx6.insert('insert', '\n')
            for i in range(len(x4) - 3, len(x4)):
                tp.insert('insert', x4[i])
                tp.insert('insert', '  ')


            x0_1=[0]*19
            for i in range(16):
                x0_1[i]=x0[i]
            for i in range(16,19):
                x0_1[i]=x0[15]

            print("x0_1",x0_1)
            print(x4)

            image = a2.allshow(x0_1, x4)
            image.show()

    bu4 = tk.Button(window2, text='测试方向预测', width=20, height=2,command=text4).place(x=635, y=160)

    def text5():
        t1.delete(0.0, tk.END)  # 删除所有值
        t2.delete(0.0, tk.END)  # 删除所有值
        tx0.delete(0.0, tk.END)  # 删除所有值
        tx4.delete(0.0, tk.END)  # 删除所有值
        tx6.delete(0.0, tk.END)  # 删除所有值
        t3.delete(0.0, tk.END)  # 删除所有值
        tc.delete(0.0, tk.END)  # 删除所有值
        tp.delete(0.0, tk.END)
        #先判断地址是否成功，后输出实际数据
        print(location)
        if location=='':
            tk.messagebox.showinfo(title='error', message='请输入地址')
            print("输入地址")


        else:
            x0 = a2.start5(location)
            for i in range(len(x0)):
                tx0.insert('insert', i+1)
                tx0.insert('insert', ':')
                tx0.insert('insert', x0[i])
                tx0.insert('insert', '\n')
        # 级比检测
       # x0 = a2.start2()
            p = a2.test_start(x0)
            t1.insert('insert', p)

        # 平移变换#################
            n = 0
            while n < 10 and p == '不符合':
                c = 100
                for i in range(len(x0)):
                    x0[i] = x0[i] + c
                n = n + 1
                p = a2.test_start(x0)
            print("nnnnnnnn:", n)

            c1 = 100 * n
            tc.insert('insert', c1)
            t3.insert('insert', p)


        # 结果检测
            a, b = a2.matx(x0)
            x4 = a2.pre(x0, a, b)
            ave, x6 = a2.test_end(x0, x4)
            t2.insert('insert', ave)

        # 输出预测数据
            for i in range(0,len(x4)-3):
                tx4.insert('insert', i+1)
                tx4.insert('insert', ':')
                tx4.insert('insert', x4[i])
                tx4.insert('insert', '\n')
        #输出残差值
            for i in range(len(x6)):
                tx6.insert('insert', i+1)
                tx6.insert('insert', ':')
                tx6.insert('insert', x6[i])
                tx6.insert('insert', '\n')
            for i in range(len(x4) - 3, len(x4)):
                tp.insert('insert', x4[i])
                tp.insert('insert', '  ')


            x0_1 = [0] * 19
            for i in range(16):
                x0_1[i] = x0[i]
            for i in range(16, 19):
                x0_1[i] = x0[15]

            print("x0_1", x0_1)
            print(x4)

            image = a2.allshow(x0_1, x4)
            image.show()

    bu5 = tk.Button(window2, text='数据分析方向预测', width=20, height=2,command=text5).place(x=635, y=210)

    def text7():
        t1.delete(0.0, tk.END)  # 删除所有值
        t2.delete(0.0, tk.END)  # 删除所有值
        tx0.delete(0.0, tk.END)  # 删除所有值
        tx4.delete(0.0, tk.END)  # 删除所有值
        tx6.delete(0.0, tk.END)  # 删除所有值
        t3.delete(0.0, tk.END)  # 删除所有值
        tc.delete(0.0, tk.END)  # 删除所有值
        tp.delete(0.0, tk.END)
        #先判断地址是否成功，后输出实际数据
        print(location)
        if location=='':
            tk.messagebox.showinfo(title='error', message='请输入地址')
            print("输入地址")

        else:
            x0 = a2.start7(location)
            for i in range(len(x0)):
                tx0.insert('insert', i+1)
                tx0.insert('insert', ':')
                tx0.insert('insert', x0[i])
                tx0.insert('insert', '\n')
        # 级比检测
       # x0 = a2.start2()
            p = a2.test_start(x0)
            t1.insert('insert', p)

        # 平移变换#################
            n = 0
            while n < 10 and p == '不符合':
                c = 100
                for i in range(len(x0)):
                    x0[i] = x0[i] + c
                n = n + 1
                p = a2.test_start(x0)
            print("nnnnnnnn:", n)

            c1 = 100 * n
            tc.insert('insert', c1)
            t3.insert('insert', p)

        # 结果检测
            a, b = a2.matx(x0)
            x4 = a2.pre(x0, a, b)
            ave, x6 = a2.test_end(x0, x4)
            t2.insert('insert', ave)
        # 输出预测数据
            for i in range(0,len(x4)-3):
                tx4.insert('insert', i+1)
                tx4.insert('insert', ':')
                tx4.insert('insert', x4[i])
                tx4.insert('insert', '\n')
        #输出残差值
            for i in range(len(x6)):
                tx6.insert('insert', i+1)
                tx6.insert('insert', ':')
                tx6.insert('insert', x6[i])
                tx6.insert('insert', '\n')
            for i in range(len(x4) - 3, len(x4)):
                tp.insert('insert', x4[i])
                tp.insert('insert', '  ')


            x0_1 = [0] * 19
            for i in range(16):
                x0_1[i] = x0[i]
            for i in range(16, 19):
                x0_1[i] = x0[15]

            print("x0_1", x0_1)
            print(x4)

            image = a2.allshow(x0_1, x4)
            image.show()

    bu7 = tk.Button(window2, text='界面设计方向预测', width=20, height=2,command=text5).place(x=635, y=260)

    def text6():
        t1.delete(0.0, tk.END)  # 删除所有值
        t2.delete(0.0, tk.END)  # 删除所有值
        tx0.delete(0.0, tk.END)  # 删除所有值
        tx4.delete(0.0, tk.END)  # 删除所有值
        tx6.delete(0.0, tk.END)  # 删除所有值
        t3.delete(0.0, tk.END)  # 删除所有值
        tc.delete(0.0, tk.END)  # 删除所有值
        tp.delete(0.0, tk.END)
        #先判断地址是否成功，后输出实际数据
        print(location)
        if location=='':
            tk.messagebox.showinfo(title='error', message='请输入地址')
            print("输入地址")


        else:
            x0 = a2.start6(location)
            for i in range(len(x0)):
                tx0.insert('insert', i+1)
                tx0.insert('insert', ':')
                tx0.insert('insert', x0[i])
                tx0.insert('insert', '\n')
        # 级比检测
       # x0 = a2.start2()
            p = a2.test_start(x0)
            t1.insert('insert', p)

        # 平移变换#################
            n = 0
            while n < 10 and p == '不符合':
                c = 100
                for i in range(len(x0)):
                    x0[i] = x0[i] + c
                n = n + 1
                p = a2.test_start(x0)
            print("nnnnnnnn:", n)

            c1 = 100 * n
            tc.insert('insert', c1)
            t3.insert('insert', p)

        # 结果检测
            a, b = a2.matx(x0)
            x4 = a2.pre(x0, a, b)
            ave, x6 = a2.test_end(x0, x4)
            t2.insert('insert', ave)
        # 输出预测数据
            for i in range(0,len(x4)-3):
                tx4.insert('insert', i+1)
                tx4.insert('insert', ':')
                tx4.insert('insert', x4[i])
                tx4.insert('insert', '\n')
        #输出残差值
            for i in range(len(x6)):
                tx6.insert('insert', i+1)
                tx6.insert('insert', ':')
                tx6.insert('insert', x6[i])
                tx6.insert('insert', '\n')
            for i in range(len(x4) - 3, len(x4)):
                tp.insert('insert', x4[i])
                tp.insert('insert', '  ')


            x0_1 = [0] * 19
            for i in range(16):
                x0_1[i] = x0[i]
            for i in range(16, 19):
                x0_1[i] = x0[15]

            print("x0_1", x0_1)
            print(x4)

            image = a2.allshow(x0_1, x4)
            image.show()

    bu6 = tk.Button(window2, text='互联网方向预测', width=20, height=2, command=text6).place(x=635, y=310)

    def text7():
        t1.delete(0.0, tk.END)  # 删除所有值
        t2.delete(0.0, tk.END)  # 删除所有值
        tx0.delete(0.0, tk.END)  # 删除所有值
        tx4.delete(0.0, tk.END)  # 删除所有值
        tx6.delete(0.0, tk.END)  # 删除所有值
        t3.delete(0.0, tk.END)  # 删除所有值
        tc.delete(0.0, tk.END)  # 删除所有值
        tp.delete(0.0, tk.END)
        #先判断地址是否成功，后输出实际数据
        print(location)
        if location=='':
            tk.messagebox.showinfo(title='error', message='请输入地址')
            print("输入地址")


        else:
            x0 = a2.start7(location)
            for i in range(len(x0)):
                tx0.insert('insert', i+1)
                tx0.insert('insert', ':')
                tx0.insert('insert', x0[i])
                tx0.insert('insert', '\n')
        # 级比检测
       # x0 = a2.start2()
            p = a2.test_start(x0)
            t1.insert('insert', p)

        # 平移变换#################
            n = 0
            while n < 10 and p == '不符合':
                c = 100
                for i in range(len(x0)):
                    x0[i] = x0[i] + c
                n = n + 1
                p = a2.test_start(x0)
            print("nnnnnnnn:", n)

            c1 = 100 * n
            tc.insert('insert', c1)
            t3.insert('insert', p)

        # 结果检测
            a, b = a2.matx(x0)
            x4 = a2.pre(x0, a, b)

        # 对结果变换
            for i in range(len(x4)):
                x4[i] = x4[i] - c1

            for i in range(len(x0)):  # 画图前将x0回到原始数据
                x0[i] = x0[i] - c1
            ave, x6 = a2.test_end(x0, x4)
            t2.insert('insert', ave)

        # 输出预测数据
            for i in range(0,len(x4)-3):
                tx4.insert('insert', i+1)
                tx4.insert('insert', ':')
                tx4.insert('insert', x4[i])
                tx4.insert('insert', '\n')
        #输出残差值
            for i in range(len(x6)):
                tx6.insert('insert', i+1)
                tx6.insert('insert', ':')
                tx6.insert('insert', x6[i])
                tx6.insert('insert', '\n')
            for i in range(len(x4) - 3, len(x4)):
                tp.insert('insert', x4[i])
                tp.insert('insert', '  ')


            x0_1 = [0] * 19
            for i in range(16):
                x0_1[i] = x0[i]
            for i in range(16, 19):
                x0_1[i] = x0[15]

            print("x0_1", x0_1)
            print(x4)

            image = a2.allshow(x0_1, x4)
            image.show()

    bu7 = tk.Button(window2, text='云平台方向预测', width=20, height=2,command=text7).place(x=635, y=360)

    def text8():
        t1.delete(0.0, tk.END)  # 删除所有值
        t2.delete(0.0, tk.END)  # 删除所有值
        tx0.delete(0.0, tk.END)  # 删除所有值
        tx4.delete(0.0, tk.END)  # 删除所有值
        tx6.delete(0.0, tk.END)  # 删除所有值
        t3.delete(0.0, tk.END)  # 删除所有值
        tc.delete(0.0, tk.END)  # 删除所有值
        tp.delete(0.0, tk.END)
        #先判断地址是否成功，后输出实际数据
        print(location)
        if location=='':
            tk.messagebox.showinfo(title='error', message='请输入地址')
            print("输入地址")

        else:
            x0 = a2.start8(location)
            for i in range(len(x0)):
                tx0.insert('insert', i+1)
                tx0.insert('insert', ':')
                tx0.insert('insert', x0[i])
                tx0.insert('insert', '\n')
        # 级比检测
       # x0 = a2.start2()
            p = a2.test_start(x0)
            t1.insert('insert', p)

        # 平移变换#################
            n = 0
            while n < 10 and p == '不符合':
                c = 100
                for i in range(len(x0)):
                    x0[i] = x0[i] + c
                n = n + 1
                p = a2.test_start(x0)
            print("nnnnnnnn:", n)

            c1 = 100 * n
            tc.insert('insert', c1)
            t3.insert('insert', p)



        # 结果检测
            a, b = a2.matx(x0)
            x4 = a2.pre(x0, a, b)

        # 对结果变换
            for i in range(len(x4)):
                x4[i] = x4[i] - c1

            for i in range(len(x0)):  # 画图前将x0回到原始数据
                x0[i] = x0[i] - c1
            ave, x6 = a2.test_end(x0, x4)
            t2.insert('insert', ave)


            ave, x6 = a2.test_end(x0, x4)
            t2.insert('insert', ave)
        # 输出预测数据
            for i in range(0,len(x4)-3):
                tx4.insert('insert', i+1)
                tx4.insert('insert', ':')
                tx4.insert('insert', x4[i])
                tx4.insert('insert', '\n')
        #输出残差值
            for i in range(len(x6)):
                tx6.insert('insert', i+1)
                tx6.insert('insert', ':')
                tx6.insert('insert', x6[i])
                tx6.insert('insert', '\n')
            for i in range(len(x4) - 3, len(x4)):
                tp.insert('insert', x4[i])
                tp.insert('insert', '  ')


                x0_1 = [0] * 19
                for i in range(16):
                    x0_1[i] = x0[i]
                for i in range(16, 19):
                    x0_1[i] = x0[15]

                print("x0_1", x0_1)
                print(x4)

            image = a2.allshow(x0_1, x4)
            image.show()
    bu8 = tk.Button(window2, text='其他', width=20, height=2,command=text8).place(x=635, y=410)



def show3():
    window3 = tk.Toplevel(window)
    window3.title('工作岗位结构预测')
    window3.geometry('800x475')
    label1 = tk.Label(window3, text='工作结构-经验预测', font=('宋体', 20), width=30, height=3).pack()
    label2 = tk.Label(window3, text='填入相应数字:', font=('宋体', 15), width=15, height=1).place(x=1,y=60)
    #wraplength=3#用于换行
    labelsize=tk.Label(window3,text="size", font=('宋体', 13)).place(x=10,y=80)
    labeltype = tk.Label(window3, text="type", font=('宋体', 13)).place(x=130, y=80)
    labelcity = tk.Label(window3, text="city", font=('宋体', 13)).place(x=250, y=80)
    labeledu = tk.Label(window3, text="education", font=('宋体', 13)).place(x=370, y=80)
    labelclassify = tk.Label(window3, text="classify", font=('宋体', 13)).place(x=490, y=80)
    labelsalary = tk.Label(window3, text="salary", font=('宋体', 13)).place(x=610, y=80)
    e1=tk.Entry(window3,width=10)
    e1.place(x=10,y=100)
    e2=tk.Entry(window3,width=10)
    e2.place(x=130,y=100)
    e3=tk.Entry(window3,width=10)
    e3.place(x=250,y=100)
    e4=tk.Entry(window3,width=10)
    e4.place(x=370,y=100)
    e5=tk.Entry(window3,width=10)
    e5.place(x=490,y=100)
    e6=tk.Entry(window3,width=10)
    e6.place(x=610,y=100)

    tes1="1:小型企业" \
         "2:中型企业" \
         "3:大型企业"
    '''
    tes2="1:民营，私企2:股份制  " \
         "3:国企  " \
         "4:合资     " \
         "5:上市公司 " \
         "6:事业单位 " \
         "7:外商独资 " \
         "8:其 他"
    '''
    tes2 = """1:民营/私企 2:股份制  3:国企  4:合资   5:上市公司  6:事业单位 7:外商独资 8:其 他"""


    tes3="1:北京" \
         "2:上海" \
         "3:重庆" \
         "4:天津" \
         "5:广州" \
         "6:深圳"
    tes4="""1:本科       2:大专，高职3:硕士     4:初中，高中5:中技，中职，中专，职高6:其他"""

    tes5="1:编程开发 " \
         "2:测试     " \
         "3:云平台   " \
         "4:界面设计 " \
         "5:游戏     " \
         "6:互联网   " \
         "7:数据分析  " \
         "8:其他"
    tes6="1:面议       " \
         "2:5000以下   " \
         "3:5000-15000 " \
         "4:15000-50000" \
         "5:50000以上"
    '''
    tes7="经验应届生:1" \
         "经验在读:2  " \
         "经验1年:3   " \
         "经验2年:4   " \
         "经验3年:5   " \
         "3年以上:6   "
    '''
    labeltes1 = tk.Label(window3, text=tes1, font=('宋体', 11),wraplength=80).place(x=10, y=140)
    labeltes2 = tk.Label(window3, text=tes2 ,justify = 'left', font=('宋体', 11),wraplength=92).place(x=130, y=140)
    labeltes3 = tk.Label(window3, text=tes3,font=('宋体', 11), wraplength=50).place(x=250, y=140)
    labeltes4 = tk.Label(window3, text=tes4, justify='left', font=('宋体', 11), wraplength=92).place(x=360, y=140)
    labeltes5 = tk.Label(window3, text=tes5, justify='left', font=('宋体', 11), wraplength=92).place(x=490, y=140)
    labeltes6 = tk.Label(window3, text=tes6, justify='left', font=('宋体', 11), wraplength=110).place(x=600, y=140)

    labelresult = tk.Label(window3, text="结果为", font=('宋体', 15)).place(x=20, y=300)
    t1=tk.Text(window3,font=('宋体', 20),width=20,height=1)
    t1.place(x=100,y=300)

 #   labeltes7 = tk.Label(window3, text=tes7, font=('宋体', 11), wraplength=105).place(x=90, y=340)

    def pre():
        a=e1.get()
        b=e2.get()
        c=e3.get()
        d=e4.get()
        e=e5.get()
        f=e6.get()
        print(a,b,c,d,e,f)


        if ((a=='1' or a=='2' or a=='3') and (b=='1' or b=='2' or b=='3' or b=='4' or b=='5' or b=='6' or b=='7' or b=='8') and (c=='1' or c=='2' or c=='3' or c=='4' or c=='5' or c=='6') and (d=='1' or d=='2' or d=='3' or d=='4' or d=='5' or d=='6') and (e=='1' or e=='2' or e=='3' or e=='4' or e=='5' or e=='6' or e=='7' or e=='8') and (f=='1' or f=='2' or f=='3' or f=='4' or f=='5')):
            predict,number_train,number_test,rate = a3.tree(a, b, c, d, e, f)

            print(predict[0])

            if predict[0] == 1:
                re = '应届生'
            elif predict[0] == 2:
                re = '在读'
            elif predict[0] == 3:
                re = '至少1年工作经验'
            elif predict[0] == 4:
                re = '至少2年工作经验'
            elif predict[0] == 5:
                re = '至少3年工作经验'
            else:
                re = '至少3年以上工作经验'

            t1.insert('insert', re)
       #     t1.insert('insert', predict[0])

        else:
            tk.messagebox.showinfo(title='error', message='输入出错，请重新输入')


    bu1 = tk.Button(window3, text='预测', width=20, height=2,command=pre).place(x=420, y=380)

    def dele():
        t1.delete(0.0, tk.END)  # 删除所有值
    bu2 = tk.Button(window3, text='清除结果', width=20, height=2,command=dele).place(x=600, y=380)


    def model():
        window4 = tk.Toplevel(window)
        window4.title('预测模型')
        window4.geometry('800x475')

        label1 = tk.Label(window4, text='决策树模型', font=('宋体', 20),width=30, height=3).pack()
        label2 = tk.Label(window4, text='特征值: 公司规模（size），公司性质（tpye），所在地（city），学历要求（education）', font=('宋体', 13)).place(x=30, y=120)
        label3 = tk.Label(window4, text=' 工作方向（classify），工资待遇（salary）',font=('宋体', 13)).place(x=90, y=145)
        label4 = tk.Label(window4, text='预测值：经验要求（experience）', font=('宋体', 13)).place(x=30, y=170)


        label5 = tk.Label(window4, text='训练集数量:', font=('宋体', 13)).place(x=30, y=200)
        t5 = tk.Text(window4, font=('宋体', 13), width=10, height=1)
        t5.place(x=140, y=200)

        label6 = tk.Label(window4, text='测试集数量:', font=('宋体', 13)).place(x=30, y=230)
        t6 = tk.Text(window4, font=('宋体', 13), width=10, height=1)
        t6.place(x=140, y=230)

        label7 = tk.Label(window4, text='正确率:', font=('宋体', 13)).place(x=30, y=260)
        t7 = tk.Text(window4, font=('宋体', 13), width=10, height=1)
        t7.place(x=140, y=260)

        predict, number_train, number_test,rate = a3.tree(1,1,1,1,1,1)
        t5.insert('insert', number_train)
        t6.insert('insert', number_test)
        t7.insert('insert', rate)

    bu3 = tk.Button(window3, text='查看模型', width=15, height=1,command=model).place(x=530, y=30)


button1=tk.Button(window,text='工作岗位数据可视化',width=22,height=3,command=show1)
button1.pack()
button2=tk.Button(window,text='工作岗位数量预测',width=22,height=3,command=show2)
button2.pack()
button3=tk.Button(window,text='工作岗位结构预测',width=22,height=3,command=show3)
button3.pack()

window.mainloop()

