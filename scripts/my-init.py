import os
import pathlib
import re

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
    with open(os.path.join(root_folder,'configuration.yaml'), 'w') as f:
        f.write(init_text)
    with open(os.path.join(root_folder,'automations.yaml'), 'w') as f:
        pass
    with open(os.path.join(root_folder,'scripts.yaml'), 'w') as f:
        pass
    with open(os.path.join(root_folder,'scenes.yaml'), 'w') as f:
        pass


def update_config(host_ip:str, root_folder:str):
    rep_str = f"http://{host_ip}:8124"

    with open(os.path.join(root_folder,'configuration.yaml'), 'r') as f:
        file_text = f.read()

    file_text = re.sub(r'http:\/\/.+:8124', rep_str, file_text)
    
    with open(os.path.join(root_folder,'configuration.yaml'), 'w') as f:
        f.write(file_text)


def main():
    config_root_folder = '/config'
    try:
        HOST_IP = os.environ['HOST_IP']
    except Exception as e:
        HOST_IP = 'localhost'

    print(f"Host IP is: {HOST_IP}", flush=True)

    config_file = os.path.join(config_root_folder,'configuration.yaml')

    if pathlib.Path(config_file).is_file():
        update_config(HOST_IP, config_root_folder)
    else:
        create_configs(HOST_IP, config_root_folder)


if __name__ == '__main__':
    main()
