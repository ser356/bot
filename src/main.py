import random
import bot
import images
from utils.utils import logging

def main():
    # random choice between the two functions
    if random.choice([True, False]):
        bot.bot()
        logging.info("Bot function called")
        
    else:
        images.post_image()
        logging.info("Images function called")
        
if __name__ == "__main__":
    main()