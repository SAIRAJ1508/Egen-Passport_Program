# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1EmR1CTsnvTlo48YL5jOjaIGG5iFUcCon
"""

FROM python:3.7.11-slim-buster

COPY . /app

WORKDIR /app

RUN pip install -r requirements.txt

ENTRYPOINT ["python"]

CMD ["raw_data___pubsub.py"]