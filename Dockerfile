FROM python:3.7

ADD ./src /code/src
ADD app.py /code
ADD requirements.txt /code

ENV PYTHONPATH=$PYTHONPATH:./src/
WORKDIR /code
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN chmod 777 -R .
CMD python app.py