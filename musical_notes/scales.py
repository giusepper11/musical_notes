NOTES = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
SCALES = {"major": (0, 2, 4, 5, 7, 9, 11)}


def scales(tonic: str, tonality: str) -> dict[str, list[str]]:
    """
    Generates a scale based on a tonic and a tonality.
    Parameters:
        tonic (str): The tonic of the scale.
        tonality (str): The tonality of the scale.
    Returns:
        dict[str, list[str]]: A dictionary with the notes and degrees of the scale.
    Examples:
        >>> scales('C', 'major')
        {'notes': ['C', 'D', 'E', 'F', 'G', 'A', 'B'], 'degree': ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII']}

        >>> scales('A', 'major')
        {'notes': ['A', 'B', 'C#', 'D', 'E', 'F#', 'G#'], 'degree': ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII']}
    """
    intervals = SCALES[tonality]
    tone_position = NOTES.index(tonic)
    return {
        "notes": [NOTES[(interval + tone_position) % 12] for interval in intervals],
        "degree": ["I", "II", "III", "IV", "V", "VI", "VII"],
    }
