from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


class TypeIgnoreStopOver(Enum):
    """
    The stop over inluded to quote fare.

    Properties
    ----------
    NO_STOP_OVER
        No Stop over included.
    STOP_OVER
        Stop over included.
    IGNORE_SEGMENT
        Segment Ignored.
    """

    NO_STOP_OVER = "NoStopOver"
    STOP_OVER = "StopOver"
    IGNORE_SEGMENT = "IgnoreSegment"
