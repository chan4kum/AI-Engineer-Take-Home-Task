from src.extractors.base_extractor import BaseExtractor
import numpy as np

class LetterComposition(BaseExtractor):
    def extract(self, sequence):
        """
        Implement letter composition feature extraction
        Interface Segregation: Only implements what's necessary
        """
        composition = np.zeros(len(self.amino_acids), dtype=float)
        total_letters = len(sequence)
        for letter in sequence:
            composition[self.amino_acid_to_index.get(letter, self.amino_acid_to_index['X'])] += 1
        return composition / total_letters