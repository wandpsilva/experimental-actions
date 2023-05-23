FROM alpine

COPY entrypoint.sh /entrypoint.sh

CMD ["chmod +x /entrypoint.sh"]