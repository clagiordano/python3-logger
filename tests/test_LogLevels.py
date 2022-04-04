import pytest
from clagiordano.python3_logger.LogLevels import LogLevels

@pytest.mark.parametrize("level,expected_value", [
    ('EMERGENCY', 0),
    ('ALERT', 1),
    ('CRITICAL', 2),
    ('ERROR', 3),
    ('WARNING', 4),
    ('NOTICE', 5),
    ('INFO', 6),
    ('DEBUG', 7)
])
def test_log_levels(level, expected_value):
    """
    Tests log levels
    """
    assert LogLevels[level].value == expected_value
