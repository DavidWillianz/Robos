import chromedriver_binary
import time
import os

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium import webdriver

class RoboYoutube():
    def __init__(self):
        path_chromedriver = os.getcwd() + '\\chromedriver-win64\\chromedriver.exe'
        service = Service(executable_path=path_chromedriver)

        self.driver = webdriver.Chrome(service=service)
        self.url_base = 'https://www.youtube.com/results?search_query='

    def iniciar(self, busca):
        url_pesquisa = self.url_base + str(busca)

        self.driver.get(url_pesquisa)
        time.sleep(0.5)
        self.pegar_informacoes()
    
    def pegar_informacoes(self):
        titulos = self.driver.find_elements(By.XPATH, '//*[@id="video-title"]/yt-formatted-string')

        for titulo in titulos:
            print('Video encontrado! - titulo: ' + titulo.text)

        
        print('\033[36mPesquisa finalizada com sucesso!\033[0m')

robo_youtube = RoboYoutube()
robo_youtube.iniciar('python')