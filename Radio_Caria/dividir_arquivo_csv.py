import csv

def dividir_arquivo_csv(nome_arquivo, numero_partes):
    # Lê o arquivo CSV e conta o número de linhas
    with open(nome_arquivo, newline='', encoding='utf-8') as csvfile:
        leitor = csv.reader(csvfile)
        linhas = list(leitor)
        numero_linhas = len(linhas)
    
    print(f"O arquivo original tem {numero_linhas} linhas.")
    
    # Calcula o número de linhas por parte (excluindo a linha de cabeçalho)
    linhas_por_parte = (numero_linhas - 1) // numero_partes
    linhas_restantes = (numero_linhas - 1) % numero_partes

    # Divide o arquivo em partes e escreve novos arquivos CSV
    for i in range(numero_partes):
        inicio = i * linhas_por_parte + 1
        fim = inicio + linhas_por_parte
        if i == numero_partes - 1:  # Adiciona as linhas restantes na última parte
            fim += linhas_restantes
        
        parte_linhas = linhas[inicio:fim]
        
        nome_arquivo_parte = f"{nome_arquivo.split('.')[0]}_parte_{i+1}.csv"
        with open(nome_arquivo_parte, mode='w', newline='', encoding='utf-8') as arquivo_parte:
            escritor = csv.writer(arquivo_parte)
            # Adiciona o cabeçalho "Links" em cada parte
            escritor.writerow(['Links'])
            escritor.writerows(parte_linhas)
        
        print(f"Parte {i+1} salva como {nome_arquivo_parte} com {len(parte_linhas) + 1} linhas.")

# Solicita o nome do arquivo e o número de partes ao user
nome_arquivo = input("Digite o nome do arquivo CSV (com extensão): ")
numero_partes = int(input("Em quantas partes deseja dividir o arquivo? "))

dividir_arquivo_csv(nome_arquivo, numero_partes)
