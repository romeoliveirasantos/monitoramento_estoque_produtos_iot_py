import smtplib
from email.mime.text import MIMEText

def enviar_notificacao_email(mensagem):
    remetente = 'seuemail@gmail.com'
    destinatario = 'destinatario@gmail.com'
    senha = 'sua_senha'

    msg = MIMEText(mensagem)
    msg['Subject'] = 'Alerta de Estoque Baixo'
    msg['From'] = remetente
    msg['To'] = destinatario

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login(remetente, senha)
        server.sendmail(remetente, destinatario, msg.as_string())
