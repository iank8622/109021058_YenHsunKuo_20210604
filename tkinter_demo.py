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
    
    count = 0
    while count != 6:
        number = randint(1,42)
        if number not in ranList:
            ranList.append(number)
            count += 1
        lab2.config(text = ranList)

def switch_color():
    global color
    labRan = randint(0,4)
    btnRan = randint(0,4)
    while btnRan == labRan:
        btnRan = randint(0,4)

    labRan = color[labRan]
    btnRan = color[btnRan]


    lab1.config(bg = labRan)
    lab2.config(bg = labRan)

    addBtn.config(bg = btnRan)
    subBtn.config(bg = btnRan)
    ranBtn.config(bg = btnRan)
    colorBtn.config(bg = btnRan)

    



x = 0
ranList = []
color = ["red", "yellow", "green", "blue", "purple"]

window = Tk() # 新增TK物件
window.title("GUI(tkinter) Demo") # title("") 設定標題
window.config(bg = "#505787") # config(bg = "色碼") 設定背景顏色

'''使用者元件'''
lab1 = Label(window, text = x, width = 15, height = 3, bg = "#ffc472") # Label(傳入視窗, text = "顯示文字", width = 12 #字數, height = 3 #字數)
lab1.pack()

addBtn = Button(window, text = "Add", width = 10, height = 2, bg = "#eefffa", command = add_result)
addBtn.pack() # pack() 放入視窗內

subBtn = Button(window, text = "Sub", width = 10, height = 2, bg = "#eefffa", command = sub_result)
subBtn.pack() # pack() 放入視窗內

lab2 = Label(window, text = ranList, width = 15, height = 3, bg = "#ffc472")
lab2.pack()

ranBtn = Button(window, text = "Lotto Draw", width = 10, height = 2, bg = "#eefffa", command = lotto)
ranBtn.pack() # pack() 放入視窗內

colorBtn = Button(window, text = "Switch Color", width = 10, height = 2, bg = "#eefffa", command = switch_color)
colorBtn.pack() # pack() 放入視窗內


btnExit = Button(window, text = "Exit", width = 10, height = 2, command = window.destroy) # Button(傳入視窗, text = "顯示文字", command #命令 = window.destroy #清除視窗)
btnExit.pack() # pack() 放入視窗內

window.geometry("600x400+100+50") # geometry("寬x高+視窗初始x軸+視窗初始y軸") 設定視窗大小及初始位置
window.mainloop() # 主循環
