FROM homeassistant/home-assistant:stable

# Add our custom entrypoint
COPY --chown=root docker-entrypoint.sh /usr/local/sbin/
COPY --chown=root my-init.py /
ENTRYPOINT ["/usr/local/sbin/docker-entrypoint.sh"]

# Rest of your dockerfile here...