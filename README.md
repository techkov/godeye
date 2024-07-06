# godeye 👁️

## Description 📄

**Godeye** - web-based tool, built for network activity monitoring on specific device *(Raw Beta Version Available for Now Only)*;

## Installation ⚙️

Here is the detailed process of installation:

1. Clone the repository - `git clone https://github.com/techkov/godeye.git | cd godeye`
2. Create the Virtual Environment - `python -m venv .venv`
3. Activate the Virtual Environment - `source ./.venv/bin/activate`
4. Install required packages using `requirements.txt` file - `python -m pip install -r requirements.txt`

## Usage 📑

To start the program, simply enter: `sudo python -m godeye`;

*Requires `sudo`, because of `tshark` module, which captures packets;*

---

### Disclaimer 🚫

#### For now, we do not recommend using this tool, because `Flask` Server is in debug mode currently, the usage of non-secured connection may lead to unpredictable and bad consequences. We are working on resolving this issue

## Thanks, Bye 👋🏻
