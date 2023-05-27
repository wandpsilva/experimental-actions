FROM alpine:3.10

COPY entrypoint.sh /entrypoint.sh

RUN chmod +x /entrypoint.sh

RUN apk update && apk add bash

RUN curl -Lo tmp/ghlinux.tar.gz \
  https://github.com/cli/cli/releases/download/v2.10.1/gh_2.10.1_linux_amd64.tar.gz \
  && tar --strip-components=1 -xf tmp/ghlinux.tar.gz \
  && rm tmp/ghlinux.tar.gz

ENTRYPOINT ["/entrypoint.sh"]