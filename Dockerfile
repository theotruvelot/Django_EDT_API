FROM python:3
EXPOSE 8000
ENV PORT 8080
ENV HOST 0.0.0.0
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/
ENTRYPOINT [ "python" "manage.py"]
CMD [ "runserver", "0.0.0.0:8080" ]
