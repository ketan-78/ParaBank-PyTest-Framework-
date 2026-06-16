import configparser

config = configparser.ConfigParser()
config.read("config/config.ini")


def get_config_value(key):
    return config.get("DEFAULT", key)