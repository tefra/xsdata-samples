from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class NoteTypeEnumSimple(Enum):
    """
    :cvar CAUTION: This indicates that the note is an alert which shall
        be considered carefully.
    :cvar EXAMPLE: This indicates that the note represents an example,
        e.g. a code example etc.
    :cvar EXERCISE: This indicates that the note represents an exercise
        for the reader.
    :cvar HINT: This indicates that the note represents a hint which
        helps the user for better understanding.
    :cvar INSTRUCTION: This indicates that the note represents an
        instruction, e.g. a step by step procedure.
    :cvar OTHER: This indicates that the note is something else. The
        particular type of the note shall then be specified in the label
        of the note.
    :cvar TIP: This indicates that the note represents which is good to
        know. It is similar to a hint, but focuses more to good practice
        than to better understanding.
    """
    CAUTION = "CAUTION"
    EXAMPLE = "EXAMPLE"
    EXERCISE = "EXERCISE"
    HINT = "HINT"
    INSTRUCTION = "INSTRUCTION"
    OTHER = "OTHER"
    TIP = "TIP"
