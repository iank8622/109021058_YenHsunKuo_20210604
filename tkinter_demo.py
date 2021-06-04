'''
GUI(tkinter)
'''
from tkinter import *
from random import randint

def add_result():
    global x
    x += 1
    lab1.config(text = x)

def sub_result():
    global x
    x -= 1
    lab1.config(text = x)

def lotto():
    global ranList
    ranList = []
    lottoList = [lottoLab1, lottoLab2, lottoLab3, lottoLab4, lottoLab5, lottoLab6, ]

    
    count = 0
    while count != 6:
        number = randint(1,42)
        if number not in ranList:
            ranList.append(number)
            count += 1

    count = 0
    for lottoLab in lottoList:
        lottoLab.config(text = ranList[count])
        count += 1

def switch_color():
    global color
    labList = [lab1, lottoLab1, lottoLab2, lottoLab3, lottoLab4, lottoLab5, lottoLab6, ]

    for lab in labList:
        labRan = color[randint(0,4)]
        lab.config(bg = labRan)




x = 0
ranList = []
color = ["red", "yellow", "green", "blue", "purple"]

window = Tk() # 新增TK物件
window.title("GUI(tkinter) Demo") # title("") 設定標題
window.config(bg = "#505787") # config(bg = "色碼") 設定背景顏色

'''使用者元件'''
lab1 = Label(window, text = x, width = 12, height = 3, bg = "#ffc472") # Label(傳入視窗, text = "顯示文字", width = 12 #字數, height = 3 #字數)
lab1.pack()

addBtn = Button(window, text = "Add", width = 10, height = 2, command = add_result)
addBtn.pack() # pack() 放入視窗內

subBtn = Button(window, text = "Sub", width = 10, height = 2, command = sub_result)
subBtn.pack() # pack() 放入視窗內

lottoLab1 = Label(window, text = ranList, width = 12, height = 3, bg = "#ffc472")
lottoLab1.pack()

lottoLab2 = Label(window, text = ranList, width = 12, height = 3, bg = "#ffc472")
lottoLab2.pack()

lottoLab3 = Label(window, text = ranList, width = 12, height = 3, bg = "#ffc472")
lottoLab3.pack()

lottoLab4 = Label(window, text = ranList, width = 12, height = 3, bg = "#ffc472")
lottoLab4.pack()

lottoLab5 = Label(window, text = ranList, width = 12, height = 3, bg = "#ffc472")
lottoLab5.pack()

lottoLab6 = Label(window, text = ranList, width = 12, height = 3, bg = "#ffc472")
lottoLab6.pack()

ranBtn = Button(window, text = "Lotto Draw", width = 10, height = 2, command = lotto)
ranBtn.pack() # pack() 放入視窗內

colorBtn = Button(window, text = "Switch Color", width = 10, height = 2, command = switch_color)
colorBtn.pack() # pack() 放入視窗內


btnExit = Button(window, text = "Exit", width = 10, height = 2, command = window.destroy) # Button(傳入視窗, text = "顯示文字", command #命令 = window.destroy #清除視窗)
btnExit.pack() # pack() 放入視窗內

window.geometry("600x600+100+50") # geometry("寬x高+視窗初始x軸+視窗初始y軸") 設定視窗大小及初始位置
window.mainloop() # 主循環
