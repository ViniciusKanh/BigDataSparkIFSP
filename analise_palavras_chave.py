import os
import fitz  # PyMuPDF
from pyspark.sql import SparkSession
from IPython.display import HTML, display

# Configurar uma sessão Spark
spark = SparkSession.builder.appName("Análise de Palavras-chave").getOrCreate()

# Diretório contendo os documentos PDF
pdf_dir = "/content/drive/My Drive/Faculdade/Aula/2023.2/Sistemas Distribuidos/Trabalho de BigData/Aplicação Pratica/Documentos"

# Função para buscar palavras em um PDF
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

# Palavras-chave que você deseja buscar nos documentos PDF
palavras_chave = ["Requisitos", "Vinicius", "Estudo"]

# Lista os arquivos PDF no diretório e busca as palavras-chave
pdf_files = [pdf_file_name for pdf_file_name in os.listdir(pdf_dir) if pdf_file_name.endswith('.pdf')]

# Converter a lista para um RDD Spark
pdf_files_rdd = spark.sparkContext.parallelize(pdf_files)

# Utilize a função buscar_palavras_em_pdf nos documentos PDF
resultados = pdf_files_rdd.flatMap(lambda pdf_file_name: buscar_palavras_em_pdf(os.path.join(pdf_dir, pdf_file_name), palavras_chave))

# Crie uma saída HTML mais bonita e estilizada
output_html = """
<style>
    .result {
        background-color: #f7f7f7;
        padding: 10px;
        margin: 10px;
        border: 1px solid #ddd;
        border-radius: 5px;
    }

    .keyword {
        font-weight: bold;
        color: #0073e6;
    }

    .filename {
        font-style: italic;
    }

    .error {
        background-color: #ffdddd;
        padding: 10px;
        margin: 10px;
        border: 1px solid #ff9999;
        border-radius: 5px;
    }
</style>
<h2>Resultados da Busca em Documentos PDF</h2>
"""

for resultado in resultados.collect():
    output_html += resultado

# Exibir a saída HTML estilizada no Colab Notebook
display(HTML(output_html))

# Encerra a sessão Spark
spark.stop()
