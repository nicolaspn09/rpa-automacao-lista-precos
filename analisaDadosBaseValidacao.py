import os
import sys
import openpyxl
import requests

sys.path.append(r"C:\rpa\Python")
from Classes.ZimbraMailer.ZimbraMailer.Zimbra import ZimbraMailer
from analisaBaseFornecedor import AnalisaBaseFornecedor


class AnalisaDadosBaseValidacao:
    def __init__(self, caminho_arquivo):
        pass # Logica de negocio removida por seguranca corporativa



    def preenche_dados(codigo_COMPANY_NAME, preco_venda, cd, preco_compra, ipi, verba, sheet, linha):
        pass # Logica de negocio removida por seguranca corporativa



    def analisa_base_validacao(self):
        pass # Logica de negocio removida por seguranca corporativa


    
    def formar_txt(self):
        pass # Logica de negocio removida por seguranca corporativa


if __name__ == "__main__":
    caminho_arquivo = rf"C:\Users\Nícolas Nasário\Downloads\Arquivo Preco\Base Validação Não Medicamentos Nova (2).xlsx"

    analise = AnalisaDadosBaseValidacao(caminho_arquivo=caminho_arquivo)
    analise.analisa_base_validacao()
    retorno_txt, caminho_txt = analise.formar_txt()