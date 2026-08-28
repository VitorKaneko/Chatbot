import openpyxl
import urllib.parse import quote
import webbrowser
from time import sleep
import pyautogui
import os

#abre o whatsapp web
webbrowser.open('https://web.whatsapp.com/')
sleep(30)

#armazena os dados da planilha em variáveis (planilha e página da planilha)
planilha = openpyxl.load_workbook('clientes.xlsx')
pagina_clientes = planilha['Sheet1']

#laço para percorrer todas as linhas da planilha, começa da linha 2 para evitar cabeçalho
for linha in pagina_clientes.iter_rows(min_row=2):
    #variáveis da planilha armazenadas
    nome = linha[0].value
    telefone = linha[1].value
    vencimento = linha[2].value

    #inserindo os valores das variáveis na mensagem que será enviada para o cliente
    mensagem = f'{nome}, seu boleto vence no dia {vencimento.strftime('%d/%m/%Y')}. Link do pagamento http://google.com'

    try:
        #cria link do whatsapp para cada cliente 
        link_mensagem = f'https://web.whatsapp.com/send?phone={telefone}&text={quote(mensagem)}'
        #abre o navegador para enviar mensagem
        webbrowser.open(link_mensagem)
        sleep(10)
        #encontra o ícone de envio
        seta = pyautogui.locateCenterOnScreen('seta.png')
        sleep(10)
        #clica no ícone de envio
        pyautogui.click(seta[0], seta[1])
        sleep(10)
        #fecha a aba do navegador
        pyautogui.hotkey('ctrl', 'w')
        sleep(10)
    except:
        #caso não ocorra o envio o contato é armazenado.
        print(f'Não foi possível enviar mensagem para {nome}')
        with open('erros.csv', 'a', newline='', encoding='utf-8') as arquivo:
            arquivo.write(f'{nome},{telefone}{os.linesep}')