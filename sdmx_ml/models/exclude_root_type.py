from enum import Enum

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/common"


class ExcludeRootType(Enum):
    """
    ExcludeRootType is a single enumerated value that indciates that child
    values should be included, but that the actual root should not.
    """

    EXCLUDEROOT = "excluderoot"
