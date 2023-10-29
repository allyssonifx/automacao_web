from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Configurar o driver do navegador
# Certifique-se de ter o driver correto para o navegador instalado e configurado
driver = webdriver.Chrome()
first = True
paths = ['/html/body/div[2]/div[2]/main/div/div[2]/article/div/table/tbody/tr[1]/td[4]/small/a','/html/body/div[2]/div[2]/main/div/div[2]/article/div/table/tbody/tr[2]/td[3]/p/small/a','/html/body/div[2]/div[2]/main/div/div[2]/article/div/table/tbody/tr[3]/td[3]/p/small/a','/html/body/div[2]/div[2]/main/div/div[2]/article/div/table/tbody/tr[4]/td[3]/p/small/a','/html/body/div[2]/div[2]/main/div/div[2]/article/div/table/tbody/tr[5]/td[4]/p/small/a','/html/body/div[2]/div[2]/main/div/div[2]/article/div/table/tbody/tr[6]/td[3]/p/small/a','/html/body/div[2]/div[2]/main/div/div[2]/article/div/table/tbody/tr[7]/td[3]/p/small/a','/html/body/div[2]/div[2]/main/div/div[2]/article/div/table/tbody/tr[9]/td[4]/p/small/a','/html/body/div[2]/div[2]/main/div/div[2]/article/div/table/tbody/tr[10]/td[3]/p/small/a','/html/body/div[2]/div[2]/main/div/div[2]/article/div/table/tbody/tr[11]/td[3]/p/small/a','/html/body/div[2]/div[2]/main/div/div[2]/article/div/table/tbody/tr[12]/td[3]/p/a','/html/body/div[2]/div[2]/main/div/div[2]/article/div/table/tbody/tr[13]/td[4]/p/small/a','/html/body/div[2]/div[2]/main/div/div[2]/article/div/table/tbody/tr[14]/td[3]/p[1]/small/a','/html/body/div[2]/div[2]/main/div/div[2]/article/div/table/tbody/tr[15]/td[3]/p[1]/small/a','/html/body/div[2]/div[2]/main/div/div[2]/article/div/table/tbody/tr[16]/td[3]/p/small/a','/html/body/div[2]/div[2]/main/div/div[2]/article/div/table/tbody/tr[17]/td[3]/p[1]/small/a','/html/body/div[2]/div[2]/main/div/div[2]/article/div/table/tbody/tr[18]/td[3]/p[1]/small/a','/html/body/div[2]/div[2]/main/div/div[2]/article/div/table/tbody/tr[19]/td[3]/p/small/a','/html/body/div[2]/div[2]/main/div/div[2]/article/div/table/tbody/tr[20]/td[3]/p/small/a','/html/body/div[2]/div[2]/main/div/div[2]/article/div/table/tbody/tr[21]/td[3]/p[1]/small/a','/html/body/div[2]/div[2]/main/div/div[2]/article/div/table/tbody/tr[22]/td[3]/p/small/a','/html/body/div[2]/div[2]/main/div/div[2]/article/div/table/tbody/tr[23]/td[3]/p/small/a','/html/body/div[2]/div[2]/main/div/div[2]/article/div/table/tbody/tr[23]/td[3]/p/small/a','/html/body/div[2]/div[2]/main/div/div[2]/article/div/table/tbody/tr[24]/td[3]/p[1]/small/a','/html/body/div[2]/div[2]/main/div/div[2]/article/div/table/tbody/tr[25]/td[3]/p/small/a','/html/body/div[2]/div[2]/main/div/div[2]/article/div/table/tbody/tr[26]/td[3]/p/small/a','/html/body/div[2]/div[2]/main/div/div[2]/article/div/table/tbody/tr[27]/td[3]/p[1]/small/a','/html/body/div[2]/div[2]/main/div/div[2]/article/div/table/tbody/tr[28]/td[4]/p/small/a','/html/body/div[2]/div[2]/main/div/div[2]/article/div/table/tbody/tr[29]/td[3]/p/small/a','/html/body/div[2]/div[2]/main/div/div[2]/article/div/table/tbody/tr[30]/td[3]/p/small/a','/html/body/div[2]/div[2]/main/div/div[2]/article/div/table/tbody/tr[31]/td[3]/p/small/a','/html/body/div[2]/div[2]/main/div/div[2]/article/div/table/tbody/tr[32]/td[3]/p/small/a','/html/body/div[2]/div[2]/main/div/div[2]/article/div/table/tbody/tr[33]/td[3]/p/small/a','/html/body/div[2]/div[2]/main/div/div[2]/article/div/table/tbody/tr[34]/td[4]/p[1]/small/a','/html/body/div[2]/div[2]/main/div/div[2]/article/div/table/tbody/tr[35]/td[3]/p[1]/small/a','/html/body/div[2]/div[2]/main/div/div[2]/article/div/table/tbody/tr[36]/td[3]/p[1]/small/a','/html/body/div[2]/div[2]/main/div/div[2]/article/div/table/tbody/tr[37]/td[3]/p/small/a','/html/body/div[2]/div[2]/main/div/div[2]/article/div/table/tbody/tr[38]/td[3]/p[1]/small/a','/html/body/div[2]/div[2]/main/div/div[2]/article/div/table/tbody/tr[39]/td[4]/p[1]/small/a','/html/body/div[2]/div[2]/main/div/div[2]/article/div/table/tbody/tr[40]/td[3]/p[1]/small/a','/html/body/div[2]/div[2]/main/div/div[2]/article/div/table/tbody/tr[41]/td[3]/p[1]/small/a','/html/body/div[2]/div[2]/main/div/div[2]/article/div/table/tbody/tr[42]/td[3]/p[1]/small/a','/html/body/div[2]/div[2]/main/div/div[2]/article/div/table/tbody/tr[43]/td[3]/p[1]/small/a','/html/body/div[2]/div[2]/main/div/div[2]/article/div/table/tbody/tr[44]/td[3]/p[1]/small/a','/html/body/div[2]/div[2]/main/div/div[2]/article/div/table/tbody/tr[45]/td[3]/p[1]/small/a','/html/body/div[2]/div[2]/main/div/div[2]/article/div/table/tbody/tr[46]/td[3]/p[1]/small/a']
# Acessar o site
paths.remove('/html/body/div[2]/div[2]/main/div/div[2]/article/div/table/tbody/tr[12]/td[3]/p/a')
c = 1
for p in paths:
    print(c)
    driver.get('https://www.iucnredlist.org/resources/spatial-data-download')


    # Encontrar o campo de login e inserir o valor
    driver.find_element('xpath', p).click()
    sleep(2)
    if first:
        driver.find_element('xpath', '/html/body/div[2]/div[2]/main/div/div/a').click()
        sleep(2)
        driver.find_element('xpath', '/html/body/div[6]/div/div/div/form/div[1]/input').send_keys('allysson.soemail@gmail.com')
        driver.find_element('xpath', '/html/body/div[6]/div/div/div/form/div[2]/input').send_keys('Abacaxi123')
        driver.find_element('xpath', '/html/body/div[6]/div/div/div/form/div[3]/label').click()
        driver.find_element('xpath', '/html/body/div[6]/div/div/div/form/div[4]/button').click()
        first=False
    sleep(1)
    driver.find_element('xpath', '/html/body/div[5]/div/div/div/div/div/textarea').send_keys('download'+str(c))
    driver.find_element('xpath', '/html/body/div[5]/div/div/div/button[3]').click()
    sleep(1)
    driver.find_element('xpath', '/html/body/div[5]/div/div/div/div/div/div[1]/input[1]').click()
    driver.find_element('xpath', '/html/body/div[5]/div/div/div/button[3]').click()
    sleep(1)
    driver.find_element('xpath', '/html/body/div[5]/div/div/div/div/div/div/label').click()
    driver.find_element('xpath', '/html/body/div[5]/div/div/div/button[3]').click()
    sleep(1)
    driver.find_element('xpath', '/html/body/div[5]/div/div/div/button').click()
    c+=1
    sleep(1)
# Encontrar o campo de senha e inserir o valor
# password_field = driver.find_element(By.ID, 'password-field')
# password_field.send_keys('sua_senha')

# # Encontrar o botão de login e clicar nele
# login_button = driver.find_element(By.ID, 'login-button')
# login_button.click()

# # Aguardar a página de login ser carregada completamente
# wait = WebDriverWait(driver, 10)
# wait.until(EC.url_to_be('https://www.example.com/dashboard'))

# Realizar outras ações na página logada...

# Fechar o navegador
driver.quit()
