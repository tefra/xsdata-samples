from enum import Enum

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


class RoadworksDurationEnum(Enum):
    """
    Expected durations of roadworks in general terms.

    :cvar LONG_TERM: The roadworks are expected to last for a long term
        ( duration &gt; 6 months)
    :cvar MEDIUM_TERM: The roadworks are expected to last for a medium
        term (1 month &lt; duration &lt; = 6 months).
    :cvar SHORT_TERM: The roadworks are expected to last for a short
        term ( duration &lt; = 1 month)
    """

    LONG_TERM = "longTerm"
    MEDIUM_TERM = "mediumTerm"
    SHORT_TERM = "shortTerm"
