import string
import time
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Diccionarios de palabras clave para diferentes temas, incluyendo puntos de recompensa genéricos
diccionarios = {
    "comida": ["recetas", "restaurantes", "cocina", "comida rápida", "postres", "platos saludables",
               ("Acrobacias de ardillas voladoras", 10),
               ("Noche de fajitas vegetarianas", 10),
               ("Consejos de golf", 10)],
    "películas": ["próximos estrenos", "mejores películas", "actores famosos", "géneros de películas", "películas clásicas",
                  ("Puzle de mitad de semana", 5),
                  ("Alta tecnología: TV QD-OLED", 5),
                  ("Completa este puzle", 5)],
    "juegos": ["videojuegos", "juegos en línea", "consolas de juegos", "mejores juegos del año", "juegos de mesa"],
    "deportes": ["fútbol", "baloncesto", "tenis", "natación", "atletismo", "deportes extremos"],
    "países": ["países del mundo", "mapas de países", "mejores lugares para visitar", "culturas del mundo"],
    "lugares": ["lugares turísticos", "ciudades famosas", "monumentos históricos", "playas paradisíacas"],
    "música": ["géneros musicales", "artistas famosos", "conciertos en vivo", "álbumes más vendidos",
               ("¿Conoces la respuesta?", 5),
               ("¿Sabes la respuesta?", 5),
               ("Cita del día", 5)]
}

# Crear una instancia del controlador de Edge
driver = webdriver.Edge()

# Realizar 100 búsquedas aleatorias
for _ in range(100):
    # Seleccionar un tema aleatorio
    tema = random.choice(list(diccionarios.keys()))

    # Seleccionar una palabra clave aleatoria del diccionario del tema
    palabra_clave = random.choice(diccionarios[tema])

    # Si la palabra clave es una tupla, es un punto de recompensa genérico
    if isinstance(palabra_clave, tuple):
        query = palabra_clave[0]
        print(f"¡Has ganado {palabra_clave[1]} puntos por '{query}'!")
    else:
        # Generar la consulta de búsqueda aleatoria
        query = f"{palabra_clave} {random.choice(['ideas', 'mejores', 'consejos', 'noticias'])}"

    # Navegar a la página de inicio de Bing
    driver.get("https://www.bing.com")

    # Esperar hasta que el elemento de búsqueda esté presente en la página
    search_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "q"))
    )

    # Escribir la consulta en el cuadro de búsqueda
    search_box.send_keys(query)
    search_box.send_keys(Keys.RETURN)

    # Esperar un momento antes de la siguiente búsqueda
    time.sleep(2)

# Cerrar el navegador
driver.quit()
