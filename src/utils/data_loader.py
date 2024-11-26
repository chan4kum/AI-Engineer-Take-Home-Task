import pandas as pd

class DataLoader:
    """Separate data loading responsibility"""
    @staticmethod
    def load_data(file_path):
        """Load data from CSV"""
        df = pd.read_csv(file_path)
        return df, df['Sequence'].str.len().max()