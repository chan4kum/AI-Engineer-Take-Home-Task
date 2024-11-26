import logging
import os
from logging.handlers import RotatingFileHandler

class LoggerFactory:
    @staticmethod
    def get_logger(name: str, log_dir: str = 'logs'):
        # Create logs directory if it doesn't exist
        os.makedirs(log_dir, exist_ok=True)
        
        logger = logging.getLogger(name)
        logger.setLevel(logging.INFO)
        
        # Console Handler
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)
        console_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        console_handler.setFormatter(console_formatter)
        
        # File Handler with Log Rotation
        file_handler = RotatingFileHandler(
            os.path.join(log_dir, f'{name}.log'), 
            maxBytes=1048576,  # 1 MB
            backupCount=5
        )
        file_handler.setLevel(logging.INFO)
        file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(file_formatter)
        
        # Add handlers to logger
        logger.addHandler(console_handler)
        logger.addHandler(file_handler)
        
        return logger
