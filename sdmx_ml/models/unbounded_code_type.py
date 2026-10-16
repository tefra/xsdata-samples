from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_1/common"


class UnboundedCodeType(StrEnum):
    """
    UnboundedCodeType provides single textual value of "unbounded", for use
    in OccurentType.

    :cvar UNBOUNDED: Object has no upper limit on occurrences.
    """

    UNBOUNDED = "unbounded"
