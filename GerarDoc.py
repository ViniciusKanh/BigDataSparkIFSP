import os
import random
import string

# Função para gerar uma palavra aleatória
def generate_random_word(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))

# Função para criar um documento TXT com palavras aleatórias e palavras específicas
def create_random_and_specific_txt_file(directory, file_name, num_words, specific_words):
    with open(os.path.join(directory, file_name), 'w') as file:
        for _ in range(num_words):
            if random.random() < 0.2:  # 20% de chance de incluir uma palavra específica
                random_word = random.choice(specific_words)
            else:
                word_length = random.randint(3, 10)  # Define o comprimento da palavra aleatória
                random_word = generate_random_word(word_length)
            file.write(random_word + ' ')

# Crie a pasta "documentos" se ela não existir
if not os.path.exists("documentos"):
    os.makedirs("documentos")

# Número de documentos que você deseja gerar
num_documents = 10

# Lista de palavras específicas que você deseja incluir
specific_words = ["tecnologia", "inovação", "eficiência", "energética", "comunicação"]

# Gere os documentos TXT com palavras aleatórias e palavras específicas dentro da pasta "documentos"
for i in range(num_documents):
    file_name = f'document_{i + 1}.txt'
    num_words = random.randint(50, 200)  # Define o número de palavras aleatórias por documento
    create_random_and_specific_txt_file("documentos", file_name, num_words, specific_words)

print(f'{num_documents} documentos TXT com palavras aleatórias e palavras específicas foram gerados na pasta "documentos".')
