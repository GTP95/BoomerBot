FROM python:3.9
RUN groupadd -r user && useradd -r -g user user
COPY * /home/user/
RUN pip install -r /home/user/requirements.txt
RUN chmod +x /home/user/main.py
RUN ln -s /home/user/main.py /usr/local/sbin/boomerbot
RUN chmod +x /usr/local/sbin/boomerbot
USER user
WORKDIR /home/user
CMD boomerbot [L] bot \#bottest -p 7536987