# HardHat C2 0-Day Authentication Bypass
This vulnerability is present because HardHatC2 relies on a static JWT signing key that allows unauthenticated creation of valid access tokens for any role.

# How To Use
```
➜ python3 auth_bypass.py -h
usage: bypass.py [-h] [-u USER]

options:
  -h, --help            show this help message and exit
  -u USER, --user USER  User and password that will be created

```
# Mitigation
Adopt a Secure JWT Key Management Process. Do not hard-code keys in the repository or configuration files. For development or testing purpose, use a securely generated random signing key in the `/HardHatC2/TeamServer/appsettings.json` file.

Credits to [@author Siam Thanat Hack Co., Ltd.](https://blog.sth.sh/hardhatc2-0-days-rce-authn-bypass-96ba683d9dd7)
