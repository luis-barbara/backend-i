import logging
import sys
from datetime import datetime

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logger.addHandler(logging.StreamHandler(sys.stdout))

def audit(func):
    def wrapper(*args, **kwargs):
        logger.info(f"start at {datetime.now()}")
        result = func(*args, **kwargs)
        logger.info(f"finish at {datetime.now()}")
        return result
    return wrapper


