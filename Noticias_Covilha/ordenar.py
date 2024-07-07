import csv

# Nome do arquivo CSV de entrada
csv_filename = 'filtered_links_19_23.csv'
# Nome do arquivo CSV de saída
output_filename = 'final_links_19_23.csv'

# Função para extrair a data do link
def extract_date_from_link(link):
    date_part = link[34:42]  # Extrai a parte da data do link (20101116)
    year = date_part[:4]
    month = date_part[4:6]
    day = date_part[6:8]
    return year, month, day

# Ler os links do arquivo CSV
with open(csv_filename, 'r', newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    links = [row[0] for row in reader]

# Ordenar os links pela data
sorted_links = sorted(links, key=lambda link: extract_date_from_link(link))

# Salvar os links ordenados em um novo arquivo CSV
with open(output_filename, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    for link in sorted_links:
        writer.writerow([link])

print(f"Links ordenados salvos em {output_filename}")


