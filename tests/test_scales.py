"""
AAA - Arrange, Act, Assert
"""
from pytest import mark, raises

from musical_notes.scales import NOTES, SCALES, scale


def test_scale_should_work_with_lower_case_notes():
    """Test scales."""
    # Arrange
    tonic = "c"
    tonality = "major"

    # Act
    result = scale(tonic, tonality)

    # Assert
    assert result


def test_scale_should_return_error_if_note_not_found():
    """Test scales."""
    # Arrange
    tonic = "x"
    tonality = "major"

    error_message = f"Note not found in {NOTES}"

    # Act
    with raises(ValueError) as error:
        scale(tonic, tonality)

    # Assert
    assert error_message == error.value.args[0]


def test_scale_should_return_error_if_tonality_not_found():
    """Test scales."""
    # Arrange
    tonic = "c"
    tonality = "x"

    error_message = f"Tonality not found in {list(SCALES.keys())}"

    # Act
    with raises(KeyError) as error:
        scale(tonic, tonality)

    # Assert
    assert error_message == error.value.args[0]


@mark.parametrize(
    "tonic,expected",
    [
        ("C", ["C", "D", "E", "F", "G", "A", "B"]),
        ("C#", ["C#", "D#", "F", "F#", "G#", "A#", "C"]),
        ("F", ["F", "G", "A", "A#", "C", "D", "E"]),
    ],
)
def test_scale_should_return_correct_scale(tonic, expected):
    """Test scales."""
    # Act
    result = scale(tonic, "major")

    # Assert
    assert expected == result["notes"]


def test_should_return_all_seven_degrees():
    """Test scales."""
    # Arrange
    tonic = "C"
    tonality = "major"
    # Act
    result = scale(tonic, tonality)

    # Assert
    assert ["I", "II", "III", "IV", "V", "VI", "VII"] == result["degree"]
