import pandas as pd

class DataSaver:
    """Separate data saving responsibility"""
    @staticmethod
    def save_features(data, extractors, output_path):
        """Save extracted features"""
        features = data[['ID'] + [extractor.__class__.__name__ for extractor in extractors]]
        features.to_csv(output_path, index=False)