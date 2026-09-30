import time

#funcion que recibe dos rutas: el archivo que va a leer y el archivo donde va a escribir el resultado
def procesar_texto_secuencial(ruta_entrada, ruta_salida):
    """Procesa el archivo de texto secuencialmente."""
    try:
        #Abre el archivo de entrada en modo lectura y el archivo de salida en modo escritura
        with open(ruta_entrada, 'r', encoding='utf-8') as f_in, open(ruta_salida, 'w', encoding='utf-8') as f_out: 
            
            for linea in f_in: #recorre el archivo de entrada linea por linea
                linea_limpia = linea.strip() #elimina los espacios en blanco al inicio y al final de la linea
                linea_mayusculas = linea_limpia.upper() # convierte el texto a mayusculas
                f_out.write(linea_mayusculas + '\n') #escribe la linea procesada en el archivo de salida, agregando el salto de linea que se quito.
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo {ruta_entrada}") #eror si no se encuentra el archivo de entrada

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

    inicio = time.time() 
    procesar_texto_secuencial(ruta_entrada, ruta_salida)
    fin = time.time()
    print(f"Tiempo total de procesamiento secuencial: {fin - inicio:.2f} segundos")
    print(f"Archivo procesado secuencialmente guardado en {ruta_salida}")