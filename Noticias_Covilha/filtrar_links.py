import csv

# Nome do arquivo CSV original
csv_filename = 'links_noticias_NC_09_19.csv'
# Nome do arquivo CSV filtrado
filtered_csv_filename = 'filtered_links_09_19.csv'

# Lista para armazenar os links filtrados
filtered_links = []

# Abrir o arquivo CSV original e iterar sobre as linhas
with open(csv_filename, 'r', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        url = row['Links']
        # Verificar se "idseccao=1" está no URL
        if 'idseccao=1&' in url:
            filtered_links.append(url)

# Escrever os links filtrados em um novo arquivo CSV
with open(filtered_csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Links'])  # Escreve o cabeçalho
    for link in filtered_links:
        writer.writerow([link])

print(f"Links filtrados salvos em {filtered_csv_filename}")
