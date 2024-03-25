from enum import Enum

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure"


class UsageType(Enum):
    """
    An enumeration of optional | mandatory to indicate the usage of an attribute or
    measure.
    """

    MANDATORY = "mandatory"
    OPTIONAL = "optional"
