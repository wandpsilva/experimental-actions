FROM alpine:3.10

COPY entrypoint.sh /entrypoint.sh

CMD ["/entrypoint.sh"]