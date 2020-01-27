FROM alpine
RUN apk update && apk add python && apk add --update py-pip && pip instal flask
COPY app.py /opt/
ENTRYPOINT python /opt/app.py