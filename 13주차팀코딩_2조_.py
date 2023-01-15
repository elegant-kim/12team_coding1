from tkinter import *
window = Tk()
window.geometry("500x700")
window.title("좋아하는 연예인 선택하기")

def myFunc():
    if var.get() == 1:
        labelbg.configure(image= photo1)
    elif var.get() == 2:
        labelbg.configure(image= photo2)
    elif var.get() == 3:
        labelbg.configure(image= photo3)
    else:
        labelbg.configure(image= photo4)


labelv = Label(window, text= "좋아하는 연예인 투표", font= ("궁서체", 20), fg= "blue")

var = IntVar()

rb1 = Radiobutton(window, text= "카리나", variable=var, value=1)
rb2 = Radiobutton(window, text= "윈터", variable=var, value=2)
rb3 = Radiobutton(window, text= "지젤", variable=var, value=3)
rb4 = Radiobutton(window, text= "닝닝", variable=var, value=4)

buttonView = Button(window, text="사진 보기", command= myFunc)

photo1 = PhotoImage(file= "aespa/KARINA.png")
photo2 = PhotoImage(file= "aespa/WINTER.png")
photo3 = PhotoImage(file= "aespa/GISELLE.png")
photo4 = PhotoImage(file= "aespa/NINGNING.png")

labelbg = Label(window, width = 500, height = 500, bg = "yellow", image = None)

######### 실행

labelv.pack()

rb1.pack()
rb2.pack()
rb3.pack()
rb4.pack()

buttonView.pack()
labelbg.pack()

window.mainloop()