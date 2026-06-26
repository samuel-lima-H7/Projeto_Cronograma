import csv
import os
lista_tarefa = list()
def info(dia_da_semana, quantidade):
    for c in range(quantidade): 
        dados1 = list()
        print("-="*20)
        hora = input("Digite o inicio do compromisso: ")
        compromisso = input("Digite o compromisso: ")
        print("-=" * 20)
        dados1.append(dia_da_semana)
        dados1.append(hora)
        dados1.append(compromisso)
        lista_tarefa.append(dados1)
    return lista_tarefa

def armazena(informações):
    lista_info = informações
    with open("database.csv", "a", newline="", encoding="utf-8-sig") as arquivo:
        planilha = csv.writer(arquivo, delimiter=";")
        for a in lista_info:
            planilha.writerow([a[0], a[1], a[2]])


if __name__ == "__main__":
    sim_ou_não = str(input("Deseja armazenar alguma informação no arquivo? : ")).lower().strip()
    if sim_ou_não[0] == "s":
        dia = str(input("Digite o dia do qual quer agregar tarefas: "))
        while True:
            try:
                quant = int(input("Digite a quantidade de tarefas que deseja fazer: "))
                break
            except ValueError:
                print("Valor inválido, digite novamente.")
        dados_finais = info(dia, quant)
        armazena(dados_finais)