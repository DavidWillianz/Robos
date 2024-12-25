import pandas as pd
import pyautogui
import time, os

class CadastroMembros():
    def __init__(self):
        pyautogui.hotkey('win', 'r')
        pyautogui.typewrite('https://www.gabrielcasemiro.com.br/atividade_pyautogui \n')
        time.sleep(4)
    
    def iniciar(self):
        self.ler_arquivo_xlsx()
    
    def ler_arquivo_xlsx(self) -> None:
        CAMINHO_ARQUIVO = os.getcwd() + '\\Robos\\cadastro_membros\\assets\\dados_cadastrais.xlsx'
        df_informacoes = pd.read_excel(CAMINHO_ARQUIVO)
        
        self.processar_informacoes(df_informacoes)
    
    def processar_informacoes(self, df_informacoes: pd.DataFrame):
        caminhos_imagens = self.gerar_caminho_arquivos()

        for _, linha in df_informacoes.iterrows():
            pyautogui.click(pyautogui.locateCenterOnScreen(caminhos_imagens['nome_img'], confidence=0.8), duration=1)
            pyautogui.typewrite(linha.iloc[0], interval=0.25)

            pyautogui.click(pyautogui.locateCenterOnScreen(caminhos_imagens['email_img'], confidence=0.8), duration=1)
            pyautogui.typewrite(linha.iloc[1], interval=0.25)

            pyautogui.click(pyautogui.locateCenterOnScreen(caminhos_imagens['telefone_img'], confidence=0.8), duration=1)
            pyautogui.typewrite(linha.iloc[2], interval=0.25)

            pyautogui.click(pyautogui.locateCenterOnScreen(caminhos_imagens['sexo_img'], confidence=0.8), duration=1)
            
            if linha.iloc[3] == "Masculino":
                pyautogui.click(pyautogui.locateCenterOnScreen(caminhos_imagens['masculino_img'], confidence=0.8), duration=1)
            else:
                pyautogui.click(pyautogui.locateCenterOnScreen(caminhos_imagens['feminino_img'], confidence=0.8), duration=1)
            
            self.printar_tela(linha)
        print('\033[36mCadastros finalizados!\033[0m')

    def gerar_caminho_arquivos(self) -> dict:
        caminho_base = os.path.join(os.getcwd(), 'Robos', 'cadastro_membros', 'assets')
        
        nome_img = os.path.join(caminho_base, 'nome.png')
        email_img = os.path.join(caminho_base, 'email.png')
        telefone_img = os.path.join(caminho_base, 'telefone.png')
        sexo_img = os.path.join(caminho_base, 'sexo.png')
        masculino_img = os.path.join(caminho_base, 'masculino.png')
        feminino_img = os.path.join(caminho_base, 'feminino.png')

        return {
            'nome_img': nome_img,
            'email_img': email_img,
            'telefone_img': telefone_img,
            'sexo_img': sexo_img,
            'masculino_img': masculino_img,
            'feminino_img': feminino_img,
        }
            
    def printar_tela(self, linha: pd.Series) -> None:
        botao_enviar_img = os.getcwd() + r'\Robos\cadastro_membros\assets\botao_enviar.png'
        
        pyautogui.screenshot(f'Cadastro_{linha.iloc[0]}.png')
        pyautogui.click(pyautogui.locateCenterOnScreen(botao_enviar_img, confidence=0.8), duration=1)
        time.sleep(3)

        print(f'Cadastro {linha.iloc[0]}, finalizado!')

cadastro = CadastroMembros()
cadastro.iniciar()