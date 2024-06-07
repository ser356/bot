import requests
from utils.utils import *


def bot():
    credentials = get_credentials()
    print(credentials)
    auth = OAuth1(credentials["consumer_key"], credentials["consumer_secret"], credentials["access_token"], credentials["access_token_secret"])
    content = build_content()
    greeting = get_greeting()
    payload = {
        "text": greeting + " " + content,
    }
    url, auth = connect_to_oauth(
        **credentials
    )
    response = requests.post(
        auth=auth, url=url, json=payload
    )
    logging.info(response.json())
    if response.status_code != 201:
        logging.error(response.json())
        raise ValueError("Request failed...Exiting"+response.status_code)
    else:
        logging.info("Tweet posted...Exiting"+response.status_code)
            

def main():
    bot()

if __name__ == "__main__":
    main()
