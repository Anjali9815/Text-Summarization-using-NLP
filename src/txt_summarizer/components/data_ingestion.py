import os
import urllib.request as request
import zipfile
import certifi
import ssl
import urllib.request
from pathlib import Path
from txt_summarizer.logging import logger
from txt_summarizer.utils.common import get_file_size
from txt_summarizer.entity import DataIngestionConfig

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config


    
    
    
    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            try:
                # Create an SSL context
                context = ssl.create_default_context(cafile=certifi.where())
                
                # Open the URL and read the response
                with urllib.request.urlopen(self.config.source_URL, context=context) as response:
                    with open(self.config.local_data_file, 'wb') as out_file:
                        out_file.write(response.read())
                        
                logger.info(f"Downloaded {self.config.local_data_file} successfully!")
            except urllib.error.URLError as e:
                logger.error(f"Failed to download {self.config.source_URL}: {e}")
        else:
            logger.info(f"File already exists of size: {get_file_size(Path(self.config.local_data_file))}")
                
        
    def extract_zip_file(self):
        """
        zip_file_path: str
        Extracts the zip file into the data directory
        Function returns None
        """
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)

