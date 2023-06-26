from tkinter import *
pg = Tk()
pg.geometry("500x500")
pg.title("Imagen")
pg.configure(background="#264653")

dupla = {"mutable":"Elemento que puede cambiar",
         "inmutable":"Elemento que no puede cambiar",
         "tkinter":"Libreria de Python"}
def fn1():
    lb1["text"] = dupla["mutable"]
def fn2():
    lb2["text"] = dupla["inmutable"]
def fn3():
    lb3["text"] = dupla["tkinter"]


bt1 = Button(pg, text="¿Que es Mutable?", command=fn1)
bt1.place(relx=0.5, rely=0.05, anchor=CENTER)

lb1 = Label(pg, text=".")
lb1.place(relx=0.5, rely=0.15, anchor=CENTER)

bt2 = Button(pg, text="¿Que es Inmutable?", command=fn2)
bt2.place(relx=0.5, rely=0.25, anchor=CENTER)

lb2 = Label(pg, text=".")
lb2.place(relx=0.5, rely=0.35, anchor=CENTER)

bt3 = Button(pg, text="¿Que es Tkinter?", command=fn3)
bt3.place(relx=0.5, rely=0.45, anchor=CENTER)

lb3 = Label(pg, text=".")
lb3.place(relx=0.5, rely=0.55, anchor=CENTER)




pg.mainloop()