import multiprocessing
import time

def leer_linea(archivo_entrada, cola):
    #Lee los lineas del archivo de entrada y las coloca en la cola
    with open(archivo_entrada, 'r', encoding='utf-8') as f:
        for linea in f:
            cola.put(linea)
    cola.put(None)

def limpiar_linea(cola_entrada, cola_salida):
    #Limpia las lineas de la cola
    while True:
        linea = cola_entrada.get()
        if linea is None:
            cola_salida.put(None)
            break
        linea_limpia = linea.strip()
        cola_salida.put(linea_limpia)

def transformar_linea(cola_entrada, cola_salida):
    #Transforma las lineas de la cola
        while True:
            linea = cola_entrada.get()
            if linea is None:
                cola_salida .put(None)
                break
            linea_Mayusculas = linea.upper()
            cola_salida.put(linea_Mayusculas)

def escribir_linea(cola_entrada,archivo_salida):
    #Lee las lineas de la cola de entrada y las coloca en la cola de salida
   with open(archivo_salida, 'w', encoding='utf-8') as f:
        while True:
            linea = cola_entrada.get()
            if linea is None:
                break
            f.write(linea + '\n')


def elegir_tamaño():
    opciones = {
        "1": ("ejercicio_02/texto_entrada_1000.txt",     "ejercicio_02/texto_salida_secuencial_1000.txt"),
        "2": ("ejercicio_02/texto_entrada_100000.txt",   "ejercicio_02/texto_salida_secuencial_100000.txt"),
        "3": ("ejercicio_02/texto_entrada_1000000.txt",  "ejercicio_02/texto_salida_secuencial_1000000.txt"),
    }
    print("Elige el tamaño del archivo a procesar:")
    print("1) 1 000 líneas")
    print("2) 100 000 líneas")
    print("3) 1 000 000 líneas")
    opcion = input("Opción: ").strip()
    while opcion not in opciones:
        opcion = input("Opción inválida. Elige 1, 2 o 3: ").strip()
    return opciones[opcion]

if __name__ == '__main__':
    ruta_entrada, ruta_salida = elegir_tamaño()

    #crear colas 
    cola_lectura = multiprocessing.Queue()
    cola_limpieza = multiprocessing.Queue()
    cola_mayusculas = multiprocessing.Queue()
    

    inicio = time.time()

    proceso_lectura = multiprocessing.Process(target=leer_linea, args=(ruta_entrada, cola_lectura))
    proceso_limpieza = multiprocessing.Process(target=limpiar_linea, args=(cola_lectura, cola_limpieza))
    proceso_transformacion = multiprocessing.Process(target=transformar_linea, args=(cola_limpieza, cola_mayusculas))
    proceso_escritura = multiprocessing.Process(target=escribir_linea, args=(cola_mayusculas, ruta_salida))

    proceso_lectura.start()
    proceso_limpieza.start()
    proceso_transformacion.start()
    proceso_escritura.start()

    proceso_lectura.join()
    print("lectura terminó")
    proceso_limpieza.join()
    print("limpieza terminó")
    proceso_transformacion.join()
    print("transformación terminó")
    proceso_escritura.join()
    print("escritura terminó")

    fin = time.time()
    print(f"Archivo procesado paralelamente guardado en {ruta_salida}")
    print(f"Tiempo de ejecución: {fin - inicio:.2f} segundos")