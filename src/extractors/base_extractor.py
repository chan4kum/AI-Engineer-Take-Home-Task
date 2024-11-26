from src.core.abstract_base import FeatureExtractor
import numpy as np

class BaseExtractor(FeatureExtractor):
    def __init__(self, amino_acids):
        """It will initialize common functionality for extractors"""
        self.amino_acids = amino_acids
        self.amino_acid_to_index = {aa: i for i, aa in enumerate(amino_acids)}