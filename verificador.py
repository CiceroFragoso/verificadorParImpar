from time import sleep


numero= int(input("digite um numero : "))
resultado = numero %2
print("=*="*30)
sleep(2)
if resultado == 0 :
    print("o numero : {} e pá".format(numero))
else :
    print("o numero : {} e impar".format(numero))
