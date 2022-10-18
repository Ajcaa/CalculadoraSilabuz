# -------CALCULADORA ------- #

num1 = float(input("Elija un Primer Numero: "))
num2 = float(input("Elija un Segundo Numero: "))


print("""a) Suma
b) Resta,
c) Multiplicacion
d) Division 
e) Potencia""")

op = input("Ahora elija un operador con respecto a la letra: ").lower()

def suma():
    x = num1 + num2
    print("La suma de", num1, "más", num2, "es:", x)

def resta():
    y = num1 - num2
    print("Restar", num1, "menos", num2, "es igual a:", y)

def multiplicacion():
    z = num1 * num2
    print("El numero", num1, "multiplicado por", num2, "es:", z)

def division():
    p = num1 / num2
    print("El numero", num1, "dividido entre", num2, "es:", p)

def potencia():
    r = num1 ** num2
    print("el numero", num1,"elevado a la", num2,
    "es:", r)

while op not in ("a","b","c","d","e"):
    op = input("Por favor, elija una letra entre a,b,c,d,e: ")

if op == "a":
    suma()
if op == "b":
    resta()
if op == "c":
    multiplicacion()
if op == "d":
    division ()
if op == "e":
    potencia()
