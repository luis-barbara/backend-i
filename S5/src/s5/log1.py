import logging
import sys
from datetime import datetime

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - [%(levelname)s] - %(filename)s@%(lineno)d - %(funcName)s",
    handlers=[logging.StreamHandler(sys.stdout)] 
)

logger = logging.getLogger(__name__)

def audit(func):
    def wrapper(*args, **kwargs):
        logger.info(f"start at {datetime.now()}")
        result = func(*args, **kwargs)
        logger.info(f"finish at {datetime.now()}")
        return result
    return wrapper


