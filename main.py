import os

import pytesseract
from pdf2image import convert_from_path
from PIL import Image


def convert_pdf_to_img(pdf_path):
    pdfs = pdf_path
    pdf_name = pdfs.split(".")[0]
    pdf_name = pdf_name.split("/")[1]
    pages = convert_from_path(pdfs, 350)

    i = 1
    for page in pages:
        page.save(f'images/{pdf_name}_'.format(pdf_name) + str(i) + '.jpg', 'JPEG')
        i = i+1     


def extract_text_from_images():
    for img in os.listdir('images'):
        image_path = os.path.join('images', img)
        text = pytesseract.image_to_string(Image.open(image_path))
        img_name = img.split(".")[0]
        with open(f'text/{img_name}.txt', 'a') as f:
            if text == '':
                continue
            # check if the file is empty
            if os.stat(f'text/{img_name}.txt').st_size == 0:
                f.write(text)
            else:
                f.truncate(0)
                f.write(text)



if __name__ == "__main__":
    # make images, text, and pdfs directories
    os.makedirs('images', exist_ok=True)
    os.makedirs('text', exist_ok=True)
    os.makedirs('pdfs', exist_ok=True)
    for pdf in os.listdir('pdfs'):
        pdf_path = os.path.join('pdfs', pdf)
        convert_pdf_to_img(pdf_path)
        extract_text_from_images()
        print("\033[92m" + f"Successfully converted {pdf} to text" + "\033[0m")