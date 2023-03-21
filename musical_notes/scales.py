NOTES = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
SCALES = {"major": (0, 2, 4, 5, 7, 9, 11)}


def scale(tonic: str, tonality: str) -> dict[str, list[str]]:
    """
    Generates a scale based on a tonic and a tonality.
    Parameters:
        tonic (str): The tonic of the scale.
        tonality (str): The tonality of the scale.
    Returns:
        dict[str, list[str]]: A dictionary with the notes and degrees of the scale.
    Raises:
        ValueError: If the tonic is not found in the NOTES list.
        KeyError: If the tonality is not found in the SCALES dictionary.
    Examples:
        >>> scale('C', 'major')
        {'notes': ['C', 'D', 'E', 'F', 'G', 'A', 'B'], 'degree': ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII']}

        >>> scale('a', 'major')
        {'notes': ['A', 'B', 'C#', 'D', 'E', 'F#', 'G#'], 'degree': ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII']}
    """
    tonic = tonic.upper()
    try:
        intervals = SCALES[tonality]
        tone_position = NOTES.index(tonic)
    except ValueError:
        raise ValueError(f"Note not found in {NOTES}")
    except KeyError:
        raise KeyError(f"Tonality not found in {list(SCALES.keys())}")

    return {
        "notes": [NOTES[(interval + tone_position) % 12] for interval in intervals],
        "degree": ["I", "II", "III", "IV", "V", "VI", "VII"],
    }
