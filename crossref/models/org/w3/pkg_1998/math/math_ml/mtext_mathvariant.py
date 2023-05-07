from enum import Enum

__NAMESPACE__ = "http://www.w3.org/1998/Math/MathML"


class MtextMathvariant(Enum):
    NORMAL = "normal"
    BOLD = "bold"
    ITALIC = "italic"
    BOLD_ITALIC = "bold-italic"
    DOUBLE_STRUCK = "double-struck"
    BOLD_FRAKTUR = "bold-fraktur"
    SCRIPT = "script"
    BOLD_SCRIPT = "bold-script"
    FRAKTUR = "fraktur"
    SANS_SERIF = "sans-serif"
    BOLD_SANS_SERIF = "bold-sans-serif"
    SANS_SERIF_ITALIC = "sans-serif-italic"
    SANS_SERIF_BOLD_ITALIC = "sans-serif-bold-italic"
    MONOSPACE = "monospace"
    INITIAL = "initial"
    TAILED = "tailed"
    LOOPED = "looped"
    STRETCHED = "stretched"
