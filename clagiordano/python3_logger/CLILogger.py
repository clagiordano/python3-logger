import re
from clagiordano.python3_logger.AbstractLogger import AbstractLogger
from clagiordano.python3_logger.LogLevels import LogLevels

class CLILogger(AbstractLogger):
    """
    Command Line logger with optional colors
    """
    __ansi = True
    __EMERGENCY = f'\033[1;41m{LogLevels.EMERGENCY.name:>10}\033[0m'
    __ALERT     = f'\033[41m{LogLevels.ALERT.name:>10}\033[0m'
    __CRITICAL  = f'\033[1;31m{LogLevels.CRITICAL.name:>10}\033[0m'
    __ERROR     = f'\033[31m{LogLevels.ERROR.name:>10}\033[0m'
    __WARNING   = f'\033[1;33m{LogLevels.WARNING.name:>10}\033[0m'
    __NOTICE    = f'\033[33m{LogLevels.NOTICE.name:>10}\033[0m'
    __INFO      = f'\033[1;32m{LogLevels.INFO.name:>10}\033[0m'
    __DEBUG     = f'\033[1;30m{LogLevels.DEBUG.name:>10}\033[0m'

    def __format(self, badge, message) -> str:
        """
        Formats and returns an output string
        """
        output = f"[{badge}]: {message}"
        if self.__ansi is False:
            ansi_escape = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')
            output = ansi_escape.sub('', output)

        return output

    def set_ansi(self, value) -> None:
        """
        Enable or disable ANSI color usage, possible values True or False
        """
        self.__ansi = bool(value)

    def emergency(self, message) -> None:
        """
        It outputs an emergency message and exits
        """
        print(self.__format(self.__EMERGENCY, message))
        raise SystemExit(8)

    def alert(self, message) -> None:
        """
        It outputs an alert message and exits
        """
        print(self.__format(self.__ALERT, message))
        raise SystemExit(7)

    def critical(self, message) -> None:
        """
        It outputs a critical message and exits
        """
        print(self.__format(self.__CRITICAL, message))
        raise SystemExit(6)

    def error(self, message) -> None:
        """
        It outputs an error message
        """
        print(self.__format(self.__ERROR, message))

    def warning(self, message):
        """
        It outputs a warning message
        """
        print(self.__format(self.__WARNING, message))

    def notice(self, message) -> None:
        """
        It outputs a notice message
        """
        print(self.__format(self.__NOTICE, message))

    def info(self, message) -> None:
        """
        It outputs a info message
        """
        print(self.__format(self.__INFO, message))

    def debug(self, message) -> None:
        """
        It outputs a debug message
        """
        print(self.__format(self.__DEBUG, message))
