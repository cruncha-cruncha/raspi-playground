#!/bin/sh

cd $(dirname "$0")

curl https://icanhazip.com/ > latest.txt

source ../secrets/static-ip-env.sh

python3 compare_and_notify.py