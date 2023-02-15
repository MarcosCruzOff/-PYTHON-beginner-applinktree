from tkinter import *
import webbrowser

App = Tk()

App.title("App Linktree")
App.geometry("380x720")

icon = PhotoImage(file="icon.png")
App.wm_iconphoto(True, icon)

#Background do app
fundo = PhotoImage(file="fundo.png")
background = Label(App,image=fundo)
background.place(x=-2, y=0)

#Imagem de perfil
canvas = Canvas(App, width=200, height=150,  bg="#2d506b", highlightthickness=0)
canvas.pack(pady=10)

perfil = PhotoImage(file= "Eu.png")
resized_image = perfil.subsample(6, 6)
canvas.create_image(100,75, image=resized_image)

#Criando título e sub-títulos em texto
nome = Label(App, text="Marcos Cruz", font=("jetBrains Mono", 20, "bold"),  bg="#2d506b", fg="white")
nome.pack(pady=1)
titulo = Label(App, text="Programador FullStack", font=("jetBrains Mono",14, "italic"),bg="#2d506b", fg="white")
titulo.pack()

#Separador
linha = Canvas(App, width=100, height=50, bg="#2d506b", highlightthickness=0)
linha.pack(pady=5)

#links
def github(event):
    webbrowser.open_new_tab('https://github.com/MarcosCruzOff')

def linkedin(event):
    webbrowser.open_new_tab('https://www.linkedin.com/in/marcos-cruz-8b9024224/')
    
def youtube(event):
    webbrowser.open_new_tab('https://www.youtube.com/channel/UCe2tbSDb9Q0A3mdMowKyPNg')
    

btn_git = Canvas(App, width=250, height=50, bg="#3770a0", highlightthickness=0)
btn_git.create_text(125,25, text="GitHub", font=("jetBrains Mono",15), fill="white")
btn_git.bind("<Button-1>",github)
btn_git.pack(pady=5)

btn_link = Canvas(App, width=250, height=50,  bg="#3770a0", highlightthickness=0)
btn_link.create_text(125,25, text="linkedin", font=("jetBrains Mono", 15), fill="White")
btn_link.bind("<Button-1>", linkedin)
btn_link.pack(pady=5)

btn_tube = Canvas(App, width=250, height=50, bg="#3770a0", highlightthickness=0)
btn_tube.create_text(125,25, text="Youtube", font=("jetBrains Mono",15), fill="White")
btn_tube.bind("<Button-1>", youtube)
btn_tube.pack(pady=5)
    
    


App.mainloop()