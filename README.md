# godeye 👁️

## Description 📄

**Godeye** - web-based tool, built for network activity monitoring on specific device *(Raw Beta Version Available for Now Only)*;

## Installation ⚙️

Here is the detailed process of installation:

1. Clone the repository - `git clone https://github.com/techkov/godeye.git | cd godeye`
2. Create the Virtual Environment - `python -m venv .venv`
3. Activate the Virtual Environment - `source ./.venv/bin/activate`
4. Install required packages using `requirements.txt` file - `python -m pip install -r requirements.txt`

## Usage & Setup 📑

1. Create `logs` directory - `mkdir logs && touch ./logs/app.log`
2. Startup the engines - `waitress-serve --host 0.0.0.0 --port 8000 wsgi:wsgi`

*Requires `sudo`, because of `tshark` module, which captures packets;*

### Apache2 Setup 🛡️

1. Apache2 Installation - `sudo apt update && sudo apt install apache2`
2. Apache2 Configuration - `sudo a2enmod proxy && sudo a2enmod proxy_http`

3. Apache2 Config ( open file: `sudo nano /etc/apache2/sites-available/[server_ip].conf` ):

```<VirtualHost *:80>
    ServerName [server_ip]

    # Logging configuration
    ErrorLog ${APACHE_LOG_DIR}/error.log
    CustomLog ${APACHE_LOG_DIR}/access.log combined

    # Proxy settings for Waitress
    ProxyPreserveHost On
    ProxyPass / http://localhost:8000/
    ProxyPassReverse / http://localhost:8000/

    <Proxy *>
        Order deny,allow
        Allow from all
    </Proxy>
</VirtualHost>
```

Enable Virtual Host and Restart Apache2 - `sudo a2ensite [server_ip].conf && sudo systemctl restart apache2`

## Thanks, Bye 👋🏻
