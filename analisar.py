import re
import glob
import json

# Constantes
ARQ_DE_KEYWORDS = "keywords.txt"
PATH_PRONTUARIOS = r".\prontuarios"
IDENTACAO_SIMPLES = "   "
IDENTACAO_DUPLA = "        "
IDENTACAO_TRIPLA = "             "
IDENTACAO_QUADRUPLA = "               "

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

	def extrair_nome_arquivo(path):
		partes = path.split("\\")
		return partes[-1]

# Classe Ocorrencia, representa a o ocorrência de uma palavra-chave
# em uma sentença em uma linha em um prontuário.
class Ocorrencia:
	def __init__(self, nome_prontuario, num_linha, keyword, sentenca):
		self.nome_prontuario = Utils.extrair_nome_arquivo(nome_prontuario)
		self.num_linha = num_linha
		self.keyword = keyword
		self.sentenca = sentenca

	def get_nome_prontuario(self):
		return self.nome_prontuario
	
	def get_keyword(self):
		return self.keyword
	
	def get_num_linha(self):
		return self.num_linha
		
	def get_sentenca(self):
		return self.sentenca
		
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

# Imprimir relatório

## Cabeçalho
print("RELATÓRIO DA ANALISE DE PRONTUÁRIOS")
print()

## Lista de prontuários
print("1. LISTA DE PRONTUÁRIOS")
for indice in range(len(prontuarios)):
	numero_do_topico = str(indice + 1)
	nome_do_prontuario = Utils.extrair_nome_arquivo(prontuarios[indice])
	print(IDENTACAO_SIMPLES + "1." + numero_do_topico + ". " + nome_do_prontuario)
print()

## Lista de Palavras-chave
print("2. LISTA DE PALAVRAS-CHAVE")
for indice in range(len(keywords)):
	numero_do_topico = str(indice + 1)
	print(IDENTACAO_SIMPLES + "2." + numero_do_topico + ". " + keywords[indice])
print()

## Lista de palavras-chave diferentes por prontuário
print("3. OCORRÊNCIAS DE PALAVRAS-CHAVE POR PRONTUÁRIO")
indice_prontuario = 0
indice_keyword = 0
prontuario_anterior = ""
keyword_anterior = ""
for ocorrencia in lista_ocorrencias:
	nome_do_prontuario = ocorrencia.get_nome_prontuario()
	if not nome_do_prontuario == prontuario_anterior:
		indice_prontuario += 1
		numero_do_topico_prontuario = str(indice_prontuario)
		prontuario_anterior = nome_do_prontuario
		print(IDENTACAO_SIMPLES + "3." + numero_do_topico_prontuario + ". " + nome_do_prontuario)
		keyword_anterior = ""
	keyword = ocorrencia.get_keyword()
	if not keyword == keyword_anterior:
		keyword_anterior = keyword
		print(IDENTACAO_DUPLA + "-" + keyword)
print()

## Lista de sentencas com palavras-chave por prontuário	
print("4. SENTENCAS ONDE OCORREM AS PALAVRAS-CHAVE")
indice_prontuario = 0
indice_keyword = 0
indice_linha = 0
prontuario_anterior = ""
keyword_anterior = ""
for ocorrencia in lista_ocorrencias:
	nome_do_prontuario = ocorrencia.get_nome_prontuario()
	if not nome_do_prontuario == prontuario_anterior:
		indice_prontuario += 1
		numero_do_topico_prontuario = str(indice_prontuario)
		prontuario_anterior = nome_do_prontuario
		print(IDENTACAO_SIMPLES + "4." + numero_do_topico_prontuario + ". " + nome_do_prontuario)
		keyword_anterior = ""
		indice_keyword = 0
	keyword = ocorrencia.get_keyword()
	if not keyword == keyword_anterior:
		indice_keyword += 1
		keyword_anterior = keyword
		topico_keyword = str(indice_prontuario) + "." + str(indice_keyword)
		print(IDENTACAO_DUPLA + "4." + topico_keyword + ". " + keyword)
		indice_linha = 1
		num_linha = ocorrencia.get_num_linha()
		topico_linha = topico_keyword + "." + str(indice_linha)
		print(IDENTACAO_TRIPLA + "4." + topico_linha + ". Linha " + str(num_linha))
		print(IDENTACAO_QUADRUPLA + ocorrencia.get_sentenca())
	else:
		indice_linha += 1
		num_linha = ocorrencia.get_num_linha()
		topico_linha = topico_keyword + "." + str(indice_linha)
		print(IDENTACAO_TRIPLA + "4." + topico_linha + ". Linha " + str(num_linha))
		print(IDENTACAO_QUADRUPLA + ocorrencia.get_sentenca())		
"""
	for keyword in range(len(keywords)):
		print("\t2." + numero_do_topico + ". " + keywords[indice])
		
		
for ocorrencia in lista_ocorrencias:
	nome_do_prontuario = ocorrencia.get_nome_prontuario()
	if not nome_do_prontuario == prontuario_anterior:
		indice_prontuario += 1
		numero_do_topico_prontuario = str(indice_prontuario)
		prontuario_anterior = nome_do_prontuario
		print(IDENTACAO_SIMPLES + "3." + numero_do_topico_prontuario + ". " + nome_do_prontuario)
	keyword = ocorrencia.get_keyword()
	if not keyword == keyword_anterior:
		keyword_anterior = keyword
		indice_keyword += 1
		topico_keyword = str(indice_prontuario) + "." + str(indice_keyword)
		prontuario_anterior = nome_do_prontuario
		print(IDENTACAO_DUPLA + "3." + topico_keyword + ". " + keyword)			
print()
print(len(lista_ocorrencias))
print(len(keywords))
print(len(prontuarios))
print(keywords)
"""