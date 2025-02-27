"""
Programa: retorno_invest
Descrição: Este programa calcula os retornos para investimento determinado pelo usuário
Autor: Filipe Eich
Data: 27/02/2025
Versao: 0.0.1
"""

#Alocaçao de memoria

M="montante"
c="capital inicial"
i="taxa de juros em decimal"
t="prazo de investimento"


#Entrada de dados

c = float(input("\nOlá! Vamos calcular o retorno para seu investimento?? Comece digitando qual o capital inicial - em R$: "))
i = float(input("\nAgora, me diga qual a taxa de juros (a taxa deve estar em valor decimal - entre 0 e 1): "))
t = float(input("\nPor fim, atribua o prazo de investimento na mesma base de tempo que a taxa de juros descrita (a.a. ou a.m., por exemplo): "))


# Processamento de dados

#M=C⋅(1+i)^t

M=c*((1+i)**t)


#Saida de dados

print(f"\nO valor capitalizado ao final do período será de R${M:.2f}")


