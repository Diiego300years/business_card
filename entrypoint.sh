#!/bin/bash

# Sprawdź, czy katalog 'migrations' istnieje, jeśli nie, uruchom 'flask db init'
if [ ! -d "./migrations" ]; then
  echo "Folder 'migrations' doesn't exist, I'm starting init..."
  flask db init
  flask db migrate -m "docker test migrations"
else
  echo "Folder called 'migrations' exist."
fi

flask db upgrade

# Uruchomienie aplikacji Flask
exec "$@"
