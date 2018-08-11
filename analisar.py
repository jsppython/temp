import pickle
import utils
import relatorio

# Classe Ocorrencia, representa a o ocorrência de uma palavra-chave
# em uma sentença em uma linha em um prontuário.
class Ocorrencia:
	def __init__(self, nome_prontuario, num_linha, keyword, sentenca):
		self.nome_prontuario = utils.extrair_nome_arquivo(nome_prontuario)
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
prontuarios = utils.get_prontuarios()
keywords = utils.get_keywords()
lista_ocorrencias = []
for prontuario in prontuarios:
	for keyword in keywords:
		linhas_do_prontuario = utils.get_linhas_arq_texto(prontuario)
		for num_da_linha in range(len(linhas_do_prontuario)):
			linha = linhas_do_prontuario[num_da_linha]
			sentenca = utils.extrair_sentenca(linha, keyword)
			if sentenca:
				ocorrencia = Ocorrencia(prontuario, num_da_linha, keyword, sentenca) 
				lista_ocorrencias.append(ocorrencia) 

# Gerar o relatório		
relatorio.gerar(prontuarios, keywords, lista_ocorrencias)

# Salvar a lista de ocorrencias
saida = open("ocorrencias.bin", "wb")
conteudo_binario = pickle.dump(lista_ocorrencias, saida, pickle.HIGHEST_PROTOCOL)
saida.close()

# Carregar a lista de ocorrencias
entrada = open("ocorrencias.bin", "rb")
lista_ocorrencias = pickle.load(entrada)
entrada.close()

# Imprimir a lista de ocorrencias
for ocorrencia in lista_ocorrencias:
	print("PRONTUARIO: " + ocorrencia.get_nome_prontuario())
	print("PALAVRA-CHAVE: " + ocorrencia.get_keyword())
	print("NUMERO DA LINHA: " + str(ocorrencia.get_num_linha()))
	print("SENTENCA: \"" + ocorrencia.get_sentenca().strip() + "\"")
	print()
	print()