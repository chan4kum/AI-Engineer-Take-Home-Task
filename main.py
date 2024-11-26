from src.extractors.one_hot_encoder import OneHotEncoder
from src.extractors.letter_composition import LetterComposition
from src.pipeline.feature_extraction_pipeline import FeatureExtractionPipeline
from src.utils.config_manager import ConfigManager
from src.utils.logger import LoggerFactory
import pandas as pd

def main():
    # Initialize logger
    logger = LoggerFactory.get_logger('main')
    
    try:
        # Load configuration
        config = ConfigManager.load_config()
        
        # Configuration details
        amino_acids = config['project']['amino_acids']
        max_length = config['project']['extractors']['one_hot']['max_length']
        input_file = config['project']['data']['input_file']
        output_file = config['project']['data']['output_file']
        
        # Dynamically set max_length
        df = pd.read_csv(input_file)
        max_length = df['Sequence'].str.len().max()

        # Define extractors
        one_hot_encoder = OneHotEncoder(max_length=max_length, amino_acids=amino_acids)
        letter_composition = LetterComposition(amino_acids=amino_acids)

        # Create pipeline with extractors
        pipeline = FeatureExtractionPipeline(
            file_path=input_file,
            output_path=output_file,
            extractors=[one_hot_encoder, letter_composition]
        )

        # Run the pipeline
        pipeline.run_pipeline()
        
    except Exception as e:
        logger.error(f"Unexpected error in main execution: {e}")

if __name__ == "__main__":
    main()