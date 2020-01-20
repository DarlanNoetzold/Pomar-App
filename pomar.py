from tkinter import *
from sklearn import tree

longa = 2
lisa = 1
irregular = 0

uva = 5
bergamota = 4
mamao = 3
banana = 2
maca = 1
laranja = 0

pomar = [[150,lisa],[130, lisa], [180, irregular], [160, irregular],[120, irregular],[190, lisa],[80, longa],
         [100, longa],[120,longa],[300,longa],[280,longa],[250,longa],[80,irregular],[90,irregular],[5,lisa],
         [10,lisa],[3,lisa]]
resultado = [maca, maca, laranja, laranja, maca, laranja, banana,
             banana, banana, mamao, mamao, mamao,bergamota,bergamota,
             uva, uva, uva]

clf = tree.DecisionTreeClassifier()
clf = clf.fit(pomar, resultado)

def bt_onclick():
    peso = enPeso.get()
    superficie = enSuperficie.get()
    resultadoUsuario = clf.predict([[peso, superficie]])
    if resultadoUsuario == 1:
        lbResultado = Label(janela, text="É uma Maçã!",font=("Helvetica", 16),fg="red")
        lbResultado.place(x=10, y=200)
    elif resultadoUsuario == 0:
        lbResultado = Label(janela, text="É uma Laranja!",font=("Helvetica", 16),fg="orange")
        lbResultado.place(x=10, y=200)
    elif resultadoUsuario == 2:
        lbResultado = Label(janela, text="É uma Banana!", font=("Helvetica", 16), fg="goldenrod")
        lbResultado.place(x=10, y=200)
    elif resultadoUsuario == 3:
        lbResultado = Label(janela, text="É um Mamão!", font=("Helvetica", 16), fg="orangered2")
        lbResultado.place(x=10, y=200)
    elif resultadoUsuario == 4:
        lbResultado = Label(janela, text="É uma Bergamota!", font=("Helvetica", 16), fg="orange2")
        lbResultado.place(x=10, y=200)
    elif resultadoUsuario == 5:
        lbResultado = Label(janela, text="É uma Uva!", font=("Helvetica", 16), fg="purple")
        lbResultado.place(x=10, y=200)
janela= Tk()

lbTit = Label(janela, text="Scanner de Frutas",font=("Helvetica", 16),fg="black")
lbTit.place(x=85,y=10)
lbPeso = Label(janela, text="Peso da fruta: ",font=("Helvetica", 16),fg="black")
lbPeso.place(x=10,y=50)
enPeso = Entry(janela, width=20)
enPeso.place(x=200,y=60)

lbSuperficie = Label(janela, text="Superficíe da fruta: ",font=("Helvetica", 16),fg="black")
lbSuperficie.place(x=10,y=100)
lbLegenda = Label(janela, text="Irregular = 0|Lisa = 1|Longa = 2",font=("Helvetica", 10),fg="gray25")
lbLegenda.place(x=10,y=132)
enSuperficie = Entry(janela, width=20)
enSuperficie.place(x=200,y=110)

bt = Button(janela, width=20, text="Enviar", command=bt_onclick)
bt.place(x=110,y=175)

janela.title("Pomar")
janela.geometry("350x250")
janela.mainloop()

print("teste")
input("tchau")

