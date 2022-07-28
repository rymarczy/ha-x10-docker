#!/bin/bash
set -euxo pipefail
# Run anything else you want to run before HA starts...
python /my-init.py
# Run original entrypoint
exec /init