from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class BuildTypeEnumSimple(StrEnum):
    """
    :cvar BUILD_TYPE_DEBUG: Used for debugging.
    :cvar BUILD_TYPE_RELEASE: Used for releasing.
    """

    BUILD_TYPE_DEBUG = "BUILD-TYPE-DEBUG"
    BUILD_TYPE_RELEASE = "BUILD-TYPE-RELEASE"
