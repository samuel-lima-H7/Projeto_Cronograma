#IMPORTAÇÃO DAS BIBLIOTECAS
from Leitura import leitura, data_atual
import smtplib
import os
from dotenv import load_dotenv
from email.mime.text import MIMEText
from datetime import datetime, timezone, timedelta

#DEFINIÇÃO DA HORA EM BRASILIA A CONCIDERAR O ATRASO DE 3 HORAS
fuso_brasilia = timezone(timedelta(hours=-3))
hora_atual = datetime.now(fuso_brasilia).strftime("%H:%M")

if os.path.exists(".env"):
    load_dotenv()

#FUNÇÃO QUE RECEBE A LISTA E LE E CRIA UMA MENSAGEM
def mensagem_enviar(parametro_tarefas):
    if not parametro_tarefas:
        return "Você não tem compromissos agendados para hoje! Aproveite o dia."
    mensagem_str = ''
    for c in parametro_tarefas:
        mensagem = f"Hoje as {c[0]}, você tem o seguinte compromisso: {c[1]}"
        mensagem_str += f"""{mensagem} \n \n"""
    return mensagem_str

#LÊ AS INFORMAÇÕES DE OUTRA ARQUIVO E DEFINE A MENSAGEM
lista_de_hoje = leitura()
mensagem_final = mensagem_enviar(lista_de_hoje)
print(mensagem_final)

#DEFINIÇÃO DE VARIÁVEIS PARA ENVIO DE E-MAIL
remetente = os.environ.get("EMAIL_USER")
senha = os.environ.get("EMAIL_PASS")
destinatario = "Wplimaw01@gmail.com"
msg = MIMEText(f" CUMPRA SEUS COMPROMISSOS: \n \n {mensagem_final}", "plain")
msg["From"] = remetente
msg["To"] = destinatario
msg["Subject"] = f"Cronograma de Hoje - {data_atual.capitalize()}, horário: {hora_atual}"

#ENVIA O E-MAIL
with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
    server.login(remetente, senha)
    server.send_message(msg)
    print("E-mail enviado com sucesso!")