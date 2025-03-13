FROM python:latest
RUN pip install matplotlib numpy 
COPY main.py /main.py
CMD ["python3", "/main.py"]
