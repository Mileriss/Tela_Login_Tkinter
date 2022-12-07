from tkinter import *
from tkinter import messagebox as msg
from tkinter.font import Font

# Função para exibir a mensagem ao clicar no botão
def loginEfetuado():
    #msg.showinfo(title="Bem vindo(a)!", message=f"Olá {campo_usuario.get()}!")
    if campo_usuario == "":
        msg.showwarning(title="Campo usuário vazio", message="Preencha o campo usuário!")
    elif campo_senha == "":
        msg.showwarning(title="Campo senha vazio", message="Preencha o campo 'senha'!")
    elif campo_usuario and campo_senha == "":
        msg.showwarning(title="Campos vazios", message="Preencha os campos para prosseguir!")


# Criação da aplicação
tela = Tk()
tela.title("Tela de login")
tela.geometry("400x350")
tela.configure(background="black")
tela.resizable(False, False)

# Criação das fontes
fonte_titulo = Font(tela, family="Ink Free", size=24, weight='bold')
fonte_labels = Font(tela, family="Century Gothic", size=16, weight='bold')
fonte_entry = Font(tela, family="Arial", size=12)
fonte_checkbutton = Font(tela, family="Arial", size=10)
fonte_btn = Font(tela, family="Calibri", size=12, weight='bold')

# Elementos do titulo principal
txt_titulo = Label(tela, 
font=fonte_titulo,
text="Tela de login",
relief='sunken',
bd=5,
cursor='target')
txt_titulo.pack(padx=10, pady=10, fill=BOTH)

# Elementos do campo 'Usuário'
txt_usuario = Label(tela,
font=fonte_labels,
text="Usuário:",
bg='black',
fg='white',
bd=3)
txt_usuario.pack(padx=2, pady=5)

campo_usuario = Entry(tela,
font=fonte_entry,
relief='groove',
cursor='spraycan',
highlightbackground='purple',
highlightthickness=3,
highlightcolor='green',
bd=5)
campo_usuario.pack(padx=3, pady=2)

# Elementos do campo 'Senha'
txt_senha = Label(tela,
font=fonte_labels,
text="Senha:",
bg='black',
fg='white',
bd=3)
txt_senha.pack(padx=2, pady=5)

campo_senha = Entry(tela,
font=fonte_entry,
show="*",
cursor='spraycan',
highlightbackground='purple',
highlightthickness=3,
highlightcolor='green',
bd=5)
campo_senha.pack(padx=3, pady=2)

# Elementos do campo 'Salvar senha'
check_salvar_senha = Checkbutton(tela,
font=fonte_checkbutton,
text="Salvar senha?",
bg='black',
fg='white')
check_salvar_senha.pack(padx=5, pady=2)

# Elementos do botão 'Enviar'
btn_enviar = Button(tela,
font=fonte_btn,
text="Enviar",
justify=CENTER,
cursor='pirate',
command=loginEfetuado)
btn_enviar.pack(padx=4, pady=2)

tela.mainloop()