import pathlib

init_check = pathlib.Path('/config/init-check')
if init_check.is_file():
    quit()

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
"    url: http://localhost:8124\n"
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
with open('/config/configuration.yaml', 'a') as f:
    f.write(init_text)
with open('/config/automations.yaml', 'a') as f:
    pass
with open('/config/scripts.yaml', 'a') as f:
    pass
with open('/config/scenes.yaml', 'a') as f:
    pass


with open('/config/init-check', 'a') as f:
    pass