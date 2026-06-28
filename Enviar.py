from Lei
import smtplib
import os
from dotenv import load_dotenv
from email.mime.text import MIMEText
from datetime import datetime, timezone, timedelta

if os.path.exists(".env"):
    load_dotenv()

remetente = os.environ.get("EMAIL_USER")
senha = os.environ.get("EMAIL_PASS")
destinatario = "samuel.aguiar0106@gmail.com"

def mensagem_enviar(parametro_tarefas):
    if not parametro_lista:
        return "Você não tem compromissos agendados para hoje! Aproveite o dia."

    mensagem_str = ''
    for c in parametro_tarefas:
        mensagem = f"Hoje as {c[0]}, voce tem o seguinte compromisso: {c[1]}"
        mensagem_str += f"{mensagem} \n"
    return mensagem_str

lista_de_hoje = 
mensagem_final = mensagem_funcion(lista_de_hoje)
print(mensagem_final)

msg = MIMEText(f"{mensagem_final}", "plain")
msg["From"] = remetente
msg["To"] = destinatario

# CORREÇÃO: Força o Python a calcular o horário oficial de Brasília (-3 horas em relação ao UTC)
fuso_brasilia = timezone(timedelta(hours=-3))
hora_atual = datetime.now(fuso_brasilia).strftime("%H:%M")

# Agora você pode colocar o horário no assunto com total segurança!
msg["Subject"] = f"Cronograma de Hoje - {Arquivo_Notifica.data_atual.capitalize()}, horário: {hora_atual}"

# Só envia o e-mail se as credenciais existirem (evita travar o GitHub Actions)
with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(remetente, senha)
        server.send_message(msg)
        print("E-mail enviado com sucesso!")