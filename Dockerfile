FROM centos:centos7

# Install EPEL
RUN yum install -y epel-release

# Install pre-requisites
RUN yum install -y libselinux-utils redhat-lsb python-devel python-pip gcc

# Install peekaboo
RUN pip install peekaboo
COPY etc/peekaboo-docker.conf /etc/peekaboo.conf

# Expose port 5050
EXPOSE 5050

# Run application
CMD /usr/bin/peekaboo
