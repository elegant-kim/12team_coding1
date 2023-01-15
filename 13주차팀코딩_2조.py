from tkinter import *
window = Tk()
window.geometry("500x500")
window.title("반려동물 선택하기")

def myFunc():
    if var.get() == 1:
        labelbg.configure(image= photo1)
    elif var.get() == 2:
        labelbg.configure(image= photo2)
    else:
        labelbg.configure(image= photo3)


labelv = Label(window, text= "좋아하는 동물 투표", font= ("궁서체", 20), fg= "blue")

var = IntVar()

rb1 = Radiobutton(window, text= "강아지", variable=var, value=1)
rb2 = Radiobutton(window, text= "고양이", variable=var, value=2)
rb3 = Radiobutton(window, text= "토끼", variable=var, value=3)
buttonView = Button(window, text="사진 보기", command= myFunc)

photo1 = PhotoImage(file= "gif/dog.gif")
photo2 = PhotoImage(file= "gif/cat.gif")
photo3 = PhotoImage(file= "gif/rabbit.gif")

labelbg = Label(window, width = 500, height = 500, bg = "yellow", image = None)

######### 실행

labelv.pack()

rb1.pack()
rb2.pack()
rb3.pack()

buttonView.pack()
labelbg.pack()

window.mainloop()