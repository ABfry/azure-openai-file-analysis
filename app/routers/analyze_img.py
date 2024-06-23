from fastapi import APIRouter
import dotenv
from fastapi import UploadFile
import os
import base64
import re

from openai import AsyncAzureOpenAI

dotenv.load_dotenv()

analyze_img_router = APIRouter(prefix="/analyze-img", tags=["image"])


@analyze_img_router.post("/api/analyze-img")
async def analyze_img(image: UploadFile):
    # 入力された画像データをバイナリ形式で取得
    image_data = await image.read()

    # AzureOpenAIに送信するためにbase64形式に変換
    image_64 = image_to_base64(image_data)

    # 画像形式の判定
    image_type = judge_image_type(image_data)

    # AzureOpenAIの呼び出し
    ai = ConversationRunner()
    response = await ai.run(image_64, image_type)

    # 結果の抽出
    content = response.choices[0].message.content

    print("----------結果----------")
    print(content)
    print("----------------------")

    return {"message": f"{response}"}


# バイナリデータをbase64形式に変換
def image_to_base64(image_data: bytes) -> str:
    return base64.b64encode(image_data).decode("utf-8")


# バイナリデータから画像形式を判定
# 参考 : https://xaro.hatenablog.jp/entry/2017/05/17/103000
def judge_image_type(image_data: bytes) -> str:
    # JPEG
    if re.match(b"^\xff\xd8", image_data[:2]):
        print("画像形式 : jpeg")
        return "jpeg"
    elif re.match(b"^\x89\x50\x4e\x47\x0d\x0a\x1a\x0a", image_data[:8]):
        print("画像形式 : png")
        return "png"
    else:
        print("画像形式 : その他")
        return "other"


# AzureOpenAIの呼び出し
class ConversationRunner:
    def __init__(self):
        self.openai = AsyncAzureOpenAI(
            api_key=os.getenv("AZURE_OPENAI_KEY"),
            api_version="2024-05-01-preview",
            azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
        )

    async def run(self, image_data: base64, image_type: str):
        try:
            response = await self.openai.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {
                        "role": "user",
                        "content": [
                            {
                                "type": "text",
                                "text": "入力された画像について説明してください",
                            },
                            {
                                "type": "image_url",
                                "image_url": {
                                    "url": f"data:image/{image_type};base64,{image_data}"
                                },
                            },
                        ],
                    }
                ],
            )
        except Exception as e:
            print(f"Error: {e}")
            return None

        return response
