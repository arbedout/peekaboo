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
sudo yum install -y epel-release
sudo yum install -y libselinux-utils redhat-lsb python-devel python-pip
sudo pip install -r requirements.txt
git clone https://github.com/mickep76/peekaboo.git
cd peekaboo
./peekaboo.py
```

# Run using Docker

You can quickly run it inside a Docker container using:


## Build docker image

```bash
docker build -t peekaboo:latest .
```

## Run docker image

```bash
docker run -d -p 5000:5000 --name=peekaboo peekaboo:latest
```

## Stop container:

```bash
docker stop peekaboo
```

# Query

Query using YAML:

```bash
curl -i http://<host>:5000/info
```

Query using JSON:

```bash
curl -i -H "Accept: application/json" http://<host>:5000/info
```
