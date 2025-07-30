import yaml
import os


def load_config(config_path: str = None):
    if config_path is None:
        # Get the directory of the current script (config_loader.py)
        current_dir = os.path.dirname(os.path.abspath(__file__))

        # Go up one level to the project root
        project_root = os.path.dirname(current_dir)

        # Construct the full path to config.yaml
        config_path = os.path.join(project_root, 'config', 'config.yaml')

    print(f"Attempting to load config from: {config_path}")
    with open(config_path, "r") as file:
        config = yaml.safe_load(file)
        print(f"Loaded configuration from {config_path}")
        return config

# print(load_config())