import logging.config

from log_config.logging_settings import logging_config
from module_1 import main

logging.config.dictConfig(logging_config)

logger = logging.getLogger(__name__)

logger.error("error Start")

# print(logger.parent, logger.root)

main()
