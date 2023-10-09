# Tutaj pisz swój kod, młody padawanie ;-)
a = int(input("Podaj a: "))
b = int(input("podaj b: "))

while b>0:
        r = a%b
        a=b
        b=r

print(a)
