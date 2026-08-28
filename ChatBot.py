import openpyxl
import urllib.parse import quote
import webbrowser
from time import sleep
import pyautogui
import os

webbrowser.open('https://web.whatsapp.com/')
sleep(30)

planilha = openpyxl.load_workbook('clientes.xlsx')
pagina_clientes = planilha['Sheet1']

for linha in pagina_clientes.iter_rows(min_row=2):
    nome = linha[0].value
    telefone = linha[1].value
    vencimento = linha[2].value

    mensagem = f'{nome}, seu boleto vence no dia {vencimento.strftime('%d/%m/%Y')}. Link do pagamento http://google.com'

    try:
        link_mensagem = f'https://web.whatsapp.com/send?phone={telefone}&text={quote(mensagem)}'
        webbrowser.open(link_mensagem)
        sleep(10)
        seta = pyautogui.locateCenterOnScreen('set.png')
        sleep(10)
        pyautogui.click(seta[0], seta[1])
        sleep(10)
        pyautogui.hotkey('ctrl', 'w')
        sleep(10)
    except:
        print(f'Não foi possível enviar mensagem para {nome}')
        with open('erros.csv', 'a', newline='', encoding='utf-8') as arquivo:
            arquivo.write(f'{nome},{telefone}{os.linesep}')