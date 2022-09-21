FROM ubuntu:18.04
RUN apt-get update && apt-get install -y python3 python3-pip

WORKDIR /app
COPY . /app/

RUN pip3 install -r requirements.txt
CMD ["python3","replace_txt_api.py"]