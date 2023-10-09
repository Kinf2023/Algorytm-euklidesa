a = int(input("podaj a: "))
b = int(input("podaj b: "))
while a!=b:
    if a>b:
        a = a-b
    if a<b:
        b = b-a

print(b)
