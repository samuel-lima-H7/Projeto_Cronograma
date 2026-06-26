from datetime import datetime, timezone, timedelta
import csv
import os

dias_semana = {
    "Monday": "segunda",
    "Tuesday": "terça",
    "Wednesday": "quarta",
    "Thursday": "quinta",
    "Friday": "sexta",
    "Saturday": "sábado",
    "Sunday": "domingo"
}

fuso_brasilia = timezone(timedelta(hours=-3))
data = datetime.now(fuso_brasilia)
hoje_ingles = data.strftime("%A")
data_atual = dias_semana.get(hoje_ingles, "segunda")

def leitura():

    dados = list()
    try:
        with open("database.csv", "r", newline="", encoding="utf-8-sig") as conteudo:
            info_arquivo = csv.reader(conteudo, delimiter=";")
            for linha, valor in enumerate(info_arquivo):
                if linha == 0 or not valor: # Proteção contra linhas vazias
                    continue
                dia_inserido = str(valor[0].lower().strip())
                if dia_inserido == data_atual:
                    tarefas_hora = [valor[1], valor[2]]
                    dados.append(tarefas_hora)
    except FileNotFoundError:
        print("Arquivo de dados ainda não existe.")
    return dados

print(leitura())