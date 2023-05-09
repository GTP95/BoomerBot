FROM python:3.9
COPY * /root/bot/
RUN pip install -r /root/bot/requirements.txt
WORKDIR /root/bot
CMD python /root/bot/main.py \#bottest