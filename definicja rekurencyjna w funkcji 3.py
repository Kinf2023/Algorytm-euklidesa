a = int(input("podaj a: "))
b = int(input("podaj b: "))

def nwd(a,b):
    if a==b:
        return a
    if a > b:
        return nwd(a -b,b)
    if a < b:
        return nwd(a,b-a)

print(nwd(a,b))
