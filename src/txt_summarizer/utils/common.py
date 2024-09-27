import os, yaml
from tabnanny import verbose
from txt_summarizer import logger
from box.exceptions import BoxError
from box import config_box
from pathlib import Path
from typing import Any
from ensure import ensure_annotations


@ensure_annotations
# read yaml file and return the content of file
def read_yaml(path : Path) -> config_box:
    try:
        with open(path) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info("Yaml file loaded Successfully")
            return config_box(content)
    except BoxError as e:
        raise ValueError("Yaml file not found or cannot be loaded") from e
    except Exception as e:
        raise ValueError("Unexpected error while loading yaml file") from e
    

#create directories for the provided list of directories
@ensure_annotations
def create_dir(directory_path : list, verbose = True)-> str:
    for path in directory_path:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Directory created: {path}")


# get the size of the file
@ensure_annotations
def get_file_size(file_path : Path) -> str:
    size_kb = round(os.path.getsize(file_path) / 1024)
    return f"{size_kb} Kb"
