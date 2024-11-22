# print("Welcome to my Curreny Converter")

# cambio = 3.75 #cambio de dolar a sol 
# usd = float(input("Ingrese la cantidad en dolares que quiere cambiar: "))
# soles = usd * cambio
# print("El cambio en soles es: " + str(soles))



#i want to be able to input a currency and the program will look for it in the list of currencies
def currency_converter():
    currencies = {
    "usd": 3.75,
    "eur": 3.95,
    "cad": 2.71,
    "aud": 2.46,
    "jpy": 0.02
}
    print("Moneda disponibles: ")
    
    print(currencies)
    
    selected_key = input("Ingrese la moneda que desea cambiar: ").lower()

    #checando si la moneda existe en el diccionario
    if selected_key in currencies:
        amount = float(input("Inserte la cantidad que desea cambiar: "))

        cambio = currencies[selected_key]
        resultadocambio = amount * cambio

        print(f"El resultado es: {resultadocambio}")
    
    else: 
        print("La moneda no fue encontrada")

currency_converter()