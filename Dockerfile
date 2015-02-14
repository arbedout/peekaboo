FROM centos:centos7

# Install EPEL
RUN yum install -y epel-release

# Install pre-requisites
RUN yum install -y libselinux-utils redhat-lsb python-devel python-pip gcc

# Install Python modules
COPY requirements.txt /root/requirements.txt
RUN pip install -r /root/requirements.txt

# Copy files
RUN mkdir -p /home/peekaboo/plugins
COPY peekaboo.py /home/peekaboo/peekaboo.py
COPY plugins/* /home/peekaboo/plugins/
RUN chmod +x /home/peekaboo/peekaboo.py

# Expose port 5000
EXPOSE 5000

# Run appliaction
CMD cd /home/peekaboo ;\
    ./peekaboo.py
