import random
import requests
from requests_oauthlib import OAuth1
import os
import pandas as pd

import dotenv

dotenv.load_dotenv()


consumer_key = os.getenv("api-key")
consumer_secret = os.getenv("api-secret-key")
access_token = os.getenv("access-token")
access_token_secret = os.getenv("access-token-secret")
bearer_token = os.getenv("bearer-token")


import os

def mi_csv_con_musica():
    # Obtiene la ruta del directorio actual del script
    dir_path = os.path.dirname(os.path.realpath(__file__))
    # Une la ruta del directorio con el nombre del archivo
    file_path = os.path.join(dir_path, "data_pruned.csv")
    df = pd.read_csv(file_path)
    return df

def build_spotify_url(df):
    # get random row and append id to url
    random_row = df.sample()
    track_id = random_row["id"].values[0]
    url = f"https://open.spotify.com/track/{track_id}"
    return url


import matplotlib.pyplot as plt
import numpy as np
import random

def sierpinski(n):
    """ Genera los puntos del triángulo de Sierpinski. """
    if n == 0:
        return np.array([[0, 0], [1, 0], [0.5, np.sqrt(3)/2]])
    else:
        prev_points = sierpinski(n - 1)
        top = (prev_points + np.array([0.5, np.sqrt(3)/2])) / 2
        left = (prev_points + np.array([0, 0])) / 2
        right = (prev_points + np.array([1, 0])) / 2
        return np.concatenate([left, top, right])
def random_color():
    # Elige un índice para el componente de color alto/bajo
    idx = random.randint(0, 2)
    color = [0, 0, 0]
    # Establece un componente de color al azar a un valor alto (cercano a 1) o bajo (cercano a 0)
    color[idx] = random.choice([random.uniform(0, 0.3), random.uniform(0.7, 1)])
    # Establece los otros componentes de color a valores aleatorios
    color[(idx+1)%3] = random.random()
    color[(idx+2)%3] = random.random()
    return tuple(color)

# En tu código, reemplaza la línea que genera el color aleatorio con una llamada a esta función
color=random_color()

def plot_sierpinski(n):
    """ Dibuja el triángulo de Sierpinski de nivel n. """
    points = sierpinski(n)
    fig = plt.figure(figsize=(6, 6))
    ax = fig.add_subplot(111)
    ax.set_facecolor('black')
    for i in range(len(points)):
        plt.fill(points[i:i+2, 0], points[i:i+2, 1], color=random_color())
    plt.axis('equal')
    plt.axis('off')

    # Nivel del triángulo de Sierpinski a generar

    plt.savefig("sierpinski.png")





def connect_to_oauth(consumer_key, consumer_secret, access_token, access_token_secret):
    url = "https://api.twitter.com/2/tweets"
    auth = OAuth1(consumer_key, consumer_secret, access_token, access_token_secret)
    return url, auth

import base64

def build_content():
    nivel = random.randint(1, 10)
    plot_sierpinski(nivel)
    with open("sierpinski.png", "rb") as img_file:
        encoded_string = base64.b64encode(img_file.read()).decode('utf-8')
    url = build_spotify_url(mi_csv_con_musica())
    payload = {
        "text": url,
        "media": encoded_string
    }
    return payload  

def main():
    #content = build_spotify_url(mi_csv_con_musica())
    content = build_content()
    payload = {
        "status": content["text"],
        "media": content["media"]
    }
    url, auth = connect_to_oauth(
        consumer_key, consumer_secret, access_token, access_token_secret
    )
    response = requests.post(
        auth=auth, url=url, json=payload
    )
    
    print(response.json())


if __name__ == "__main__":
    main()