#Problema3
#Juan Esteban Clavijo García - 202225709

def funcionfx(a):
    global fx
    if a<=0:
        fx=8*a*a-6
    else:
        fx=3*a+5
    return fx

x=float(input("Digite el valor de x:"))
funcionfx(x)
print("")
print("F (",x,")=",fx)
