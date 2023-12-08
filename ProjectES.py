import Estoque
import Funcoes
import tkinter as tk
from tkinter import Text
from tkinter import simpledialog


def adicionar_ingrediente():                                                                                                           
    nome_ingrediente = simpledialog.askstring("Adicionar item ao estoque", "Digite o nome do produto a ser adicionado:")                
    quantidade_ingrediente = simpledialog.askfloat("Quantidade total em gramas ou mililitros", "Digite a quantidade quem vem em uma embalagem do produto:")
    preco_ingrediente = simpledialog.askfloat("Valor do produto", "Digite o valor que foi pago pelo produto:")

    if nome_ingrediente and quantidade_ingrediente and preco_ingrediente:
        # Verifica se o ingrediente já está na lista
        if not Funcoes.ingrediente_existe(nome_ingrediente,lista_ingredientes):
            ingrediente = Estoque.Ingredientes(nome_ingrediente, float(quantidade_ingrediente), float(preco_ingrediente))
            lista_ingredientes.append(ingrediente)
        else:
            tk.messagebox.showwarning("Aviso", f"O ingrediente '{nome_ingrediente}' já está na lista.")
    mostrar_ingredientes()



def remover_ingrediente():
    nome_ingrediente = simpledialog.askstring("Remover Ingrediente", "Digite o nome do ingrediente a ser removido:")
    
    for ingrediente in lista_ingredientes:
        if ingrediente.nome.lower() == nome_ingrediente.lower():
            lista_ingredientes.remove(ingrediente)
            break
        else:
            tk.messagebox.showwarning("Aviso", f"O ingrediente '{nome_ingrediente}' não existe no estoque.")
            break  
    
    mostrar_ingredientes()

def modificar_ingrediente():
    nome_ingrediente = simpledialog.askstring("Modificar Ingrediente", "Digite o nome do ingrediente a ser modificado:")
    
    for ingrediente in lista_ingredientes:
        if ingrediente.nome.lower() == nome_ingrediente.lower():
            novo_preco = simpledialog.askfloat("Modificar Ingrediente", f"Digite a novo preco em R$ para {ingrediente.nome}:")
            nova_quantidade = simpledialog.askfloat("Modificar Ingrediente", f"Digite a nova quantidade em gramas ou mililitros para {ingrediente.nome}:")
            ingrediente.preco = novo_preco if novo_preco is not None else ingrediente.preco
            ingrediente.quantidade = nova_quantidade if nova_quantidade is not None else nova_quantidade.preco
            break
        else:
            tk.messagebox.showwarning("Aviso", f"O ingrediente '{nome_ingrediente}' não existe no estoque.")
            break        
    
    mostrar_ingredientes()

def salvar_ingredientes():
    Funcoes.salvar_ingredientes_csv(lista_ingredientes, nome_doc)

def mostrar_ingredientes():
    resultado.delete(1.0, "end")  # Limpa o conteúdo atual do widget Text

    resultado.insert("1.0", "Ingredientes  |   Preço   |   Quantidade  \n")

    for ingrediente in lista_ingredientes:
        resultado.insert("end", f"\n{ingrediente}")

def mostrar_ingredientes_receita():
    resultado.delete(1.0, "end")  # Limpa o conteúdo atual do widget Text

    resultado.insert("1.0", "Receita:\n")

    preco_total = 0
    for x in lista_ingredientes_receita:
        resultado.insert("end", f"\n{x[2]}g de {x[0]}, R$ {float(x[1]):.2f}")
        preco_total += float(x[1])

    resultado.insert("end", f"\n\npreço total: R$ {float(preco_total):.2f}")

def criar_receita():
    nome_ingrediente = simpledialog.askstring("Adicionar ingrediente", "Insira o nome do ingrediente que deseja utilizar")
    quant_ingrediente = simpledialog.askfloat("Quantidade ingrediente", "Insira a quantidade do ingrediente que deseja utilizar (g ou ml)")

    for ingrediente in lista_ingredientes:
        if ingrediente.nome.lower() == nome_ingrediente.lower():

            valor_total = Funcoes.preco_unitario(ingrediente.preco, ingrediente.quantidade)*quant_ingrediente
            peso = quant_ingrediente
            
            trinca = (ingrediente.nome, valor_total, peso)

            lista_ingredientes_receita.append(trinca)
            break        
        else:
            tk.messagebox.showwarning("Aviso", f"O ingrediente '{nome_ingrediente}' não existe no estoque.")
            break
    mostrar_ingredientes_receita()

def reiniciar_receita():
    lista_ingredientes_receita.clear()
    resultado.delete(1.0, "end")  # Limpa o conteúdo atual do widget Text
    resultado.insert("1.0", "Receita:\n")    

# Lista para armazenar os ingredientes
lista_ingredientes = []
nome_doc = 'ingredientes.csv'
lista_ingredientes_carregados = Funcoes.carregar_ingredientes_csv(nome_doc)
lista_ingredientes.extend(lista_ingredientes_carregados)
lista_ingredientes_receita = []

# Cria a janela principal
janela = tk.Tk()
janela.title("Gestão de Ingredientes")

# Define o tamanho da janela
largura = 1000
altura = 550
janela.geometry(f"{largura}x{altura}")

botao_adicionar = tk.Button(janela, text="Adicionar Ingrediente", height = 1, width = 18, command=adicionar_ingrediente)
botao_adicionar.place(x=5,y=20)

botao_remover = tk.Button(janela, text="Remover Ingrediente", height = 1, width = 18,command=remover_ingrediente)
botao_remover.place(x=5,y=50)

botao_modificar = tk.Button(janela, text="Modificar Ingrediente", height = 1, width = 18, command=modificar_ingrediente)
botao_modificar.place(x=5,y=80)

botao_mostrar = tk.Button(janela, text="Mostrar Ingredientes", height = 1, width = 18, command=mostrar_ingredientes)
botao_mostrar.place(x=5,y=110)

botao_salvar = tk.Button(janela, text="Salvar Ingredientes", height = 1, width = 18, command=salvar_ingredientes)
botao_salvar.place(x=5,y=140)

resultado = Text(janela, height=30, width=100)
resultado.place(x=150, y = 20)

botao_cria_receita = tk.Button(janela, text="Adicionar a receita",height = 1, width = 18, command=criar_receita)
botao_cria_receita.place(x=5,y=410)

botao_reiniciar_receita = tk.Button(janela, text="Reiniciar receita",height = 1, width = 18, command=reiniciar_receita)
botao_reiniciar_receita.place(x=5,y=440)

botao_mostrar_receita = tk.Button(janela, text="Mostrar receita",height = 1, width = 18, command=mostrar_ingredientes_receita)
botao_mostrar_receita.place(x=5,y=470)

janela.mainloop()
