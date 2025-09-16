# Importações
from selenium import webdriver
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
import os
import time
from datetime import date

load_dotenv()
user = os.environ['TELE_USER']
pwd  = os.environ['TELE_PASS']
today = date.today().strftime("%d/%m/%Y")

# abrindo navegador
navegador = webdriver.Chrome()
navegador.maximize_window()
# passando url para busca
navegador.get('https://upixnetworks.hubsoft.com.br/')

# email
navegador.find_element(By.XPATH, '//*[@id="input_2"]').send_keys(user)
navegador.find_element(By.XPATH, '//*[@id="stageForm"]/div[2]/button').click()
time.sleep(3)

# password
navegador.find_element(By.XPATH, '//*[@id="input_4"]').send_keys(pwd)
navegador.find_element(By.XPATH, '//*[@id="stageForm"]/div[2]/button').click()
time.sleep(20)

# Downloads relatorios
navegador.find_element(By.XPATH, '//*[@id="quick-panel-toggle"]').click()
time.sleep(5)

# Filtro de Data
navegador.find_element(By.XPATH, '/html/body/div[4]/md-dialog/md-dialog-content/hubsoft-fila-exportacao-relatorio/div[2]/div/md-datepicker[1]/div[1]/input').clear()
navegador.find_element(By.XPATH, '/html/body/div[4]/md-dialog/md-dialog-content/hubsoft-fila-exportacao-relatorio/div[2]/div/md-datepicker[1]/div[1]/input').send_keys(today)
time.sleep(5)
navegador.find_element(By.XPATH, "//body").click()
time.sleep(5)

# atualizar com filtro
navegador.find_element(By.XPATH, '/html/body/div[4]/md-dialog/md-dialog-content/hubsoft-fila-exportacao-relatorio/div[2]/button').click()
time.sleep(10)

# download
navegador.find_element(By.XPATH, '/html/body/div[4]/md-dialog/md-dialog-content/hubsoft-fila-exportacao-relatorio/hubsoft-multi-selection-table/div/div[1]/table/tbody/tr[1]/td[9]/span/b/a').click()
time.sleep(5)
navegador.find_element(By.XPATH, '/html/body/div[4]/md-dialog/md-dialog-content/hubsoft-fila-exportacao-relatorio/hubsoft-multi-selection-table/div/div[1]/table/tbody/tr[2]/td[9]/span/b/a').click()
time.sleep(5)
navegador.find_element(By.XPATH, '/html/body/div[4]/md-dialog/md-dialog-content/hubsoft-fila-exportacao-relatorio/hubsoft-multi-selection-table/div/div[1]/table/tbody/tr[3]/td[9]/span/b/a').click()
time.sleep(5)
navegador.find_element(By.XPATH, '/html/body/div[4]/md-dialog/md-dialog-content/hubsoft-fila-exportacao-relatorio/hubsoft-multi-selection-table/div/div[1]/table/tbody/tr[4]/td[9]/span/b/a').click()
time.sleep(5)
