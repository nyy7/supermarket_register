# Supermarket Register

A dockerized software which calculates the cost of purchase for a number of product.

## Prerequisites

The user needs to have docker, docker-compose and make installed to run the program. For rhel, run the following command to install required packages.

```
yum install -y make

yum install -y docker

# install docker-compose
curl -L https://github.com/docker/compose/releases/download/1.17.0/docker-compose-`uname -s`-`uname -m` -o /usr/local/bin/docker-compose
chmod +x /usr/local/bin/docker-compose

```

## Installing

The following command will build the docker image.

```
make build

```

And the following command will build the image and run all the test cases. The test report is returned in the shell.

```
make test

```
Make a test run

```
make run-example

```
 

## Run

```
make run

docker exec -e SKU='A12T-4GH7-QPL9-3N4M' regc supermarket_register

```
