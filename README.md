# HardHat C2 0-Day Authentication Bypass
This vulnerability is present because HardHatC2 relies on a static JWT signing key that allows unauthenticated creation of valid access tokens for any role.

# How To Use
```
➜ pip3 install requirements.txt
➜ python3 .\auth_bypass.py -h
usage: auth_bypass.py [-h] [-u USER] [-p PASSWORD] [-i IP] [-P PORT]

options:
  -h, --help            show this help message and exit
  -u, --user USER       User and password that will be created
  -p, --password PASSWORD
                        User and password that will be created
  -i, --ip IP           The IP of the HardHat C2 running on
  -P, --port PORT       The port of the HardHat C2 running on

```
# Mitigation
Adopt a Secure JWT Key Management Process. Do not hard-code keys in the repository or configuration files. For development or testing purpose, use a securely generated random signing key in the `/HardHatC2/TeamServer/appsettings.json` file.

Credits to [@author Siam Thanat Hack Co., Ltd.](https://blog.sth.sh/hardhatc2-0-days-rce-authn-bypass-96ba683d9dd7)
