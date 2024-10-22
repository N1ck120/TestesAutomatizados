from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

# Configuração do ChromeDriver
chrome_options = Options()
#chrome_options.add_argument("--headless")  # Opcional, para rodar em modo headless
chrome_options.add_argument("--disable-gpu")

service = Service('./chromedriver-win64/chromedriver.exe')  # Insira o caminho do seu ChromeDriver
driver = webdriver.Chrome(service=service, options=chrome_options)

# Acesse a página do leilão
driver.get("http://127.0.0.1:5500/index.html")

# Aguarde a página carregar completamente
time.sleep(2)

# Encontre o campo de input e o botão de envio
input_element = driver.find_element(By.ID, "input")
button_element = driver.find_element(By.ID, "btn")

# Teste com valor abaixo de 4000
valor_abaixo = 3500
input_element.clear()  # Limpa o campo de input
input_element.send_keys(str(valor_abaixo))  # Preenche com valor abaixo de 4000
button_element.click()  # Clica no botão de envio
print(f"Valor enviado: {valor_abaixo}")
time.sleep(2)  # Aguarda 2 segundos para observar o efeito

# Teste com valor acima de 4000
valor_acima = 4500
input_element.clear()  # Limpa o campo de input
input_element.send_keys(str(valor_acima))  # Preenche com valor acima de 4000
button_element.click()  # Clica no botão de envio
print(f"Valor enviado: {valor_acima}")
time.sleep(2)  # Aguarda 2 segundos para observar o efeito

# Fechar o navegador
driver.quit()
