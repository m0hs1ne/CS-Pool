FROM alpine:latest

RUN apk update && apk upgrade && apk add --no-cache python3 py3-pip \
    net-tools tcpdump ca-certificates

COPY script.sh script.sh

CMD ["./script.sh"]
