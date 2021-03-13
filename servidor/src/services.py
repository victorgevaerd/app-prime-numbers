def get_primes(number_one: int, number_two: int):
    """Função que retorna todos números primos em um intervalo
    """
    if number_one < 0 or number_two < 0:
        return {'status': 0, 'message': 'Somente válido valores naturais'}
    if number_one >= number_two:
        largest = number_one
        smallest = number_two
    else:
        largest = number_two
        smallest = number_one
    primes = calculate_primes(largest=largest, smallest=smallest)
    return primes

def calculate_primes(largest: int, smallest: int):
    """Função que utiliza o 'Crivo de Eratóstenes' para descobrir os
    números primos em um intervalo
    (mais info em: https://pt.wikipedia.org/wiki/Crivo_de_Erat%C3%B3stenes)
    """
    result = []
    if largest > 2:
        dividers = [2]  # iniciando resposta com o único primo par
        max_limit = int((largest ** (1/2)) // 1)  # limite máximo necessário para achar todos primos
        max_limit_dividers = int((max_limit ** (1/2)) // 1)
        for number in range(3, max_limit+1, 2):  # formando lista com do 2 até o limite máximo com valores ímpares
            dividers.append(number)

        # transforma a lista de divisores para só divisores primos
        i = 1
        while dividers[i] <= max_limit_dividers:
            for j in range(len(dividers)-1, i+1, -1):
                if dividers[j] % dividers[i] == 0:
                    dividers.pop(j)
            i += 1

        # listando todos números primos no intervalo definido
        min_number = smallest if smallest % 2 != 0 else smallest+1
        for n in range(min_number, largest+1, 2):
            add = True
            i = 0
            while add and i < len(dividers)-1:
                if n % dividers[i] == 0:  # verifica se é divisível
                    add = False
                i += 1
            if add:
                result.append(n)
    return result
