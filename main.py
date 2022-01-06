import math
a=float(input("Kvadrāta malas garums: "))
if a<5:
  a=float(input("Kvadrāta malas garums(no 5cm): "))
kv1=math.pow(a,2)
kv2=math.pow(a+5,2)
proc=(kv2/kv1)*100
print("Procenti:",round(proc))