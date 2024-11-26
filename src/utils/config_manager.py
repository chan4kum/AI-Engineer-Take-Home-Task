import yaml
import os
from typing import Dict, Any

class ConfigManager:
    @staticmethod
    def load_config(config_path: str = 'configs/config.yaml') -> Dict[str, Any]:
        try:
            with open(config_path, 'r') as file:
                return yaml.safe_load(file)
        except FileNotFoundError:
            raise ConfigError(f"Configuration file not found at {config_path}")
        except yaml.YAMLError as e:
            raise ConfigError(f"Error parsing configuration file: {e}")

class ConfigError(Exception):
    """Custom exception for configuration-related errors"""
    pass