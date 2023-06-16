import logging


class CustomFormatter(logging.Formatter):
    def format(self, record):
        if hasattr(record, 'funcName'):  # Check if the record has a 'funcName' attribute (for functions)
            record.caller = record.funcName
        elif hasattr(record, 'classname'):  # Check if the record has a 'classname' attribute (for classes)
            record.caller = record.classname
        else:  # Default to the filename if no class or function name is available
            record.caller = record.filename

        return super().format(record)

