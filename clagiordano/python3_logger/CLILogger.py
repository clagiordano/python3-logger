import re
from clagiordano.python3_logger.AbstractLogger import AbstractLogger

class CLILogger(AbstractLogger):
    """
    Command Line logger with optional colors
    """
    __ansi = True
    __EMERGENCY = '\033[1;41mEMERGENCY\033[0m'
    __ALERT     = '\033[41mALERT\033[0m'
    __CRITICAL  = '\033[1;31mCRITICAL\033[0m'
    __ERROR     = '\033[31mERROR\033[0m'
    __WARNING   = '\033[1;33mWARNING\033[0m'
    __NOTICE    = '\033[33mNOTICE\033[0m'
    __INFO      = '\033[1;32mINFO\033[0m'
    __DEBUG     = '\033[1;30mDEBUG\033[0m'

    def __format(self, badge, message):
        output = f"[{badge}]: {message}"

        if self.__ansi is False:
            ansi_escape = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')
            output = ansi_escape.sub('', output)

        return output

    def set_ansi(self, value):
        """
        Enable or disable ANSI color usage, possible values True or False
        """
        self.__ansi = bool(value)

    def emergency(self, message):
        """
        It outputs an emergency message and exits
        """
        print(self.__format(self.__EMERGENCY, message))
        raise SystemExit(8)

    def alert(self, message):
        """
        It outputs an alert message and exits
        """
        print(self.__format(self.__ALERT, message))
        raise SystemExit(7)

    def critical(self, message):
        """
        It outputs a critical message and exits
        """
        print(self.__format(self.__CRITICAL, message))
        raise SystemExit(6)

    def error(self, message):
        """
        It outputs an error message
        """
        print(self.__format(self.__ERROR, message))

    def warning(self, message):
        """
        It outputs a warning message
        """
        print(self.__format(self.__WARNING, message))

    def notice(self, message):
        """
        It outputs a notice message
        """
        print(self.__format(self.__NOTICE, message))

    def info(self, message):
        """
        It outputs a info message
        """
        print(self.__format(self.__INFO, message))

    def debug(self, message):
        """
        It outputs a debug message
        """
        print(self.__format(self.__DEBUG, message))
