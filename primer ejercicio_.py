a=float(input("a-> "))
b=float(input("b-> "))
c=float(input("c-> "))

resultado=((a*a*a)*((b*b)-(2*a*c)))/(2*b)

print(f"{resultado}")

#______________________________________


resultado_1=(3+5*8)<3
resultado_2=((-6*4/3)+2)<2
a=float(input("a-> "))
b=float(input("b-> "))

resultado_3=(a>b)

resultado_f=(resultado_1 and resultado_2) or resultado_3

print(resultado_1)
print(resultado_2)
print(resultado_3)
print(resultado_f)