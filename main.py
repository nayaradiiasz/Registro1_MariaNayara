#Programa principal do projeto XYZ
print("Bem vindo ao projeto XYZ")
#Funcionalidade de Loop até 10
for i in range(1,10):
  print("Loop")
#Funcionalidade peidr valor ao usuário até ele digitar 0
user = int(input("Insira um número: "))
while user != 0:
  print("Diferente de Zero")
  user = int(input("Insira outro número: "))
print("Saiu do loop")

#Funcionalidade multiplicação até 10
userNum = int(input("Insira um número inteiro: "))
for cont in range(1,userNum):
  print(f"{cont} x {userNum} = {cont*userNum}")
