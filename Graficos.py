import matplotlib.pyplot as plt

import os
import fitz  # PyMuPDF
import pandas as pd
import json
from pyspark.sql import SparkSession
from IPython.display import HTML, display, FileLink
import shutil

# Configurar uma sessão Spark
spark = SparkSession.builder.appName("Análise de Palavras-chave").getOrCreate()

# Diretório contendo os documentos PDF
pdf_dir = "/content/drive/My Drive/Faculdade/Aula/2023.2/Sistemas Distribuidos/Trabalho de BigData/Aplicação Pratica/Documentos"

# Diretório para exportar os resultados
export_dir = "/content/drive/My Drive/Faculdade/Aula/2023.2/Sistemas Distribuidos/Trabalho de BigData/Aplicação Pratica/Dados"

def buscar_palavras_em_pdf(pdf_file_path, palavras_chave):
    try:
        # Abre o PDF e lê o texto
        pdf_document = fitz.open(pdf_file_path)
        
        resultados = []  # Armazenará os resultados para este PDF
        
        for page_num in range(len(pdf_document)):
            page = pdf_document[page_num]
            text = page.get_text()
            
            # Verifica se as palavras-chave estão presentes no texto
            for palavra in palavras_chave:
                if palavra.lower() in text.lower():
                    resultados.append(f'<p class="result"><span class="keyword">{palavra}</span> encontrada na página {page_num + 1} do arquivo <span class="filename">{pdf_file_path}</span></p>')
        
        return resultados

    except Exception as e:
        return [f'<p class="error">Erro ao processar o arquivo <span class="filename">{pdf_file_path}</span>: {str(e)}</p>']
    
    
palavras_chave = ["Requisitos de Sistema", "Terceira Idade", "Medicos"]

pdf_files = [pdf_file_name for pdf_file_name in os.listdir(pdf_dir) if pdf_file_name.endswith('.pdf')]


pdf_files_rdd = spark.sparkContext.parallelize(pdf_files)

# Realize a busca e obtenha os resultados
resultados = pdf_files_rdd.flatMap(lambda pdf_file_name: buscar_palavras_em_pdf(os.path.join(pdf_dir, pdf_file_name), palavras_chave))

# Inicialize um dicionário para armazenar as contagens
contagens = {palavra: 0 for palavra in palavras_chave}

# Atualize as contagens com base nos resultados
for resultado in resultados.collect():
    for palavra in palavras_chave:
        if palavra.lower() in resultado.lower():
            contagens[palavra] += 1

# Crie um gráfico de barras com as contagens atualizadas
plt.figure(figsize=(10, 6))
plt.bar(contagens.keys(), contagens.values(), color='skyblue')
plt.xlabel('Palavras-Chave')
plt.ylabel('Contagem de Ocorrências')
plt.title('Frequência de Palavras-Chave em Documentos PDF')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

spark.stop()