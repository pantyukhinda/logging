import sys

from log_config.log_filters import (
    ErrorLogFilter,
    DebugWarningLogFilter,
    CriticalLogFilter,
)

logging_config = {
    "version": 1,
    "disable_existing_loggers": True,
    "formatters": {
        "default": {
            "format": "default_formatter#%(levelname)-8s %(name)s:%(funcName)s - %(message)s"
        },
        "formatter_01": {
            "format": "[%(asctime)s] #%(levelname)-8s %(filename)s:"
            "%(lineno)d - %(name)s:%(funcName)s - %(message)s"
        },
        "formatter_02": {
            "format": "#%(levelname)-8s [%(asctime)s] - %(filename)s:"
            "%(lineno)d - %(name)s:%(funcName)s - %(message)s"
        },
        "formatter_03": {"format": "#%(levelname)-8s [%(asctime)s] - %(message)s"},
    },
    "filters": {
        "critical_filter": {"()": CriticalLogFilter},
        "error_filter": {"()": ErrorLogFilter},
        "debug_warning_filter": {"()": DebugWarningLogFilter},
    },
    "handlers": {
        "default": {
            "class": "logging.StreamHandler",
            "formatter": "default",
        },
        "stderr": {
            "class": "logging.StreamHandler",
        },
        "stdout": {
            "class": "logging.StreamHandler",
            "formatter": "formatter_02",
            "filters": ["debug_warning_filter"],
            "stream": sys.stdout,
        },
        "error_file": {
            "class": "logging.FileHandler",
            "filename": "error.log",
            "mode": "a",
            "level": "WARNING",  # Уровень хендлера указывает какие логи попадают в хендлер
            "formatter": "formatter_01",
            "filters": [
                "error_filter"
            ],  # Какие логи пройдут далее, обрабатывают фильтры
            # Остальные логи обрабатываются root
        },
        "critical_file": {
            "class": "logging.FileHandler",
            "filename": "critical.log",
            "mode": "a",
            "formatter": "formatter_03",
            "filters": ["critical_filter"],
        },
    },
    "loggers": {
        "module_1": {
            "handlers": ["error_file"],
            "level": "DEBUG",  # Уровень логгера указывает какие логи вообще собираем
            # Если уровень не указан он = 0, т.е. наследуется от родителя.
            # По умолчанию от root.
        },
        "module_2": {
            "handlers": ["stdout"],
        },
        "module_3": {
            "handlers": ["stderr", "critical_file"],
        },
        "__main__": {
            "handlers": ["error_file"],
            "level": "ERROR",
        },
    },
    "root": {
        "formatter": "default",
        "handlers": ["default"],
        "level": "DEBUG",  # Этот уровень передается по наследству остальным логгерам
        # Если он не указан, то он по умолчанию = WARNING
    },
}
