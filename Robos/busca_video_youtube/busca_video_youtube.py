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

    def iniciar(self) -> None:
        pesquisa = input('Escreva aqui o que voçê deseja pesquisar: ')
        url_pesquisa = self.url_base + pesquisa

        self.driver.get(url_pesquisa)
        time.sleep(0.5)
        self.pegar_informacoes()
    
    def pegar_informacoes(self) -> None:
        titulos_videos = []

        QUANTIDADE_PAGINAS = 5
        pagina_atual = 1

        while pagina_atual < QUANTIDADE_PAGINAS:
            titulos = self.driver.find_elements(By.XPATH, '//*[@id="video-title"]/yt-formatted-string')

            self.escrever_titulos(titulos, titulos_videos)
            self.realizar_paginacao(pagina_atual)

            pagina_atual += 1
        
        print('\033[36mPesquisa finalizada com sucesso!\033[0m')

    def escrever_titulos(self, titulos: list, titulos_videos: list) -> None:
        for titulo in titulos:
            if titulo.text not in titulos_videos:
                print('Video encontrado! - titulo: ' + titulo.text)

                titulos_videos.append(titulo.text)

    def realizar_paginacao(self, pagina_atual: int) -> None:
        print(f'\033[36mRealizando paginação, pagina atual: {pagina_atual + 1}\033[0m')

        DISTANCIA_SCROLL = 10000
        scrollar_tela = pagina_atual * DISTANCIA_SCROLL
        self.driver.execute_script(f'window.scrollTo(0, {scrollar_tela});')
        time.sleep(4)

robo_youtube = RoboYoutube()
robo_youtube.iniciar()