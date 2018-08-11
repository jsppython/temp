import glob
import re

# Constantes
ARQ_DE_KEYWORDS = "keywords.txt"
PATH_PRONTUARIOS = r".\prontuarios"


def get_prontuarios():
	prontuarios = glob.glob(PATH_PRONTUARIOS + r"\*.txt")
	return prontuarios	

def get_linhas_arq_texto(nome_arquivo):
	arquivo = open(nome_arquivo, "r")
	lista_de_linhas = arquivo.readlines()
	arquivo.close()
	return lista_de_linhas

def get_conteudo_arquivo(nome_arquivo):
	arquivo = open(nome_arquivo, "r")
	conteudo = arquivo.read()
	arquivo.close()
	return conteudo		

def get_keywords():
	linhas = get_linhas_arq_texto(ARQ_DE_KEYWORDS)
	keywords = []
	for linha in linhas:
		keywords.append(linha.strip())
	return keywords

def extrair_sentenca(texto, keyword):
	sentenca = None
	padrao = r"[^\.\n]*\b" + keyword + r"\b[^\.\n]*[\.\n]"
	matches = re.search(padrao, texto, re.I)
	if matches:
		sentenca = matches.group(0)
	return sentenca

def extrair_nome_arquivo(path):
	partes = path.split("\\")
	return partes[-1]