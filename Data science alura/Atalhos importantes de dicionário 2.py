# ==============================================================================
# 📂 GUIA PRÁTICO: ENTENDENDO E MANIPULANDO DICIONÁRIOS EM PYTHON
# ==============================================================================

# 1. CRIANDO UM DICIONÁRIO
# Dicionários guardam informações no formato Chave: Valor (Key: Value).
dicionario = {
    'Matrícula': 2000168933,
    'dia de cadastro': 25,
    'mês de cadastro': 10,
    'turma': '2E'
}

print("--- 1. Dicionário Inicial ---")
print(f"{dicionario}\n")


# 2. MODIFICANDO O DICIONÁRIO
# É possível remover elementos existentes ou adicionar novas chaves dinamicamente.

# .pop() -> Remove uma chave específica e o valor atrelado a ela
# dicionario.pop('turma')

# Adicionando uma nova chave 'Modalidade' com o valor 'EAD'
dicionario["Modalidade"] = "EAD"

print("--- 2. Dicionário Após Modificações (Adicionado 'Modalidade') ---")
print(f"{dicionario}\n")


# 3. EXTRAINDO DADOS (MÉTODOS ESTRUTURAIS)
print("--- 3. Métodos Estruturais de Dicionários ---")

# .items() -> Retorna uma lista contendo tuplas de cada par (chave, valor)
a = dicionario.items()
print(f"Método .items():\n-> {a}\n")

# .keys() -> Retorna uma lista com todas as chaves mapeadas no dicionário
b = dicionario.keys()
print(f"Método .keys():\n-> {b}\n")

# .values() -> Retorna uma lista com todos os valores guardados no dicionário
c = dicionario.values()
print(f"Método .values():\n-> {c}\n")


# 4. DESEMPACOTAMENTO E ITERAÇÃO (FOR LOOP)
# Usando o .items(), conseguimos rodar um 'for' que separa a chave e o valor
# em duas variáveis distintas (chaves, valores) a cada repetição.
print("--- 4. Percorrendo o Dicionário de Forma Limpa (Loop For) ---")
for chaves, valores in dicionario.items():
    print(f"Chave: {chaves} | Valor: {valores}")

print("-" * 60)


# ==============================================================================
# 💡 EXTRATO TEÓRICO: FUNÇÕES BUILT-IN ÚTEIS
# ==============================================================================
# Lembre-se destas três funções nativas do Python para te ajudar no dia a dia:
#
# 1. sum(sequencia) -> Soma elementos numéricos de uma lista/tupla.
#    Exemplo: sum([100.0, 400.0, 200.0]) resulta em 700.0
#
# 2. dir(objeto) -> Mostra todos os métodos e atributos disponíveis para o objeto.
#    Exemplo: dir(dicionario) vai te mostrar métodos como 'items', 'keys', 'pop', etc.
#
# 3. help(funcao) -> Abre o manual/documentação oficial do Python para aquela função.
#    Exemplo: help(print) explica tudo o que o comando print pode fazer.
# ==============================================================================
