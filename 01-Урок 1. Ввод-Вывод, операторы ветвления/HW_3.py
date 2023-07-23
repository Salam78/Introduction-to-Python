n=int(input("Введите номер билета: "))

a=n // 1000
b=n % 1000

d1=a // 100
d2=a % 100//10
d3=a % 10

sum1=d1+d2+d3
print("Сумма первых трех чисел--->",sum1)
d4=b // 100
d5=b % 100//10
d6=b % 10

sum2=d4+d5+d6
print ("Сумма последних трех чисел--->",sum2)
if sum1 == sum2:
  print("YES")
else:
  print("NO")