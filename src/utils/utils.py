from requests_oauthlib import OAuth1
import os
import dotenv
import pandas as pd
import logging
import pretty_errors

logging.basicConfig(level=logging.INFO)

dotenv.load_dotenv()



def get_credentials():
    consumer_key = os.getenv("api-key")
    consumer_secret = os.getenv("api-secret-key")
    access_token = os.getenv("access-token")
    access_token_secret = os.getenv("access-token-secret")
    
    if not all([consumer_key, consumer_secret, access_token, access_token_secret]):
        raise ValueError("Credentials not found")
    else:
        logging.info("Credentials found...")

    return {
        "consumer_key": consumer_key,
        "consumer_secret": consumer_secret, 
        "access_token": access_token, 
        "access_token_secret": access_token_secret
    }
    
    
    
def connect_to_oauth(consumer_key, consumer_secret, access_token, access_token_secret):
    url = "https://api.twitter.com/2/tweets"
    auth = OAuth1(consumer_key, consumer_secret, access_token, access_token_secret)
    
    if not all([url, auth]):
        raise ValueError("Connection failed")
    else:
        logging.info("Connection successful")
    return url, auth



def read_csv(name):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(dir_path, name)
    df = pd.read_csv(file_path)
    df = df.drop_duplicates()
    
    logging.info("CSV with music loaded...")
    return df

def build_spotify_url(df):
    random_row = df.sample()
    track_id = random_row["id"].values[0]
    url = f"https://open.spotify.com/track/{track_id}"
    
    logging.info("Spotify URL built...")
    return url

def build_content():
    url = build_spotify_url(read_csv("../data_pruned.csv"))
    
    logging.info("Content built...")
    return url

def get_greeting():
    greeting = read_csv("../greeting.csv")
    
    logging.info("Greeting loaded...")
    return ' '.join(map(str, greeting.sample(n=1).values[0]))