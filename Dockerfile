FROM centos:centos7

# Install EPEL
RUN yum install -y epel-release

# Install pre-requisites
RUN yum install -y libselinux-utils redhat-lsb python-devel python-pip gcc

# Install Python modules
RUN mkdir -p /home/peekaboo/plugins/{info,status}
COPY requirements.txt /home/peekaboo/requirements.txt
RUN pip install -r /home/peekaboo/requirements.txt

# Install application
COPY peekaboo.py /home/peekaboo/peekaboo.py
COPY plugins/info/* /home/peekaboo/plugins/info/
COPY plugins/status/* /home/peekaboo/plugins/status/
RUN chmod +x /home/peekaboo/peekaboo.py

# Expose port 5000
EXPOSE 5000

# Run application
CMD cd /home/peekaboo ;\
    ./peekaboo.py
