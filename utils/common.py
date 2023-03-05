import configparser
import os

# Define the path to the configuration file
CONFIG_FILE = os.path.join(os.path.dirname(__file__), "..", "configs", "config.ini")

# Create a ConfigParser object
config_parser = configparser.ConfigParser()

# Read the configuration file
config_parser.read(CONFIG_FILE)


def get_config_value(section, key):
    """
    This function returns the value of the specified key from the specified section of the configuration file.
    """
    try:
        value = config_parser.get(section, key)
    except configparser.NoSectionError:
        print(f"Error: Section '{section}' not found in the configuration file")
        return None
    except configparser.NoOptionError:
        print(f"Error: Key '{key}' not found in the '{section}' section of the configuration file")
        return None
    else:
        return value
