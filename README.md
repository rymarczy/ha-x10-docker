# Home Assistant with X10

This repository is meant to build and deploy a Home Assistant docker container with X10 support via [mochad](https://github.com/bjonica/mochad). 

A simple web-ui configuration text editor is also installed via CausticLab's [hass-configurator-docker](https://github.com/CausticLab/hass-configurator-docker). 

# Installation

Install docker and docker-compose, on linux:
```
sudo apt install docker docker-compose
```
Be sure to add your user to the docker user group:
```
sudo groupadd docker

sudo usermod -aG docker $USER
```
Clone this repository:
```
git clone git@github.com:rymarczy/ha-x10-docker.git
```
Inside of cloned directly, update `HOST_IP` environmental variable in `docker-compose.yml` to the local IP address of the machine that will be running home assistant. It is set to `127.0.0.1` by default. This is required for i-frame of the web-ui configuration editor to run correctly. 
```
  environment:
    - HOST_IP=127.0.0.1
```
Then, build and launch docker containers. `-d` option launches the containers in the background. 
```
docker-compose up -d
```
`docker ps` can be used to verify the containers are running correctly.
```
CONTAINER ID   IMAGE                                        COMMAND                  CREATED         STATUS          NAMES
f637b5ced73d   ha-x10-docker_homeassistant                  "/usr/local/sbin/doc…"   16 hours ago    Up 11 seconds   homeassistant
3b6522c5c3a8   ha-x10-docker_mochad                         "./mochad -d"            16 hours ago    Up 11 seconds   mochad
c91c7246a855   causticlab/hass-configurator-docker:latest   "/app/run.sh"            16 hours ago    Up 11 seconds   config
```

Home assistant instance should now be available from `http://<HOST_IP>:8123` in your web browser.

# Configuration

The web-ui configuration should be available by clicking **Config Editor** on the left hand toolbar. 

Mochad X10 settings can not be configured through the UI.

Modify the `configuration.yaml` file in the `/app/config` folder to add/modify/delete X10 devices:

One light device is added by default for demonstration purposes:
```
light:
  - platform: mochad
    devices:
      - address: a1
        name: test_light
        comm_type: pl

```
Detailed configuration instructions are available on the [home assistant](https://www.home-assistant.io/integrations/mochad/) web site. 

Restart home assistant after saving any changes to `configuration.yaml` to see updates in UI.  

- *Developer Tools* > *Check Configuration (Make sure check succeeds)* > *Restart*