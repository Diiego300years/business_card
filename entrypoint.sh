#!/bin/bash

# Uruchomienie migracji
flask db init
flask db migrate -m "docker test migrations"
flask db upgrade

# Uruchomienie aplikacji Flask
exec "$@"
