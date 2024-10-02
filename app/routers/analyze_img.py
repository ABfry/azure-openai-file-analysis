from fastapi import APIRouter
import dotenv
from fastapi import UploadFile

import base64


from util.pdf_to_image import pdf_to_image_byte
from azureai.call_azure import ConversationRunner
from util.judge_file import judge_image_type, is_pdf

dotenv.load_dotenv()

analyze_img_router = APIRouter(prefix="/analyze-img", tags=["image"])


@analyze_img_router.post("/api/analyze-img")
async def analyze_img(file: UploadFile):

    # PDFの場合は画像に変換
    if is_pdf(file.filename):
        print("PDFファイルをjpegに変換します")
        image_data = await pdf_to_image_byte(file)
    else:
        # 入力された画像データをバイナリ形式で取得
        data = await file.read()

        # PDFと形式を合わせるためにリストに変換
        image_data = [data]

    # AzureOpenAIに送信するためにbase64形式に変換
    image_64 = image_to_base64(image_data)

    # 画像形式の判定 最初の要素から
    image_type = judge_image_type(image_data[0])

    # AzureOpenAIの呼び出し
    ai = ConversationRunner()
    response = await ai.run(image_64, image_type)

    # 結果の抽出
    content = response.choices[0].message.content

    print("----------結果----------")
    print(content)
    print("----------------------")

    return {"message": f"{content}"}


# バイナリデータをbase64形式に変換
def image_to_base64(image_data: list[bytes]) -> str:
    data = []
    for image in image_data:
        data.append(base64.b64encode(image).decode("utf-8"))
    return data
