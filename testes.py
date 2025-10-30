from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time



# Inicializando o driver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Acessando o GGAS
driver.get("https://ggas.copergas.com.br/ggas-teste-qintess")

# Encontrando a caixa de pesquisa e realizando uma ação
login = driver.find_element(By.ID, "login")
senha = driver.find_element(By.ID, "senha")
button = driver.find_element(By.ID, "button3")

login.send_keys("caroline.qintess")
senha.send_keys("Admin123")


button.click()


time.sleep(50) 




# Fechando o navegador
#driver.quit()