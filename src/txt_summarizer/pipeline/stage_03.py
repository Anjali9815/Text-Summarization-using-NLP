from txt_summarizer.components.data_transformation import DataTransformation
from txt_summarizer.config.configuration import ConfigurationManager
from txt_summarizer.logging import logger

class DataTransformationPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            config = ConfigurationManager()
            data_transformation_config = config.get_data_transformation_config()
            data_transformation = DataTransformation(config=data_transformation_config)
            data_transformation.convert()
        except Exception as e:
            logger.exception(e)
            raise e
