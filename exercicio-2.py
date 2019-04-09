#!/usr/bin/env python

minutos = int(input("Digite os minutos usados: "))

def functionMinutos(minutos):
    
    if minutos < 200:
        preco = 0.20
    else:
        
        if minutos <= 400:
            preco = 0.18 

        else:
            preco = 0.15
        
    print("Valor gastado no mes é de {}".format(minutos * preco))

functionMinutos(minutos)
