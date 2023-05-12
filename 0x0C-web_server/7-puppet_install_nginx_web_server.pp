server {
    listen 80 default_server;
    listen [::]:80 default_server;
    root /var/www/html;
    index index.html;

    server_name _;

    location /redirect_me {
        return 301 https://fusedtc.tech/;
    }
}

