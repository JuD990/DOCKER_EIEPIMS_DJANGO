# ./nginx/Dockerfile
FROM nginx:latest
COPY ./default.conf /etc/nginx/conf.d/default.conf
COPY wait-for-it.sh /wait-for-it.sh
RUN chmod +x /wait-for-it.sh
CMD ["/wait-for-it.sh", "frontend:3000", "--", "nginx", "-g", "daemon off;"]
