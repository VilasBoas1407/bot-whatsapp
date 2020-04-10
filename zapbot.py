from selenium import webdriver
import time

class WhatsappBot:
    def __init__(self):
        self.mensagem = "Teste de bot utilizando Python"
        self.grupos = ["Eu"]
        options = webdriver.ChromeOptions();
        options.add_argument('lang=pt-br')
        self.driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')

    def EnviarMensagens(self):

        self.driver.get('https://web.whatsapp.com/')
        time.sleep(30)
        for grupo in self.grupos:    
            grupo = self.driver.find_element_by_xpath(f"//span[@title='{grupo}']")
            time.sleep(1)
            grupo.click()
            chat_box = self.driver.find_element_by_class_name('_1Plpp')
            time.sleep(1)
            chat_box.click()
            chat_box.send_keys(self.mensagem)
            time.sleep(1)
            botao_enviar = self.driver.find_element_by_xpath('//span[@data-icon="send"]')
            botao_enviar.click()
            time.sleep(3)

bot = WhatsappBot()
bot.EnviarMensagens()

