a=float(input("a-> "))
b=float(input("b-> "))

print(f"los numeros ingresados son\n\t- a : {a}\n\t- b : {b}")

if(input(" - Ingres x si desea intercabiar de posicion los numeros : ")=="x"or "X"):
    a,b=b,a
    print(f"\tel valor de a es :{a}")
    print(f"\tel valor de b es :{b}")
else:
    print("a :'v")