FROM python:3.12
WORKDIR /Desktop 
COPY . .
RUN pip install flask
EXPOSE 80 
CMD ["python", "app.py"]