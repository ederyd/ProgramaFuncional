# ----------------------------------------------------------------------
# PROGRAMA FUNCIONAL: FUNCIÓN DE ORDEN SUPERIOR
# Lenguaje: Python
# ----------------------------------------------------------------------

# --- 1. Funciones de Transformación (Funciones Pasadas como Parámetro) ---

def elevar_al_cuadrado(numero):
    """
    Función simple que eleva un número al cuadrado.
    Esta función será pasada como parámetro.
    """
    return numero ** 2

def elevar_al_cubo(numero):
    """
    Función simple que eleva un número al cubo.
    Esta función será pasada como parámetro.
    """
    return numero ** 3

# --- 2. Función de Orden Superior ---

def aplicar_operacion(lista_de_numeros, funcion_a_aplicar):
    """
    Función de Orden Superior: Acepta una lista y OTRA FUNCIÓN como parámetro.

    Esta función recorre la lista y aplica la 'funcion_a_aplicar' a cada
    elemento, devolviendo una nueva lista con los resultados.

    Parámetros:
    - lista_de_numeros (list): La lista de valores de entrada.
    - funcion_a_aplicar (function): La función que se aplicará a cada elemento.
    """
    resultados = []
    for numero in lista_de_numeros:
        # Aquí es donde se llama la función que se pasó como parámetro
        resultado = funcion_a_aplicar(numero)
        resultados.append(resultado)
    return resultados

# --- 3. Uso y Ejecución del Programa ---

# 1. Definimos los datos de entrada
datos = [1, 2, 3, 4, 5]
print(f"Lista de entrada: {datos}\n")

# 2. Uso 1: Pasamos la función 'elevar_al_cuadrado' como parámetro
# Observa: Pasamos el NOMBRE de la función, NO la llamamos con paréntesis ()
cuadrados = aplicar_operacion(datos, elevar_al_cuadrado)
print("--- Resultado de elevar al CUADRADO ---")
print(f"Función aplicada: elevar_al_cuadrado")
print(f"Resultados: {cuadrados}") # Salida: [1, 4, 9, 16, 25]
print("-" * 35)

# 3. Uso 2: Pasamos la función 'elevar_al_cubo' como parámetro
cubos = aplicar_operacion(datos, elevar_al_cubo)
print("--- Resultado de elevar al CUBO ---")
print(f"Función aplicada: elevar_al_cubo")
print(f"Resultados: {cubos}") # Salida: [1, 8, 27, 64, 125]
print("-" * 35)
