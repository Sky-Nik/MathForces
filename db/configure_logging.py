import logging


def configure_logging():
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s %(levelname)s %(message)s\n',
        handlers=[
            logging.FileHandler('logging.log'),
            logging.StreamHandler(),
        ],
    )
