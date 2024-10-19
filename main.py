import pyautogui
import time
import pyperclip

def abrir_navegador():
    pyautogui.press('win')
    time.sleep(1)
    pyautogui.write('chrome')  # Ou o navegador que preferir
    pyautogui.press('enter')
    time.sleep(3)
    pyautogui.write('https://mail.google.com/')  # URL do Gmail ou Outlook
    pyautogui.press('enter')
    time.sleep(7)  # Tempo de carregamento do site (ajuste conforme necessário)

def abrir_email_assunto(assunto):
    screenshot = pyautogui.screenshot()
    localizacao = pyautogui.locateOnScreen('search_button.png')  # Imagem do botão de busca
    if localizacao is not None:
        pyautogui.click(localizacao)
        time.sleep(1)
        pyautogui.write(assunto) 
        pyautogui.press('enter')
        time.sleep(3)
        email_localizacao = pyautogui.locateOnScreen('email_item.png')  # Imagem de um item de e-mail
        if email_localizacao is not None:
            pyautogui.click(email_localizacao)
            time.sleep(2)
            return True
        else:
            print("E-mail não encontrado na lista.")
    else:
        print("Botão de busca não encontrado.")
    return False

def responder_email(mensagem):
    resposta_botao = pyautogui.locateOnScreen('reply_button.png')  # Botão "Responder"
    if resposta_botao is not None:
        pyautogui.click(resposta_botao)
        time.sleep(2)
        pyperclip.copy(mensagem)  # Copia a mensagem para a área de transferência
        pyautogui.hotkey('ctrl', 'v')  # Cola a mensagem
        time.sleep(2)
        pyautogui.hotkey('ctrl', 'enter')  # Envia a resposta usando Ctrl + Enter
    else:
        print("Botão 'Responder' não encontrado.")

def main():
    abrir_navegador()
    if abrir_email_assunto("Assunto importante"):  # Altere para o assunto desejado
        responder_email("Esta é uma resposta automática.")
    else:
        print("E-mail não encontrado.")

if __name__ == "__main__":
    main()
