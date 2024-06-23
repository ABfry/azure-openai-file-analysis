# GPT4o 画像分析サンプル

AzureOpenAI の GPT4o を使用し入力された画像の説明をさせる

## 使用例

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

### アクセス

[localhost:8000/docs](localhost:8000/docs)

---
