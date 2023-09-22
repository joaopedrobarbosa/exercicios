#importar bibliotecas
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time

# navegar até o whatsapp web
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://web.whatsapp.com/')
time.sleep(10)

#definir contatos e grupos para enviar mensagem
contatos = ['Luis Claudio']
mensagem = 'E ai viadinho' 
print(mensagem)

#campo de mensagem privada
def buscar_contato(contato):
    campo_pesquisa = driver.find_element("xpath",'//div[contains(@class, "copyable-text selectable-text")]')
    time.sleep(3)
    campo_pesquisa.click()
    campo_pesquisa.send_keys(contato)
    campo_pesquisa.send_keys(Keys.ENTER)


def enviar_mensagem(mensagem):
    for c in range(0,100):
        campo_mensagem = driver.find_element("xpath",'//p[contains(@class, "selectable-text copyable-text")]')
        campo_mensagem.click() 
        time.sleep(1)
        campo_mensagem.send_keys(mensagem)
        campo_mensagem.send_keys(Keys.ENTER)
    
    campo_mensagem.send_keys(Keys.ENTER)

for contato in contatos:
    buscar_contato(contato)
    enviar_mensagem(mensagem)

#' copyable-text selectable-text'