import os
os.system("cls")#Codigos Para limpiar pantalla
#Conversor de Euros a pesos colombianos
def convertir_euros_a_pesos(euros, tasa_cambio):
    pesos = euros * tasa_cambio
    return pesos

def main():
    try:
        euros = float(input("Ingresa la cantidad de euros a convertir: "))
        tasa_cambio = float(input("Ingresa la tasa de cambio actual de euros a pesos colombianos: "))
        
        pesos = convertir_euros_a_pesos(euros, tasa_cambio)
        
        print(f"{euros} euros equivale a {pesos} pesos colombianos.")
        
    except ValueError:
        print("¡Error! Asegúrate de ingresar un número válido.")

if __name__ == "__main__":
    main()
def mi_funcion():
    # Código de la función
while True:
    mi_funcion("cls")
    respuesta = input("¿Desea volver a ejecutar la función? (s/n): ")
    if respuesta.lower() != "s":
        break
