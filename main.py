print("Input the first number: ")
a = int(input())
print("Input the second number: ")
b = int(input())
while a != 0 and b != 0:
  if a>b:
    a = a%b
  else:
    b = b%a

nod = a+b
print(nod)
