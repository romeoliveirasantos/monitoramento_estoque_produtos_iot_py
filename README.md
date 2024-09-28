Middleware IoT - Monitoramento de Estoque de Produtos de Manicure
Este projeto utiliza sensores para monitorar a quantidade de esmaltes e produtos de manicure em estoque. A plataforma ThingSpeak é usada para armazenar os dados coletados, e notificações são enviadas por e-mail quando o estoque está baixo, permitindo o reabastecimento.

Funcionalidades
Enviar dados de estoque (quantidade de esmaltes e produtos) para a plataforma ThingSpeak.
Monitorar os níveis de estoque em tempo real.
Enviar notificações por e-mail quando o estoque estiver baixo.
Requisitos
Antes de iniciar, certifique-se de ter as seguintes ferramentas instaladas:

Python 3.x
pip
VSCode
Dependências do Python

As bibliotecas a seguir são necessárias para executar o projeto:
**requests**: Para enviar os dados para a API ThingSpeak.
**smtplib**: Para envio de notificações por email (já incluso na biblioteca padrão do Python).
**paho-mqtt**: Caso você use sensores com protocolo MQTT (opcional).
Instalação
1. Clonar o Repositório
Clone este repositório na sua máquina local:
git clone https://github.com/seu-usuario/seu-repositorio.git

2. Criar Ambiente Virtual
No diretório do projeto, crie e ative um ambiente virtual Python:
   

  ```
      python -m venv venv
      Ativando:
      No Windows - .\venv\Scripts\activate
      No Linux/Mac - source venv/bin/activate
  ```

3. Instalar Dependências
Instale as dependências listadas no arquivo requirements.txt:

  
  ```
    pip install -r requirements.txt
    Caso você não tenha o requirements.txt ainda, você pode criar um assim:
    pip install requests paho-mqtt
    pip freeze > requirements.txt
  ```

4. Criar Conta no ThingSpeak
Acesse o ThingSpeak e crie uma conta.
Crie um canal para monitorar os dados de estoque.
Anote as API keys fornecidas pelo ThingSpeak, pois você precisará delas no código.

```
    Configuração

    1. Configurar a API do ThingSpeak
    No arquivo main.py, insira suas chaves da API do ThingSpeak:

  
    THINGSPEAK_WRITE_API_KEY = 'SUA_WRITE_API_KEY'
    THINGSPEAK_CHANNEL_ID = 'SEU_CHANNEL_ID'
    2. Configurar Envio de Email
    Ainda no main.py, configure as credenciais de email para enviar notificações quando o estoque estiver baixo:

    remetente = 'seuemail@gmail.com'
    destinatario = 'destinatario@gmail.com'
    senha = 'sua_senha'
    Para usar o Gmail, você pode precisar ativar a opção "Acesso a aplicativos menos seguros" na sua conta do Google ou configurar uma senha de aplicativo se estiver usando a autenticação em duas etapas.
```
  Uso
  1. Executar o Script
  Execute o arquivo main.py para iniciar o monitoramento e o envio de dados para o ThingSpeak:
  
  ```
     python main.py
  ```   
  2. Monitoramento
  O script envia dados para o ThingSpeak, atualizando as quantidades de esmaltes e produtos no estoque.
  Quando o estoque estiver abaixo de um nível específico, um email de alerta será enviado automaticamente.
  Estrutura do Projeto

```
    middleware-iot-estoque/
    │
    ├── main.py             # Script principal para monitorar o estoque e enviar notificações
    ├── notificacao.py      # (Opcional) Módulo separado para envio de notificações
    ├── README.md           # Instruções e informações sobre o projeto
    ├── requirements.txt    # Dependências do projeto
    └── venv/               # Ambiente virtual (não incluído no GitHub)
    Personalização
    Intervalo de tempo: Modifique o intervalo de tempo para o monitoramento contínuo, se necessário.
    Níveis de estoque: Altere os valores que disparam as notificações de estoque baixo dentro da função monitorar_estoque().
```