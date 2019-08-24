from random import choice, randint, random, uniform
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

##
def modulo_abs(a):
    resultado = abs(2 - (a*a))
    return resultado
##
def lista_string(palavra):
    lista_final = [] 
    for i in range(len(palavra)):
        num_aleatorio = randint(1,100)
        sub_lista = [palavra[i], num_aleatorio]
        lista_final.append(sub_lista)
        lista_final.sort(key=lambda x: x[1])
        num_aleatorio = 0
    return lista_final
##
def lista_inverte_binario(l1, l2):
    l3 = []
    l4 = []

    for i in range(8):
        if i < 2:
            l3.append(l1[i])
            l4.append(l2[i])
        elif i < 7:
            l3.append(l2[i])
            l4.append(l1[i])
        else:
            l3.append(l1[i])
            l4.append(l2[i])
    return l3, l4

def lista_string(palavra):
    lista_final = []
    num_aleatorio = randint(1,100)
    
    for i in range(len(palavra)):
        sub_lista = [palavra[i], num_aleatorio]
        lista_final.append(sub_lista)

    return lista_final


num = float(input("Digite um nĂºmero:"))
print(convertBinaPraReal('11111111'))
#print(strNum('ronicley'))
#print(troca('00000000'))
#print(trocaTroca('00001111', '11110000'))
#print(mod(-2))
#print(criaListaCemStrings())
##print(modulo_abs(num))
##palavra = input("Digite algo:")
##resultado = lista_string(palavra)
##print(resultado)
##for i in range(10):
##    print(resultado[i])
##l1 = [0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8]
##l2 = [1.1,1.2,1.3,1.4,1.5,1.6,1.7,1.8]
##print("Lista 01:", l1)
##print("Lista 02:", l2)
##print(lista_inverte_binario(l1, l2))
##palavra = input("Digite algo:")
##print(lista_string(palavra))
