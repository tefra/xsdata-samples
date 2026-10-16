from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_1/common"


class WildcardType(StrEnum):
    """
    WildcardType is a single value code list, used to include the '*'
    character - indicating that the identification component is wildcarded.

    :cvar ASTERISK: Indicates that any value of the identifier component
        is allowed.
    """

    ASTERISK = "*"
