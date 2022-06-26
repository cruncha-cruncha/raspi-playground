## Github
1. generate new access token
2. pull repo
3. update (remote set-url) origin to include token

## Docker
    > curl -fsSL https://get.docker/com -o get-docker.sh
    > sudo sh get-docker.sh

    
## Network
1. enable SSH, disable root SSH
2. Connect via ethernet
3. Assign static ip
4. Turn off wifi (until next reboot)
    ```> sudo ifconfig wlan0 down```

## Gotchas
- use "Respond only on interface eth0" option in pihole admin settings
- have to run docker commands as sudo, so any docker setup scripts have to be run as sudo too
	