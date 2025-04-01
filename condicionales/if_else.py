print("Ingrese su edad:")
edad = input()

if int(edad) >= 18 :
    print("Ud. es mayor de edad.")
else:
    print("Ud. es menor de edad.")

sueldo = int(input("Ingrese su sueldo:"))

if sueldo > 4386000:
    print("Ud. pertence a la clase AB")
elif sueldo > 2070000:
    print("Ud. pertence a la clase C1a")
elif sueldo > 1374000:
    print("Ud. pertence a la clase C1b")
elif sueldo > 899000:
    print("Ud. pertence a la clase C2")
elif sueldo > 810000:
    print("Ud. pertence a la clase C3")
elif sueldo > 562000:
    print("Ud. pertence a la clase D")
else:
    print("Ud. pertence a la clase E")