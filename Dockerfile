FROM python:3.7.3-alpine
COPY src /app
WORKDIR /app
RUN pip3 install -r requirements.txt 
RUN python3 -m textblob.download_corpora
EXPOSE 3002
ENTRYPOINT [ "python3" ]
CMD [ "sentiment_analysis.py" ]