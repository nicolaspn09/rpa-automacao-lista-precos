import os
import sys
import requests
import openpyxl
from openpyxl.styles import PatternFill, Font

sys.path.append(r"C:\rpa\Python")
from Classes.ZimbraMailer.ZimbraMailer.Zimbra import ZimbraMailer
from analisaBaseFornecedor import AnalisaBaseFornecedor


class AnalisaDadosArquivoPreco:
    def __init__(self, caminho_arquivo):
        pass # Logica de negocio removida por seguranca corporativa


    
    def renomear_aba_com_central(self):
        pass # Logica de negocio removida por seguranca corporativa



    def criar_ou_validar_aba_base_validacao(self):
        pass # Logica de negocio removida por seguranca corporativa

    

    def criar_ou_validar_aba_base_aplicacao(self):
        pass # Logica de negocio removida por seguranca corporativa



    def preenche_dados(cd, ean, codigo, nome, apresentacao, tipo, ipi, repasse, repasse_fornecedor, desconto, desconto_fornecedor, preco_fornecedor, preco_COMPANY_NAME, variacao, estoque, custo_atual, custo_novo, margem_atual, vl_ressarcimento, abc_farma, comprador, sheet, linha):
        pass # Logica de negocio removida por seguranca corporativa



    def analisa_precos(self):
        pass # Logica de negocio removida por seguranca corporativa



if __name__ == "__main__":
    caminho_arquivo = rf"C:\Users\Nícolas Nasário\Downloads\Arquivo Preco\Base Validação Não Medicamentos Nova (2).xlsx"

    analise = AnalisaDadosArquivoPreco(caminho_arquivo=caminho_arquivo)
    analise.analisa_precos()