from txt_summarizer.components.model_evaluation import ModelEvaluation
from txt_summarizer.config.configuration import ConfigurationManager
from txt_summarizer.logging import logger

class ModelEvaluationPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            config = ConfigurationManager()
            model_evaluation_config = config.get_model_evaluation_config()
            model_evaluation_config = ModelEvaluation(config=model_evaluation_config)
            model_evaluation_config.evaluate()
        except Exception as e:
            logger.exception(e)
            raise e
