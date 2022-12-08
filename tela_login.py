from tkinter import *
from tkinter import messagebox as msg
from tkinter.font import Font

# Função para exibir as mensagens na interação com os campos Usuário e Senha
def camposPreenchimento():
    if campo_usuario.get() == "":
        msg.showwarning(title="Usuário vazio", message="O campo USUÁRIO não pode ficar vazio!")
    elif campo_senha.get() == "":
        msg.showwarning(title="Senha vazio", message="O campo SENHA não pode ficar vazio!")
    elif campo_usuario.get() == "" and campo_senha.get() == "":
        msg.showerror(title="Campos vazios", message="Os campos não podem ficar vazios!")
    else:
        msg.showinfo(title="Bem vindo(a)", message=f"Olá {campo_usuario.get()}!")

# Criação da aplicação
tela = Tk()
tela.title("Tela de login")
tela.geometry("400x350")
tela.configure(background="#041036")
tela.resizable(False, False)

# Criação das fontes
fonte_titulo = Font(tela, family="Ink Free", size=24, weight='bold')
fonte_labels = Font(tela, family="Century Gothic", size=16, weight='bold')
fonte_entry = Font(tela, family="Arial", size=12)
fonte_checkbutton = Font(tela, family="Arial", size=10, weight='bold')
fonte_btn = Font(tela, family="Calibri", size=12, weight='bold')

# Elementos do titulo principal
txt_titulo = Label(tela, 
font=fonte_titulo,
text="Tela de login",
relief='raised',
bd=3,
cursor='target',
bg="#5e027d",
fg="white")
txt_titulo.pack(padx=10, pady=10, fill=BOTH)

# Elementos do campo 'Usuário'
txt_usuario = Label(tela,
font=fonte_labels,
text="Usuário:",
bg='#041036',
fg='white',
bd=3)
txt_usuario.pack(padx=2, pady=5)

campo_usuario = Entry(tela,
font=fonte_entry,
relief='groove',
cursor='spraycan',
highlightbackground='#5e027d',
highlightthickness=3,
highlightcolor='#eaf51d',
bd=3)
campo_usuario.pack(padx=3, pady=2)

# Elementos do campo 'Senha'
txt_senha = Label(tela,
font=fonte_labels,
text="Senha:",
bg='#041036',
fg='white',
bd=3)
txt_senha.pack(padx=2, pady=5)

campo_senha = Entry(tela,
font=fonte_entry,
show="*",
cursor='spraycan',
highlightbackground='#5e027d',
highlightthickness=3,
highlightcolor='#eaf51d',
bd=3)
campo_senha.pack(padx=3, pady=2)

# Elementos do campo 'Salvar senha'
check_salvar_senha = Checkbutton(tela,
font=fonte_checkbutton,
text="Salvar senha?",
fg='black',
onvalue=1,
offvalue=0,
height=1)
check_salvar_senha.pack(padx=5, pady=5)

# Elementos do botão 'Enviar'
btn_enviar = Button(tela,
font=fonte_btn,
text="Enviar",
justify=CENTER,
cursor='pirate',
relief='raised',
bd=5,
command=camposPreenchimento)
btn_enviar.pack(padx=4, pady=5)

tela.mainloop()