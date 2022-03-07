import pytest
from pydantic import ValidationError

from app.schemas.episode import EpisodeSearch


@pytest.mark.parametrize(
    "test_input",
    [
        {"segment": "Z01i04"},
        {"segment": "S11E04"},
        {"segment": "S01E24"},
    ],
)
def test_segment_validator(test_input):
    with pytest.raises(ValidationError):
        EpisodeSearch(**test_input)
