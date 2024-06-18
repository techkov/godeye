import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s : %(name)s - %(levelname)s : %(message)s',
    handlers=[
        logging.FileHandler('/home/isakov/godeye/logs/app.log'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)
