import csv

# Nome do arquivo CSV original
csv_filename = 'final_links_19_23.csv'
# Nome do arquivo CSV filtrado
filtered_csv_filename = 'final_links_19_23.csv'

# Conjunto para armazenar os identificadores únicos de links
unique_identifiers = set()
# Lista para armazenar os links filtrados
filtered_links = []

# Função para extrair a parte do link entre as duas últimas barras
def get_link_identifier(url):
    parts = url.split('/')
    if len(parts) > 2:
        return parts[-2] + '/' + parts[-1]
    return url

# Abrir o arquivo CSV original e iterar sobre as linhas
with open(csv_filename, 'r', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        url = row['Links']
        identifier = get_link_identifier(url)
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
