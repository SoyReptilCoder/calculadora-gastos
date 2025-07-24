# main.py

from functions import calcular_ahorro

def main():
    try:
        ingresos = float(input("Ingresos mensuales: $"))
        gastos = float(input("Gastos mensuales: $"))

        ahorro, porcentaje = calcular_ahorro(ingresos, gastos)

        print(f"\nTe quedan ${ahorro:.2f}")
        print(f"Ahorro: {porcentaje:.2f}%")
    except ValueError:
        print("Error: Ingresá un número válido.")

if __name__ == "__main__":
    main()
