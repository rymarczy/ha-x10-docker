import os
import pathlib
import re
import logging

logging.basicConfig(level=logging.INFO)
 
def create_configs(host_ip:str, root_folder:str):
    init_text = (
    "\n"
    "# Loads default set of integrations. Do not remove.\n"
    "default_config:\n"
    "\n"
    "# Text to speech\n"
    "tts:\n"
    "  - platform: google_translate\n"
    "\n"
    "automation: !include automations.yaml\n"
    "script: !include scripts.yaml\n"
    "scene: !include scenes.yaml\n"
    "\n"
    "panel_iframe:\n"
    "  configurator:\n"
    "    title: Config Editor\n"
    "    icon: mdi:wrench\n"
    f"    url: http://{host_ip}:8124\n"
    "\n"
    "mochad:\n"
    "  host: mochad\n"
    "  port: 1099\n"
    "\n"
    "light:\n"
    "  - platform: mochad\n"
    "    devices:\n"
    "      - address: a1\n"
    "        name: test_light\n"
    "        comm_type: pl\n"
    )
    os.makedirs(root_folder, exist_ok=True)
    config_file = os.path.join(root_folder,'configuration.yaml')
    with open(config_file, 'w') as f:
        f.write(init_text)
    logging.info(f"{config_file} created with default initialization.")

    auto_file = os.path.join(root_folder,'automations.yaml')
    with open(auto_file, 'w') as f:
        pass
    logging.info(f"Blank {auto_file} created.")

    script_file = os.path.join(root_folder,'scripts.yaml')
    with open(script_file, 'w') as f:
        pass
    logging.info(f"Blank {script_file} created.")

    scene_file = os.path.join(root_folder,'scenes.yaml')
    with open(scene_file, 'w') as f:
        pass
    logging.info(f"Blank {scene_file} created.")


def update_config(host_ip:str, root_folder:str):
    rep_str = f"http://{host_ip}:8124"
    config_file = os.path.join(root_folder,'configuration.yaml')

    with open(config_file, 'r') as f:
        file_text = f.read()

    file_text = re.sub(r'http:\/\/.+:8124', rep_str, file_text)

    with open(config_file, 'w') as f:
        f.write(file_text)
    logging.info(f"Updated {config_file} to use {host_ip} for HOST_IP for config editor.")


def main():
    config_root_folder = '/config'
    try:
        HOST_IP = os.environ['HOST_IP']
    except Exception as e:
        logging.error(f"No 'HOST_IP' environmental variable found, using 'localhost'.")
        HOST_IP = 'localhost'

    logging.info(f"Host IP is: {HOST_IP}")

    config_file = os.path.join(config_root_folder,'configuration.yaml')

    if pathlib.Path(config_file).is_file():
        logging.info(f"Existing {config_file} found, updating config file...")
        update_config(HOST_IP, config_root_folder)
    else:
        logging.info(f"Existing {config_file} NOT found, creating config files...")
        create_configs(HOST_IP, config_root_folder)


if __name__ == '__main__':
    main()
