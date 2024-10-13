from txt_summarizer.components.data_validation import DataValiadtion
from txt_summarizer.config.configuration import ConfigurationManager
from txt_summarizer.logging import logger

class DataValidationPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            config = ConfigurationManager()
            data_validation_config = config.get_data_validation_config()
            data_validation = DataValiadtion(config=data_validation_config)
            data_validation.validate_all_files_exist()
        except Exception as e:
            logger.exception(e)
            raise e
