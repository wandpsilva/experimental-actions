FROM alpine:3.10

COPY entrypoint.sh /entrypoint.sh

RUN chmod +x /entrypoint.sh

RUN apk update && apk add bash

RUN mkdir /ghcli

WORKDIR /ghcli

RUN wget https://github.com/cli/cli/releases/download/v1.0.0/gh_1.0.0_linux_386.tar.gz -O ghcli.tar.gz

RUN tar --strip-components=1 -xf ghcli.tar.gz

ENTRYPOINT ["/entrypoint.sh"]