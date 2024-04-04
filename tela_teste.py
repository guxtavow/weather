import tkinter as tk

# Função para imprimir uma mensagem quando o botão for clicado
def imprimir_mensagem():
    print("Botão clicado!")

# Criando a janela principal
janela = tk.Tk()

# Adicionando um título à janela
janela.title("Minha Aplicação Tkinter")

# Definindo as dimensões da janela
janela.geometry("300x200")

# Criando um rótulo na janela
rotulo = tk.Label(janela, text="Olá, Mundo!")
rotulo.pack()

# Criando um botão na janela
botao = tk.Button(janela, text="Clique Aqui", command=imprimir_mensagem)
botao.pack()

# Iniciando o loop principal da janela
janela.mainloop()
