#!/bin/bash

# Export environment variables from the .env file
if [ -f .env ]; then
    export $(grep -v '^#' .env | xargs)
fi

# Start the Flask application
flask run --host=0.0.0.0

