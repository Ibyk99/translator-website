#!/bin/bash
sudo yum install python -y
sudo yum install python-pip -y
sudo pip install flask
sudo yum install nginx -y
sudo pip install gunicorn
sudo pip install boto3
sudo yum install git -y

sudo systemctl start nginx
sudo systemctl enable nginx



#git clone https://github.com/Ibyk99/translator-website.git



