import csv

# Nome do arquivo CSV original
csv_filename = 'links_noticias_RCB_12_23.csv'
# Nome do arquivo CSV filtrado
filtered_csv_filename = 'filtered_RCB_12_23.csv'

# Conjunto para armazenar os identificadores únicos dos links
unique_identifiers = set()
# Lista para armazenar os links filtrados
filtered_links = []

# Abrir o arquivo CSV original e iterar sobre as linhas
with open(csv_filename, 'r', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        url = row['Links']
        # Extrair os últimos 9 caracteres do link
        identifier = url[-9:]
        # Adicionar o link ao filtro se o identificador for único
        if identifier not in unique_identifiers:
            unique_identifiers.add(identifier)
            filtered_links.append(url)

# Escrever os links filtrados e únicos em um novo arquivo CSV
with open(filtered_csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Links'])  # Escreve o cabeçalho
    for link in filtered_links:
        writer.writerow([link])

print(f"Links filtrados e únicos salvos em {filtered_csv_filename}")
