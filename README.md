# GPT4o ファイル分析サンプル

AzureOpenAI の GPT4o を使用し入力された画像の説明をさせる
PDF、PNG、JPEG対応

## 使用例

![IMG_8730](https://github.com/ABfry/openai-api-image-read/assets/88941921/d79536c6-4218-46ec-b8e6-5b7e3b6c35c2)
↓
![スクリーンショット 2024-06-23 15 19 54](https://github.com/ABfry/openai-api-image-read/assets/88941921/7935f5ed-c5c5-486e-acbf-1f0ab827d89d)

---

![IMG_7676](https://github.com/ABfry/openai-api-image-read/assets/88941921/394236e0-4191-45a8-a7e1-2e42d65ce950)

↓

![スクリーンショット 2024-06-23 15 21 40](https://github.com/ABfry/openai-api-image-read/assets/88941921/f21dc63f-b0d0-49a8-a629-b00a5dd4416f)

## つかいかた

### git clone の実行

```sh
git clone https://github.com/ABfry/openai-api-image-read.git
```

### .env 設定

`app/.env.example`を参考して`app/.env`に.env ファイルを作成
API_KEY と ENDPOINT の取得は https://learn.microsoft.com/ja-jp/azure/ai-services/openai/assistants-quickstart?tabs=command-line%2Ctypescript&pivots=programming-language-python を参照

### Docker の起動

```sh
make up(docker-compose up)
```

### FastAPI Docs アクセス

[localhost:8000/docs](localhost:8000/docs)

---
