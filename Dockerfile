FROM python:3.8

WORKDIR /src

COPY requirements.txt .

#RUN pip install -r requirements.txt

RUN pip3 install rasa && pip3 install rasa-x --extra-index-url https://pypi.rasa.com/simple

COPY src/ .

#CMD [ "rasa", "shell" ]