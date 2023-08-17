import pytesseract
from PIL import Image
from io import BytesIO
import pypdfium2 as pdfium


pytesseract.pytesseract.tesseract_cmd=r'C:\Users\P2848116\OneDrive - Charter Communications\Documents\Visual Studio Code\saas\gpt\Scripts\pytesseract.exe'

# 1. Convert PDF file into images via pypdfium2

def convert_pdf_to_images(file_path, scale=300/72):
    file_path = r'C:\Users\P2848116\OneDrive - Charter Communications\Documents\Visual Studio Code\saas\gpt\gpt-data-extraction\sample.pdf'
    pdf_file = pdfium.PdfDocument(file_path)

    page_indices = [i for i in range(len(pdf_file))]

    renderer = pdf_file.render(
        pdfium.PdfBitmap.to_pil,
        page_indices=page_indices
        # scale=scale
    )

    final_images = []


    for i, image in zip(page_indices, renderer):

        image_byte_array = BytesIO()
        image.save(image_byte_array, format='jpeg', optimize=True)
        image_byte_array = image_byte_array.getvalue()
        final_images.append(dict({i: image_byte_array}))

    return final_images

# 2. Extract text from images via pytesseract


def extract_text_from_img(list_dict_final_images):

    image_list = [list(data.values())[0] for data in list_dict_final_images]
    image_content = []

    for index, image_bytes in enumerate(image_list):

        image = Image.open(BytesIO(image_bytes))
        raw_text = pytesseract.pytesseract.image_to_string(image)
        image_content.append(raw_text)

    return "\n".join(image_content)


def extract_content_from_url(url: str):
    images_list = convert_pdf_to_images(url)
    text_with_pytesseract = extract_text_from_img(images_list)

    return text_with_pytesseract


# 3. Extract structured info from text via LLM


# # 4. Send data to make.com via webhook
# def send_to_make(data):
#     # Replace with your own link
#     webhook_url = "https://hook.eu1.make.com/xxxxxxxxxxxxxxxxx"

#     json = {
#         "data": data
#     }

#     try:
#         response = requests.post(webhook_url, json=json)
#         response.raise_for_status()  # Check for any HTTP errors
#         print("Data sent successfully!")
#     except requests.exceptions.RequestException as e:
#         print(f"Failed to send data: {e}")


# 5. Streamlit app
def main():
    content = extract_content_from_url(r"C:\Users\P2848116\OneDrive - Charter Communications\Documents\Visual Studio Code\saas\gpt\gpt-data-extraction\sample.pdf")
    print(content)
                

if __name__ == '__main__':
   #multiprocessing.freeze_support()
    main()
