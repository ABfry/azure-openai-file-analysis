import re
import mimetypes


# バイナリデータから画像形式を判定
# 参考 : https://xaro.hatenablog.jp/entry/2017/05/17/103000
def judge_image_type(image_data: bytes) -> str:
    if re.match(b"^\xff\xd8", image_data[:2]):
        print("画像形式 : jpeg")
        return "jpeg"
    elif re.match(b"^\x89\x50\x4e\x47\x0d\x0a\x1a\x0a", image_data[:8]):
        print("画像形式 : png")
        return "png"
    else:
        print("画像形式 : その他")
        return "other"


# PDFかどうかを判定
def is_pdf(file_name: str) -> bool:
    mime = mimetypes.guess_type(file_name)[0]
    return mime == "application/pdf"
