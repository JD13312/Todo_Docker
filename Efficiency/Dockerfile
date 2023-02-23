FROM python:3
COPY . /app
WORKDIR /app
RUN pip install -r requirnments.txt
EXPOSE 3001
CMD flask run --host 0.0.0.0

