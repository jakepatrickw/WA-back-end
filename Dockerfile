FROM python:3.8

WORKDIR /usr/local/watergun-assassin-backend
COPY requirements.txt .
COPY watergun_assassin .
RUN pip install -r requirements.txt

EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]