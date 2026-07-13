# Dados Brutos simulando o banco de dados da empresa
dados_brutos = [
    (101, "SP", 2.5, "Sucesso"),
    (102, "RJ", 4.1, "Sucesso"),
    (103, "MG", 1.8, "Erro"),  # Dado Inválido
    (104, "SP", -1.0, "Sucesso"),  # Dado Corrompido
    (105, "PR", 3.0, "Sucesso"),
    (106, "RJ", 2.9, "Sucesso"),
    (107, "SP", 3.2, "Sucesso"),
    (108, "MG", 2.2, "Sucesso"),
    (109, "PR", 1.5, "Sucesso"),
    (110, "RJ", 5.0, "Sucesso")
]


# 1. Fase de Filtro e Saneamento de Dados
def filtro(a):
    lista_correta = []
    for i in range(len(a)):
        if a[i][2] > 0 and a[i][3] == "Sucesso":
            lista_correta.append(a[i])
    return lista_correta


# 2. Fase de Agrupamento e Cálculo de Médias
def media_de_tempo(dados_limpos):
    lista_final = {}

    # Agrupando os tempos nas respectivas chaves (Estados)
    for i in dados_limpos:
        estado = i[1]
        tempo = i[2]

        if estado not in lista_final:
            lista_final[estado] = [tempo]
        else:
            lista_final[estado].append(tempo)

    dicionario_medias = {}

    # Calculando a média real de cada estado
    for estado, lista_de_tempos in lista_final.items():
        media = sum(lista_de_tempos) / len(lista_de_tempos)
        dicionario_medias[estado] = round(media, 1)

    return dicionario_medias


# 3. Fase de Visualização do Dashboard
def exibir_dashboard(dicionario_medias):
    print("==================================================")
    print("   DASHBOARD DE PERFORMANCE LOGÍSTICA - REGIONAL   ")
    print("==================================================")
    print("")

    for estado, media in dicionario_medias.items():
        quantidade_barras = int(media)
        barras = "█" * quantidade_barras
        print(f"{estado} | {barras} ({media}h de média)")

    print("")
    print("==================================================")
    print("Status do Sistema: Processado com Sucesso.")


# --- EXECUÇÃO DO PIPELINE (O fluxo do programa) ---
if __name__ == "__main__":
    # Passo 1: Executa o filtro de limpeza
    dados_limpos = filtro(dados_brutos)

    # Passo 2: Executa o motor lógico de médias
    medias_calculadas = media_de_tempo(dados_limpos)

    # Passo 3: Renderiza o gráfico final no terminal
    exibir_dashboard(medias_calculadas)