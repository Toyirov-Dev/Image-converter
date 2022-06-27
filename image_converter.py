from tkinter import*
from tkinter import filedialog,simpledialog
from tkinter  import messagebox
import re
from PIL import Image

# Dastur oynasi:
root = Tk()
root.title("Image convertor!")
root.geometry('450x500')
root.config(bg='#19497C')



# funksiyalar
def About():     
    label = messagebox.showinfo("About", "Dastur Toyirov Ziyodullo tomonidan\n 23.05.2202 - sanada yartildi.\n\n Dastur vazifasi: suratlarni  \n Convert qilish. Masalan, .jpg-ni .png-ga \n yoki boshqa farmatlarga!.\n\nTelegram: @Desperados_partfolio")

def Qollanma():     
    label = messagebox.showinfo("Qo'llanma", "Siz suratlarni convert qilish uchun \n Birinchi inputga surat joylashgan\n manzilni kiritishingiz kerak. Masalan\n 'suratlar/rasm.jpg' va shunga o'xshash.\n Siz ikkinchi inputga suratni\n qanday saqlashni ya'ni nomini\n yozishingiz lozim masalan, 'conv.png'\n\n Agar sizda suratlar muvoffaqqiyatli\n convert bo'layotgan bo'lsa unda sizni\n tabriklaymiz!\n\n Support: About bo'limida.")


def cmdExit():     
    quit()


def convert():
	get1 = input1.get()
	get2 = input2.get()

	img = Image.open(get1)
	img.save(get2)

	print("Surat muvofaqqiyatli saqlandi!")
	
	

def Error():     
    label = messagebox.showerror("ERROR", "Dastur nomalum sabablarga ko'ra\n ERROR-ga tushib qoldi!\n\n Dastur vaqtinchalik ishlamaydi!")


# Sarlavha:
Sarlavha = Label(root, text="Image convertor!",
	fg='Black',
	font=('Times', 17, 'bold'),
	bg='#19497C')
Sarlavha.place(x=140, y=20)



# by 
by = Label(root, text="by",
	fg='Black',
	font=('Times', 13, 'italic'),
	bg='#19497C')
by.place(x=215, y=45)



# coder 
coder = Label(root, text="       Toyirov Dev",
	fg='Black',
	font=('Times', 15, 'bold'),
	bg='#19497C')
coder.place(x=140, y=65)



# chiziq
chiziq = Label(root, text="---------------------------------------------------------",
	fg='Black',
	font=('Times', 15, 'bold'),
	bg='#19497C')
chiziq.place(x=25, y=90)



# input1 ga tavfsif
tvf1 = Label(root, text="Suratni manzilini yozing formati bilan!",
	fg='Black',
	font=('Times', 9, 'italic'),
	bg='#19497C')
tvf1.place(x=140, y=130)



# input1
input1 = Entry(root, bg='#DFDFDF',
	fg = 'black',
	font = ('Colibri', 10, 'bold'),
	relief = SOLID,
	width = 35)
input1.place(x=105, y=155)



# input2 ga tavfsif
tvf2 = Label(root, text="    Suratni convert qilish uchun ismi\nbilan farmatini yozing!",
	fg='Black',
	font=('Times', 9, 'italic'),
	bg='#19497C')
tvf2.place(x=140, y=200)



# input2
input2 = Entry(root, bg='#DFDFDF',
	fg = 'black',
	font = ('Colibri', 10, 'bold'),
	relief = SOLID,
	width = 35)
input2.place(x=105, y=240)



# chiziq2
chiziq2 = Label(root, text="---------------------------------------------------------",
	fg='Black',
	font=('Times', 15, 'bold'),
	bg='#19497C')
chiziq2.place(x=25, y=280)



# Convert button:
c_button = Button(root, text='convert',
	bg='#1ECBE1',
	fg='black',
	font=('Times', 10, 'bold'),
	relief=SOLID,
	cursor='hand2',
	width=20,
	command=convert)
c_button.place(x=155, y=320)



# menu-ga yo'l
tvf3 = Label(root, text="'help' menu-sidan bo'limidan yordam oling!",
	fg='Black',
	font=('Times', 10, 'italic'),
	relief=SOLID,
	bg='#19497C')
tvf3.place(x=105, y=475)





convertMenu = Menu(root)
root.configure(menu=convertMenu)


helpMenu = Menu(convertMenu, tearoff = False)
convertMenu.add_cascade(label='Help', menu = helpMenu)

helpMenu.add_command(label='About', command=About) 
helpMenu.add_command(label="Qo'llanma", command=Qollanma) 
helpMenu.add_separator()
helpMenu.add_command(label='Chiqish', command = cmdExit) 



root.mainloop()
