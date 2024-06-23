from openai import AsyncAzureOpenAI
import os
import base64


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
