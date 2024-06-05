import os
import random
import requests
from requests_oauthlib import OAuth1
import pandas as pd
import dotenv
from sierpinski.sierpinski import plot_sierpinski

dotenv.load_dotenv()

consumer_key = os.getenv("api-key")
consumer_secret = os.getenv("api-secret-key")
access_token = os.getenv("access-token")
access_token_secret = os.getenv("access-token-secret")

# def upload_image(auth, image_path):
#     url = "https://upload.twitter.com/1.1/media/upload.json"

#     with open(image_path, "rb") as image_file:
#         image_data = image_file.read()

#     files = {"media": image_data}
#     response = requests.post(url, auth=auth, files=files)
#     response.raise_for_status()

#     media_id = response.json()["media_id_string"]

#     return media_id


def mi_csv_con_musica():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(dir_path, "data_pruned.csv")
    df = pd.read_csv(file_path)
    return df

def build_spotify_url(df):
    random_row = df.sample()
    track_id = random_row["id"].values[0]
    url = f"https://open.spotify.com/track/{track_id}"
    return url

def connect_to_oauth(consumer_key, consumer_secret, access_token, access_token_secret):
    url = "https://api.twitter.com/2/tweets"
    auth = OAuth1(consumer_key, consumer_secret, access_token, access_token_secret)
    return url, auth

def build_content():
    # nivel = random.randint(1, 10)
    # plot_sierpinski(nivel)
    url = build_spotify_url(mi_csv_con_musica())
    return url

def main():
    auth = OAuth1(consumer_key, consumer_secret, access_token, access_token_secret)
    content = build_content()
    greeting = pd.read_csv("greeting.csv")
    # media_id = upload_image(auth, "sierpinski.png")
    payload = {
        "text": ' '.join(map(str, greeting.sample(n=1).values[0])) + " " + content,
        # "media_ids": media_id
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
