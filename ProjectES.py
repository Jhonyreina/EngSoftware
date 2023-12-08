import tkinter as tk
from tkinter import Tk, Text, Button
from tkinter import simpledialog
import csv

class Ingredientes:
    def __init__(self, nome, quantidade):
        self.nome = nome
        self.quantidade = quantidade

    def __str__(self):
        return f"{self.quantidade} unidades de {self.nome}"

    def to_csv(self):
        return [self.nome, str(self.quantidade)]

    @classmethod
    def from_csv(cls, dados):
        return cls(dados[0], float(dados[1]))

def ingrediente_existe(nome_ingrediente):
    for ingrediente in lista_ingredientes:
        if ingrediente.nome.lower() == nome_ingrediente.lower():
            return True
    return False

def adicionar_ingrediente():
    nome_ingrediente = simpledialog.askstring("Adicionar ingrediente", "Digite o nome do ingrediente a ser adicionado:")
    quantidade_ingrediente = simpledialog.askfloat("Quantidade do ingrediente", "Digite a quantidade ou peso a ser utilizado:")

    if nome_ingrediente and quantidade_ingrediente:
        # Verifica se o ingrediente já está na lista
        if not ingrediente_existe(nome_ingrediente):
            ingrediente = Ingredientes(nome_ingrediente, float(quantidade_ingrediente))
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
    
    mostrar_ingredientes()

def modificar_ingrediente():
    nome_ingrediente = simpledialog.askstring("Modificar Ingrediente", "Digite o nome do ingrediente a ser modificado:")
    
    for ingrediente in lista_ingredientes:
        if ingrediente.nome.lower() == nome_ingrediente.lower():
            nova_quantidade = simpledialog.askfloat("Modificar Ingrediente", f"Digite a nova quantidade para {ingrediente.nome}:")
            ingrediente.quantidade = nova_quantidade if nova_quantidade is not None else ingrediente.quantidade
            break
    
    mostrar_ingredientes()

def salvar_ingredientes():
    salvar_ingredientes_csv(lista_ingredientes)

def mostrar_ingredientes():
    resultado.delete(1.0, "end")  # Limpa o conteúdo atual do widget Text

    resultado.insert("1.0", "Ingredientes:\n")

    #lista_ingredientes_carregados = carregar_ingredientes_csv()
    #uniao_sinistra = set(lista_ingredientes).union(lista_ingredientes_carregados)
    #lista_ingredientes.extend(lista_ingredientes_carregados)
    for ingrediente in lista_ingredientes:
        resultado.insert("end", f"\n{ingrediente}")

def salvar_ingredientes_csv(ingredientes):
    with open('ingredientes.csv', 'w', newline='') as arquivo_csv:
        escritor = csv.writer(arquivo_csv)
        for ingrediente in ingredientes:
            escritor.writerow(ingrediente.to_csv())

def carregar_ingredientes_csv():
    ingredientes_carregados = []
    try:
        with open('ingredientes.csv', 'r') as arquivo_csv:
            leitor = csv.reader(arquivo_csv)
            for linha in leitor:
                ingrediente = Ingredientes.from_csv(linha)
                ingredientes_carregados.append(ingrediente)
    except FileNotFoundError:
        pass
    return ingredientes_carregados

# Lista para armazenar os ingredientes
lista_ingredientes = []
lista_ingredientes_carregados = carregar_ingredientes_csv()
lista_ingredientes.extend(lista_ingredientes_carregados)

# Cria a janela principal
janela = tk.Tk()
janela.title("Gestão de Ingredientes")

# Define o tamanho da janela
largura = 600
altura = 600
janela.geometry(f"{largura}x{altura}")

botao_adicionar = tk.Button(janela, text="Adicionar Ingrediente", command=adicionar_ingrediente)
botao_adicionar.pack()

botao_remover = tk.Button(janela, text="Remover Ingrediente", command=remover_ingrediente)
botao_remover.pack()

botao_modificar = tk.Button(janela, text="Modificar Ingrediente", command=modificar_ingrediente)
botao_modificar.pack()

botao_mostrar = tk.Button(janela, text="Mostrar Ingredientes", command=mostrar_ingredientes)
botao_mostrar.pack()

botao_salvar = tk.Button(janela, text="Salvar Ingredientes", command=salvar_ingredientes)
botao_salvar.pack()

#botao_carregar = tk.Button(janela, text="Carregar Ingredientes", command=mostrar_ingredientes)
#botao_carregar.pack()

resultado = Text(janela, height=10, width=40)
resultado.pack()

# Inicia o loop principal da interface gráfica
janela.mainloop()
