server {


    root /home/cleyton/html/mangaio.tag.i;


    index index.html index.htm;
    server_name mangaio.tag.i;

    access_log /var/log/nginx/mangaio.tag.i.access.log;
    error_log /var/log/nginx/mangaio.tag.i.error.log;


    location / {
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header Host $http_host;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_redirect off;
        proxy_pass http://127.0.0.1:8002;
    }

#    location /media  {
#        alias /home/cleyton/html/meusite_tagi/media;
#    }

#    location /static {
#        alias /home/cleyton/html/meusite_tagi/static;
#    }

    keepalive_timeout 5;

    client_max_body_size 4G;

}

