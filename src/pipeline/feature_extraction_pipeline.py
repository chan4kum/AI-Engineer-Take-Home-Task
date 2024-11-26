import pandas as pd
from typing import List
from src.core.abstract_base import FeatureExtractor
from src.utils.logger import LoggerFactory
from src.utils.data_loader import DataLoader
from src.utils.data_saver import DataSaver

class FeatureExtractionPipeline:
    def __init__(self, file_path: str, output_path: str, extractors: List[FeatureExtractor]):
        self.logger = LoggerFactory.get_logger(self.__class__.__name__)
        self.file_path = file_path
        self.output_path = output_path
        self.extractors = extractors
        self.data = None
        self.max_sequence_length = None
    
    def load_data(self):
        try:
            self.data, self.max_sequence_length = DataLoader.load_data(self.file_path)
            self.logger.info(f"Data loaded successfully from {self.file_path}")
        except Exception as e:
            self.logger.error(f"Failed to load data: {e}")
            raise
    
    def apply_extractors(self):
        try:
            for extractor in self.extractors:
                feature_name = extractor.__class__.__name__
                self.data[feature_name] = self.data['Sequence'].apply(extractor.extract)
            self.logger.info("Feature extraction completed successfully")
        except Exception as e:
            self.logger.error(f"Feature extraction failed: {e}")
            raise
    
    def save_features(self):
        try:
            DataSaver.save_features(self.data, self.extractors, self.output_path)
            self.logger.info(f"Features saved successfully to {self.output_path}")
        except Exception as e:
            self.logger.error(f"Failed to save features: {e}")
            raise
    
    def run_pipeline(self):
        try:
            self.load_data()
            self.apply_extractors()
            self.save_features()
            self.logger.info("Feature extraction pipeline completed successfully")
        except Exception as e:
            self.logger.error(f"Pipeline execution failed: {e}")
            raise