import logging
import os

def setup_logger():
    # Create logger folder if dees not exist
    os.makedirs("logs",exist_ok=True)

    logger=logging.getLogger("parabank_automation")
    logger.setLevel(logging.INFO)

    # logger level in PyTest  and their hierarchy: DEBUG > INFO > WARNING > ERROR > FATAL 
    # And a logger show the log for the same and  above level

    # Prevent duplicate logs
    if not logger.handlers:
        file_handler=logging.FileHandler("logs/test.log")
        console_handler=logging.StreamHandler()

        # "%(asctime)s - %(levelname)s - %(message)s" --> 2026-05-20 11:10:00 - INFO - Task Created
        formatter=logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")

        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)

        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

    return logger   

logger = setup_logger()