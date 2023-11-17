FROM python:3.9
RUN groupadd -r user && useradd -r -g user user
COPY * /home/user
RUN pip install -r /home/user/requirements.txt
RUN chmod +x /home/user/main.py
RUN ln -s /home/user/main.py /usr/local/sbin/boomerbot
USER user
WORKDIR /home/user
CMD python /root/bot/main.py \#bottest