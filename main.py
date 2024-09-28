import requests
import smtplib
from email.mime.text import MIMEText

# Dados do ThingSpeak
THINGSPEAK_WRITE_API_KEY = 'SUA_WRITE_API_KEY'
THINGSPEAK_CHANNEL_ID = 'SEU_CHANNEL_ID'
THINGSPEAK_URL = f'https://api.thingspeak.com/update?api_key={THINGSPEAK_WRITE_API_KEY}'

# Função para enviar dados do estoque para o ThingSpeak
def enviar_dados_estoque(qtd_esmaltes, qtd_produtos):
    try:
        response = requests.get(f"{THINGSPEAK_URL}&field1={qtd_esmaltes}&field2={qtd_produtos}")
        if response.status_code == 200:
            print("Dados enviados com sucesso!")
        else:
            print(f"Falha ao enviar dados: {response.status_code}")
    except Exception as e:
        print(f"Erro ao conectar com ThingSpeak: {e}")

# Função para enviar notificação por email
def enviar_notificacao_email(mensagem):
    remetente = 'email_remetente@gmail.com'
    destinatario = 'destinatario@gmail.com'
    senha = 'senha_do_email_remetente'

    msg = MIMEText(mensagem)
    msg['Subject'] = 'Alerta de Estoque Baixo'
    msg['From'] = remetente
    msg['To'] = destinatario

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login(remetente, senha)
        server.sendmail(remetente, destinatario, msg.as_string())

# Função de monitoramento e notificação
def monitorar_estoque():
    qtd_esmaltes = 10  # Exemplo de quantidade
    qtd_produtos = 5   # Exemplo de quantidade

    enviar_dados_estoque(qtd_esmaltes, qtd_produtos)

    if qtd_esmaltes < 5:
        enviar_notificacao_email("Alerta: Estoque de esmaltes baixo!")
    if qtd_produtos < 3:
        enviar_notificacao_email("Alerta: Estoque de produtos baixo!")

if __name__ == "__main__":
    monitorar_estoque()
