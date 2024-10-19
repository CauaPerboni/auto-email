# Automação de E-mail

Este projeto usa PyAutoGui para automatizar a leitura e resposta de e-mails no Gmail ou Outlook.

## Funcionalidades

- Abre o navegador e acessa a interface de e-mail.
- Busca e abre um e-mail com base no assunto.
- Responde ao e-mail com uma mensagem predefinida ou inserida pelo usuário.
- Marca o e-mail como lido após a abertura.

## Requisitos

- Python 3.x
- PyAutoGui
- Pyperclip

## Instalação

Para instalar as dependências necessárias, você pode usar o `pip`. Execute os seguintes comandos em seu terminal:
    ```bash
    pip install pyautogui pyperclip

## Uso

1. Clonar o repositório: clone o repositório em seu computador:
    ```bash
    git clone https://github.com/seu_usuario/automacao_email.git

2. Navegar até o diretório do projeto: Use o terminal para acessar a pasta do projeto:
    ```bash
    cd automacao_email

3. Executar o script: Execute o script principal:
    ```bash
    python seu_script.py

Nota: Certifique-se de que seu navegador esteja instalado e que você esteja logado na conta de e-mail que deseja automatizar (Gmail ou Outlook).

4. Ajustes de Imagem: Verifique se as imagens de referência (capturas de tela) necessárias para a automação estão na pasta do projeto. As imagens devem incluir:

- search_button.png: Imagem do botão de busca.
- email_item.png: Imagem de um item de e-mail.
- reply_button.png: Imagem do botão "Responder".

5. Configurar Mensagens: Você pode personalizar a mensagem de resposta diretamente no código, ou modificar o código para receber uma entrada do usuário para a mensagem a ser enviada.




