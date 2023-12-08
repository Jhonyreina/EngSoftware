import csv
import Estoque

def ingrediente_existe(nome_ingrediente, lista_ingredientes):
    for ingrediente in lista_ingredientes:
        if ingrediente.nome.lower() == nome_ingrediente.lower():
            return True
    return False

def salvar_ingredientes_csv(ingredientes, arquivo):
    with open(arquivo, 'w', newline='') as arquivo_csv:
        escritor = csv.writer(arquivo_csv)
        for ingrediente in ingredientes:
            escritor.writerow(ingrediente.to_csv())

def carregar_ingredientes_csv(arquivo):
    ingredientes_carregados = []
    try:
        with open(arquivo, 'r') as arquivo_csv:
            leitor = csv.reader(arquivo_csv)
            for linha in leitor:
                ingrediente = Estoque.Ingredientes.from_csv(linha)
                ingredientes_carregados.append(ingrediente)
    except FileNotFoundError:
        pass
    return ingredientes_carregados

def preco_unitario(floatcust, floatpeso):
    preco_unit = floatcust/floatpeso
    return preco_unit