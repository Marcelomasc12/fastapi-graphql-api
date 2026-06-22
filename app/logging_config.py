import logging


def configure_logging():
    logging.basicConfig(
        level=logging.INFO,
        format='{"level": "%(levelname)s", "message": "%(message)s"}',
    )
