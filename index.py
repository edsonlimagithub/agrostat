from selenium import webdriver
from selenium.webdriver.firefox.options import Options
#from selenium.webdriver.common.action_chains import ActionChains

import os
import time

from agrostat import Agrostat

options = Options()
profile = webdriver.FirefoxProfile();

executable_path = '../geckodriver'
dir_local = os.getcwd()
print(dir_local)

options.headless = True
options.set_preference("browser.download.folderList", 2)
options.set_preference("browser.download.manager.showWhenStarting", False)
options.set_preference("browser.download.dir", dir_local + "/files/")
options.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/x-gzip,application/vnd.ms-excel")

driver = webdriver.Firefox(executable_path= executable_path, options=options)

try:

    agrostat = Agrostat()
    agrostat.get_driver(driver)

    print('Acessando URL principal')
    url = 'https://indicadores.agricultura.gov.br/agrostat/index.htm'
    agrostat.initial_page(url)
    time.sleep(10)
    
    agrostat.get_iframe('/html/body/iframe')
    time.sleep(2)

    print('Clicar na aba "Exportação Importação"')
    agrostat.click_xpath('//td[text()="Exportação Importação"]')
    time.sleep(5)

    print('Clicar na aba "Produto por Região/UF/URF"')
    agrostat.click_xpath('//td[text()="Produto por Região/UF/URF para Bloco/País"]')
    time.sleep(5)
    
    print('Clicar na opcao "* TODOS OS PAISES *"')
    agrostat.click_xpath('//div[text()="* TODOS OS PAISES *"]')
    time.sleep(5)
    
    print('Clicar na opcao "* TODOS OS ESTADOS *"')
    agrostat.click_xpath('//div[text()="(Regiao) *TODOS OS ESTADOS*"]')
    time.sleep(5)
    
    #raise Exception('Exceção manual')
    
    print('Selecionar todos os produtos')
    agrostat.select_all_produts()
    time.sleep(5)
  
    print('Marcar Exportação')
    agrostat.click_xpath('//*[text()="Exportacao"]')
    time.sleep(2)

    print('Marcar Importação')
    agrostat.click_xpath('//*[text()="Importacao"]')
    time.sleep(2)

    print('Marcar Agronegócio')
    agrostat.click_xpath('//*[text()="Agronegócio"]/../div[1]')
    time.sleep(5)

    print('Descendo a página')
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

    time.sleep(5)

    print('Marcar 2020')
    agrostat.click_xpath('//*[text()="2020"]/../div[1]')
    time.sleep(5)

    print('Marcar 2021')
    agrostat.click_xpath('//*[text()="2021"]/../div[1]')
    time.sleep(5)

    print('Clicar em Download')
    agrostat.click_xpath('//div[@title="Enviar para Excel"]')
    time.sleep(20)
    
    driver.close()
    
except Exception as e:
    print(e)
    driver.close()

print('Script finalizado.')