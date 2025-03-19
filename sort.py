salpicon =  [] # Lista principal
salpiconPrice = [] # Lista de precios que será ordenada con sort
salpiconSort = [] # Lista principal que será ordenada usando salpiconPrince
while True:
    fruta = input("¿Qué fruta deseas añadir?: ")
    precio = int(input(f"Digite el precio de {fruta}: "))
    producto = {
        "fruta": fruta,
        "precio": precio
    }

    salpicon.append(producto)

    # Se rompe el ciclo infinito cuando la lista principal tenga una longitud de 10 datos
    if len(salpicon) == 10:
        break

# Extrae el precio de cada objeto (producto) de la lista (salpicon) y los añade a una lista aparte (salpiconPrice)
for f in salpicon:
    salpiconPrice.append(f["precio"])

# Ordena la lista de precios de mayor a menor
salpiconPrice.sort(reverse=True)

# Se recorre la lista ordena (salpiconPrice) como base para recorrer los objetos de la lista principal permitiendo así ordenar la lista principal tomando como base la lista de precios ordenada
for precio in salpiconPrice:
    for product in salpicon:
        if product["precio"] == precio:
            salpiconSort.append(product)
            print(product)
