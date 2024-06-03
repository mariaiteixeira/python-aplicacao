# Exercícios da quarta aula

#1 - Crie um dicionário representando informações sobre uma pessoa, como nome, idade e cidade.

pessoa = [{'nome': 'Maria', 'idade': 23, 'cidade': 'Belo Horizonte'}]

#2 - Utilizando o dicionário criado no item 1:

# Modifique o valor de um dos itens no dicionário (por exemplo, atualize a idade da pessoa);
# Adicione um campo de profissão para essa pessoa;
# Remova um item do dicionário.

pessoa[0]['idade'] = 24 

pessoa[0]['profissao'] = 'Engenheira' 

del pessoa[0]['cidade'] 

#3 - Crie um dicionário utilizando para representar números e seus quadrados de 1 a 5.

numeros = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Resposta do curso:

numeros_quadrados = {x: x**2 for x in range(1, 6)} 
print(numeros_quadrados)

#4 - Crie um dicionário e verifique se uma chave específica existe dentro desse dicionário.

pessoa = {'nome': 'Armano', 'idade': 22, 'cidade': 'Aplausos'} 

if 'nome' in pessoa: 
    print("A chave 'nome' existe no dicionário.") 
else: print("A chave 'nome' não existe no dicionário.")

#5 - Escreva um código que conte a frequência de cada palavra em uma frase utilizando um dicionário.

frase = "Aqui em casa temos uma escaminha diluída."

contagem_palavras = {} 
palavras = frase.split() 
for palavra in palavras: 
    contagem_palavras[palavra] = contagem_palavras.get(palavra, 0) + 1 
    print(contagem_palavras)