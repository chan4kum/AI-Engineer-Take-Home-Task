from src.extractors.base_extractor import BaseExtractor
import numpy as np

class OneHotEncoder(BaseExtractor):
    def __init__(self, max_length, amino_acids):
        """
        Initialize One Hot Encoder with dynamic max length
        Open/Closed Principle: Extends BaseExtractor without modifying it
        """
        super().__init__(amino_acids)
        self.max_length = max_length
    
    def extract(self, sequence):
        """
        Implement feature extraction with dynamic length handling 
        Liskov Substitution Principle: Can be used wherever FeatureExtractor is expected
        """
        # Truncate or pad sequence to max_length
        truncated_sequence = sequence[:self.max_length]
        padded_sequence = truncated_sequence.ljust(self.max_length, 'X')
        
        # Create one-hot encoding
        one_hot = np.zeros((self.max_length, len(self.amino_acids)), dtype=int)
        for i, letter in enumerate(padded_sequence):
            one_hot[i, self.amino_acid_to_index.get(letter, self.amino_acid_to_index['X'])] = 1
        
        return one_hot.flatten()