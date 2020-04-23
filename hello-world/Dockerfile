FROM python:3.6

RUN mkdir /app

RUN pip install Flask

COPY hello.py /app/hello.py

ENTRYPOINT [ "python", "/app/hello.py" ]