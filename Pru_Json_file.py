import json
x = '[{"name": "John", "age" : 30, "city": "New York"}, {"name": "Rafa", "age" : 54, "city": "Castellón"}]'
y = json.loads(x)
print(y)

with open("Salida.txt", 'a') as fichero:
    for k in range(100):
        y[0]["age"] = k
        #Escribimos el json convirtiéndolo a una cadena
        fichero.write(f"{str(y)}\n")
        #Escribimos el json utilizando la función dump de json
        json.dump(y,fichero)
        fichero.write("\n")

    
