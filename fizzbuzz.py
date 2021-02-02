x=int(input("Digite um número:"))
aux= x%3
aux1=x%5
if aux==0 and aux1==0 :
	print("FizzBuzz")
else:
	print(x)