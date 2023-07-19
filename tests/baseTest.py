import pytest
import logging.config


@pytest.mark.usefixtures("setup")
class BaseTest:
    # Load the logging configuration from the file
    logging.config.fileConfig('config/logging.ini')
    log = logging.getLogger("mylogger")

    def getLogger(self):
        return self.log