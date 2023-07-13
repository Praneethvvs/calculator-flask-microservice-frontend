FROM python:3.9
COPY . /usr/application
WORKDIR /usr/application
ENV APP_URL
EXPOSE 5000
RUN cat requirements.txt | xargs -n 1 -L 1 python -m pip install
ENTRYPOINT ["python", "app.py"]