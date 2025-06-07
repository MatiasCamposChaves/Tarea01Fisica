import math

def ingresarVectorComp():
    x = float(input("Ingrese el componente X del vector: "))
    y = float(input("Ingrese el componente Y del vector: "))
    return (x, y)

def ingresarVectorMag():
    magnitud = float(input("Ingrese la magnitud del vector: "))
    angulo_grados = float(input("Ingrese el ángulo (en grados) respecto al eje X: "))
    angulo_radianes = math.radians(angulo_grados)
    x = magnitud * math.cos(angulo_radianes)
    y = magnitud * math.sin(angulo_radianes)
    return (x, y)

def main():
    print("=== SUMA DE N VECTORES ===")
    n = int(input("¿Cuántos vectores desea sumar?: "))

    suma_x = 0
    suma_y = 0

    for i in range(n):
        print(f"\nVector #{i+1}")
        print("¿Cómo desea ingresar el vector?")
        print("1. Por componentes")
        print("2. Por magnitud y dirección")
        opcion = input("Seleccione una opción (1 o 2): ")

        if opcion == '1':
            x, y = ingresarVectorComp()
        elif opcion == '2':
            x, y = ingresarVectorMag()
        else:
            print("Opción invalida, intente de nuevo.")
            continue  

        suma_x += x
        suma_y += y

    print("\n=== RESULTADO ===")
    print(f"Vector resultante: ({suma_x:.2f}, {suma_y:.2f})")

if __name__ == "__main__":
    main()