import pytest
from database.models import validate_marks
def test_valid(): assert validate_marks(5,10)==5
def test_invalid():
    with pytest.raises(ValueError): validate_marks(11,10)
