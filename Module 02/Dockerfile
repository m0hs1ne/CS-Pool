FROM nginx:alpine

RUN apk add --no-cache tor openssh

RUN adduser -D lharba && echo "lharba:password" | chpasswd

RUN ssh-keygen -A

COPY sshd_config /etc/ssh/sshd_config

COPY nginx.conf /etc/nginx/nginx.conf

COPY torrc /etc/tor/torrc

COPY index.html /usr/share/nginx/html

CMD nginx && /usr/sbin/sshd && tor