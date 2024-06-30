from pdf2image import convert_from_bytes
from fastapi import File
import io

OUTPUT_FOLDER = "./data"
FILE_NAME = "tmp"
FILE_PATH = f"{OUTPUT_FOLDER}/{FILE_NAME}.jpeg"


# PDFをImage(byte形式)に変換する
# 参考 : https://qiita.com/East-Da/items/2b2982f8dfcea33c0e80
async def pdf_to_image_byte(pdf: File) -> list[bytes]:
    pdf_data = await pdf.read()

    # PDFの全ページをjpegに変換
    image_path = convert_from_bytes(pdf_data, fmt="jpeg")

    img_byte_arr_list = []
    for image in image_path:
        # バイトストリームに変換
        img_byte_arr = io.BytesIO()
        image.save(img_byte_arr, format="JPEG")
        img_byte_arr = img_byte_arr.getvalue()
        img_byte_arr_list.append(img_byte_arr)

    print(f"ページ数 : {len(image_path)}")

    return img_byte_arr_list
