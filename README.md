# IMAGE-CHECK
# PURPOSE
- Finding Missing Image.

# GETTING STARTED

### Step 1: 
- Remote into EC2 `ssh ec2-52-194-236-78.ap-northeast-1.compute.amazonaws.com`
- cd `home/machintos-hd/image-check`

### Step 2:
- python manage.py runserver 0:80

# Deploy Django with Nginx and gunicorn
### 1. Install Nginx
`sudo apt-get install nginx`

We can test with nginx whether it is working or not by
`sudo service nginx start`

If we go to the URL, i.e. http://ec2-XX-XX-X-XXX.compute-X.amazonaws.com and it should show us “Welcome to nginx”. Now stop the server to configure it further.

`sudo service nginx stop`

Config application:

`sudo vim /etc/nginx/sites-enabled/default`

Change the values according to our need, some basic things would be:

`access_log  /PATH/TO/THE PROJECT/nginx-access.log;
error_log  /PATH/TO/THE PROJECT/nginx-error.log info;`

###2. Work on Gunicorn
Install gunicorn pyth

`pip install gunicorn psycopg2`

run command :

`python manage.py collectstatic`

`sudo ufw allow 8000`

To test whether gunicorn running or not:

`gunicorn --bind 0.0.0.0:8000 GUChecktool.wsgi`

It will running as python manage.py runserver command

Run this to deactivate:

`deactivate`

Then config gunicorn service

sudo vim /etc/systemd/system/gunicorn.service`

and paste this code:

```
[Unit]
Description=gunicorn daemon
After=network.target

[Service]
User=ubuntu
Group=www-data
WorkingDirectory= /PATH/TO/THE/PROJECT/DIRECTORY
ExeccStart= /PATH/TO/THE/PROJECT/ENVIRONMENT/bin/gunicorn --access-logfile - --workers 3 
--bind unix:/PATH/TO/THE/PROJECT/DIRECTORY.sock PROJECT.wsgi:application

[Install]
WantedBy=multi-user.target
```

Then run this command to start gunicorn

`sduo systemctl start gunicorn`

Enable gunicorn service:

`sudo systemctl enable gunicorn`

C

`sudo systemctl status gunicorn`

`sudo journalctl -u gunicorn`

`sudo systemctl daemon-reload`

`sudo systemctl restart gunicorn`

`sudo vim /etc/nginx/sites-available/PROJECT`

```buildoutcfg
server
    listen 80;
    server_name SERVER_IP_ADRESS;
    location = /favicon.ico { access_log off; log_not_found off;}
    location /static/ {
        root /PATH/TO/THE/PROJECT/DIRECTORY;
    }
    location /{
        include proxy_params;
        proxy_pass http://unix:/PATH/TO/THE/PROJECT/DIRECTORY.sock;
    }
```

`sudo ln -s /etc/nginx/sites-available/PROJECT /etc/nginx/sites-enabled`

`sudo system restart nginx`

`sudo ufw delete allow 8000`

`sudo ufw allow 'Nginx Full'`

