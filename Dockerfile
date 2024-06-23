FROM python:3.11.5-slim
ENV PYTHONUNBUFFERED=1

WORKDIR /src
COPY ./app ./

# popplerインストール
RUN apt-get update && \
    apt-get install -y poppler-utils

RUN pip install --upgrade pip
RUN pip install -r requirements_base.txt
RUN pip install -r requirements.txt

# 変換したファイルを一時保存するためのフォルダを作成
RUN mkdir -p /app/data/

ENTRYPOINT ["uvicorn", "main:app", "--host", "0.0.0.0", "--reload"]
