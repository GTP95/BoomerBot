FROM python:3.9
COPY * /root/bot/
RUN pip install -r /root/bot/requirements.txt
RUN chmod +x /root/bot/main.py
RUN ln -s /root/bot/main.py /usr/local/sbin/boomerbot
RUN groupadd -r user && useradd -r -g user user
USER user
WORKDIR /root/bot
CMD python /root/bot/main.py \#bottest