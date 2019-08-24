from random import choice, randint, uniform
from fractions import Fraction
def mod(valor):
    return abs(2 - float(valor)**2)

def criaListaCemStrings():
    arq = open('palavras.txt', 'r', encoding="utf8")
    palavras = arq.read()
    listaPalavras = palavras.split('\n')
    saida = []
    for i in range(100):
        saida.append(choice(listaPalavras))
    return saida

def num02 (listaFuncao):
    novaLista = []
    num = 1 
    for item in listaFuncao:
        listaAdd = [item, num] 
        
        novaLista.append(listaAdd)
         
    return novaLista

def trocaTroca(string1, string2):
    str1 = string1[0:4]+string2[4::]
    str2 = string1[4::]+string2[0:4]
    return str1, str2
def troca(string):
    split = [i for i in string]
    r = ''
    i = randint(0, len(split))
    if (split[i]=='0'):
        split[i] = '1'
    else:
        split[i] = '0'
    return r.join(split)

def strNum(string):
    return [string, uniform(0, 1000)]

def convertBinaPraReal(valor):
    part1 = int(str(valor[0])+str(valor[1]), 2)
    print(part1)
    cont = 1
    for i in valor[2::]:
        part2 = Fraction(int(i), 2**cont)
        cont+=1
    final = int(part1)+float(part2)
    return final

print(convertBinaPraReal('11111111'))
#print(strNum('ronicley'))
#print(troca('00000000'))
#print(trocaTroca('00001111', '11110000'))
#print(mod(-2))
#print(criaListaCemStrings())
