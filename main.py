import os

arquivos_extraidos = []

def pegar_arquivos_pasta(pasta):
    lista_arquivos = os.listdir(pasta)
    # se tiver txt e vendas no nome do arquivo, então eu vou pegar o nome do mês
    for arquivos_especificos in lista_arquivos:
        if '.txt' in arquivos_especificos and 'Vendas' in arquivos_especificos:
            #significa que eu quero pegar só o nome do mês
            arquivos_extraidos.append(arquivos_especificos.split()[2].replace('.txt', ''))
    # caso contrario se for uma pasta
        elif '.txt' not in arquivos_especificos:
            pegar_arquivos_pasta(f'{pasta}/{arquivos_especificos}')

if __name__ == "__main__":
    pegar_arquivos_pasta('Arquivos')
    for arquivo in arquivos_extraidos:
        print('-=-' * 5)
        print(arquivo)