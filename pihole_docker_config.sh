#!/bin/sh

# TODO: pass json configuration file to pihole?

# echo on
set -x

# volume for application configuration data
if ! docker volume create pihole; then
    exit 1
fi

# volume for DNS configuration
if ! docker volume create dnsmasq; then
    exit 1
fi

# important vars
TZ="Canada/Eastern"
PASSWORD="salmonslippers"
ADMIN_PORT="8081"
IP_ADDR="192.168.2.99"

read -p "Continue? " yn
case $yn in
    [Yy]* ) break;;
    * ) exit;;
esac

# cleanup from last run
docker stop pihole && docker rm pihole

# run
docker run -d \
--name=pihole \
-e TZ=$TZ \
-e WEBPASSWORD=$PASSWORD \
-e SERVERIP=$IP_ADDR \
-e DNSMASQ_USER=root \
-v pihole:/etc/pihole \
-v dnsmasq:/etc/dnsmasq \
-p $ADMIN_PORT:80 \
-p 53:53/tcp \
-p 53:53/udp \
--restart=unless-stopped \
--pull=always \
pihole/pihole

# HELPFUL COMMANDS
# docker ps                 # list running containers
# docker ps -a              # list all containers
# docker stop pihole        # stop pihole container
# docker image ls           # list all images
# docker rmi pihole/pihole  # remove image
