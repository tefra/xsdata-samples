from enum import Enum

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/common"


class WildcardType(Enum):
    """
    WildcardType is a single value code list, used to include the '*'
    character - indicating that the identification component is wildcarded.

    :cvar ASTERISK: Indicates that any value of the identifier component
        is allowed.
    """

    ASTERISK = "*"
