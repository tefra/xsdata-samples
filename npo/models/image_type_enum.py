from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "urn:vpro:shared:2009"


class ImageTypeEnum(StrEnum):
    PICTURE = "PICTURE"
    PORTRAIT = "PORTRAIT"
    STILL = "STILL"
    LOGO = "LOGO"
    ICON = "ICON"
    PROMO_LANDSCAPE = "PROMO_LANDSCAPE"
    PROMO_PORTRAIT = "PROMO_PORTRAIT"
    BACKGROUND = "BACKGROUND"
