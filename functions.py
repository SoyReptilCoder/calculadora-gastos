# funciones.py

def calcular_ahorro(ingresos, gastos):
    ahorro = ingresos - gastos
    porcentaje = (ahorro / ingresos) * 100 if ingresos else 0
    return ahorro, porcentaje
