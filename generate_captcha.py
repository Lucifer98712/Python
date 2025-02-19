from captcha.image import ImageCaptcha
from PIL import Image
import string
import random

def generate_captcha_text(length=6):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def generate_and_save_captcha(image_width=300, image_height=100, captcha_length=6, save_path="CAPTCHA.png"):
    image = ImageCaptcha(width=image_width, height=image_height)
    captcha_text = generate_captcha_text(captcha_length)
    image.write(captcha_text, save_path)  # Generates and saves the CAPTCHA image
    return captcha_text

if __name__ == "__main__":
    captcha_text = generate_and_save_captcha()
    print("CAPTCHA text:", captcha_text)
    # Optional: Display the generated CAPTCHA image
    Image.open("CAPTCHA.png").show()  # Added .show() to display the image