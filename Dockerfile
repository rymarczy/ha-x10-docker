FROM homeassistant/home-assistant:stable

# Add our custom entrypoint
COPY --chown=root ./scripts/docker-entrypoint.sh /usr/local/sbin/
COPY --chown=root ./scripts/my-init.py /

ENTRYPOINT ["/usr/local/sbin/docker-entrypoint.sh"]
