# Marco Vinícius Costódio Pellizzaro

"""
Para  obter  os  pontos  relativos  a  este  trabalho,  você  deverá  criar  um  programa,  utilizando  a 
linguagem  Python, C, ou C++.  Este  programa,  quando  executado,  irá  determinar  se  uma  string de 
entrada  faz  parte  da  linguagem  𝐿    definida  por  𝐿 = {𝑥 | 𝑥 ∈
 {𝑎,𝑏}∗ 𝑒 𝑐𝑎𝑑𝑎 𝑎 𝑒𝑚 𝑥 é 𝑠𝑒𝑔𝑢𝑖𝑑𝑜 𝑝𝑜𝑟 𝑝𝑒𝑙𝑜 𝑚𝑒𝑛𝑜𝑠 𝑑𝑜𝑖𝑠 𝑏} segundo o alfabeto  Σ={𝑎,𝑏,𝑐}.  
O  programa  que  você  desenvolverá  irá  receber  como  entrada um arquivo de texto  (.txt) 
contendo várias strings. A primeira linha do arquivo indica quantas strings estão no arquivo de texto de 
entrada. As linhas subsequentes contém uma string por linha.  A seguir está um exemplo das linhas que 
podem existir em um arquivo de testes para o programa que você irá desenvolver: 
3 
abbaba 
abababb 
bbabbaaab 
Neste  exemplo  temos  3  strings  de  entrada.  O  número  de  strings em  cada  arquivo  será 
representado  por  um  número  inteiro  positivo.  A  resposta  do  seu  programa  deverá  conter  uma, e 
somente uma linha de saída para cada string. Estas linhas conterão a string de entrada e o resultado 
da validação conforme o formato indicado a seguir: 
abbaba: não pertence.   
A  saída  poderá  ser  enviada  para  um  arquivo  de  textos,  ou  para  o  terminal  padrão  e  será 
composta de uma linha de saída por string de entrada. No caso do exemplo, teremos 3 linhas de saída. 
Para que seu programa possa ser testado você deve criar, no mínimo, três arquivos de entrada 
contendo um número diferente de strings diferentes. Os arquivos de entrada criados para os seus testes 
devem estar disponíveis tanto no ambiente repl.it quanto no ambiente Github. Observe que o professor 
irá  testar  seu  programa  com  os  arquivos  de  testes  que  você  criar  e  com,  no  mínimo  um  arquivo  de 
testes criado pelo próprio professor.  
"""

nome_arquivo = str(input("insira o nome do arquivo:"))

partes = nome_arquivo.split(".")

nome_arquivo = partes[0] + ".txt"

with open(nome_arquivo, "r") as arquivo:
    linhas = arquivo.readlines()

    cont = 0
    for x in linhas:
        item = x.split("\n")
        linhas[cont] = item[0]

        cont+=1

resultados = []

if int(linhas[0]) > len(linhas) - 1:
    print("ERRO, menos Strings do que mencionado")

else:
    cont = 1
    while int(linhas[0]) > cont - 1:
        estado = "S0"
        for x in linhas[cont]:
            if x != "a" or x != "b" or x != "c":
                print("ERRO, alfabeto incoerente")
                quit()
            if   estado == "S0":
                if x == "a":
                    estado = "S1"
            elif estado == "S1":
                if x == "b":
                    estado = "S2"
                else:
                    break
            elif estado == "S2":
                if x == "b":
                    estado = "S0"
                else:
                    break
        String = linhas[cont].split("\n")
        if estado == "S0":
            resultados.append(str(String[0]) + ": Pertence")
        else:
            resultados.append(str(String[0]) + ": Não pertence")
        cont += 1

    for p in resultados:
        print(p)
