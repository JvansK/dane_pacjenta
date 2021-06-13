from tkinter import *

def zapisz():
   plik = open('spis.csv','a')
   plik.write(str(e.get()))
   plik.write(';')
   plik.write(str(e1.get()))
   plik.write(';')
   plik.write(str(e2.get()))
   plik.write(';')
   plik.write(str(e3.get()))
   plik.write(';')
   plik.write(str(e4.get()))
   plik.write(';')
   plik.write(str(e5.get()))
   plik.write('\n')
   eStr.set('')
   e1Str.set('')
   e2Str.set('')
   e3Str.set('')
   e4Str.set('')
   e5Str.set('')
   plik.close()

def czysc():
   eStr.set('')
   e1Str.set('')
   e2Str.set('')
   e3Str.set('')
   e4Str.set('')
   e5Str.set('')

top = Tk()

eStr = StringVar()
e1Str = StringVar()
e2Str = StringVar()
e3Str = StringVar()
e4Str = StringVar()
e5Str = StringVar()

l = Label(top, text = "Imie")
l.grid(row = 0, column = 0)

e = Entry(top, textvariable=eStr)
e.grid(row = 0, column = 1)

l1 = Label(top, text = "Nazwisko")
l1.grid(row = 1, column = 0)

e1 = Entry(top, textvariable=e1Str)
e1.grid(row = 1, column = 1)

l2 = Label(top, text = "Pesel")
l2.grid(row = 2, column = 0)

e2 = Entry(top,textvariable=e2Str )
e2.grid(row = 2, column = 1)

l3 = Label(top, text = "tel.kontaktowy")
l3.grid(row = 3, column = 0)

e3 = Entry(top,textvariable=e3Str )
e3.grid(row = 3, column = 1)

l4 = Label(top, text = "e-mail")
l4.grid(row = 4, column = 0)

e4 = Entry(top, textvariable=e4Str)
e4.grid(row = 4, column = 1)

l5 = Label(top, text = "Adres")
l5.grid(row = 5, column = 0)

e5 = Entry(top,textvariable=e5Str )
e5.grid(row = 5, column = 1)


butt = Button(top, text = "Zapisz", command = zapisz)
butt.grid(row = 6, column = 0)


butt1 = Button(top, text = "Wyczyść", command = czysc)
butt1.grid(row = 6, column = 1)



top.mainloop()