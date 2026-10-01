from PIL import Image
import os
import time
import multiprocessing


def convertir_a_gris(ruta_imagen):
    """Convierte una imagen a escala de grises."""
    try:
        imagen = Image.open(ruta_imagen)
        imagen_gris = imagen.convert('L')  # 'L' representa escala de grises
        nombre_archivo, extension = os.path.splitext(ruta_imagen)
        ruta_gris = nombre_archivo + "_gris" + extension
        imagen_gris.save(ruta_gris)
        print(f"Imagen convertida: {ruta_imagen} -> {ruta_gris}")
    except FileNotFoundError:
        print(f"Error: No se encontró la imagen {ruta_imagen}")
    except Exception as e:
        print(f"Error al procesar {ruta_imagen}: {e}")


def procesar_lote(lista_imagenes):
    for image in lista_imagenes:
        convertir_a_gris(image)


if __name__ == '__main__':
    directorio_actual = os.path.dirname(os.path.abspath(__file__))
    directorio_imagenes = os.path.join(directorio_actual, "images")

    lista_imagenes = [
        os.path.join(directorio_imagenes, f)
        for f in os.listdir(directorio_imagenes)
        if os.path.isfile(os.path.join(directorio_imagenes, f))
    ]

    num_procesos = 4
    tamano_porcion = len(lista_imagenes) // num_procesos

    procesos = []

    tiempo_inicial = time.time()

    for i in range(num_procesos):
        inicio = i * tamano_porcion

        fin = (i + 1) * tamano_porcion if i < num_procesos - 1 else len(
            lista_imagenes)

        porcion = lista_imagenes[inicio:fin]

        p = multiprocessing.Process(target=procesar_lote, args=(porcion,))
        procesos.append(p)
        p.start()

    for p in procesos:
        p.join()

    tiempo_fin = time.time()

    print(
        f"Tiempo total de procesamiento: {tiempo_fin - tiempo_inicial:.2f} segundos")