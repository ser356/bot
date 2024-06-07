import json
import random
from PIL import Image, ImageDraw, ImageFont
import textwrap
import os

def get_json_quotes():
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Construct the path to the json file
    json_file_path = os.path.join(script_dir, "datasets/quotes.json")
    with open(json_file_path, "r") as file:
        quotes = json.load(file)
        
    random_quote = random.choice(quotes)
    
    return random_quote['Quote'], random_quote['Author']

def create_image():
    # Create an image with a black background
    img = Image.new('RGB', (800, 600), color='black')
    d = ImageDraw.Draw(img)


    # Define the font and the lines of text
    script_dir = os.path.dirname(os.path.abspath(__file__))
    font_path = os.path.join(script_dir, "Coffee Fills.ttf")
    font = ImageFont.truetype(font_path, 20)
    quote, author = get_json_quotes()

    # Wrap the quote text
    max_width = 700  # Maximum width of the text area
    wrapped_quote = textwrap.fill(quote, width=50)  # Adjust width to fit the text within the max_width
    lines = wrapped_quote.split('\n') + [f"- {author}"]

    # Calculate total height of the text block
    total_height = 0
    for line in lines:
        bbox = d.textbbox((0, 0), line, font=font)
        _, _, _, height = bbox
        total_height += height

    # Calculate initial y_text position to center the text block vertically
    y_text = (img.height - total_height) // 2

    # Draw each line of text
    for line in lines:
        bbox = d.textbbox((0, 0), line, font=font)
        width, height = bbox[2] - bbox[0], bbox[3] - bbox[1]
        position = ((img.width - width) // 2, y_text)
        y_text += height

        # Choose a random color for the text
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

        # Draw the text
        d.text(position, line, fill=color, font=font)

    return img

