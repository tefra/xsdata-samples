from enum import Enum

__NAMESPACE__ = "http://www.w3.org/1999/xhtml/datatypes/"


class FrameTargetValue(Enum):
    BLANK = "_blank"
    SELF = "_self"
    PARENT = "_parent"
    TOP = "_top"
