FROM centos:centos7
MAINTAINER Yanyan Ni <niyanyan7@gmail.com>

RUN yum -y install epel-release 
RUN yum -y install python-pip
RUN pip install coverage
RUN pip install xmlrunner 
RUN mkdir -p /usr/local/supermarket_register/scripts
RUN mkdir -p /usr/local/supermarket_register/tests

COPY ./scripts/*.py /usr/local/supermarket_register/scripts/
COPY ./tests/* /usr/local/supermarket_register/tests/

RUN chmod +x /usr/local/supermarket_register/scripts/register.py
RUN chmod +x /usr/local/supermarket_register/tests/test_register.py
RUN chmod +x /usr/local/supermarket_register/tests/test_calculator.py

RUN ln -s /usr/local/supermarket_register/scripts/register.py /usr/bin/supermarket_register
