# Peekaboo

Peekabo expose hardware info through HTTP.

# Install

In order to run peekaboo you need to satisfy the following dependecies:

```bash
dzdo groupadd dmidecode
dzdo usermod <user> -G dmidecode
dzdo tee -a /etc/sudoers.d/dmidecode << EOT >/dev/null
%dmidecode ALL=(ALL) NOPASSWD:/usr/sbin/dmidecode
EOF
dzdo yum install -y libselinux-utils redhat-lsb python-pip
dzdo pip install requirements.txt
git clone git@gitlab:michael.persson/peekaboo.git
cd peekaboo
./peekaboo.py
```

# Run using Docker

For can quickly run it inside a Docker container:

```bash
docker build .
docker run -p 5000:5000 <image id>
```

# Query

Query using YAML:

```bash
curl -i http://<host>:5000/config
```

Query using JSON:

```bash
curl -i -H "Accept: application/json" http://<host>:5000/config
```
