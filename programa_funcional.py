# ----------------------------------------------------------------------
# DOCUMENTACIÓN DE LA TAREA: PROGRAMACIÓN FUNCIONAL
# ----------------------------------------------------------------------
# Nombre del Alumno: Eder Yañez Díaz
# Fecha de Creación: 06 de Noviembre de 2025
# Lenguaje Utilizado: Python
# Versión: Python 3.11.2
# Propósito del Programa: Demostrar el concepto de una Función de Orden Superior,
#                         pasando una función como argumento a otra función.
# ----------------------------------------------------------------------

# ----------------------------------------------------------------------
# INTRODUCCIÓN TEÓRICA A LA PROGRAMACIÓN FUNCIONAL (PF)
# ----------------------------------------------------------------------
# 1. ANTECEDENTES Y ORIGEN:
# La Programación Funcional (PF) es un paradigma de programación basado en el
# concepto matemático de función. Sus bases fueron establecidas en la década
# de 1930 por Alonzo Church con el 'Cálculo Lambda', un sistema formal para
# expresar la computación basado en la abstracción y la aplicación de funciones.
# Los lenguajes puramente funcionales como Lisp (1958) y Haskell implementan
# directamente estos principios.

# 2. PILARES DE LA PF:
# A diferencia de la programación imperativa (que se enfoca en 'cómo' cambiar
# el estado), la PF se enfoca en 'qué' calcular, basándose en dos principios:
#
# A. FUNCIONES PURAS: Una función es pura si:
#    a) Siempre devuelve el mismo resultado para los mismos argumentos de entrada.
#    b) No produce 'efectos secundarios' (no modifica variables fuera de su ámbito,
#       no interactúa con el sistema de archivos, etc.).
#
# B. INMUTABILIDAD: Los datos no cambian una vez creados. En lugar de modificar
#    una estructura de datos existente, se crea una nueva con el cambio deseado.

# 3. JUSTIFICACIÓN DEL USO:
# La PF es valorada por varias razones clave:
#    a) Concurrencia y Paralelismo: La ausencia de efectos secundarios y la
#       inmutabilidad hacen que las funciones puras sean inherentemente seguras
#       para ejecutar en paralelo sin riesgo de 'condiciones de carrera'.
#    b) Mantenimiento y Debugging: El código es más predecible y fácil de probar
#       porque el resultado solo depende de la entrada.
#    c) Funciones de Orden Superior (HOS): Permiten pasar funciones como datos,
#       lo que conduce a código más abstracto, reutilizable y conciso (como se
#       demuestra en este programa).

# ----------------------------------------------------------------------
# DEMOSTRACIÓN DEL CONCEPTO: FUNCIÓN DE ORDEN SUPERIOR
# ----------------------------------------------------------------------

# --- 1. Funciones de Transformación (Funciones Pasadas como Parámetro) ---

def elevar_al_cuadrado(numero):
    """
    Función simple (callback) que eleva un número al cuadrado (x^2).
    Esta función será pasada como parámetro a 'aplicar_operacion'.
    """
    return numero ** 2

def elevar_al_cubo(numero):
    """
    Función simple (callback) que eleva un número al cubo (x^3).
    Esta función será pasada como parámetro a 'aplicar_operacion'.
    """
    return numero ** 3

# --- 2. Función de Orden Superior ---

def aplicar_operacion(lista_de_numeros, funcion_a_aplicar):
    """
    FUNCIÓN DE ORDEN SUPERIOR: Acepta una lista y OTRA FUNCIÓN como parámetro.

    Esta función recorre la lista y aplica la 'funcion_a_aplicar' a cada
    elemento, devolviendo una nueva lista con los resultados.

    Parámetros:
    - lista_de_numeros (list): La lista de valores de entrada.
    - funcion_a_aplicar (function): La función que se aplicará a cada elemento.
    
    Retorna:
    - list: Una nueva lista con los resultados transformados.
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
print("--- Demostración de Funciones de Orden Superior en Python ---")
print(f"Lista de entrada: {datos}\n")

# 2. Uso 1: Pasamos la función 'elevar_al_cuadrado' como parámetro
# La función aplicar_operacion reusa su lógica, solo cambia el comportamiento
# que le pasamos.
cuadrados = aplicar_operacion(datos, elevar_al_cuadrado)
print("--- Resultado de elevar al CUADRADO ---")
print(f"Función aplicada: elevar_al_cuadrado")
print(f"Resultados: {cuadrados}")
print("-" * 35)

# 3. Uso 2: Pasamos la función 'elevar_al_cubo' como parámetro
# El código de 'aplicar_operacion' no ha cambiado, solo la función que recibe.
cubos = aplicar_operacion(datos, elevar_al_cubo)
print("--- Resultado de elevar al CUBO ---")
print(f"Función aplicada: elevar_al_cubo")
print(f"Resultados: {cubos}")
print("-" * 35)

# 4. Uso 3: Usando una función anónima (lambda) como parámetro
# Demostrando aún más flexibilidad del paradigma funcional.
multiplicar_por_diez = lambda x: x * 10
multiplicados = aplicar_operacion(datos, multiplicar_por_diez)
print("--- Resultado de multiplicar por DIEZ (usando lambda) ---")
print(f"Función aplicada: lambda x: x * 10 (función anónima)")
print(f"Resultados: {multiplicados}")
print("-" * 35)
