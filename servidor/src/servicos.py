import asyncio


async def calcula_primos(first_num: int, second_num: int):
    """Função que utiliza o 'Crivo de Eratóstenes' para descobrir os
    números primos em um intervalo
    """
    try:
        first_num = int(first_num)
        second_num = int(second_num)
    except ValueError:
        return {'status': 0, 'message': 'Valores inválidos'}
    if first_num < 0 or second_num < 0:
        return {'status': 0, 'message': 'Somente válido valores naturais'}
    if first_num >= second_num:
        maior = first_num
        menor = second_num
    else:
        maior = second_num
        menor = first_num
    primos = crivo_eras(maior)
    i = 0
    while primos[i] < menor and i < len(primos):
        i += 1
    for j in range(i-1, -1, -1):
        primos.pop(j)
    return primos

def crivo_eras(num: int):
    """Crivo de Eratóstenes (mais info em: https://pt.wikipedia.org/wiki/Crivo_de_Erat%C3%B3stenes)
    """
    if num < 2:
        resposta = []
    else:
        resposta = [2]
        for n in range(3, num+1, 2):
            resposta.append(n)
        if len(resposta) > 3:
            max_limite = (num ** (1/2)) // 1
            i = 1
            while resposta[i] <= max_limite:
                for w in range(len(resposta)-1, i+1, -1):
                    if resposta[w] % resposta[i] == 0:
                        resposta.pop(w)
                i += 1
    return resposta

async def get_historico():
    pass
