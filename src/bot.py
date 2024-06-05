import random
import requests
from requests_oauthlib import OAuth1
import os
import pandas as pd

import dotenv

import matplotlib.pyplot as plt
import numpy as np
import random
import base64


from sierpinski.sierpinski import plot_sierpinski




dotenv.load_dotenv()


consumer_key = os.getenv("api-key")
consumer_secret = os.getenv("api-secret-key")
access_token = os.getenv("access-token")
access_token_secret = os.getenv("access-token-secret")
bearer_token = os.getenv("bearer-token")





def mi_csv_con_musica():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(dir_path, "dataset/data_pruned.csv")
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
    
    
    content = build_content()
    greeting = pd.read_csv("datasets/greeting.csv")
    
    payload = {
        
        
        "status": greeting.sample(n=1).values[0]+" "+content["text"],
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
