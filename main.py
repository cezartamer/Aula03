### Exercício 1: Verificação de Qualidade de Dados
# Você está analisando um conjunto de dados de vendas e precisa garantir 
# que todos os registros tenham valores positivos para `quantidade` e `preço`. 
# Escreva um programa que verifique esses campos e imprima "Dados válidos" se ambos 
# forem positivos ou "Dados inválidos" caso contrário.

# qtd = 10
# preco = 20

# if preco > 0 and qtd > 0 :
#     print("Dados Válidos")
# else:
#     print("Dados Inválidos")



### Exercício 2: Classificação de Dados de Sensor
# Imagine que você está trabalhando com dados de sensores IoT. 
# Os dados incluem medições de temperatura. Você precisa classificar cada leitura 
# como 'Baixa', 'Normal' ou 'Alta'. Considerando que:

# temp = 20

# if temp < 10:
#     print("Temperatura baixa")
# elif temp >= 10 and temp <=20:
#     print("Temperatura normal")
# else:
#     print("Temperatura alta")

### Exercício 3: Filtragem de Logs por Severidade
# Você está analisando logs de uma aplicação e precisa filtrar mensagens 
# com severidade 'ERROR'. Dado um registro de log em formato de dicionário 
# como `log = {'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Falha na conexão'}`, 
# escreva um programa que imprima a mensagem se a severidade for 'ERROR'.

# log = {'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Falha na conexão'}

# if log['level'] == "ERROR":
#     print(log['message'])


### Exercício 4: Validação de Dados de Entrada
# Antes de processar os dados de usuários em um sistema de recomendação, 
# você precisa garantir que cada usuário tenha idade entre 18 e 65 anos e tenha 
# fornecido um email válido. Escreva um programa que valide essas condições 
# e imprima "Dados de usuário válidos" ou o erro específico encontrado.

# idade = 19
# email = 'cezar@gmailcom'

# if not(idade >= 18 and idade <= 65):
#     print("Idade fora do recomendado.")
# elif "@" not in email or "." not in email:
#     print("Email fora do padrão.")
# else:
#     print("Dados válidos")


### Exercício 5: Detecção de Anomalias em Dados de Transações
# Você está trabalhando em um sistema de detecção de fraude e precisa identificar 
# transações suspeitas. Uma transação é considerada suspeita se o valor for superior 
# a R$ 10.000 ou se ocorrer fora do horário comercial (antes das 9h ou depois das 18h). 
# Dada uma transação como `transacao = {'valor': 12000, 'hora': 20}`, verifique se ela é suspeita.

# transacao = {'valor': 10000, 'hora': 20}

# if transacao['valor'] > 10000 or not(9 > transacao['hora'] < 18):
#     print("Transação suspeita!")
# else:
#     print("Transaçao ok")


### Exercício 6. Contagem de Palavras em Textos
# Objetivo:** Dado um texto, contar quantas vezes cada palavra única aparece nele.

# texto = "O compotamento será assim: quando e pressionado o atalho 'CTRL + /' a linha sobre o cursor e comentada com '//' e o cursor é deslocado para a próxima na linha, no sentindo de que, podemos seguir pressionando e comentando linhas em sequência."
# texto = texto.replace(",","")
# texto = texto.replace(".","").lower()

# lista = texto.split()

# contar_palavras ={}

# for palavra in lista:
#         if palavra in contar_palavras:
#             contar_palavras[palavra] += 1
#         else:
#             contar_palavras[palavra] = 1
# print(contar_palavras)


### Exercício 7. Normalização de Dados
# Objetivo:** Normalizar uma lista de números para que fiquem na escala de 0 a 1.

# numeros = [10, 20, 30, 40, 50]
# minimo = min(numeros)
# maximo = max(numeros)
# normalizados = [(x - minimo) / (maximo - minimo) for x in numeros]

# print(normalizados)


### Exercício 8. Filtragem de Dados Faltantes
# Objetivo:** Dada uma lista de dicionários representando dados de usuários, filtrar aqueles que têm um campo específico faltando

# usuarios = [
#     {"nome": "Alice", "email": "alice@example.com"},
#     {"nome": "Bob", "email": ""},
#     {"nome": "Carol", "email": "carol@example.com"}
# ]

# Usuarios_validos = []

# for usuario in usuarios:
#     if usuario["email"] !="":
#         Usuarios_validos = usuario["email"]

# print(Usuarios_validos)

# usuarios = [
#     {"nome": "Alice", "email": "alice@example.com"},
#     {"nome": "Bob", "email": ""},
#     {"nome": "Carol", "email": "carol@example.com"}
# ]

# usuarios_validos = [usuario for usuario in usuarios if usuario["email"]]

# print(usuarios_validos)


### Exercício 9. Extração de Subconjuntos de Dados
# Objetivo:** Dada uma lista de números, extrair apenas aqueles que são pares.

# lista = list()
# lista = [1,2,3,4,5,6,7,8,9]

# for k,l in enumerate(lista):
#     if l%2 != 0:
#         del lista[k]
#     #else:
#     #    print(f"O valor {l} é impar")
# print(lista)



### Exercício 10. Agregação de Dados por Categoria
# Objetivo:** Dado um conjunto de registros de vendas, calcular o total de vendas por categoria.

# vendas = [{"Categoria":"Sapato", "Valor":200},
#          {"Categoria":"Camaemesa", "Valor":100} ,
#          {"Categoria":"Sapato", "Valor":210},
#          {"Categoria":"Camaemesa", "Valor":140},
#          {"Categoria":"Roupa", "Valor":58}
# ]

# total_por_categoria = {}
# for i in vendas:
#     categoria = i["Categoria"]
#     valor = i["Valor"]

#     if categoria in total_por_categoria:
#         total_por_categoria[categoria] +=valor
#     else:
#         total_por_categoria[categoria] =valor
    
# print(total_por_categoria)



### Exercícios com WHILE

### Exercício 11. Leitura de Dados até Flag
# Ler dados de entrada até que uma palavra-chave específica ("sair") seja fornecida.

# while True:
#     palavra = input("Digite uma palavra, caso queira sair, digite:'sair': ").lower() 
#     if palavra == "sair":
#         break
#     else:
#         print(palavra)

### Exercício 12. Validação de Entrada
# Solicitar ao usuário um número dentro de um intervalo específico até que a entrada seja válida.

# while True:
#     num = input("Digite um número entre 5 e 13: ")
#     if num.isnumeric():
#         if int(num) in range(5,14):
#             print(num)
#             break
#         else:
#             print("Por favor, digite um numero dentro do intervalo")
#     else:
#         print("Por favor, não corresponte a um número")

### Exercício 13. Consumo de API Simulado
# Simular o consumo de uma API paginada, onde cada "página" de dados é processada em loop até que não haja mais páginas.

# pagina = 1
# total_paginas = 10

# while pagina <= total_paginas:
#     print(f"Processando pagina {pagina} de {total_paginas}")
#     pagina +=1

### Exercício 14. Tentativas de Conexão
# Simular tentativas de reconexão a um serviço com um limite máximo de tentativas.

# max_tentativa = 10
# tentativa = 1

# while tentativa <=max_tentativa:
#     print(f"Processando tentativa {tentativa} de {max_tentativa}")
#     # if True:
#     #     print("Conexão realizada com sucesso.")
#     #     break
#     # else:
#     #     print("Conexão não obteve sucesso.")
#     tentativa +=1





### Exercício 15. Processamento de Dados com Condição de Parada
# Processar itens de uma lista até encontrar um valor específico que indica a parada.

lista = list()
lista = [1,2,3,4,5,6,7,8,9]
valor = 6
i = 0

while lista[i] !=valor:
    i +=1
print(lista[i])
