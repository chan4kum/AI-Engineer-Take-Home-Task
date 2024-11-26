from abc import ABC, abstractmethod
class FeatureExtractor(ABC):
    """Abstract base class for feature extractors following Single Responsibility Principle"""
    @abstractmethod
    def extract(self, sequence):
        """Abstract method to extract features from a sequence"""
        pass