from captcha.image import ImageCaptcha
from PIL import Image


def generate_captcha_text(length=6):
    import string
    import random
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))


def generate_and_save_captcha(image_width=300, image_height=100, captcha_length=6, save_path="CAPTCHA.png"):
    image = ImageCaptcha(width=image_width, height=image_height)
    captcha_text = generate_captcha_text(captcha_length)
    data = image.generate(captcha_text)
    image.write(captcha_text, save_path)
    return captcha_text


if __name__ == "__main__":
    captcha_text = generate_and_save_captcha()
    print("CAPTCHA text: ", captcha_text)
Image.open("CAPTCHA.png")
