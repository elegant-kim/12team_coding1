from tkinter import *
window = Tk()
window.geometry("500x500")

var = IntVar()

labelv = Label(window, text= "좋아하는 동물 투표", font= ("궁서체", 20), fg= "blue")

rb1 = Radiobutton(window, text= "강아지", variable=var, value=1)
rb2 = Radiobutton(window, text= "고양이", variable=var, value=2)
rb3 = Radiobutton(window, text= "토끼", variable=var, value=3)

photo1 = PhotoImage(file= "gif/dog.gif")
photo2 = PhotoImage(file= "gif/cat.gif")
photo3 = PhotoImage(file= "gif/rabbit.gif")

label1 = Label(window, text= "강아지")
label2 = Label(window, text= "고양이")
label3 = Label(window, text= "토끼")

labelp1 = Label(window, image= photo1)
labelp2 = Label(window, image= photo2)
labelp3 = Label(window, image= photo3)

button1 = Button(window, text="사진 보기")

######### 실행

labelv.pack()

rb1.pack()
rb2.pack()
rb3.pack()

button1.pack()

window.mainloop()