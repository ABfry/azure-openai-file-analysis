from pdf2image import convert_from_bytes
from fastapi import File
import mimetypes
import io

OUTPUT_FOLDER = "./data"
FILE_NAME = "tmp"
FILE_PATH = f"{OUTPUT_FOLDER}/{FILE_NAME}.jpeg"


# PDFをImage(byte形式)に変換する
# 参考 : https://qiita.com/East-Da/items/2b2982f8dfcea33c0e80
async def pdf_to_image_byte(pdf: File):
    pdf_data = await pdf.read()

    # PDFの全ページをjpegに変換
    image_path = convert_from_bytes(pdf_data, fmt="jpeg")

    # バイトストリームに変換
    img_byte_arr = io.BytesIO()
    image_path[0].save(img_byte_arr, format="JPEG")
    img_byte_arr = img_byte_arr.getvalue()

    return img_byte_arr


# PDFかどうかを判定
def is_pdf(file_name: str) -> bool:
    mime = mimetypes.guess_type(file_name)[0]
    return mime == "application/pdf"
