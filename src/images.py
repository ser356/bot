import io
import tweepy

import os
import dotenv
from utils.utils import *
from utils.letra import create_image

credentials = get_credentials()


api_key = credentials["consumer_key"]
api_secret = credentials["consumer_secret"]
access_token = credentials["access_token"]
access_token_secret = credentials["access_token_secret"]


def get_twitter_conn_v1(api_key, api_secret, access_token, access_token_secret) -> tweepy.API:
    """Get twitter conn 1.1"""

    auth = tweepy.OAuth1UserHandler(api_key, api_secret)
    auth.set_access_token(
        access_token,
        access_token_secret,
    )
    return tweepy.API(auth)

def get_twitter_conn_v2(api_key, api_secret, access_token, access_token_secret) -> tweepy.Client:
    """Get twitter conn 2.0"""

    client = tweepy.Client(
        consumer_key=api_key,
        consumer_secret=api_secret,
        access_token=access_token,
        access_token_secret=access_token_secret,
    )

    return client

def post_image():
    client_v1 = get_twitter_conn_v1(api_key, api_secret, access_token, access_token_secret)
    client_v2 = get_twitter_conn_v2(api_key, api_secret, access_token, access_token_secret)


    img = create_image()
    # Crear un objeto BytesIO
    byte_stream = io.BytesIO()

    # Guardar la imagen en el objeto BytesIO
    img.save(byte_stream, format='PNG')

    # Mover el cursor al inicio del objeto BytesIO
    byte_stream.seek(0)
    media = client_v1.media_upload(filename="temp.png", file=byte_stream)
    media_id = media.media_id

    client_v2.create_tweet(text="", media_ids=[media_id])

if __name__ == "__main__":
    post_image()