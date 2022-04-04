from abc import ABC, abstractmethod

class AbstractLogger(ABC):
    """
    This class defines the interface for all derived Logger classes
    and their mandatory methods
    """
    @abstractmethod
    def emergency(self, message) -> None:
        """
        It logs an emergency message
        """

    @abstractmethod
    def alert(self, message) -> None:
        """
        It logs an alert message
        """

    @abstractmethod
    def critical(self, message) -> None:
        """
        It logs a critical message
        """

    @abstractmethod
    def error(self, message) -> None:
        """
        It logs an error message
        """

    @abstractmethod
    def warning(self, message) -> None:
        """
        It logs a warning message
        """

    @abstractmethod
    def notice(self, message) -> None:
        """
        It logs a notice message
        """

    @abstractmethod
    def info(self, message) -> None:
        """
        It logs an info message
        """

    @abstractmethod
    def debug(self, message) -> None:
        """
        It logs a debug message
        """
