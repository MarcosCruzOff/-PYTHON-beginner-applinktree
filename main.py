from tkinter import *
import webbrowser

#cores
azul_escuro = "#2d506b"
azul_claro = "#3770a0"
branco = "white"

def github(event):
    webbrowser.open_new_tab('https://github.com/MarcosCruzOff')

def linkedin(event):
    webbrowser.open_new_tab('https://www.linkedin.com/in/marcos-cruz-8b9024224/')

def youtube(event):
     webbrowser.open_new_tab('https://www.youtube.com/channel/UCe2tbSDb9Q0A3mdMowKyPNg')

#configuração básica do app
app = Tk()
app.title("App logintree")
app.geometry("380x720")
app.resizable(False, False)

icon = PhotoImage(file="image/icon.png")
app.iconphoto(True, icon)

background = PhotoImage(file="image/fundo.png")
background_app = Label(app, image=background)
background_app.place(x=-2, y=0)

#Foto do Perfil
perfil = PhotoImage(file="image/Eu.png")
resize_image= perfil.subsample(6,6)
perfil_campo= Label(app, image=resize_image)
perfil_campo.pack(pady=10)

#Nome e título
nome = Label(app, text="Marcos Cruz", font=("jetBrains Mono", 20, "bold"),bg=azul_escuro, fg=branco)
nome.pack()

titulo = Label(app, text="Programador Fullstack",font=("jetBrains Mono", 14, "bold"),bg=azul_escuro, fg=branco)
titulo.pack()

#linha separadora
linha = Canvas(app, width=200, height=50, bg=azul_escuro, highlightthickness=0)
linha.pack(pady=5)

#botões
btn_git = Label(app, text="Github", font=("jetBrains Mono", 15), fg=branco, bg=azul_claro, width=25, height=2)
btn_git.bind("<Button-1>", github)
btn_git.pack()

btn_git = Label(app, text="Linkedin", font=("jetBrains Mono", 15), fg=branco, bg=azul_claro, width=25, height=2)
btn_git.bind("<Button-1>", linkedin)
btn_git.pack(pady=10)

btn_git = Label(app, text="Youtube", font=("jetBrains Mono", 15), fg=branco, bg=azul_claro, width=25, height=2)
btn_git.bind("<Button-1>", youtube)
btn_git.pack()


mainloop()