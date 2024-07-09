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

1. Create `logs` directory (assuming you are in `~`) - `mkdir logs && touch ./logs/app.log`
2. Startup the engines - `waitress-serve --host 0.0.0.0 wsgi:wsgi`

*Requires `sudo`, because of `tshark` module, which captures packets;*

---

### Disclaimer 🚫

#### This code isn't the best program to run with sudo, as `waitress` does not provide enough protection for the code executed with root privileges. But using `nginx` or `Apache httpd` can save the situation. Soon we are going to add `nginx` setup version

## Thanks, Bye 👋🏻
