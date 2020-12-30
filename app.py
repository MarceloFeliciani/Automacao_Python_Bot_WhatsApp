
# 1 - Importar bibliotecas necessárias
import pywhatkit # permite enviar mensagens para o whatsApp. Instalar com o pip install pywhatkit
import keybord # permite o uso do teclado. Instalar com o pip install keyboard
import time # permite estabelecer o tempo para envio de novas mensagens
from datetime import datetime  # permite utilizar data e hora específicas

# 2 - Definir para quais contatos enviar mensagens
contatos = ['+5551999927000', '+55519999270001'] # colocar os contatos da lista

# 3 - Definir intervalo de tempo
while len(contatos) >= 1:
    pywhatkit.sendwhatmsg(contatos[0], 'VAMOS AUTOMATIZAR TUDO!', datetime.now().hour, datetime.now().minute + 2) # vai esperar 2 minuots para enviar a mensagem para o contato index 0
    del contatos[0] # apaga o contato que recebeu a mensagem a anterior para não receber novamente
    time.sleep(60) # aguarda 60 segundos para próxima msg
    keybord.press_and_release('ctrl + w') # vai fechar a aba atual do navegador, para não abrir várias abas.

# 4 - Testes
# abrir o whatsApp Web, celular com internet funcionando, não mexer no mouse que clicar no play, pois a biblioteca "vê" os movimentos do mouse

