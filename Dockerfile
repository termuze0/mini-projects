FROM python:3.9
WORKDIR /workspaces
COPY . .
RUN pip install flask
EXPOSE 80 
CMD ["python", "app.py"]