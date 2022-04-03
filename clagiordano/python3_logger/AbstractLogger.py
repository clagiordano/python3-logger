from abc import ABC, abstractmethod

class AbstractLogger(ABC):
    """
    This class defines the interface for all derived Logger classes
    and their mandatory methods
    """
    @abstractmethod
    def emergency(self, message):
        """
        It logs an emergency message
        """

    @abstractmethod
    def alert(self, message):
        """
        It logs an alert message
        """

    @abstractmethod
    def critical(self, message):
        """
        It logs a critical message
        """

    @abstractmethod
    def error(self, message):
        """
        It logs an error message
        """

    @abstractmethod
    def warning(self, message):
        """
        It logs a warning message
        """

    @abstractmethod
    def notice(self, message):
        """
        It logs a notice message
        """

    @abstractmethod
    def info(self, message):
        """
        It logs an info message
        """

    @abstractmethod
    def debug(self, message):
        """
        It logs a debug message
        """
