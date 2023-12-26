from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class DisplayPresentationEnumSimple(Enum):
    """
    :cvar PRESENTATION_CONTINUOUS: The presentation of data shall form a
        continuous graph between data points.
    :cvar PRESENTATION_DISCRETE: The presentation of data shall be step-
        shaped between data points.
    """

    PRESENTATION_CONTINUOUS = "PRESENTATION-CONTINUOUS"
    PRESENTATION_DISCRETE = "PRESENTATION-DISCRETE"
