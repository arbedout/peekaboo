FROM centos:centos7

# Install EPEL
RUN yum install -y epel-release

# Install pre-requisites
RUN yum install -y libselinux-utils redhat-lsb python-devel python-pip gcc

# Install Python modules
RUN mkdir -p /var/lib/peekaboo/plugins/{info,status}
COPY requirements.txt /var/lib/peekaboo/requirements.txt
RUN pip install -r /var/lib/peekaboo/requirements.txt

# Install application
COPY peekaboo.py /usr/bin/peekaboo
RUN chmod +x /usr/bin/peekaboo
COPY peekaboo-docker.conf /etc/peekaboo.conf
COPY plugins/info/* /var/lib/peekaboo/plugins/info/
COPY plugins/status/* /var/lib/peekaboo/plugins/status/

# Expose port 5000
EXPOSE 5050

# Run application
CMD /usr/bin/peekaboo
