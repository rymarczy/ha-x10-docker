# Home Assistant with X10

This repository is meant to bootstrap a Home Assistant docker container with X10 support via [mochad](https://github.com/bjonica/mochad). 

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
Change directory and call docker-compose to launch containers in the background:
```
cd ha-x10-docker/

docker-compose up -d
```

Home assistant instance should now be available from [http://localhost:8123](http://localhost:8123) in your web browser.

# Configuration

The web-ui configuration should be available by clicking [**Config Editor**](http://localhost:8123/configurator) on the left hand toolbar. 

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
Detailed configuraion instructions are available on the [home assistant](https://www.home-assistant.io/integrations/mochad/) web site. 

Restart home assistant after saving any changes to `configuration.yaml` to see updates in UI.  

*Developer Tools* > *Check Configuration* > *Restart*