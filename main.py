import requests
from notificacao import enviar_notificacao_email

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

# Função de monitoramento e notificação
def monitorar_estoque():
    qtd_esmaltes = 10  
    qtd_acetona = 7   
    qtd_algodao = 5

    enviar_dados_estoque(qtd_esmaltes, qtd_acetona,qtd_algodao )

    if qtd_esmaltes < 5:
        enviar_notificacao_email("Alerta: Estoque de esmaltes baixo!")
    if qtd_acetona < 3:
        enviar_notificacao_email("Alerta: Estoque de acetona baixo!")
    if qtd_algodao < 2:
        enviar_notificacao_email("Alerta: Estoque de algodão baixo!")

if __name__ == "__main__":
    monitorar_estoque()
