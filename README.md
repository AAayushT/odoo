Here I am putting some basic requirements and process of installing and configuring your system for running odoo14
and yes also my first odoo module StudentPortal

THIS IS A WAY TO INSTALL ODOO14 FROM 0 TO 100% IF YOU WANT TO WORK ON MY MODULE YOU CAN GET IT FROM CUSTOM ADDONS FILE "StudentPortal"

first as usual get all the necesarry updates done
$ sudo apt update

then dependencies
$ sudo apt install git python3-pip build-essential wget python3-dev python3-venv \
    python3-wheel libfreetype6-dev libxml2-dev libzip-dev libldap2-dev libsasl2-dev \
    python3-setuptools node-less libjpeg-dev zlib1g-dev libpq-dev \
    libxslt1-dev libldap2-dev libtiff5-dev libjpeg8-dev libopenjp2-7-dev \
    liblcms2-dev libwebp-dev libharfbuzz-dev libfribidi-dev libxcb1-dev
    
now create a system user
as you are going to use odoo14 why not make one with name odoo14
$ sudo useradd -m -d /opt/odoo14 -U -r -s /bin/bash odoo14

As you are here you already know postgreSQL its necessary as odoo uses it as database back-end
$ sudo apt install postgresql

Now like previously user for postgres
$ sudo su - postgres -c "createuser -s odoo14"

Now we need to install wkhtmopdf(or whatever it is I surely not put this wierd name)
wkhtmltopdf is a set of open-source command-line tools for rendering HTML pages into PDF and various image formats.
$ sudo wget https://github.com/wkhtmltopdf/wkhtmltopdf/releases/download/0.12.5/wkhtmltox_0.12.5-1.bionic_amd64.deb
install it
$ sudo apt install ./wkhtmltox_0.12.5-1.bionic_amd64.deb

Well its always safe to use virtual environment(hehehe!!!!)
$ sudo su - odoo14
$ git clone https://www.github.com/odoo/odoo --depth 1 --branch 14.0 /opt/odoo14/odoo
$ cd /opt/odoo14
$ python3 -m venv odoo-venv

Activate the virtual environment
$ source odoo-venv/bin/activate

Install all the required modules with pip3
(venv)$ pip3 install wheel
(venv)$ pip3 install -r odoo/requirements.txt

now deactivate it
(venv)$ deactivate

Hey you wanna use odoo you probably want to creat your own module RIGHT!!
lets create a custom folder where you can keep your own modules
$ mkdir /opt/odoo14/odoo-custom-addons

switch bac to your sudo user
$ exit

IT'S TIME FOR CONFIGURING
$ sudo nano /etc/odoo14.conf
==========================/etc/odoo14.conf===========================
[options]
; This is the password that allows database operations:
admin_passwd = my_admin_passwd
db_host = False
db_port = False
db_user = odoo14
db_password = False
addons_path = /opt/odoo14/odoo/addons,/opt/odoo14/odoo-custom-addons
=====================================================================

open system unit file
$ sudo nano /etc/systemd/system/odoo14.service
==========================================/etc/systemd/system/odoo14.service==========================================
[Unit]
Description=Odoo14
Requires=postgresql.service
After=network.target postgresql.service

[Service]
Type=simple
SyslogIdentifier=odoo14
PermissionsStartOnly=true
User=odoo14
Group=odoo14
ExecStart=/opt/odoo14/odoo-venv/bin/python3 /opt/odoo14/odoo/odoo-bin -c /etc/odoo14.conf
StandardOutput=journal+console

[Install]
WantedBy=multi-user.target
======================================================================================================================

Time to tell system that you have done some mischieve(heheheheheh!!!!)
$ sudo systemctl daemon-reload

Start the Odoo service and enable it to start on boot by running:
$ sudo systemctl enable --now odoo14

Lets verify the service 
!!!this line can become life savor!!!
[you will understand when you create your own module]
$ sudo systemctl status odoo14

Hahahahaha
Clap ur hands U done it
now go to browser
run
http://localhost:8069
!!MAGIC!!
