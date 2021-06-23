#codigo01
import sys

nome = input ("Digite seu nome:")
idade = input ("Digite sua Idade:")
print  ("Digite seu sexo:")
sexo = sys.stdin.readline()

print("Nome:" +nome +"\n" + "Sexo: %s Idade: %s"  %(sexo,idade))

#Codigo teste 02
# coding:utf-8
dedos  = int(input("Voçê tem quantos Anos?"))

if dedos == 18:
    print("Você tem 18 anos")
    elif dedos > 18:
        print("Você tem mais de 18 anos")
        else:
          print("Você é menor de idade")
          

  
