import re
import glob
import json

# Constantes
ARQ_DE_KEYWORDS = r"D:\codigo\testes\keywords.txt"
PATH_PRONTUARIOS = r"D:\codigo\arquivos"

# Classe Utilitarios, agrupamento de funções genéricas
class Utils:
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
		linhas = Utils.get_linhas_arq_texto(ARQ_DE_KEYWORDS)
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

# Classe Ocorrencia, representa a o ocorrência de uma palavra-chave
# em uma sentença em uma linha em um prontuário.
class Ocorrencia:
	def __init__(self, nome_arquivo, num_linha, keyword, sentenca):
		self.nome_arquivo = nome_arquivo
		self.num_linha = num_linha
		self.keyword = keyword
		self.sentenca = sentenca

# Percorrer todos os prontuarios. Para cada prontuário, verificar
# a ocorrência das palavras-chave. Guardar as sentenças onde as
# palavras-chave foram encontradas.
prontuarios = Utils.get_prontuarios()
keywords = Utils.get_keywords()
lista_ocorrencias = []
for prontuario in prontuarios:
	for keyword in keywords:
		linhas_do_prontuario = Utils.get_linhas_arq_texto(prontuario)
		for num_da_linha in range(len(linhas_do_prontuario)):
			linha = linhas_do_prontuario[num_da_linha]
			sentenca = Utils.extrair_sentenca(linha, keyword)
			if sentenca:
				ocorrencia = Ocorrencia(prontuario, num_da_linha, keyword, sentenca) 
				lista_ocorrencias.append(ocorrencia) 

print(len(lista_ocorrencias))
print(len(keywords))
print(len(prontuarios))
print(keywords)