# Peekaboo

Peekabo expose hardware info through HTTP.

# Install

In order to run peekaboo you need to satisfy the following dependecies:

```bash
sudo groupadd dmidecode
sudo usermod <user> -G dmidecode
sudo tee -a /etc/sudoers.d/dmidecode << EOT >/dev/null
%dmidecode ALL=(ALL) NOPASSWD:/usr/sbin/dmidecode
EOF
sudo yum install -y libselinux-utils redhat-lsb python-pip
sudo pip install requirements.txt
git clone https://github.com/mickep76/peekaboo.git
cd peekaboo
./peekaboo.py
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
