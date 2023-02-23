# cloudflare_ddns
A Python Script to update multible A records on Cloudflare

## Prerequisites
Make sure that you have Python 3 installed.
You need to install the "requests" library with pip.

## Cloudflare authentication details

You need to change these details
```sh
auth_email = "" # Your Cloudflare E-Mail
api_key = "" # Global API Token
zone_id = ""
proxy = True # Can be True or False
```

## Start
```sh
chmod +x cloudflare_ddns.py
python3 cloudflare_ddns.py
```
