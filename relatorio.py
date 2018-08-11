import utils

IDENTACAO_SIMPLES = "   "
IDENTACAO_DUPLA = "        "
IDENTACAO_TRIPLA = "             "
IDENTACAO_QUADRUPLA = "               "
QUEBRA_LINHA = "\n"

# Gerar relatório
def gerar(prontuarios, keywords, lista_ocorrencias):
	arquivo = open("RELATORIO.TXT", "w")
	## Cabeçalho
	arquivo.write("RELATÓRIO DA ANALISE DE PRONTUÁRIOS" + QUEBRA_LINHA)
	arquivo.write(QUEBRA_LINHA)

	## Lista de prontuários
	arquivo.write("1. LISTA DE PRONTUÁRIOS" + QUEBRA_LINHA)
	for indice in range(len(prontuarios)):
		numero_do_topico = str(indice + 1)
		nome_do_prontuario = utils.extrair_nome_arquivo(prontuarios[indice])
		arquivo.write(IDENTACAO_SIMPLES + "1." + numero_do_topico + ". " + nome_do_prontuario + QUEBRA_LINHA)
	arquivo.write(QUEBRA_LINHA)

	## Lista de Palavras-chave
	arquivo.write("2. LISTA DE PALAVRAS-CHAVE" + QUEBRA_LINHA)
	for indice in range(len(keywords)):
		numero_do_topico = str(indice + 1)
		arquivo.write(IDENTACAO_SIMPLES + "2." + numero_do_topico + ". " + keywords[indice] + QUEBRA_LINHA)
	arquivo.write(QUEBRA_LINHA)

	## Lista de palavras-chave diferentes por prontuário
	arquivo.write("3. OCORRÊNCIAS DE PALAVRAS-CHAVE POR PRONTUÁRIO" + QUEBRA_LINHA)
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
			arquivo.write(IDENTACAO_SIMPLES + "3." + numero_do_topico_prontuario + ". " + nome_do_prontuario + QUEBRA_LINHA)
			keyword_anterior = ""
		keyword = ocorrencia.get_keyword()
		if not keyword == keyword_anterior:
			keyword_anterior = keyword
			arquivo.write(IDENTACAO_DUPLA + "-" + keyword + QUEBRA_LINHA)
	arquivo.write(QUEBRA_LINHA)

	## Lista de sentencas com palavras-chave por prontuário	
	arquivo.write("4. SENTENCAS ONDE OCORREM AS PALAVRAS-CHAVE" + QUEBRA_LINHA)
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
			arquivo.write(IDENTACAO_SIMPLES + "4." + numero_do_topico_prontuario + ". " + nome_do_prontuario + QUEBRA_LINHA)
			keyword_anterior = ""
			indice_keyword = 0
		keyword = ocorrencia.get_keyword()
		if not keyword == keyword_anterior:
			indice_keyword += 1
			keyword_anterior = keyword
			topico_keyword = str(indice_prontuario) + "." + str(indice_keyword)
			arquivo.write(IDENTACAO_DUPLA + "4." + topico_keyword + ". " + keyword + QUEBRA_LINHA)
			indice_linha = 1
			num_linha = ocorrencia.get_num_linha()
			topico_linha = topico_keyword + "." + str(indice_linha)
			arquivo.write(IDENTACAO_TRIPLA + "4." + topico_linha + ". Linha " + str(num_linha) + QUEBRA_LINHA)
			arquivo.write(IDENTACAO_QUADRUPLA +  "\"" + ocorrencia.get_sentenca().strip() + "\"" + QUEBRA_LINHA)
		else:
			indice_linha += 1
			num_linha = ocorrencia.get_num_linha()
			topico_linha = topico_keyword + "." + str(indice_linha)
			arquivo.write(IDENTACAO_TRIPLA + "4." + topico_linha + ". Linha " + str(num_linha) + QUEBRA_LINHA)
			arquivo.write(IDENTACAO_QUADRUPLA + "\"" + ocorrencia.get_sentenca().strip() + "\"" + QUEBRA_LINHA)		
	arquivo.close()
	