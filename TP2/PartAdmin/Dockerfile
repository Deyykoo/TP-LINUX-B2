FROM nginx

RUN apt update -y

RUN chown -R nginx:nginx /etc/nginx

RUN chown -R nginx:nginx /var/cache/nginx

RUN touch /var/run/nginx.pid

RUN chown nginx:nginx /var/run/nginx.pid

USER nginx