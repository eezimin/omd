from morse import decode

import pytest


@pytest.mark.parametrize(
    "source_string,result",
    [
        ('-- .- .. -....- .--. -.-- - .... --- -. -....- ..--- ----- .---- ----.', 'MAI-PYTHON-2019'),
        ('.. .-.. --- ...- . -.-- --- ..-', 'ILOVEYOU'),
        ('', ''),
    ],
)
def test_morse(source_string, result):
    assert decode(source_string) == result
