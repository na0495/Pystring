import os

from scripts import convert_pdf_to_img, extract_text_from_images

if __name__ == "__main__":
    for pdf in os.listdir('pdfs'):
        pdf_path = os.path.join('pdfs', pdf)
        convert_pdf_to_img(pdf_path)
        extract_text_from_images()
        print("\033[92m" + f"Successfully converted {pdf} to text" + "\033[0m")