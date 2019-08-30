import main


def principal(valor):
    
    
    cemStringReal = []
    stringAvaliacao = []
    novaStrAval = []
    for i in range(len(valor)):
        cemStringReal.append(main.convertBinaPraReal(valor[i]))
    for i in range(len(cemStringReal)):
        stringAvaliacao.append(main.strNum(valor[i], main.mod(cemStringReal[i])))
    return stringAvaliacao

def avaliaPox0(valor):
    dezMenoresAval = main.fdezMenoresAval(valor)
    lista90Strings01 = []
    l =[]
    for i in range(0,len(dezMenoresAval), 2):
        str1, str2 = main.trocaTroca(dezMenoresAval[i][0], dezMenoresAval[i+1][0])
        l.append(str1)
        l.append(str2)
    for i in range(len(dezMenoresAval)):
        lista90Strings01.append([l[i], main.mod(main.convertBinaPraReal(l[i]))])
    dezStr = []
    lista = []
    l1 = []
    for i in range(10):
        lista.append(lista90Strings01[main.choice(range(len(lista90Strings01)))][0])
        troca = main.troca(lista[i])
        l1.append(troca)
        dezStr.append([l1[i], main.mod(main.convertBinaPraReal(l1[i]))])

    lista100Strings01 = lista90Strings01
    for i in dezStr:
        lista100Strings01.append(i)
    return lista100Strings01

lista100Strings01 = main.criaListaCemStrings01()

p1 = avaliaPox0(principal(lista100Strings01))
print(p1)
p2 = avaliaPox0(p1)
#print(p2)
p3 = avaliaPox0(p2)
#print(p3)
p4 = avaliaPox0(p3)
#print(p4)
p5 = avaliaPox0(p4)
#print(p5)
p6 = avaliaPox0(p5)
#print(p6)
p7 = avaliaPox0(p6)
#print(p7)
p8 = avaliaPox0(p7)
print('\n\n\n\n\n\n')
print(p8)