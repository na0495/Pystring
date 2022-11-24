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

