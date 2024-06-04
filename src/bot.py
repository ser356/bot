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


def connect_to_oauth(consumer_key, consumer_secret, access_token, access_token_secret):
    url = "https://api.twitter.com/2/tweets"
    auth = OAuth1(consumer_key, consumer_secret, access_token, access_token_secret)
    return url, auth

def main():
    song = build_spotify_url(mi_csv_con_musica())
    payload = {"text": song}
    url, auth = connect_to_oauth(
        consumer_key, consumer_secret, access_token, access_token_secret
    )
    response = requests.post(
        auth=auth, url=url, json=payload
    )
    
    print(response.json())


if __name__ == "__main__":
    main()