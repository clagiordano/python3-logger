import pytest
from clagiordano.python3_logger import __version__
from clagiordano.python3_logger.CLILogger import CLILogger

logger = CLILogger()

class TestCLILogger:
    """
    TestCLILogger
    """
    def test_version(self):
        """
        version
        """
        assert __version__ == '0.1.0'

    def test_ansi_emergency(self):
        """
        emergency
        """
        logger.set_ansi(True)
        with pytest.raises(SystemExit):
            logger.emergency("This is an EMERGENCY message")

    def test_ansi_alert(self):
        """
        alert
        """
        logger.set_ansi(True)
        with pytest.raises(SystemExit):
            logger.alert("This is an ALERT message")

    def test_ansi_critical(self):
        """
        critical
        """
        logger.set_ansi(True)
        with pytest.raises(SystemExit):
            logger.critical("This is a CRITICAL message")

    def test_ansi_error(self):
        """
        info
        """
        logger.set_ansi(True)
        logger.error("This is an ERROR message")

    def test_ansi_warning(self):
        """
        info
        """
        logger.set_ansi(True)
        logger.warning("This is a WARNING message")

    def test_ansi_notice(self):
        """
        info
        """
        logger.set_ansi(True)
        logger.notice("This is a NOTICE message")

    def test_ansi_info(self):
        """
        info
        """
        logger.set_ansi(True)
        logger.info("This is an INFO message")

    def test_ansi_debug(self):
        """
        info
        """
        logger.set_ansi(True)
        logger.debug("This is an DEBUG message")

    def test_no_ansi_emergency(self):
        """
        emergency
        """
        logger.set_ansi(False)
        with pytest.raises(SystemExit):
            logger.emergency("This is an EMERGENCY (no ansi) message")

    def test_no_ansi_alert(self):
        """
        alert
        """
        logger.set_ansi(False)
        with pytest.raises(SystemExit):
            logger.alert("This is an ALERT (no ansi) message")

    def test_no_ansi_critical(self):
        """
        critical
        """
        logger.set_ansi(False)
        with pytest.raises(SystemExit):
            logger.critical("This is a CRITICAL (no ansi) message")

    def test_no_ansi_error(self):
        """
        info
        """
        logger.set_ansi(False)
        logger.error("This is an ERROR (no ansi) message")

    def test_no_ansi_warning(self):
        """
        info
        """
        logger.set_ansi(False)
        logger.warning("This is a WARNING (no ansi) message")

    def test_no_ansi_notice(self):
        """
        info
        """
        logger.set_ansi(False)
        logger.notice("This is a NOTICE (no ansi) message")

    def test_no_ansi_info(self):
        """
        info
        """
        logger.set_ansi(False)
        logger.info("This is an INFO (no ansi) message")

    def test_no_ansi_debug(self):
        """
        info
        """
        logger.set_ansi(False)
        logger.debug("This is an DEBUG (no ansi) message")
