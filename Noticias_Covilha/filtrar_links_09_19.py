import csv

# Nome do arquivo CSV original
csv_filename = 'final_links_09_19.csv'
# Nome do arquivo CSV filtrado
filtered_csv_filename = 'final_links_09_19.csv'

# Conjunto para armazenar os identificadores únicos de links
unique_identifiers = set()
# Lista para armazenar os links filtrados
filtered_links = []

# Função para extrair o identificador do link com base no parâmetro idartigo
def get_link_identifier(url):
    if 'idartigo=' in url:
        parts = url.split('&')
        for part in parts:
            if part.startswith('idartigo='):
                return part
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
