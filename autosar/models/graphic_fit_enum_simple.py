from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class GraphicFitEnumSimple(Enum):
    """
    :cvar AS_IS: This indicates that the image shall be incorporated as
        is without scaling, rotation etc.
    :cvar FIT_TO_PAGE: Fit to the page
    :cvar FIT_TO_TEXT: fit to the text containing the graphic.
    :cvar LIMIT_TO_PAGE: This indicates that the width of the graphic
        shall be limited to the '''page width'''. The image shall not be
        scaled down but cropped.
    :cvar LIMIT_TO_TEXT: This indicates that the width of the graphic
        shall be limited to the width of the current '''text flow'''.
        The image shall not be scaled down but cropped.
    :cvar ROTATE_180: Rotate 180 degree
    :cvar ROTATE_180_LIMIT_TO_TEXT: Rotate 180 degree
    :cvar ROTATE_90_CCW: Rotate 90 degree counter clockwise
    :cvar ROTATE_90_CCW_FIT_TO_TEXT: Rotate by 90 degree counter clock
        wise and then fit to text
    :cvar ROTATE_90_CCW_LIMIT_TO_TEXT: Rotate by 90 degree counter clock
        wise and then fit to text
    :cvar ROTATE_90_CW: Rotate 90 degree clockwise
    :cvar ROTATE_90_CW_FIT_TO_TEXT: Rotate by 90 degree and then fit to
        text
    :cvar ROTATE_90_CW_LIMIT_TO_TEXT: Rotate by 90 degree and then fit
        to text
    """

    AS_IS = "AS-IS"
    FIT_TO_PAGE = "FIT-TO-PAGE"
    FIT_TO_TEXT = "FIT-TO-TEXT"
    LIMIT_TO_PAGE = "LIMIT-TO-PAGE"
    LIMIT_TO_TEXT = "LIMIT-TO-TEXT"
    ROTATE_180 = "ROTATE-180"
    ROTATE_180_LIMIT_TO_TEXT = "ROTATE-180-LIMIT-TO-TEXT"
    ROTATE_90_CCW = "ROTATE-90-CCW"
    ROTATE_90_CCW_FIT_TO_TEXT = "ROTATE-90-CCW-FIT-TO-TEXT"
    ROTATE_90_CCW_LIMIT_TO_TEXT = "ROTATE-90-CCW-LIMIT-TO-TEXT"
    ROTATE_90_CW = "ROTATE-90-CW"
    ROTATE_90_CW_FIT_TO_TEXT = "ROTATE-90-CW-FIT-TO-TEXT"
    ROTATE_90_CW_LIMIT_TO_TEXT = "ROTATE-90-CW-LIMIT-TO-TEXT"
