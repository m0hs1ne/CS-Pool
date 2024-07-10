FROM nginx:alpine

RUN apk add --no-cache tor openssh

RUN ssh-keygen -A
RUN echo "root:passwordlharba" | chpasswd

COPY sshd_config /etc/ssh/sshd_config

COPY nginx.conf /etc/nginx/nginx.conf

COPY torrc /etc/tor/torrc

COPY index.html /usr/share/nginx/html

EXPOSE 80
EXPOSE 4242

CMD nginx && /usr/sbin/sshd && tor