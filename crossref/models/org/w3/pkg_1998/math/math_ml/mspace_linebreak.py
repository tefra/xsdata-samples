from enum import Enum

__NAMESPACE__ = "http://www.w3.org/1998/Math/MathML"


class MspaceLinebreak(Enum):
    AUTO = "auto"
    NEWLINE = "newline"
    NOBREAK = "nobreak"
    GOODBREAK = "goodbreak"
    BADBREAK = "badbreak"
    INDENTINGNEWLINE = "indentingnewline"
