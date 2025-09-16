# Importações
from selenium import webdriver
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
import os
import time

load_dotenv()
user = os.environ['TELE_USER']
pwd  = os.environ['TELE_PASS']


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
time.sleep(5)

#relatorios
navegador.find_element(By.XPATH, '//*[@id="vertical-navigation"]/ms-navigation/ul/li/ul/li[12]/div/a/span').click()
time.sleep(5)

# contas a vencer
navegador.find_element(By.XPATH, '//*[@id="board-selector"]/div/div[9]').click()
time.sleep(5)
navegador.find_element(By.XPATH, '//*[@id="select_value_label_66"]/span[1]').click()
navegador.find_element(By.XPATH, '//*[@id="select_option_85"]').click()
navegador.find_element(By.XPATH, '//*[@id="select_value_label_163"]/span[1]').click()
navegador.find_element(By.XPATH, '//*[@id="select_option_170"]').click()
time.sleep(5)

# gerar relatório
navegador.find_element(By.XPATH, '//*[@id="configuracao-geral-servico-editar"]/div[2]/div/div/form/div/div/div[5]/button').click()
time.sleep(5)

# Filtros de campos
navegador.find_element(By.XPATH, '//*[@id="configuracao-geral-servico-editar"]/div[2]/div/div/div/div/hubsoft-relatorio/div/div[2]/button[4]').click()
time.sleep(5)

# Seleciona Todas colunas
navegador.find_element(By.XPATH, '//*[@id="dialogContent_199"]/md-checkbox/div[2]/span').click()
time.sleep(3)
navegador.find_element(By.XPATH, '/html/body/div[6]/md-dialog/form/md-toolbar/div/div/button[3]').click()
time.sleep(3)

# Baixa Excel
navegador.find_element(By.XPATH, '//*[@id="configuracao-geral-servico-editar"]/div[2]/div/div/div/div/hubsoft-relatorio/div/div[2]/button[1]').click()
time.sleep(3)