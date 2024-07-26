# godeye 👁️

## Description 📄

**Godeye** - web-based tool, built for network activity monitoring on specific device;

## Installation ⚙️

Here is the detailed process of installation:

1. Clone the repository - `git clone https://github.com/techkov/godeye.git | cd godeye`
2. Create the Virtual Environment - `python -m venv .venv`
3. Activate the Virtual Environment - `source ./.venv/bin/activate`
4. Install required packages using `requirements.txt` file - `python -m pip install -r requirements.txt`

## Usage & Setup 📑

1. Create `logs` directory - `mkdir logs && touch ./logs/app.log`
2. Replace *19th* line content in `core/flask/__init__.py` with Your main network interface
3. Startup the engines - `sudo waitress-serve --host 127.0.0.1 --port 8000 wsgi:wsgi`

*Requires `sudo`, because of `tshark` module, which captures packets;*

### Apache2 Setup 🛡️

1. Apache2 Installation - `sudo apt update && sudo apt install apache2`
2. Apache2 Configuration - `sudo a2enmod proxy proxy_http proxy_balancer lbmethod_byrequests rewrite`

3. Apache2 Config ( open file: `sudo nano /etc/apache2/sites-available/[server_ip].conf` ):

``` text
<VirtualHost *:80>
    ServerName [server_ip]

    ErrorLog ${APACHE_LOG_DIR}/error.log
    CustomLog ${APACHE_LOG_DIR}/access.log combined

    ProxyPreserveHost On
    ProxyPass / http://127.0.0.1:8000/
    ProxyPassReverse / http://127.0.0.1:8000/

    <Proxy *>
        Order deny,allow
        Allow from all
    </Proxy>
</VirtualHost>
```

Enable Virtual Host and Restart Apache2 - `sudo a2ensite [server_ip].conf && sudo systemctl restart apache2`

### Service Setup 🛠️

*I recommend moving your application to `/opt` directory: `sudo mv ./godeye /opt`, and you also might encounter problem with virtual environment, so recreate one*

Create Process Config - `sudo nano /etc/systemd/system/godeye.service`

``` ini
[Unit]
Description=Waitress Server for Flask App (Godeye)
After=network.target

[Service]
User=root
Group=www-data
WorkingDirectory=/opt/godeye
Environment="PATH=/opt/godeye/.venv/bin/activate"
ExecStart=/opt/godeye/.venv/bin/waitress-serve --host=127.0.0.1 --port=8000 wsgi:wsgi

[Install]
WantedBy=multi-user.target
```

Reload systemd, enable and start the service - `sudo systemctl daemon-reload && sudo systemctl enable godeye.service && sudo systemctl start godeye.service`

## Thanks, Bye 👋🏻
