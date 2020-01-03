#!/usr/bin/env bash
# Script that sets up the web server for the deployment of web static
sudo apt-get update -y
sudo apt-get install nginx -y
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/
sudo touch /data/web_static/releases/test/index.html
echo "
    <html>
        <head>
        </head>
        <body>
            Holberton School
        </body>
    </html>
" > /data/web_static/releases/test/index.html
sudo ln -fsn /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
sudo sed -i '35ilocation /hbnb_static/ {' /etc/nginx/sites-available/default
sudo sed -i '36ialias /data/web_static/current/' /etc/nginx/sites-available/default
sudo sed -i '37iautoindex off;' /etc/nginx/sites-available/default
sudo sed -i '38i}' /etc/nginx/sites-available/default
sudo service nginx restart
