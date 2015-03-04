#!/bin/bash

set -e
set -u

if ! grep 'CentOS Linux release 7' /etc/redhat-release &>/dev/null; then
    echo 'This setup script, only works on CentOS 7'
    exit 1
fi

if [ `id -u` -ne 0 ]; then
    echo 'This setup script, must run with root privileges'
    exit 1
fi

# Create group if it doesn't exist
getent group dmidecode &>/dev/null || groupadd dmidecode

# Create user if it doesn't exist
getent passwd peekaboo &>/dev/null || useradd -M -G dmidecode peekaboo

# Add sudoers rule
echo '%dmidecode ALL=(ALL) NOPASSWD:/usr/sbin/dmidecode' >/etc/sudoers.d/dmidecode

# Install pre-requisites
yum install -y libselinux-utils redhat-lsb python-devel python-pip gcc

# Install peekaboo
pip install peekaboo
cp /usr/share/peekaboo/contrib/peekaboo.service /usr/lib/systemd/system/peekaboo.service
systemctl enable peekaboo
systemctl start peekaboo
