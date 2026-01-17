from enum import Enum

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/common"


class UnboundedCodeType(Enum):
    """
    UnboundedCodeType provides single textual value of "unbounded", for use
    in OccurentType.

    :cvar UNBOUNDED: Object has no upper limit on occurrences.
    """

    UNBOUNDED = "unbounded"
