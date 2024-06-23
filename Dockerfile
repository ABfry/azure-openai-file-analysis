FROM python:3.11.5-slim
ENV PYTHONUNBUFFERED=1

WORKDIR /src
COPY ./app ./

RUN pip install --upgrade pip
RUN pip install -r requirements_base.txt
RUN pip install -r requirements.txt

# RUN apt-get update && apt-get install -y supervisor
# ADD ./attachment /attachment
# RUN cp -arp /attachment/supervisor/supervisord.d /etc/supervisord.d ;\
#     cp -arp /attachment/supervisor/supervisord.conf /etc/supervisord.conf ;\
#     cp -arp /attachment/cmd/ready.sh /ready.sh

# CMD sh /ready.sh && /usr/bin/supervisord -c /etc/supervisord.conf

ENTRYPOINT ["uvicorn", "main:app", "--host", "0.0.0.0", "--reload"]
