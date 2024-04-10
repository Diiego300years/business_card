import json
import os
from logging.handlers import RotatingFileHandler
import logging


class FlaskAppConfigurator:
    def __init__(self, app):
        self.app = app

    def load_configuration(self):
        """Load a configuration based on the FLASK_ENV environment variable."""
        current_dir = os.path.dirname(__file__)
        config_path = os.path.join(current_dir, "config.json")
        try:
            with open(config_path) as config_file:
                config = json.load(config_file)
            self.app.config.from_mapping(config[os.getenv("FLASK_ENV", 'default')])
        except Exception as e:
            logging.error(f"Error configuring logging: {e}")

    def configure_logging(self):
        """Set up logging from a configuration file."""
        log_directory = os.path.join(self.app.root_path, "logs")
        current_dir = os.path.dirname(__file__)
        config_path = os.path.join(current_dir, "config.json")

        if not os.path.exists(log_directory):
            try:
                os.makedirs(log_directory)
            except OSError as e:
                logging.error(f"OSError error: {e}")

        try:
            with open(config_path, 'r') as config_file:
                config = json.load(config_file)

            for handler_name, handler_config in config['logging']['handlers'].items():
                file_handler = RotatingFileHandler(
                    handler_config['file'],
                    maxBytes=handler_config['maxBytes'],
                    backupCount=handler_config['backupCount']
                )
                file_handler.setLevel(getattr(logging, handler_config['level']))
                file_handler.setFormatter(logging.Formatter(handler_config['formatter']))
                self.app.logger.addHandler(file_handler)

        except FileNotFoundError as e:
            logging.error(f"Error configuring logging: {e}")
