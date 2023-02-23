import requests

def getIp():

    url = "https://am.i.mullvad.net/ip"
    response = requests.get(url)
    ip = response.content.decode().strip()

    return ip

def getDnsId(dnsrecords, auth_email, api_key, zone_id):
    url = f"https://api.cloudflare.com/client/v4/zones/{zone_id}/dns_records"
    headers = {
        'X-Auth-Key': api_key,
        'X-Auth-Email': auth_email,
        'Content-Type': 'application/json'
        }

    response = requests.get(url, headers=headers)

    data = response.json()
    dns_id = []

    for item in data["result"]:
        if item["name"] in dnsrecords and item["type"] == "A":
            dns_id.insert(0,[item["id"], item["name"]])

    return dns_id

def setDnsRecords(dns_ids, ip, proxy, auth_email, api_key, zone_id):

    for dns_id in dns_ids:

        url = f"https://api.cloudflare.com/client/v4/zones/{zone_id}/dns_records/{dns_id[0]}"
        headers = {
            "Content-Type": "application/json",
            "X-Auth-Email": auth_email,
            "X-Auth-Key": api_key
        }
        payload = {
            "comment": "Updated by Jendrny.tech Scipt",
            "content": ip,
            "name": dns_id[1],
            "proxied": proxy,
            "ttl": 1
        }
        response = requests.request("PATCH", url, json=payload, headers=headers)
        print(response.text)

if __name__ == '__main__':

    # dnsrecord is the A record which will be updated
    dnsrecords = ["subdomain.example.com", "subdomain2.example.com", "subdomain3.example.com", "subdomain4.example.com", "example.com"]

    ## Cloudflare authentication details
    ## keep these private
    auth_email = "" # Your Cloudflare E-Mail
    api_key = "" # Global API Token
    zone_id = ""
    proxy = True # Can be True or False

    ip = getIp()
    dns_ids = getDnsId(dnsrecords, auth_email, api_key, zone_id)
    setDnsRecords(dns_ids, ip, proxy, auth_email, api_key, zone_id)