opciones =tuple((
    "pan",
    "tortas",
    "cafes"))

print("bienvenido a redmoon, tu panaderia espacial favorita")

for i, val in enumerate(opciones):
    print(f"""{i}, {val}""")
print("")

categorial =int(input())
print("")
if categorial ==0:
    pan =tuple((
        "cascarita",
        "rollo",
        "mestiza",
        "bolita",
        "croisant",
        "ciabatta",
        "pan siete semillas",
        "roscon",
        "pan de queso",
        "pan integral",
        "cascarita 4x1000",
        "roscon 2x1000"))
    
    precios_1 = ((
        300,
        300,
        500,
        300,
        1500,
        3000,
        2800,
        600,
        700,
        400,
        1000,
        1000))
    for i, val in enumerate(pan):
        print(f""" {i}, {val} ${precios_1[i]}""")
    opcion = int(input())
    print("")
    print(f"""has seleccionado{pan[opcion]} cuesta ${precios_1[opcion]}""")
    print("")
    print("¿cuantos deseas?")
    print("")
    
    cantidad_1 =int(input())
    print("")
    valor_1 =precios_1[opcion]*cantidad_1
    print ("en total serian $", valor_1)

    print("")
    dinero =int(input("¿cuanto dinero desea ingresar?"))
    vueltos =dinero - valor_1
    

    if dinero >= valor_1:
        print(f"""tu cambio es ${vueltos}""")
    else:
        print(f"""faltan ${-vueltos}""")

elif categorial ==1:

    tortas =tuple((
        "chocolate",
        "maria_luisa",
        "cheesecake",
        "tartaleta",
        "pie_de_limon",
        "red_velvet",
        "vainilla",
        "zanahoria",
        "tres leches",
        "torta de fresa",
        "chocolate 3x12000",
        "vainilla 5*20000"))
    
    precios_3 =((
        14000,
        13000,
        14000,
        7000,
        6500,
        8000,
        15000,
        12000,
        8000,
        1000,
        12000,
        20000))
    for i, val in enumerate(tortas):
        print(f""" {i}, {val} ${precios_3[i]}""")
    opcion =int(input())
    print(f"""has escogido la siguiente torta{tortas[opcion]}con un valor de ${precios_3[opcion]}""")
    print("cuantas porciones deseas")
    

    cantidad_3 =int(input())
    
    valor_3 =precios_3[opcion]*cantidad_3
    print("el valor total es de $", valor_3)

    dinero =int(input("ingresa el dinero: "))
    vueltos =dinero -valor_3
    

    if dinero >= valor_3:
        print(f"""sus vuletas son ${vueltos}""")
    else:
        print(f"""te hacen falta ${-vueltos}""")

elif categorial == 2:
    cafes =tuple((
        "expreso",
        "americano",
        "latte",
        "latte frio",
        "macciato",
        "afogato",
        "mocachino",
        "cafe con leche",
        "frappe",
        "cappuccino",
        "americanos 2x12000",
        "latte 3x18000"))

    precios_2 =((
     9000,
     7000,
     7500,
     7500,
     9000,
     12000,
     15000,
     6000,
     9000,
     9000,
     12000,
     18000))
    for i, val in enumerate(cafes):
          print(f""" {i}, {val} ${precios_2[i]}""") 
opcion =int(input())
print(f"""has pedido lo siguiente {cafes[opcion]}con un valor de ${precios_2[opcion]}""")
print("¿cuantos cafes deseas?")

cantidad_2 =int(input())
valor_2 =precios_2[opcion]*cantidad_2
print("el valor es $", valor_2)

dinero =int(input("ingrese el dinero: "))
vueltos = dinero - valor_2


if dinero >= valor_2:
    print(f"""sus vueltos son ${vueltos}""")
else:
    print(f"""le falta un total de $ {-vueltos} compra anulada""")
