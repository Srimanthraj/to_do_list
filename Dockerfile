FROM python:3.11

ENV PYTHONUNBUFFERED=1

WORKDIR C:\Users\windows\Desktop\django\todolist


COPY . .
RUN pip install -r requirements.txt 
EXPOSE 8000
CMD [ "python","manage.py", "runserver", "0.0.0.0:8000"]
