import time
import os

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class PesquisaDominios():
    def __init__(self):
        path_chromedriver = os.getcwd() + '\\chromedriver-win64\\chromedriver.exe'
        service = Service(executable_path=path_chromedriver)

        self.driver = webdriver.Chrome(service=service)
    
    def iniciar(self) -> None:
        self.url_site = 'https://registro.br/'
        self.driver.get(self.url_site)

        self.processar_resultados()

    def processar_resultados(self):
        lista_dominios = self.obter_dominios_do_usuario()
        resultados = self.pesquisar_dominios(lista_dominios)

        nome_arquivo = 'resultados.txt'
        with open(nome_arquivo, 'w') as arquivo:
            arquivo.write('\n'.join(resultados))

        print('\033[36mVerfificação dos dominios finalizada com sucesso!\033[0m')
        self.driver.quit()

    def obter_dominios_do_usuario(self) -> list:
        dominios = []
        quantidade_dominios = self.obter_quantidade_do_usuario()
        
        print('Digite o dominios que voçê deseja pesquisar: ')
        for numero in range(quantidade_dominios):
            dominio_escolhido = input(f'Dominio {numero + 1}: ').strip()
            if dominio_escolhido:
                dominios.append(dominio_escolhido)
            else:
                print('Preencha com o dominio desejado, não é possivel busca com o campo de pesquisa vazio')
        return dominios

    def obter_quantidade_do_usuario(self) -> int:
        print('Seja bem vindo ao sistema de pesquisa de dominios \nDigite a quantidade de dominios que voçê deseja pesquisar (quantidade minima 1):')
        while True:
            try:
                quantidade = int(input())
                if quantidade >= 1:
                    return quantidade

            except ValueError:
                print('Digite um valor inteiro, por favor')

    def pesquisar_dominios(self, dominios: list) -> list:
        print('\033[36mFazendo pesquisa dos dominios\033[0m')

        resultados = []
        for dominio in dominios:
            campo_pesquisa = self.driver.find_element(By.ID, 'is-avail-field')
            campo_pesquisa.clear()

            campo_pesquisa.send_keys(dominio)
            time.sleep(1)
            campo_pesquisa.send_keys(Keys.ENTER)

            time.sleep(2)
            resultado = self.driver.find_elements(By.XPATH, '//*[@id="conteudo"]/div/section/div[2]/div/p/span/strong')
            if resultado:
                print('Dominio: ' + dominio + ' ' +  resultado[0].text)
            else:
                raise ValueError('Não foi encontrado seletor do resultado, validar!')
            resultados.append(resultado[0].text)
        return resultados
    
pesquisa_dominios = PesquisaDominios()
pesquisa_dominios.iniciar()