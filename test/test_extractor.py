import pytest
import numpy as np
from src.extractors.one_hot_encoder import OneHotEncoder
from src.extractors.letter_composition import LetterComposition

class TestFeatureExtractors:
    @pytest.fixture
    def amino_acids(self):
        return ['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M','N','O','P','Q','R','S','T','V','W','Y','X']
    
    def test_one_hot_encoder(self, amino_acids):
        encoder = OneHotEncoder(max_length=5, amino_acids=amino_acids)
        sequence = 'ACDEF'
        
        result = encoder.extract(sequence)
        
        assert len(result) == 5 * len(amino_acids)
        assert np.sum(result.reshape(5, len(amino_acids))) == len(sequence)
    
    def test_letter_composition(self, amino_acids):
        composer = LetterComposition(amino_acids=amino_acids)
        sequence = 'AACCDEF'
        
        result = composer.extract(sequence)
        
        assert len(result) == len(amino_acids)
        assert np.isclose(np.sum(result), 1.0)
