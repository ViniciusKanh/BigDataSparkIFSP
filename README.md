# Projeto de Sistemas Distribuido - Análise de Big Data Distribuída 🚀

![Capa do Projeto](https://github.com/ViniciusKanh/BigDataSparkIFSP/raw/main/Big-Data-analysis.png)

Bem-vindo ao repositório do projeto de Sistemas Distribuido do IFSP, focado na análise distribuída de Big Data! 👋


![GitHub](https://img.shields.io/github/license/ViniciusKanh/BigDataSparkIFSP)
![GitHub last commit](https://img.shields.io/github/last-commit/ViniciusKanh/BigDataSparkIFSP)
![GitHub contributors](https://img.shields.io/github/contributors/ViniciusKanh/BigDataSparkIFSP)
![GitHub issues](https://img.shields.io/github/issues/ViniciusKanh/BigDataSparkIFSP)

## 📄 Descrição do Projeto

Este projeto tem como objetivo desenvolver um sistema de busca por palavras-chave em documentos PDF utilizando Apache Spark e PyMuPDF. A busca por palavras-chave em documentos PDF desempenha um papel crucial em diversas aplicações, como indexação de documentos e pesquisa de informações específicas. A abordagem distribuída oferecida pelo Apache Spark possibilita o processamento eficiente e escalável de grandes volumes de documentos.

## 🔧 Funcionalidades Principais

### 1. Configuração do Ambiente Spark 🚀

O código começa configurando o ambiente necessário para utilizar o Apache Spark. Isso inclui a instalação do Java, o download e a descompactação do Spark, além de definir as variáveis de ambiente essenciais.

### 2. Início de uma Sessão Spark ⚡

Uma sessão Spark é iniciada utilizando o SparkSession, permitindo assim o processamento distribuído dos documentos PDF.

### 3. Coleta de Documentos e Exportação de Resultados 📂

O código define diretórios para os documentos PDF e para a exportação dos resultados. Ele verifica se esses diretórios existem e, caso não existam, os cria.

### 4. Busca por Palavras-chave 🔍

Uma função chamada `buscar_palavras_em_pdf` é implementada. Ela recebe como entrada um arquivo PDF e uma lista de palavras-chave. A função lê o PDF, extrai o texto de cada página e verifica a presença das palavras-chave. Os resultados da busca são retornados.

### 5. Lista de Palavras-chave e Processamento em Paralelo 📋

Uma lista de palavras-chave é definida para a busca nos documentos. A lista de arquivos PDF no diretório é obtida e os arquivos são convertidos em um RDD Spark, permitindo o processamento paralelo. A função `buscar_palavras_em_pdf` é aplicada a cada documento PDF em paralelo.

### 6. Exportação de Resultados em Diferentes Formatos 📊

Os resultados podem ser exportados para formatos como CSV, Excel e JSON utilizando a função `exportar_resultados`. Além disso, o código gera uma saída HTML que exibe os resultados e fornece links para o download dos formatos exportados.

### 7. Visualização de Contagens de Palavras-chave 📈

Um gráfico de barras é gerado para visualizar a contagem de ocorrências das palavras-chave nos documentos PDF, fornecendo insights visuais sobre os resultados.

### 8. Relatório de Resumo HTML 📑

Um relatório HTML é automaticamente gerado, contendo as contagens de ocorrências das palavras-chave e apresentando os resultados de maneira organizada.

### 9. Interface de Upload e Análise de Documentos PDF 📄

O código inclui uma seção que permite aos usuários fazer o upload de um arquivo PDF para análise. Os resultados da busca são exibidos de forma organizada, com a possibilidade de adicionar comentários e anotações para uma análise mais detalhada.

### 10. Encerramento da Sessão Spark 🛑

No final do processo, o código encerra a sessão Spark, garantindo a correta finalização do ambiente de processamento distribuído.📊 Processamento distribuído de dados em larga escala.
📈 Análise de Big Data com algoritmos avançados.
🛠️ Integração com ferramentas de código aberto para análise de dados.
📊 Geração de relatórios interativos para insights valiosos.

## ✍️ Documentação Detalhada

Neste projeto, utilizamos uma abordagem prática para aprendizado e desenvolvimento. O código-fonte, bibliotecas e técnicas incluem:

- [Python](https://www.python.org/): Linguagem de programação principal.
- [PySpark](https://spark.apache.org/docs/latest/api/python/index.html): Framework para processamento de Big Data.
- [Jupyter Notebook](https://jupyter.org/): Para análise interativa.
- [Pandas](https://pandas.pydata.org/): Manipulação de dados.
- [Matplotlib](https://matplotlib.org/): Visualização de dados.

## 🧑‍💻 Autor

- Nome: Vinicius Santos 🚀
- Email: vinicius.santos@ifsp.edu.br 📧
- GitHub: [ViniciusKanh](https://github.com/ViniciusKanh)

## 📜 Licença

Este projeto é licenciado sob os termos da [Licença MIT](LICENSE).

## 🙌 Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir problemas (issues) ou enviar um pull request para melhorar este projeto. 🤝

---

Feito com ❤️ no IFSP - Instituto Federal de São Paulo
