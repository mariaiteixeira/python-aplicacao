# Exercícios da terceira aula

#1 - Crie uma lista para cada informação a seguir:

# Lista de números de 1 a 10;
# Lista com quatro nomes;
# Lista com o ano que você nasceu e o ano atual.

lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

lista_nomes = ['Maria', 'Isabel', 'Ana', 'Nicole']

lista_anos = ['2000', '2024']

#2 - Crie uma lista e utilize um loop for para percorrer todos os elementos da lista.

deuses_egipcios = ['Bast', 'Isis', 'Anubis', 'Hathor', 'Set', 'Osiris', 'Sobek', 'Maat']

for deus in deuses_egipcios:
    print(deus)

#3 - Utilize um loop for para calcular a soma dos números ímpares de 1 a 10.

soma = 0
for i in range(1, 11, 2):
    soma += i
    print(soma)

# Lembrando que com a função range() o primeiro número é o início, o segundo o fim que não perpassa e o terceiro é o passo, ou seja, o incremento.

#4 - Utilize um loop for para imprimir os números de 1 a 10 em ordem decrescente.

for i in range(10, 0, -1):
    print(i)

#5 - Solicite ao usuário um número e, em seguida, utilize um loop for para imprimir a tabuada desse número, indo de 1 a 10.

numero = int(input('Insira um número: '))

for i in range(1, 11):
    print(f'{numero} x {i} é igual a {numero * i}')

#6 - Crie uma lista de números e utilize um loop for para calcular a soma de todos os elementos. Utilize um bloco try-except para lidar com possíveis exceções.

soma = 0

for num in range(1, 5):
    try:
        soma+=1
        print(soma)
    except Exception as e:
        print(f'Aconteceu algo de errado: {e}')

#7 - Construa um código que calcule a média dos valores em uma lista. Utilize um bloco try-except para lidar com a divisão por zero, caso a lista esteja vazia.

total = 0

for num in range(1, 10):
    try:
        total += 1
    except Exception as e:
        print(f'Ocorreu um erro: {e}')

# Cálculo da média fora do loop
media = sum(range(1, 10)) / 9
print(media)
